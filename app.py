from flask import Flask, render_template, request
import pickle

filename = "spam_classification_model.pkl"
cv = pickle.load(open("transform.pkl", "rb"))
model = pickle.load(open(filename, "rb"))


app = Flask(__name__, template_folder="template")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    hypothesis = None
    if request.method == "POST":
        message = request.form["message"]
        data = [message]
        features = cv.transform(data).toarray()
        hypothesis = model.predict(features)
    return render_template("result.html", prediction=hypothesis[0])


if __name__ == "__main__":
    app.run()
