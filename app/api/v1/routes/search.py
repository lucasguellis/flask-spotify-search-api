from flask import Blueprint, request, jsonify

from ..services.search import Search


api_search_bp = Blueprint('api_search', __name__)


@api_search_bp.route('/search')
def search():
    # Get the search parameters from the query string
    parameters = request.args.to_dict()

    # Perform the search
    response = Search(parameters).search()

    # Return the URL parameters as a string
    return jsonify(response)
