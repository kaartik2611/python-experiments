# Created a basic GET POST request app using flask.

from flask import Flask , render_template , url_for, request , redirect
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id = request.form['id']
        return redirect(url_for('id',id=id))
    else:   
        return render_template('index.html')

@app.route('/<id>')
def id(id):
    return f'<h2>{id}</h2>'

if __name__ == '__main__':
    app.run(debug=True)