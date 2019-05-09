from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

from datetime import datetime
@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    print("Charging " + request.form['first_name'] + " for fruits")
    strawberryForm = request.form['strawberry']
    raspberryForm = request.form['raspberry']
    appleForm = request.form['apple']
    firstNameForm = request.form['first_name']
    lastNameForm = request.form['last_name']
    studentForm = request.form['student_id']

    return render_template("checkout.html", strawberryTemplate = strawberryForm, raspberryTemplate = raspberryForm, appleTemplate = appleForm, firstnameTemp = firstNameForm, lastnameTemp = lastNameForm, studentTemp = studentForm, sumTemp = int(strawberryForm)+int(appleForm)+int(raspberryForm))

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    