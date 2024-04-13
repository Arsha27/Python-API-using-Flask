from flask import Flask, request,jsonify

app = Flask(__name__)   #to start a flask application

#create a route 
@app.route("/get-user/<user_id>")    #http method/path parameter dynamic path you can pass to a url

def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name" : "Arsha Renjith",
        "email": "arsha@example.com"
    }

    #query parameter- addition variable to pass
    
    extra= request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data),200


#creating a post request

@app.route("/create-user",methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data),201

if __name__ == "__main__":    #run our flask server
    app.run(debug=True)
