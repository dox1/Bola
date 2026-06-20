import sqlite3
from datetime import datetime, timedelta

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("bola.db", check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                joined_at TEXT,
                is_subscribed INTEGER DEFAULT 0,
                expiry_date TEXT
            )
        """)
        self.conn.commit()

    def add_user(self, user_id, username):
        self.conn.execute("""
            INSERT OR IGNORE INTO users (user_id, username, joined_at)
            VALUES (?, ?, ?)
        """, (user_id, username, datetime.now().strftime("%Y-%m-%d %H:%M")))
        self.conn.commit()

    def is_subscribed(self, user_id):
        cur = self.conn.execute(
            "SELECT is_subscribed, expiry_date FROM users WHERE user_id = ?", (user_id,)
        )
        row = cur.fetchone()
        if not row or not row[0]:
            return False
        if row[1] and datetime.strptime(row[1], "%Y-%m-%d") < datetime.now():
            self.conn.execute(
                "UPDATE users SET is_subscribed = 0 WHERE user_id = ?", (user_id,)
            )
            self.conn.commit()
            return False
        return True

    def activate_subscription(self, user_id, days):
        expiry = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
        self.conn.execute("""
            UPDATE users SET is_subscribed = 1, expiry_date = ? WHERE user_id = ?
        """, (expiry, user_id))
        self.conn.commit()

    def get_expiry(self, user_id):
        cur = self.conn.execute(
            "SELECT expiry_date FROM users WHERE user_id = ?", (user_id,)
        )
        row = cur.fetchone()
        return row[0] if row else "غير معروف"

    def get_all_users(self):
        cur = self.conn.execute("SELECT user_id, username, joined_at, is_subscribed, expiry_date FROM users")
        return cur.fetchall()
