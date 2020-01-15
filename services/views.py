from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import *

from django.http import *
import re
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from .forms import *


def checkType(username):
	l1 = user_info.objects.filter(username = username,user_type="Farmer")
	l2 = user_info.objects.filter(username = username,user_type="Customer")
	if len(l1)>0:
		return "Farmer"
	if len(l2)>0:
		return "Customer"
	return "NoOne"

def login_user(request):
	print("Reached Login View Successfully")
	if request.session.get('username',None) is not None :
		username = request.session['username']
		if checkType(username) == "Farmer":
			return HttpResponseRedirect('/site')
		elif checkType(username) == "Customer":
			return HttpResponseRedirect('/customer')

	if request.method =="POST":

		print("reached inside request")
		username = request.POST['username']
		password = request.POST['password']
		l = user_info.objects.filter(username = username,password=password)
		if len(l)>0:
			if checkType(username) == "Farmer":
				print("reached Farmer site")
				request.session['username'] = username
				return HttpResponseRedirect('/site')
			elif checkType(username) == "Customer":
				print("reached Customer site")
				request.session['username'] = username
				return HttpResponseRedirect('/customer')
		else:
			return render(request,'services/login.html')

	return render(request,'services/login.html')




def reg_user(request):
	# fields=['name','username','password','phone_no','address','user_type']

	print("Reached reg")
	if request.method=='POST':
		# print(request)
		userInstance = user_info()
		userInstance.name = request.POST.get("uname","") 
		userInstance.username = request.POST.get("username","")
		userInstance.password = request.POST.get("password","")
		userInstance.phone_no = request.POST.get("phone","")
		userInstance.user_type = request.POST.get("utype")
		userInstance.address = 'IIITG'
		userInstance.save()
		return HttpResponseRedirect('/login')
	return render(request,'services/register.html')

# def site(request):
# 	print("inside site view")
# 	return render(request,'services/site.html')

def view_detail(request):
	return render(request, 'services/site.html')
def view_detail_db(request):
	currentUser = request.session['username']
	user_list = farm_details.objects.filter(username=currentUser);
	for u in user_list:
		print(u.username,u.crop)
	return render(request,'services/view_detail_db.html',{'view_detail': user_list})

def logout(request):
	request.session['username'] = {}
	# todo: do this for all session variables
	return HttpResponseRedirect('/login')

def customer(request):
	allUsers = farm_details.objects.all()
	return render(request, 'services/customer.html',{'allDetail': allUsers})
def buy(request):
	return render(request, 'services/buy.html')
