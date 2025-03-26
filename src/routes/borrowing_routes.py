from flask import Blueprint
from ..controllers.borrowing_controller import BorrowController

borrow_blueprint = Blueprint("borrow_blueprint", __name__)

borrow_blueprint.route("/", methods=["POST"])(BorrowController.new_borrowing_book)
borrow_blueprint.route("/<string:id>/return", methods=["PUT"])(
    BorrowController.returning_book
)
