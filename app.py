import os
from flask import Flask, render_template, request, redirect, send_file
from s3_functions import list_files, upload_file, show_image
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "devbucketflo"

@app.route("/")
def home():
    contents = list_files(BUCKET)
    return render_template('index.html')

@app.route("/pics")
def list():
    contents = list_files(BUCKET)
    return render_template('collection.html', contents=contents)

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
        upload_file(f"uploads/{f.filename}", BUCKET)
        os.remove(f"uploads/{f.filename}")
        return redirect("/pics")

if __name__ == '__main__':
    app.run(debug=True)
    