from flask import *
import sys
import os
import time
import big5
import mbti
import tweepy



ckey='Hud29LI3lWB4Xv94VJ9zBzb8N'
csecret='5nk2iu5lff96BCU6dGayGaMcZWwCQDZ0agsyYGNW8TCIPf9rvm'
atoken='1142590141-khS8xY5ekC12xOkl29QsIBwdv89dgxgOkaURGEI'
asecret='JM0sjDJzI8bF6ZvGMfUO2wsq11mdiOcZ3xc1QoCNJjfhn'
auth=tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api=tweepy.API(auth)




#define as may functions as you want

def test_function(user1):
	user = api.get_user(user1)
	# print(user.name)
	# print(user.description)
	# print(user.followers_count)
	# print(user.statuses_count)
	# print(user.profile_image_url)
	# expanded_url = user.entities['url']['urls'][0]['expanded_url']
	# display_url = user.entities['url']['urls'][0]['display_url']
	# print(user)
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

# @app.route('/location')  
# def location():  
# 	return render_template("location.html")  


# @app.route('/blocked_roads')  
# def blkd_roads():  
# 	return render_template("blocked_roads.html")  

# #methods is given to handle GET and POST request from webpage
# @app.route('/social_index',methods=['GET','POST'])  
# def scl_index():
# 	if request.method == 'POST':
# 		#         text = request.form['urls']
# 		no=1
# 		name="test"
# 		home="test"
# 		no_ppl=100
# 		return render_template("social_index.html", **locals())
# 	return render_template("social_index.html") 

# @app.route('/shelter_home_details')  
# def sltr_home():  
# 	return render_template("shltr_home_dtls.html") 








# @app.route('/scrap', methods = ['POST'])  
# def succesaass():
#     if request.method == 'POST':
#         text = request.form['urls']
#         rating, count, pstve = mainfunction(text)
#         if rating == "exit":	
#             rating, count, pstve = mainfunction(text)
#         else:
#             neg = int(count)-int(pstve)
#             return render_template("htl_rating.html", **locals())
#     return render_template("htl_rating.html", **locals())    
# 	# if request.method == 'POST':  
# 	# 	return render_template("1.html", name = "asd") 
# @app.route('/predict',methods=['GET','POST'])
# def predict():
#     if request.method == 'POST':
#         comment = request.form['comment']
#         my_prediction = NLPrun.pred(comment)
#         return render_template('result.html', prediction=my_prediction)
#     return render_template('predict.html')


# @app.route('/rte',methods=['GET','POST'])
# def rting():
#     if request.method == 'POST':
#         return render_template('rating.html')
#     return render_template('rating.html')




# @app.route('/ratelist',methods=['GET','POST'])
# def ratelist():
#     listOfUrls = []
#     with open('listfile.txt', 'r') as filehandle:
#         for line in filehandle:
#             urls = line[:-1]
#             listOfUrls.append(urls)
#     if request.method == 'POST':
#         text = request.form['url']
#         cont=1       
#         for i in listOfUrls:
#             print("xx")
#             if i == text:
#                 string_url = str(cont)+".txt"
#                 print(string_url)
#                 rating, count, pstve = NLPrun.rate(string_url)
#                 print(rating, count, pstve)
#             cont +=1
#         neg = int(count)-int(pstve)
#         return render_template("htl_rating.html", **locals())
#     return render_template('ratelist.html', len = len(listOfUrls), ListOfUrls = listOfUrls)


if __name__ == '__main__':  
	app.run(threaded=True)  
	app.debug = True


