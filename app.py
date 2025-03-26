import click
from flask import Flask, jsonify
from flask.cli import with_appcontext
from sqlalchemy import text
from src.config.database import init_db
from src.routes.book_routes import book_blueprint
from src.routes.member_routes import member_blueprint
from src.routes.borrowing_routes import borrow_blueprint


@click.command("check-db")
@with_appcontext
def check_db_command():
    """Check database connection"""
    from src.config.database import db

    try:
        db.session.execute(text("SELECT 1"))
        print("✅ Database connected successfully!")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")


def create_app():
    app = Flask(__name__)

    # Init database
    init_db(app)
    baseUrlAPI = "/api"
    app.register_blueprint(book_blueprint, url_prefix=baseUrlAPI + "/books")
    app.register_blueprint(member_blueprint, url_prefix=baseUrlAPI + "/members")
    app.register_blueprint(borrow_blueprint, url_prefix=baseUrlAPI + "/borrowings")

    # check connection DB
    app.cli.add_command(check_db_command)

    # error handlers
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Bad Request", "message": str(error)}), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not Found", "message": str(error)}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal Server Error", "message": str(error)}), 500

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
