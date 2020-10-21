from myweb.models import Cactus, MyUser
from myweb.form import addUsers, Order, showOrders
from django.shortcuts import render,redirect
from django.http import HttpResponse


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def signUp(request):
    if request.method == 'POST':
        form = addUsers(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('logIn')
    else:
        form = addUsers()
    return render(request, 'myweb/signUp.html', {'form': form})

def index(req):
	return render(req, 'myweb/index.html')

def shop(req):
    if req.method == "POST":
        name = req.POST['1']
        print(name)
        return render(req, "myweb/order.html",{'name':name})
    return render(req, 'myweb/shop.html')

def login_active(req):
    if req.method =="POST":
        Username = req.POST.get("username")
        Password = req.POST.get("password")
        user = authenticate(username=Username, password=Password)
        if user is not None:
            login(req, user)
            return render(req,'myweb/logIn.html')

    return render(req, 'myweb/index.html')

def logIn_page(req):
	return render(req, 'myweb/logIn.html')

def order(req):
   """if req.method == "POST":
        form = showOrders(req.POST)
        if form.is_valid():
            searchby = form.cleaned_data['SearchBy']
            keyword = form.cleaned_data['keyword']
            if searchby == '1':
                cactusname = Cactus.objects.filter(cactusName__contains=keyword)
        return render(req , "myweb/ShowFruit.html",{"cactus":cactusname})
    else:
        form = showOrders()
        context = {'form':form}"""
	return render(req, 'myweb/order.html')

def yourorder(req):
    return render(req, 'myweb/yourorder.html')

def test(req):
    return render(req, 'myweb/test.html')

def showorder(req):
    if req.method == "POST":
        form = showOrders(req.POST)
        if form.is_valid():
            searchby = form.cleaned_data['ชื่อต้นกระบองเพชร']

            #### 1,2,3,4 ..เพิ่มได้เรื่อยๆ.. แต่ต้องก็อบโค้ดวาง แล้วเปลี่ยน searchby == "n" n = เลข id หรือ ต้นที่เท่าไหร่ ####
            if searchby == '1':

                ordercactus = Cactus.objects.filter(id__contains=searchby)
                print("this order is :",ordercactus)
                return render(req , "myweb/yourorder.html",{"ordercactus":ordercactus})
            elif searchby == '2':

                ordercactus = Cactus.objects.filter(id__contains=searchby)
                print("this order is :",ordercactus)
                return render(req , "myweb/yourorder.html",{"ordercactus":ordercactus})
            elif searchby == '3':

                ordercactus = Cactus.objects.filter(id__contains=searchby)
                print("this order is :",ordercactus)
                return render(req , "myweb/Allorder.html",{"ordercactus":ordercactus})
            elif searchby == '4':

                ordercactus = Cactus.objects.filter(id__contains=searchby)
                print("this order is :",ordercactus)
                return render(req , "myweb/yourorder.html",{"ordercactus":ordercactus})



    else:
        form = showOrders()
        context = {'form':form}
        return render(req, 'myweb/order.html',context)

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