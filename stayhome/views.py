from django.shortcuts import render
from django.views.generic import ListView , DetailView


def patients(request):
	import json
	import requests

	api_patients = requests.get("https://api.covid19india.org/raw_data.json")

	try:
		patients_list = json.loads(api_patients.content)
	except Exception as e:
		patients_list="Error"
	return render(request , 'patients.html' , {'patients_list':patients_list}) 


def details(request):

	return render(request , 'details.html', {})


def home(request):
	import json
	import requests
	statewise = requests.get("https://api.covid19india.org/state_district_wise.json")
	try:
		state_status = json.loads(statewise.content)
	except Exception as e:
		state_status = "Error"
	return render(request , 'home.html', {'state_status':state_status})