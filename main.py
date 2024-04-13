from flask import Flask, request,jsonify

app = Flask(__name__)   #to start a flask application

#create a route 
@app.route("/")    #setting the default route 

def home():
    return "HOME"

if __name__ == "__main__":    #run our flask server
    app.run(debug=True)
