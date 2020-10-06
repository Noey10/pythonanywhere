from django.shortcuts import render,redirect
from django.http import HttpResponse


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('logIn')
    else:
        form = UserCreationForm()
    return render(request, 'myweb/register.html', {'form': form})

def index1(req):
	return render(req, 'myweb/index1.html')

def index(req):
	return render(req, 'myweb/index.html')

def shop(req):
	return render(req, 'myweb/shop.html')

def login_active(req):
    if req.method =="POST":
        Username = req.POST.get("username")
        Password = req.POST.get("password")
        user = authenticate(username=Username, password=Password)
        if user is not None:
            login(req, user)
            return render(req,'myweb/shop.html')

def logIn_page(req):
	return render(req, 'myweb/logIn.html')

def united(req):
	return render(req, 'myweb/united.html')

def contact(req):
	return render(req, 'myweb/contact.html')

def about(req):
	return render(req, 'myweb/about.html')

def detail(request, question_id):
    return render(request, 'myweb/detail.html')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)