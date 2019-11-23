from django.shortcuts import render
# Create your views here.






def home(request):
	return render(request, 'index.html')



#Register for new user
def register(request):
	return render(request, 'register.html')

#login view
def login(request):
	return render(request, 'login.html')

#logout
def logout(request):
	return render(request, 'logout.html')