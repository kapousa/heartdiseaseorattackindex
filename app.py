import requests as requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("index.html", res="None")


@app.route('/predictheartdiseaseorattackindex', methods=['POST'])
def predictheartdiseaseorattackindex():
    # Read input values
    Stroke = 1 if request.form.get("Stroke") == 'on' else 0
    Smoker = request.form.get("Smoker")
    BMI = request.form.get("BMI")
    PhysActivity = request.form.get("PhysActivity")
    Fruits = request.form.get("Fruits")
    PhysHlth = request.form.get("PhysHlth")
    HighBP = request.form.get("HighBP")
    DiffWalk = request.form.get("DiffWalk")
    NoDocbcCost = request.form.get("NoDocbcCost")
    HighChol = request.form.get("HighChol")
    GenHlth = request.form.get("GenHlth")
    MentHlth = request.form.get("MentHlth")
    Sex = request.form.get("Sex")
    Diabetes = request.form.get("Diabetes")
    Income = request.form.get("Income")
    AnyHealthcare = request.form.get("AnyHealthcare")
    HvyAlcoholConsump = request.form.get("HvyAlcoholConsump")
    Education = request.form.get("Education")
    CholCheck = request.form.get("CholCheck")
    Veggies = request.form.get("Veggies")
    Age = request.form.get("Age")

    # URL = 'http://127.0.0.1:5000/api/v1/79165892196618/classifydata'
    URL = 'https://bmapiproject.herokuapp.com/api/v1/35587627934582/predictevalues'

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {
        'Stroke': 1 if request.form.get("Stroke") == 'on' else 0,
        'Smoker': 1 if request.form.get("Smoker") == 'on' else 0,
        'BMI': request.form.get("BMI"),
        'PhysActivity': 1 if request.form.get("PhysActivity") == 'on' else 0,
        'Fruits': 1 if request.form.get("Fruits") == 'on' else 0,
        'PhysHlth': request.form.get("PhysHlth"),
        'HighBP': 1 if request.form.get("HighBP") == 'on' else 0,
        'DiffWalk': 1 if request.form.get("DiffWalk")== 'on' else 0,
        'NoDocbcCost': 1 if request.form.get("NoDocbcCost") == 'on' else 0,
        'HighChol': 1 if request.form.get("HighChol") == 'on' else 0,
        'GenHlth': request.form.get("GenHlth"),
        'MentHlth': request.form.get("MentHlth"),
        'Sex': request.form.get("Sex"),
        'Diabetes': request.form.get("Diabetes"),
        'Income': request.form.get("Income"),
        'AnyHealthcare': 1 if request.form.get("AnyHealthcare") == 'on' else 0,
        'HvyAlcoholConsump': 1 if request.form.get("HvyAlcoholConsump") == 'on' else 0,
        'Education': request.form.get("Education"),
        'CholCheck': 1 if request.form.get("CholCheck") == 'on' else 0,
        'Veggies': 1 if request.form.get("Veggies") == 'on' else 0,
        'Age': request.form.get("Age")
    }

    # sending get request and saving the response as response object
    r = requests.post(url=URL, json=PARAMS)
    res = "None"
    if r.status_code == 200:
        return_data = r.json()
        for k, v in return_data.items():
            res = 'Yes' if v == '0' else 'No'

    return render_template("index.html", res=res)


if __name__ == '__main__':
    app.run()
