from flask import Blueprint
from ..controllers.book_controller import BookController

book_blueprint = Blueprint('book_blueprint', __name__)

book_blueprint.route('/', methods=['GET'])(BookController.get_all_books)