import mysql.connector
from mysql.connector import Error
import os

DB_CONFIG = {
    'host': '127.0.0.1',
    'user': 'vipulm',
    'password': 'Vipul1509',
    'database': 'network_security',
    'port': 3006,
}

def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        raise RuntimeError(f"Database connection error: {e}")

def insert_log(ip_address: str, port: int, action: str):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO network_logs (ip_address, port, action) VALUES (%s, %s, %s)"
        cursor.execute(sql, (ip_address, port, action))
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        conn.close()

def fetch_logs(limit: int = 1000):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM network_logs ORDER BY log_time DESC LIMIT %s", (limit,))
        rows = cursor.fetchall()
        return rows
    finally:
        cursor.close()
        conn.close()

def count_recent_actions(ip: str, action: str, interval_minutes: int = 60):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sql = ("SELECT COUNT(*) FROM network_logs WHERE ip_address=%s AND action=%s "
               "AND log_time >= (NOW() - INTERVAL %s MINUTE)")
        cursor.execute(sql, (ip, action, interval_minutes))
        (count,) = cursor.fetchone()
        return count
    finally:
        cursor.close()
        conn.close()
