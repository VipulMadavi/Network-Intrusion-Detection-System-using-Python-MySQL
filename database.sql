CREATE DATABASE IF NOT EXISTS network_security;
USE network_security;

CREATE TABLE IF NOT EXISTS network_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    ip_address VARCHAR(50),
    port INT,
    action VARCHAR(100),
    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO network_logs (ip_address, port, action) VALUES
('192.168.1.10', 22, 'login_attempt'),
('203.0.113.55', 443, 'login_failed'),
('203.0.113.55', 443, 'login_failed'),
('203.0.113.55', 443, 'login_failed'),
('10.0.0.5', 80, 'access_granted'),
('192.0.2.99', 21, 'ftp_access'),
('198.51.100.77', 3389, 'remote_login');
