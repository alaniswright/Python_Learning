from flask import Flask, render_template
import requests

app = Flask(__name__) #create an instance of the Flask class and call it "app". "__name__" refers to this file

@app.route("/") #defines default page. In this case it will be the root file in folder
def home():
    return render_template("home.html") # Looks for a template in the templates folder, and renders it

if __name__ == "__main__": # The name __main__ gets assigned to script when activated. if statement prevents scripts that are not called __main__ from running.
    app.run(debug=True) ## run the application. Allow possible Python errors to appear on web page
