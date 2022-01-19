import pickle
from flask import Flask,render_template,request

app=Flask(__name__)
model = pickle.load(open('linear-model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result',methods=['GET','POST'])
def result():
    area=request.form.get('area')
    bedrooms=request.form.get('bedrooms')
    bathrooms=request.form.get('bathrooms')
    stories=request.form.get('stories')
    mainroad=request.form.get('mainroad')
    guestroom=request.form.get('guestroom')
    basement=request.form.get('basement')
    hotwaterheating=request.form.get('hotwaterheating')
    airconditioning=request.form.get('airconditioning')
    parking=request.form.get('parking')
    prefarea=request.form.get('prefarea')
    furnishingstatus=request.form.get('furnishingstatus')
    print(area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus)
    prediction=model.predict([[area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus]])
    print(prediction)
    res=round(prediction[0],0)
    if(mainroad):
        mainroad='yes'
    else:
        mainroad='no'    
    if(guestroom):
        guestroom='yes'
    else:
        guestroom='no'    
    if(basement):
        basement='yes'
    else:
        basement='no'    
    if(hotwaterheating):
        hotwaterheating='yes'
    else:
        hotwaterheating='no'   
    if(airconditioning):
        airconditioning='yes'
    else:
        airconditioning='no'     
    if(prefarea):
        prefarea='yes'
    else:
        prefarea='no'     
    if(furnishingstatus):
        furnishingstatus='furnished'
    elif(furnishingstatus==0.5):
        furnishingstatus="semi-furnished"
    else:
        furnishingstatus='unfurnished'                 
    return render_template('result.html',result=res,input=[area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus])

if __name__ == '__main__':
    app.run(debug=True)    