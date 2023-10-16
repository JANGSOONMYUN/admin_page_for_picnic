from flask import Flask, render_template, request, redirect, url_for
from flask import send_from_directory
import os

from get_config import get_ip_port, get_upload_dir_path
from manage_picnic import get_picnic_config, set_post_text, get_post_text

app = Flask(__name__)
UPLOAD_FOLDER = './'
content_file_name = 'picnic_ex_tmp.csv'
char_setting_name = 'character_setting.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if '.csv' not in file.filename:
        return redirect(request.url)
    if file:
        filename = os.path.join(UPLOAD_FOLDER, content_file_name)
        print(f'{file.filename} -> filename')
        file.save(filename)
        return redirect(url_for('index'))


@app.route('/download')
def download_file():
    return send_from_directory(UPLOAD_FOLDER, content_file_name, as_attachment=True)


@app.route('/modify_post_text', methods=['POST'])
def modify_post_text():
    post_text = request.form.get('post_text')
    # You can process the variable_value here
    print("Modified variable:", post_text)
    
    filename = os.path.join(UPLOAD_FOLDER, char_setting_name)
    set_post_text(post_text, filename)
    return redirect(url_for('index'))

@app.route('/load_post_text')
def load_post_text():
    filename = os.path.join(UPLOAD_FOLDER, char_setting_name)
    post_text = get_post_text(filename)
    return {"value": post_text}

if __name__ == '__main__':
    ip, port = get_ip_port('config.json')
    UPLOAD_FOLDER = get_upload_dir_path('config.json')
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host=ip, port=port, debug=True)
