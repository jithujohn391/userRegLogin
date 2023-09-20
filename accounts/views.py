from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def loginPage(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password1']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' wecome {username} !!')
			return redirect('accounts:home')
		else:
			messages.info(request, f'account done not exit plz sign in')
	form = CreateUserForm()
	return render(request, 'accounts/loginpage.html', {'form':form, 'title':'log in'})


def registerPage(request):
	if request.method == 'POST':
	        form = CreateUserForm(request.POST)
	        if form.is_valid():
	            form.save()
	            messages.success(request, f'Your account has been created. You can log in now!')    
	            return redirect('accounts:home')
	else:
		form = CreateUserForm()
	return render(request, 'accounts/registerpage.html', {'form' : form})

@login_required
def logoutUser(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("accounts:home")




def home( request):
	return render(request, 'accounts/home.html')