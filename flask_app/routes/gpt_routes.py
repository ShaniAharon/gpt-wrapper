from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for

gpt_routes = Blueprint('gpt_routes', __name__)

@gpt_routes.route('/', methods=['GET'])
def gpt():
    return "Welcome to ChatGPT API Wrapper!" #render_template("gpt.html", user=current_user)