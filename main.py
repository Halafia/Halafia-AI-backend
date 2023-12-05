from flask import Flask, render_template, jsonify, request
import halafia


app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='HALAFIA')


@app.route('/')
def page_not_found():
    return render_template('404.html'), 404

app.register_error_handler(404, page_not_found)

@app.route('/prompt', methods = ['POST', 'GET'])
def index():

    if request.method == 'POST':
        prompt = request.form['prompt']
#        dob = request.form['dob']
#        allegries = request.form['allegries']
#        medication = request.form['medication']
#        blood_group = request.form['bloodgroup']
#        location = request.form['location']

        res = {}
        res['response'] = halafia.alternate_risk_assessment(prompt)
        return jsonify(res), 200

    return render_template('index.html')

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