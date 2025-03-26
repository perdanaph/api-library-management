from flask import Blueprint
from ..controllers.member_controller import MemberController

member_blueprint = Blueprint("member_blueprint", __name__)

member_blueprint.route("/", methods=["POST"])(MemberController.create_member)
member_blueprint.route("/<string:id>/borrowings", methods=["GET"])(
    MemberController.get_member_borrowings
)
