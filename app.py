import os
from flask import Flask, render_template, request, redirect, send_file
from s3_functions import list_files_v2, upload_file
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "preprod"
@app.route("/")
def home():
    return render_template('main.html')

@app.route("/recent")
def recent():
    contents = list_files_v2(BUCKET)
    contentsLimit = list_files_v2(BUCKET)[:5:]
    print(contents)
    return render_template('main_recent.html', files = contents, filesLimit = contentsLimit)
##files = list_files_v2(BUCKET)[:5:]
@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
        upload_file(f"uploads/{f.filename}", BUCKET)
        os.remove(f"uploads/{f.filename}")
        return redirect("/recent")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
    