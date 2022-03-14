# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, send_from_directory, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_ckeditor import CKEditor, CKEditorField, upload_fail, upload_success

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 400
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'

# app.config['CKEDITOR_ENABLE_CSRF'] = True  # if you want to enable CSRF protect, uncomment this line

app.config['UPLOADED_PATH'] = os.path.join(basedir, 'uploads')

app.secret_key = 'k229u-230d-0i-0ekdopoejwlejl'

ckeditor = CKEditor(app)

class PostForm(FlaskForm):
    title = StringField('Title')
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        # WARNING: use bleach or something similar to clean the data (escape JavaScript code)
        # You may need to store the data in database here
        return render_template('post.html', title=title, body=body)
    return render_template('index.html', form=form)

@app.route('/files/<filename>')
def uploaded_files(filename):
    path = app.config['UPLOADED_PATH']
    return send_from_directory(path, filename)


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('upload')
    extension = f.filename.split('.')[-1].lower()

    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        
        return upload_fail(message='Image only!')
    
    f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    
    url = url_for('uploaded_files', filename=f.filename)
    
    return upload_success(url, filename=f.filename)


if __name__ == '__main__':
    app.run(debug=True)
