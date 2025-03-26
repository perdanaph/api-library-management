from flask import request, jsonify
from ..services.book_service import BookService


class BookController:
    @staticmethod
    def get_all_books():
        title = request.args.get("title")
        author = request.args.get("author")
        page = max(1, int(request.args.get("page", 1)))
        limit = max(1, min(int(request.args.get("limit", 10)), 100))

        try:
            result = BookService.get_all_books(title, author, page, limit)
            return jsonify(result), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
