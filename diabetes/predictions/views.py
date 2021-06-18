import pandas as pd

from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, DetailView, TemplateView
from .models import Patient
from .forms import NewPatientrecord
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def get_prediction(input):
    data = pd.read_csv(r'C:\Users\26377\Documents\Capstone\HIT-400\diabetes.csv')

    # training the model to be used for prediction in the final prediction of the system
    X = data.drop("Outcome", axis=1)
    Y = data["Outcome"]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20)

    # model training of the data for prediction
    model = LogisticRegression(solver="lbfgs", max_iter=1000)
    model.fit(X_train, Y_train)

    # get input values
    val1 = float(input['pregnancies'])
    val2 = float(input['glucose'])
    val3 = float(input['blood_pressure'])
    val4 = float(input['skin_thickness'])
    val5 = float(input['insulin'])
    val6 = float(input['BMI'])
    val7 = float(input['diabetes_pedigree_function'])
    val8 = float(input['age'])

    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
    result1 = ""
    if pred == [0]:
        result1 += "Negative"
    else:
        result1 += "Positive"

    # save to db
    Patient.objects.create(
        pregnancies=val1, glucose=val2, blood_pressure=val3, skin_thickness=val4,
        insulin=val5, BMI= val6, diabetes_pedigree_function= val7, age=val8, result=result1
    ).save()
    return result1


class Dashboard(TemplateView):
    template_name = 'predictions/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        records = Patient.objects.all()
        context['records'] = records
        context['records_count'] = len(records)
        context['negatives'] = len([rec for rec in records if rec.result == 'Negative'])
        context['positives'] = len([rec for rec in records if rec.result == 'Positive'])
        return context


class CreatePatientRecordView(CreateView):
    model = Patient
    form_class = NewPatientrecord

    def post(self, request, *args, **kwargs):
        result = get_prediction(request.POST)
        # return redirect('/predictions')
        # return self.get(request=request, result=self.result)
        return render(request, 'predictions/patient_form.html', { 'form': self.get_form(NewPatientrecord), 'classification_result': result })


class PatientRecordListView(ListView):
    model = Patient
    context_object_name = 'records'


class PatientRecordDetail(DetailView):
    model = Patient

