from flask import render_template, Flask,request
from flask_mail import Mail, Message
app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'amanikashema000@gmail.com'
app.config['MAIL_PASSWORD'] = "Amani@1998"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


mail = Mail(app)


@app.route('/')
def hello(name=None):
    return render_template('index.html',name=name)

@app.route('/send_email', methods=['GET', 'POST'])
def send_message():
    if request.method == "POST":
        fname = request.form['First_name']
        lname = request.form['Last_name']
        emailadress = request.form['email']
        msg = request.form['message']
        senders_email = 'amanikashema000@gmail.com'
        message = Message(msg,sender=senders_email,recipients=[emailadress])
        message.body = msg
        mail.send(message)
        success = "Message sent"
        return success

if __name__ == "__main__":
    app.run(debug=True)
