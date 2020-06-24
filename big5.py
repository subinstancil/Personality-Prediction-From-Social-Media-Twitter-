import pickle
from sklearn.feature_extraction.text import CountVectorizer
import plotly.express as px
import pandas as pd
import re
import csv


cEXT = pickle.load( open( "data/models/big5/cEXT.p", "rb"))
cNEU = pickle.load( open( "data/models/big5/cNEU.p", "rb"))
cAGR = pickle.load( open( "data/models/big5/cAGR.p", "rb"))
cCON = pickle.load( open( "data/models/big5/cCON.p", "rb"))
cOPN = pickle.load( open( "data/models/big5/cOPN.p", "rb"))
vectorizer_31 = pickle.load( open( "data/models/big5/vectorizer_31.p", "rb"))
vectorizer_30 = pickle.load( open( "data/models/big5/vectorizer_30.p", "rb"))


def predict_personality(text):
    scentences = re.split("(?<=[.!?]) +", text)
    text_vector_31 = vectorizer_31.transform(scentences)
    text_vector_30 = vectorizer_30.transform(scentences)
    EXT = cEXT.predict(text_vector_31)
    NEU = cNEU.predict(text_vector_30)
    AGR = cAGR.predict(text_vector_31)
    CON = cCON.predict(text_vector_31)
    OPN = cOPN.predict(text_vector_31)
    return [EXT[0], NEU[0], AGR[0], CON[0], OPN[0]]



def big5_predict():
    with open('user.csv','rt') as f:
        csvReader=csv.reader(f)
        tweetList=[rows[0] for rows in csvReader]
    length=len(tweetList)
    res_list = []
    x=[0,0,0,0,0]
    for text in tweetList:
        pdtn=predict_personality(text)
        for i in range(0,5): 
            res_list.append(x[i] + pdtn[i])
        x=res_list
        res_list=[]
    # print(x)
    df = pd.DataFrame(dict(r=x, theta=['EXT','NEU','AGR', 'CON', 'OPN']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    fig.write_image("./static/assets/images/fig1.png")
    #fig.show()
    return x,length

# print (big5_predict())