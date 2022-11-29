from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import sequential_search
import rtree_search
from main import *

app = Flask(__name__, template_folder='../frontend/templates', static_folder= "../frontend/static")

app.config['UPLOAD_FOLDER'] = './uploads'
os.makedirs(os.path.join(app.instance_path, 'uploads'), exist_ok=True)

@app.route("/")
def index():
    return render_template('index.html') 


@app.route("/<file>/<radius>", methods=['GET'])
def rangeSearch(file, radius):
    res = smt.RANGE_SEARCH(file, radius)
    # res = sequential_search.range_search(file, radius, os.getcwd(), dictionary)
    return res

@app.route("/<file>/<k>", methods=['GET'])
def KNNSearch(file, k):
    k = int(k)
    res = smt.KNN_SEARCH(file, k)
    # res = sequential_search.knn_search(file, k, os.getcwd(), dictionary)
    print(res)
    error = ""
    if (res == 0):
        error = "error de envio"
        print("vacio")
    return render_template('result.html', data = res, error = error)


@app.route("/ind/<file>/<radius>", methods=['GET'])
def rangeSearchInd(file, radius):
    res = smt.RANGE_SEARCH_RTREE(file, radius)
    # res = rtree_search.range_search_rtree(file, radius, os.getcwd(), idx, dictionary)
    return res


@app.route("/ind/<file>/<k>", methods=['GET'])
def KNNSearchInd(file, k):
    k = int(k)
    if(k < 1):
        k = 1
    res = smt.KNN_SEARCH_RTREE(file, k)
    # res = sequential_search.knn_search_rtree(file, k, os.getcwd(), dictionary, idx)
    error = ""
    if (res == []):
        error = "No se cargo nada"
    return render_template('result.html', data = res, name = file, error = error, n = k)


@app.route("/upload", methods=['POST'])
def uploader():
 if request.method == 'POST':
  # obtenemos el archivo del input "archivo"
  f = request.files['archivo']
  k = request.form['K datos']
  print(k)
  filename = secure_filename(f.filename)
  f.save(os.path.join(app.instance_path, 'Uploads', secure_filename(f.filename)))
  # Si se quiere eliminar el archivo usar remove(UPLOADS_PATH + filename)

  return redirect(url_for('KNNSearchInd', file = filename, k = k))


if __name__ == '__main__':
    smt = some_class(14500, False) # true or false is a flag that indicates if it is needed to process al 14000 images
    app.run(debug=True, use_reloader = False)
    app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='../frontend/static/images/logo_utec.png'))