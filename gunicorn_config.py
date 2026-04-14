import os

bind = f"0.0.0.0:{os.environ.get('PORT', '8080')}"
workers = 1

def on_starting(server):
    from app import init_db
    init_db()
