from flask import request, jsonify
from ..services.member_service import MemberService


class MemberController:
    def create_member():
        req_data = request.get_json()
        try:
            member = MemberService.add_member(
                name=req_data.get("name"),
                email=req_data.get("email"),
                phone=req_data.get("phone"),
                address=req_data.get("address"),
            )
            return jsonify(member.to_dict()), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
