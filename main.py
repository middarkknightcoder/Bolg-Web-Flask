from flask import Flask ,render_template ,request ,session ,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json 
import os      # join our file uploader app with the particular location
import math
from werkzeug.utils import secure_filename     # used for the sequre filename
from flask_mail import Mail 

app = Flask(__name__)     # Create Flask Application or instance

app.secret_key = "Secret_key_testing"     # Setup of secret key into the application for the session creation for in user authentication 

# Open Config.json file using file/io

with open("config.json" ,"r") as c:
    params = json.load(c)["params"]    # This Featch parmas from the config.json file
    
# Connection with the smtp protocol (Also this is used for sing in with the smtp server)

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465' ,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params["gmail-username"],
    MAIL_PASSWORD = params["gmail-password"]
)
 
mail = Mail(app)   # Here we are create Instence of the Mail class and give the application 

# For stored the file uploader url

app.config["UPLOAD_FOLDER"] = params["upload_location"]


# ********* Database SQLAlchemy *********

# Connection of the sqldatabse with Flask Application 

local_server = params["local_server"]   # Here we are consider local_server is True

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]    # Here username is password is used in xampp 
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]


db = SQLAlchemy(app)   # Create Instance of the Database or connect app with database


# Now Create Class for the Database Table Columns (Class name is same as database table name (Cpital and small word is ignore))

class Contacts(db.Model):   # Inherit db.model class into Contact Class 

    # Now Create Model for the database or column configuration 
    sno = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(80) ,nullable=False )
    email = db.Column(db.String(30) ,nullable=False)
    ph_no = db.Column(db.String(12) ,nullable=False)
    msg = db.Column(db.String(120) ,nullable=False)
    date = db.Column(db.DateTime)
 
 
class Posts(db.Model):
    
    sno = db.Column(db.Integer ,primary_key=True)
    title = db.Column(db.String(50) ,nullable=False)
    tagline = db.Column(db.String(50) ,nullable=False)
    slug = db.Column(db.String(25) ,nullable=False)
    content = db.Column(db.String(1000) ,nullable=False)
    img_file = db.Column(db.String(50) ,nullable=False)
    date = db.Column(db.String(12) ,nullable=False)
    
# ******************** Routes(URL) For Blog website ********************

@app.route("/")
def home():
    
    posts = Posts.query.filter_by().all()
    
    last = math.ceil(len(posts)/int(params["no_of_posts"]))    # Find How Many Pages Requierd OR find last page
    
    page = request.args.get("page")   # This get value from the url 
    
    if(not str(page).isnumeric()):   # Check Enter Page string is numeric or not 
        page=1    # Intialize Page No.
    
    page=int(page)   
    
    # Slicing of the Posts 
    
    posts = posts[(page-1)*int(params['no_of_posts']) : ((page-1) * int(params['no_of_posts']))+int(params["no_of_posts"])]

    # Paggination Logic :   
        
    if(page==1):
        prev = "#"
        next = "/?page=" + str(page+1)    
    elif(page==last):
        prev = "/?page=" + str(page-1)   
        next = "#"
    else:
        next = "/?page=" + str(page+1)    
        prev = "/?page=" + str(page-1)   
         
    return render_template("index.html" ,params=params ,posts=posts ,prev=prev ,next=next)      # For used params you need to transfer params into all templates so html templates can use it.  
         
         
@app.route("/post/<string:post_slug>" ,methods=["GET"])      # Here slug is part of url which is represent blog identity in url
def post_route(post_slug):                  # Here You need to used post_slug variable into the def function also this is a rule

    post = Posts.query.filter_by(slug= post_slug).first()     # This is code for the featch the post from the database table .  {Note : We are know Posts class is contain database table contain }
    # Note : Here post is one type of "class instance" you can acsess data using post.variable name into the html file.about
    
    return render_template("post.html" ,post=post ,params=params)


@app.route("/dashboard" ,methods=["GET" ,"POST"])     # In Admin Dashboard only admin login for the stored the post
def dashboard():

    if ("user" in session and session["user"] == params["admin_username"]):          # If Your user already is login or already in session then don't need to again login
        posts = Posts.query.filter_by().all()
        return render_template("dashboard.html" ,params=params ,posts=posts)
    
    if(request.method == "POST"):
        
        username = request.form.get("admin_uname")
        upassword = request.form.get("admin_password")
        
        if (username == params["admin_username"] and upassword == params["admin_password"]):
            # Here we are create Session variabel for particular user 
            session["user"] = username       
            posts = Posts.query.filter_by().all()
            return render_template("dashboard.html" ,params=params ,posts=posts) 
            
    return render_template("login.html" ,params=params)


@app.route("/edit/<string:sno>" ,methods = ["GET" ,"POST"])
def edit(sno):
    
    if("user" in session and session["user"] == params["admin_username"]):          # When user click edit button that time we are check what user is in session or not
        if (request.method == "POST"):
            box_title = request.form.get("title")   
            tagline = request.form.get("tagline")
            slug = request.form.get("slug")  
            content = request.form.get("content")
            img_file = request.form.get("img_file")
    
            if(sno=="0"):    # Here we are consisder sno = 0 for the add new post into the databse
                post = Posts(title=box_title ,tagline=tagline ,slug=slug ,content=content ,img_file=img_file ,date=datetime.now())  
                db.session.add(post)  
                db.session.commit()
                posts = Posts.query.filter_by().all()
                return redirect("/edit/0")
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = box_title
                post.tagline = tagline
                post.slug = slug 
                post.content = content
                post.img_file = img_file
                post.date = datetime.now()
                db.session.commit()        # This is used for the commit the changes
                return redirect("/edit/"+sno)    # redirect is throw the get method for the change method  
                
        post = Posts.query.filter_by(sno=sno).first()    
        return render_template("edit.html" ,params=params ,post=post ,sno=sno)
    
    
@app.route("/uploader" ,methods=["GET" ,"POST"])
def uploader():
    if ("user" in session and session["user"] == params["admin_username"]):
        if(request.method == "POST"):
            f = request.files["upload_file"]
            f.save(os.path.join(app.config["UPLOAD_FOLDER"] ,secure_filename(f.filename)))       # This is used for the join application with the our stored file location with secure name 
            return "Uploaded Successfully"
        

@app.route("/delete/<string:sno>")
def delete(sno):
    if ("user" in session and session["user"] == params["admin_username"]): 
        post=Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()          # Commit database after deleted post 
        return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.pop("user")    # pop user into the session                      
    return redirect("/dashboard")


@app.route("/about")
def about():
    return render_template("about.html" ,params=params)

@app.route("/contact" ,methods=["GET" ,"POST"])
def contact():
    
    if(request.method == 'POST'):  
        
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        entry = Contacts(name=name , email = email ,ph_no=phone  ,msg=message ,date=datetime.now())  # Here We are create the Instance of the class
        db.session.add(entry)
        db.session.commit()
        # mail.send_message("New Message from " + name,
        #                   sender=email,
        #                   recipients=params["gmail-username"],              # Comment out becuase some problem with authentication in login in smpt server
        #                   body = message + "\n" + phone)
        
    return render_template("contact.html" ,params=params)

if __name__ == "__main__":
    app.run(debug=True)
