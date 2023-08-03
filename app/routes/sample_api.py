from app.app_blueprint import api_app, render_template, jsonify
from flask import request


@api_app.route("/hello")
def get_hello():
    return "Hello! Stranger!!!"


# @api_app.app_errorhandler(404)
# @api_app.app_errorhandler(405)
# def _handle_api_error(ex):
#     if request.path.startswith('/api/'):
#         return jsonify(ex)
#     else:
#         return "에러 : ",ex
