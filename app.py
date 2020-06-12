from flask import *



#define as may functions as you want

def test_function():
    val="test"
    return val





app = Flask(__name__)  


@app.route('/')  
def home():
	val="Home" 
	return render_template("home.html", **locals())  

@app.route('/prediction',methods=['GET','POST'])  
def predict():  
	return render_template("prediction.html")


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


