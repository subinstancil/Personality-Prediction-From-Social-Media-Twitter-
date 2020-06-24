from flask import *
import sys
import os
import time
import big5
import mbti
import tweepy_config

api = tweepy_config.api



#define as may functions as you want

def test_function(user1):
	user = api.get_user(user1)
	# expanded_url = user.entities['url']['urls'][0]['expanded_url']
	# display_url = user.entities['url']['urls'][0]['display_url']
	return user.profile_image_url,user.name,user.description





app = Flask(__name__)  


@app.route('/')  
def home():
	val="Home" 
	# os.remove('./static/assets/images/fig1.png')
	return render_template("home.html", **locals())  

@app.route('/prediction',methods=['GET','POST'])  
def predict():
	if request.method == 'POST':
		username = request.form['uname']
		mbti_score = mbti.mbti_predict(username)
		profile_image, name, des = test_function(username)
		print(profile_image)
		print(mbti_score)
		val= mbti_score
		traits, length = big5.big5_predict()
		ext=traits[0]
		neu=traits[1]
		agr=traits[2]
		con=traits[3]
		opn=traits[4]
		pext=int((traits[0]/800)*100)
		pneu=int((traits[1]/800)*100)
		pagr=int((traits[2]/800)*100)
		pcon=int((traits[3]/800)*100)
		popn=int((traits[4]/800)*100)
		os.remove('user.csv')
		# print(ext,pext)
		return render_template("prediction.html", **locals())
	return render_template("home.html", **locals())

@app.route('/txtpredict')  
def tpredict():
	val="Text Predictor" 
	return render_template("tpredict.html", **locals())

@app.route('/main')  
def main():
	val="Home" 
	return render_template("main.html", **locals()) 




if __name__ == '__main__':  
	app.run(threaded=True)  
	app.debug = True


