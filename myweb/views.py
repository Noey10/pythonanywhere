from myweb.models import Cactus
from myweb.form import showOrders
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
    return render(request, 'myweb/signUp.html', {'form': form})

def index(req):
	return render(req, 'myweb/index.html')

def shop(req):
    if req.method == "POST":
        name = req.POST['1']
        print(name)
        return render(req, "myweb/order.html",{'name':name})
    return render(req, 'myweb/shop.html')

def logIn(req):
    if req.method == "POST":
        print("Hello")
        Username = req.POST.get("username")
        Password = req.POST.get("password1")
        print(Username,Password)
        user = authenticate(username=Username, password=Password)
        if user is not None:
            login(req, user)
            return render(req,'myweb/shop.html')

    return render(req, 'myweb/logIn.html')

def order(req):
    if req.method == "POST":
        form = showOrders(req.POST)
        if form.is_valid():
            searchby = form.cleaned_data['cactusName']
            addamount = form.cleaned_data['addamount']

            #print("Searchby is :",searchby,type(searchby))
            #print("addamount is :",addamount,type(addamount))
            ordercactus = Cactus.objects.all()

            for i in ordercactus:
                print("i-id : ",i.id ,"i : ",i.cactusName)
                print(i)
                #print(string)
                if searchby == str(i.cactusName):
                    trueorder = Cactus.objects.all()
                    updateamout = Cactus.objects.get(cactusName=i.cactusName)
                    #print("It in if : ",i.id)

                    updateamout.amout = int(updateamout.amout) + int(addamount)
                    updateamout.save()
            return render(req , "myweb/yourorder.html",{"trueorder":trueorder})

    else:
        form = showOrders()
        context = {'form':form}
        return render(req, 'myweb/order.html',context)

def yourorder(req):
    return render(req, 'myweb/yourorder.html')

def test(req):
    return render(req, 'myweb/test.html')

def showorder(req):
        return render(req, 'myweb/order.html')

def united(req):
	return render(req, 'myweb/united.html')

def contact(req):
	return render(req, 'myweb/contact.html')

def about(req):
	return render(req, 'myweb/about.html')


 # default function #

def detail(request, question_id):
    return render(request, 'myweb/detail.html')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)