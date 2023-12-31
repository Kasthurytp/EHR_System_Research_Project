from django.urls import path

from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('login',views.login,name='login'),
    path('searchUser',views.searchUser,name='searchUser'),
    path('newDoctor',views.newDoctor,name='newDoctor'),
    path('newPatient',views.newPatient,name='newPatient'),  
    path('newNurse',views.newNurse,name='newNurse'),
    path('users',views.users,name='users'),
    path('ePriscribing',views.ePriscribing,name='ePriscribing'),
    path('yourPractice', views.yourPractice, name='yourPractice'),
    path('laps', views.laps, name='laps'),
    path('admin_searchUserDashboard/<str:doctor_id>/',views.admin_searchUserDashboard,name='admin_searchUserDashboard'), 
    path('testing',views.testing,name='testing'),
    path('appointment',views.appointment,name='appointment'),
    path('medicalBills',views.medicalBills,name='medicalBills'), 
    path('medicalRecords',views.medicalRecords,name='medicalRecords'),
    path('medications',views.medications,name='medications'),
    path('adminDashboard',views.adminDashboard,name='adminDashboard'),
    path('doctorDashboard',views.doctorDashboard,name='doctorDashboard'),  
    path('patients',views.patients,name='patients'), 
    path('doctors',views.doctors,name='doctors'), 
    path('nurses',views.nurses,name='nurses'),
    path('newPrescription',views.newPrescription,name='newPrescription'),
    path('newAppointment',views.newAppointment,name='newAppointment'),
    path('newMedicalRecord',views.newMedicalRecord,name='newMedicalRecord'),
    path('newReport',views.newReport,name='newReport'),
    path('newMedicalBill',views.newMedicalBill,name='newMedicalBill'),
    path('newMedication',views.newMedication,name='newMedication'),
    path('doctorAppointment',views.doctorAppointment,name='doctorAppointment'),
    path('doctor_searchPatient',views.doctor_searchPatient,name='doctor_searchPatient'), 
    path('doctorMedicalBill', views.doctorMedicalBill, name='doctorMedicalBill'),
    path('doctorBillPayment', views.doctorBillPayment, name='doctorBillPayment'),
]