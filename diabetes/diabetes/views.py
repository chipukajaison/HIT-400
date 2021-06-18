from django.shortcuts import render

# import of machine learning code
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def login(request):
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def profile(request):
    return render(request, 'profile.html')


def classify(request):
    return render(request, 'classify.html')


def classification_result(request):
    data = pd.read_csv(r'C:\Users\26377\Documents\Capstone\HIT-400\diabetes.csv')

    # training the model to be used for prediction in the final prediction of the system
    X = data.drop("Outcome", axis=1)
    Y = data["Outcome"]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20)

    # model traing of the data for prediction
    model = LogisticRegression(solver="lbfgs", max_iter=1000)
    model.fit(X_train, Y_train)

    # get input values
    val1 = float(request.GET['pregnancies'])
    val2 = float(request.GET['glucose'])
    val3 = float(request.GET['blood_pressure'])
    val4 = float(request.GET['skin'])
    val5 = float(request.GET['insulin'])
    val6 = float(request.GET['bmi'])
    val7 = float(request.GET['diabetes_pf'])
    val8 = float(request.GET['age'])

    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
    result1 = ""
    if pred == [0]:
        result1 += "Negative"
    else:
        result1 += "Positive"

    return render(request, 'classify.html', {"classification_result": result1})


def predict(request):
    return render(request, 'predict.html')


def result(request):
    return render(request, 'predict.html')