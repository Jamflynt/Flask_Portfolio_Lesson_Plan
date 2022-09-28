# Step 1: Create all necessary files
# Step 2: Create your Virtual Environment and activate it
# Step 3: Code our index.html

# Step 4: Start our Flask app by importing all necessary modules and classes
from flask import Flask, render_template, request, url_for, redirect
from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage
app = Flask(__name__)

# Step 5: Create our route to render our index.html upon loading 
@app.route("/")
def index():
    return render_template("index.html")

# Create a route that loads when the user clicks the Submit Button on our app's email form
# We will be sending data here so we will use the POST method
@app.route("/sendemail/", methods=['POST'])
# Define our function for the route
def sendemail():
    # Create an if statement
    if request.method == "POST":
        name = request.form['name']
        subject = request.form['Subject']
        email = request.form['_replyto']
        message = request.form['message']
  
        # Set your credentials (note: security here, do not upload your passwords to GitHub and if you are going to )
        yourEmail = "j******@gmail.com"
        yourPassword = "#########"
        # Setting up an App Password with Gmail
        # https://support.google.com/accounts/answer/185833?hl=en
  
        # Logging in to our email (GMAIL) account
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(yourEmail, yourPassword)
  
        # Sender's and Receiver's email address
        msg = EmailMessage()
        msg.set_content("First Name : "+str(name)
                        +"\nEmail : "+str(email)
                        +"\nSubject : "+str(subject)
                        +"\nMessage : "+str(message))
        msg['To'] = yourEmail
        msg['From'] = email
        msg['Subject'] = subject
  
        # Send the message via our own SMTP server.
        try:
            # sending an email
            server.send_message(msg)
            print("Send")
        except:
            print("Fail to Send")
            pass
              
    return redirect('/')
  
if __name__ == "__main__":
    app.run(debug=True)


# Good resource for deploying your Python App: 
# https://www.pythonanywhere.com/?affiliate_id=00535ced