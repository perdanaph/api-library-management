from flask import jsonify, request
from ..services.borrowing_service import BorrowingService


class BorrowController:
    @staticmethod
    def new_borrowing_book():
        req_data = request.get_json()

        if not req_data or "book_id" not in req_data or "member_id" not in req_data:
            return jsonify({"error": "book_id and member_id are required"}), 400

        try:
            borrowing = BorrowingService.borrow_book(
                book_id=req_data["book_id"], member_id=req_data["member_id"]
            )
            return (
                jsonify(
                    {
                        "message": "Book borrowed successfully",
                        "data": borrowing.to_dict(),
                    }
                ),
                201,
            )

        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
