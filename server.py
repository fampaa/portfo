from flask import Flask, render_template, url_for, request, redirect
#here render_template is only usefull when you create "templates" folder and put your html file in there 
import csv
app = Flask(__name__)

print(__name__)

#"that means we don't necessaryily need to know what this is doing, what the code is doing underneath"   
#"we know just that this app dot root decorator gives us some extra tools for us build a server`"




# @app.route("/<username>/<int:post_id>")
# def hellow_world(username =None, post_id= None):
# 	# return "hellow, shivam!"
# 	# print(url_for('static', filename='clipboard.ico') )
#     return render_template('about.html', name = username, post_id =post_id)
     # return render_template('about.html', name = username, post_id =post_id )"Thank You, sir"
    # return "thank you mr" #in other word this return mean that what you want in return 

# @app.route("/about.html")
# def about():
# 	# return "hellow, shivam!"
#     return render_template('about.html') 

# @app .route("/favicon.ico")
# def blog():
#     return "<p>these are my thoughts on blogs</p>"   

 #favicon.ico put a little icon for website    

# @app.route("/works.html") 
# def works():      
#     return render_template('works.html')




# @app.route("/blog/2021/dogs") 
# def blog2():      
#     return "<p>this is my dog</p>"   

@app.route("/")
def my_home():
	# return "hellow, shivam!"
    return render_template('index.html')   

@app.route('/<string:page_name>')
def html_page(page_name):
   return	render_template(page_name)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
 #1middle area-
     # return 'form submitted hoooraaayyy' #render_template('login.html', error=error)  
     if request.method == 'POST':
        try:
          data=request.form.to_dict() #an easy wat for grab this information is actually to do a method called .to_dict

        #NOTES -*********** .to_dict is turning something the form data into a dictionary  **************
        # print(data)
        # write_to_file(data)
          write_to_csv(data)
          return redirect('/Thankyou.html') 
        except:
         return "did not save to database"  
     else:
        return "something went wrong buddy, Try Again!"

def write_to_file(data):
    with open('database.txt', mode='a')as database:
        email = data["email"]
        subject = data["subject"]
        message =data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv',newline='', mode='a')as database2: #TIP Heads up! In the previous video we added a parameter newline='' to the csv.writer(). But instead, we should add it to our open statement
        email = data["email"]
        subject = data["subject"]
        message =data["message"]
        csv_writer = csv.writer(database2, delimiter= ',', quotechar=':' , quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
#NOTES: delimiter means that i want to sperate them by ','
           
 #middle area*******-    error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid    
#**************

#*******
#how to run this flask server by command like this : set FLASK_APP=server.py
#then just write flask run 
#*******
#for debug mode on : set FLASK_ENV=development

# --> flask run 
#*******
 