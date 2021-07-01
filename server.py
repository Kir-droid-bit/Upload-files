import os
from flask import Flask, request, redirect, url_for,render_template,send_from_directory
from werkzeug.utils import secure_filename
app = Flask(__name__)
UPLOAD_FOLDER = r'C:\Users\Kirill\Desktop\Programs\PYTHON\Flask\uploads fiels\uploads\files' # путь загрузки файлов
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','ico']) # поддерживаемые расширения
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # говорим серверу по какому пути загружать
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
@app.route('/')
def main_page():
    return render_template('glavnaya.html')
@app.route('/uploads-files/',methods=["GET","POST"])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template("form.html")
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
