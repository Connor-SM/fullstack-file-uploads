from app import app
import os
from flask import Flask, flash, request, redirect, url_for, session, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin

UPLOAD_FOLDER = os.path.abspath(os.path.dirname(__file__)) + '/static/graph_images/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route('/upload', methods=['POST'])
def fileUpload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    destination = UPLOAD_FOLDER + 'test-' + filename
    file.save(destination)

    return jsonify({
        'filename' : 'static/graph_images/' + filename
    })
