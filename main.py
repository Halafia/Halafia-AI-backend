from flask import Flask, render_template, jsonify, request
import halafia



def page_not_found():
    return render_template('404.html'), 404

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='HALAFIA')

app.register_error_handler(404, page_not_found)

@app.route('/', methods = ['POST', 'GET'])
def index():

    if request.method == 'POST':
        prompt = request.form['prompt']

        res = {}
        res['response'] = halafia.generateResponse(prompt)
        return jsonify(res), 200

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port='5000', 
        debug=True
    )


#@halafia.route('/create file', methods= ['POST'])
#def create_file():
#    if request.method == 'POST':
#        with open(f"{request.form.get('name')}.txt", "w") as f:
#            f.write()
#        return('', 204)