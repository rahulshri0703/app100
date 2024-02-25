from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/")
def home():

    return "This is the page 22"

@app.route("/sum/<int:x>")
def sum(x):

    x = int(x)
    x = x *100

    return f"The sum is {x}"

@app.route("/predict", methods=["GET","POST"])
def predict():
    j = request.get_json()

    a = int(j["x"])
    b = int(j["y"])
    c = int(j["z"])

    s = a+b +c

    return jsonify({"sum":s})


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3000)