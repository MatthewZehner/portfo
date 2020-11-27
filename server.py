from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)
import csv

@app.route('/')
def home1():
    return render_template('index.html')

@app.route('/index.html')
def home2():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_name(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	# write_to_file(data)
    	write_to_csv(data)
    	return redirect('/thankyou.html')
    else:
    	return 'something went wrong, try again'

# def write_to_file(data):
# 	with open("database.txt", mode='a') as database:
# 		name = data["name"]
# 		email = data["email"]
# 		topic = data["topic"]
# 		message = data["message"]
# 		text = database.write(f"\n{name},{email},{topic},{message}")

def write_to_csv(data):
	with open("database.csv", mode='a') as database2:
		name = data["name"]
		email = data["email"]
		topic = data["topic"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
		csv_writer.writerow([name,email,topic,message])