from django.urls import path
from .views import (
    CreatePatientRecordView, PatientRecordDetail,
    PatientRecordListView, Dashboard)

app_name = 'predictions'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('new-record', CreatePatientRecordView.as_view(), name='new_patient'),
    path('records', PatientRecordListView.as_view(), name='patients'),
    path('record/<int:pk>', PatientRecordDetail.as_view(), name='new_patient'),
]