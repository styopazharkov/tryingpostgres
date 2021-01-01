
### The following code is the imported packages ###
from flask import Flask, redirect, url_for, render_template, request, session, abort

### The following code creates the app variable and assigns a secret key for the session dictionary ###
app = Flask(__name__)
app.secret_key = "An arbitrary key"


#### PAGE ROUTING BELOW THIS LINE ####
@app.route('/')
def index():
    return "hello" #renders html page

if __name__ == "__main__":
    app.run(debug = True) 