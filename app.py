import click
from flask import Flask
from flask.cli import with_appcontext
from sqlalchemy import  text
from src.config.database import db, init_db


@click.command('check-db')
@with_appcontext
def check_db_command():
    """Check database connection"""
    from src.config.database import db
    try:
        db.session.execute(text('SELECT 1'))
        print('✅ Database connected successfully!')
    except Exception as e:
        print(f'❌ Database connection failed: {e}')

def create_app():
    app = Flask(__name__)
    init_db(app)
    app.cli.add_command(check_db_command)
    return app

app = create_app()