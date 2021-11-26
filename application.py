import os
import io
from io import BytesIO
from flask import Flask,flash, render_template, request, redirect, url_for
from s3_functions import list_files_v2, convert_upload_files, upload_file_to_s3
from werkzeug.utils import secure_filename

IMAGES_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'svg'}

# function to check file extension
def image_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in IMAGES_EXTENSIONS

application = Flask(__name__)
application.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

UPLOAD_FOLDER = "uploads"
BUCKET = "preprod"
@application.route("/")
def home():
    return render_template('main.html')

@application.route("/recent")
def recent():
    contents = list_files_v2(BUCKET)
    contentsLimit = list_files_v2(BUCKET)[:5:]
    return render_template('main_recent.html', files = contents, filesLimit = contentsLimit)
    
@application.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        # check whether an input field with name 'user_file' exist
        if 'file' not in request.files:
            flash('No file key in request.files')
            return redirect(url_for('home'))
        f = request.files['file']
        # check whether a file is selected
        if f.filename == '':
            flash('No selected file')
            return redirect(url_for('home'))
       # if image_file(f.filename):
         #   output = convert_upload_files
        if f:
            if image_file(f.filename):        
                output = convert_upload_files(f, os.path.splitext(f.filename)[1].replace('.',''), BUCKET)
            else:
                output = upload_file_to_s3(f, BUCKET)

            if output:
                flash("Upload Succes")
                return redirect("/recent")
            else:
                flash("Unable to upload, try again")
                return redirect(url_for('home'))
       # f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
        #if( 'jpg' in os.path.splitext(f.filename)[1] or 'jpeg' in os.path.splitext(f.filename)[1] or 'svg' in os.path.splitext(f.filename)[1] or 'png' in os.path.splitext(f.filename)[1] ):
        #    convert_upload_files(f"uploads/{f.filename}",os.path.splitext(f.filename)[1].replace('.',''),BUCKET, UPLOAD_FOLDER )
        #else:
         #   upload_file(f"uploads/{f.filename}", BUCKET)
       # os.remove(f"uploads/{f.filename}")

@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    application.run(debug=True)
