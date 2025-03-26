from flask import request, jsonify
from ..services.member_service import MemberService


class MemberController:
    @staticmethod
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

    @staticmethod
    def get_member_borrowings(id):
        try:
            status = request.args.get("status")
            page = max(1, int(request.args.get("page", 1)))
            limit = max(1, min(int(request.args.get("limit", 10)), 100))
            result = MemberService.get_member_borrowings(
                id=id, status=status, page=page, limit=limit
            )
            return jsonify(result), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
