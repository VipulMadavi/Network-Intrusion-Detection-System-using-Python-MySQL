from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from db import insert_log, fetch_logs, count_recent_actions
import io, csv

app = Flask(__name__)
app.secret_key = 'replace-with-random-secret'  # replace in production

ALERT_THRESHOLD = 3  # e.g., more than 3 login_failed in the last 60 minutes

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip = request.form.get('ip_address', '').strip()
        port = int(request.form.get('port', 0)) if request.form.get('port') else 0
        action = request.form.get('action', '').strip()
        if not ip or not action:
            flash('IP address and action are required.', 'danger')
        else:
            insert_log(ip, port, action)
            flash('Log inserted.', 'success')
            return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/logs')
def logs():
    rows = fetch_logs(limit=1000)
    alerts = []
    seen_ips = set()
    for row in rows:
        ip = row['ip_address']
        if ip in seen_ips:
            continue
        seen_ips.add(ip)
        cnt = count_recent_actions(ip, 'login_failed', interval_minutes=60)
        if cnt >= ALERT_THRESHOLD:
            alerts.append({'ip': ip, 'count': cnt})
    return render_template('logs.html', rows=rows, alerts=alerts)

@app.route('/export')
def export_csv():
    rows = fetch_logs(limit=10000)
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['log_id', 'ip_address', 'port', 'action', 'log_time'])
    for r in reversed(rows):
        writer.writerow([r['log_id'], r['ip_address'], r['port'], r['action'], r['log_time']])
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        download_name='network_logs.csv'
    )

if __name__ == '__main__':
    app.run(debug=True)
