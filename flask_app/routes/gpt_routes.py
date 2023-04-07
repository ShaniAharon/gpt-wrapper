from flask import Blueprint, request, jsonify
from ..services.gpt_service import get_gpt_response
gpt_routes = Blueprint('gpt_routes', __name__)

@gpt_routes.route('/', methods=['GET'])
def gpt():
    return "Welcome to ChatGPT API Wrapper!" 


@gpt_routes.route('/chat', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message', 'No message found in JSON object')
    gpt_res = get_gpt_response(message)
    response = {
        'status': 'success',
        'received_message_from_gpt': gpt_res
    }
    return jsonify(response)