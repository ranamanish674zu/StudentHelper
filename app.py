from flask import Flask, render_template,redirect,request
# from sklearn.externals import joblib#library to load model
import joblib
app=Flask(__name__)
model=joblib.load("MarkPrediction\model.pkl")#loading the model 
#first route - main directory 
@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/',methods=['POST'])
def marks():
     if request.method=='POST':
        #   taking the input in hours variable
          hours=float(request.form['number'])
          #applying the ml using model(contains model)
          marks=str(model.predict([[hours]])[0][0])
     return render_template("index.html",your_marks =marks)

if __name__=='__main__':
    #   app.debug==True
      app.run(debug=True)