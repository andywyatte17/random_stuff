import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'
try: os.mkdir(UPLOAD_FOLDER)
except: pass
ALLOWED_EXTENSIONS = set(['mp4', 'txt', 'pdf', \
               'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploads')
def uploads():
    from jinja2 import Template
    import glob
    nav = []
    for x in glob.glob(UPLOAD_FOLDER+'/*'):
        nav.append({'href':x,
                    'caption':os.path.basename(x)})
    html = r'''<!DOCTYPE html>
<html lang="en">
    <head>
    <style>* { font-size: 32pt; }</style>
    <title>My Webpage</title> 
    </head>
    <body>
    <h1>My Webpage</h1>
    <ul id="navigation">
      {% for item in navigation %}
      <li>
        <a href="{{ item.href }}">
            {{ item.caption }}
        </a>
      </li>
      {% endfor %}
      </ul>
    {{ a_variable }} {# a comment #}
    </body>
    </html>'''
    template = Template(html)
    return template.render(navigation=nav)

@app.route('/uploads/<string:filename>')
def uploads2(filename):
    return send_from_directory(
           directory=app.config['UPLOAD_FOLDER'],
           filename=filename)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            fpath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(fpath)
            u4 = url_for('upload_file',
                 filename=fpath)
            with open(UPLOAD_FOLDER+filename+'.htm', 'wb') as f:
                f.write(fpath.encode('utf-8'))
            # print(u4)
            # return redirect(u4)
            return redirect('/uploads')
    return \
'''<!doctype html>
<head>
<style>
* { font-size: 36pt; }
</style>
</head>
<body>
<title>Upload new File</title>
<h1>Upload new File</h1>
<form method=post enctype=multipart/form-data>
  <p><input type=file name=file>
	     <input type=submit value=Upload>
    </form>
</body>
'''

if __name__=='__main__':
    app.run()
