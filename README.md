# Network Intrusion Detection Log System (Python + MySQL)

Simple Flask web app to insert and view network logs (IP, port, action) with a MySQL backend.

## Quick start

1. Install Python 3.8+ and MySQL.
2. Create a virtualenv and activate it.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the SQL in `database.sql` to create DB and sample data.
5. Set DB credentials via environment variables: `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`.
6. Run: `python app.py`
7. Open http://127.0.0.1:5000

## Project structure
See the repository root for files and `templates/`.

## License
MIT
