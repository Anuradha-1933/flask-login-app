#Project: Flask Login App
from flask import Flask,request,redirect,url_for,session,Response
app=Flask(__name__)
app.secret_key = 'supersecret'  # Required for session management
@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if username=="admin" and password=="123":
            session["username"]=username # Store username in session
            return redirect(url_for("welcome"))
        else:
            return Response("In-valid credentials,try again",mimetype="text/plain") #bydefault flask send html/text content to broswer
    return '''
    <h1>Login Page</h1>
    <form method="POST">
    Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>  
    <input type="submit" value="Login"> 
    </form>
'''

@app.route("/welcome")
def welcome():
    if "username" in session:
        return f'''
        <h2>Welcome, {session['username']}!</h2>
        <a href={url_for('logout')}>Logout</a>"
        '''
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("username", None)  # Remove username from session
    return redirect(url_for("login"))