from flask import Flask, render_template, jsonify, request
#import halafia


app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='HALAFIA')


@app.route('/404')
def page_not_found():
    return render_template('404.html'), 404

app.register_error_handler(404, page_not_found)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
            email = request.form.get('email')
            message = request.form.get('message')

    return render_template('index.html'), 200


@app.route('/form', methods = ['POST', 'GET'])
def form():
        
        return render_template('form.html'), 204



if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port='5000', 
        debug=True
    )


#@app.route('/create-file', methods= ['POST'])
#def create_file():
#    if request.method == 'POST':
#        with open(f"{request.form.get('name')}.txt", "w") as f:
#            f.write()
#        return('', 204)