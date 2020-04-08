from django.shortcuts import render
from django.views.generic import ListView , DetailView
from . models import Tabliki


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
	corona = Corona.objects.all()
	return render(request , 'details.html', {'corona':corona})


def home(request):
	import json
	import requests
	statewise = requests.get("https://api.covid19india.org/state_district_wise.json")
	try:
		state_status = json.loads(statewise.content)
	except Exception as e:
		state_status = "Error"
	return render(request , 'home.html', {'state_status':state_status})


def total(request):
	import json
	import requests
	t = Tabliki.objects.all()
	country_cases = requests.get("https://api.covid19india.org/data.json")
	try:
		total = json.loads(country_cases.content)
	except Exception as e:
		total = "Error"
	p = total['statewise'][0]
	return render(request , 'total.html' , {'total':total , 't':t , 'p':p})



def stats(request):
	import json
	import requests
	t = Tabliki.objects.all()
	country_cases = requests.get("https://api.covid19india.org/data.json")
	try:
		total = json.loads(country_cases.content)
	except Exception as e:
		total = "Error"
	p = total['statewise'][0]
	return render(request , 'stats.html', {'t':t , 'total':total , 'p':p})

def for_stats(request):
	import json
	import requests
	t = Tabliki.objects.all()
	country_cases = requests.get("https://api.covid19india.org/data.json")
	try:
		total = json.loads(country_cases.content)
	except Exception as e:
		total = "Error"
	p = total['statewise'][0]['active']
	return render(request , 'for_stats.html', {'t':t , 'total':total, 'p':p})