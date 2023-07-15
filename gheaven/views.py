from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import User, Game, Genre, App, AppsGenre, Order, Payment, PC, Activity
from django.contrib import messages
from datetime import datetime,time, timedelta, date
import time
from django.contrib.auth import logout
# Create your views here.

# User Views

def login(request):
    if request.method == 'POST':
        username = str(request.POST['username'])
        password = str(request.POST['password'])
        et = timedelta(minutes=5)
        games = Game.objects.all()
        

        if username=="host":
            if password=="host":
                return redirect('dashboard')

        user = User.objects.get(username=username)
        apps = App.objects.all()
        if user :
            if user.password == password:
                if user.remaining_time > et :
                    pcid = 1
                    pc = PC.objects.get(pc_number = pcid)
                    pc.username = user.username
                    pc.remaining_time = user.remaining_time
                    pc.availability_status = False
                    pc.save()
                    curr = time.localtime()
                    currtime = time.strftime("%H:%M:%S", curr)
                    activity = Activity.objects.create(user=user, start_time=currtime,activity_type="Logged In")
                    activity.save()
                    return render(request, "gheaven/home.html", {
                        "user" : user,
                        "games" : games,
                        "apps" : apps,
                        "timer" : user.remaining_time
                    })
                else :
                    prices = {
                        "one" : 70,
                        "two" : 130,"three" : 250,}
                    return render(request, "gheaven/lowTimeShop.html", {
                        "user" : user,
                        "packageprice" : prices,
                        "timer" : user.remaining_time   
                    })
            
        
               
    
    return render(request, "gheaven/login.html")

def register(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phonenumber = request.POST['phonenumber']
        dob = request.POST['dob']

        if User.objects.filter(username = username).exists():
            messages.warning(request, "Username already exists")
            return HttpResponseRedirect(request.path_info)

        newuser = User.objects.create()
        newuser.first_name = firstname
        newuser.last_name = lastname
        newuser.email = email
        newuser.password = password
        newuser.username = username
        newuser.phone_number = phonenumber
        newuser.date_of_birth = dob

        try :
            newuser.save()
            msg = "Successful"
            return render(request, "gheaven/alert.html", {"msg" : msg})


        except Exception as e:
            print("An error occurred while saving:", str(e))        

            return redirect('register-page')

    return render(request, "gheaven/register.html")

def logout_view(request):
    if request.method == "POST":
        usernm = request.POST['username']
        pcid = 1
        pc = PC.objects.get(pc_number = pcid)
        pc.availability_status = True
        pc.username = ""
        pc.remaining_time = None
        pc.save()
        tim = str(request.POST['timer'])
        time_parts = tim.split(":")

        hours = int(time_parts[0])
        minutes = int(time_parts[1])
        seconds = int(time_parts[2])
        tt = timedelta(hours=hours, minutes=minutes, seconds=seconds)

        user = User.objects.get(username=usernm)
        user.remaining_time = tt
        user.save()

        curr = time.localtime()
        currtime = time.strftime("%H:%M:%S", curr)
        activity = Activity.objects.create(user=user, end_time=currtime,activity_type="Logged Out")
        activity.save()

        logout(request)

        return redirect('login-page')

def home(request, user, timer):

    user1 = User.objects.get(username=user)
    time = str(timer)
    time_parts = time.split(":")

    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2])

    tt = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    user1.remaining_time = tt
    user1.save()

    games = Game.objects.all()
    return render(request,'gheaven/home.html',{
        "user" : user1,
        "games" : games,
        "timer" : timer
    })

def games(request, user, timer):
    genre = Genre.objects.all()
    games = Game.objects.all()
    user1 = User.objects.get(username=user)
    time = str(timer)
    time_parts = time.split(":")

    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2])

    tt = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    user1.remaining_time = tt
    user1.save()
    return render(request,'gheaven/games.html',{
        "user" : user1,
        "games" : games,
        "genre" : genre,
        "timer" : timer
    })

def tagwisegames(request, user, genreid, timer):
    games = Game.objects.filter(genres=genreid)
    genre = Genre.objects.all()
    user1 = User.objects.get(username=user)
    time = str(timer)
    time_parts = time.split(":")

    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2])

    tt = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    user1.remaining_time = tt
    user1.save()
    return render(request,'gheaven/games.html',{
        "user" : user1,
        "games" : games,
        "genre" : genre,
        "timer" : timer
    })

def searchgame(request,timer):
    if request.method == "POST" :
        user = request.POST['username']
        gamename = request.POST['gamename']
        game = Game.objects.filter(name=gamename)
        user1 = User.objects.get(username=user)
        genre = Genre.objects.all()
        time = str(timer)
        time_parts = time.split(":")

        hours = int(time_parts[0])
        minutes = int(time_parts[1])
        seconds = int(time_parts[2])

        tt = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        user1.remaining_time = tt
        user1.save()
        if game.exists:
            return render(request,'gheaven/games.html',{
            "user" : user1,
            "games" : game,
            "genre" : genre,
            "timer" : timer
        })

def apps(request, user, timer):
    appsgenre = AppsGenre.objects.all()
    apps = App.objects.all()
    user1 = User.objects.get(username=user)
    time = str(timer)
    time_parts = time.split(":")

    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2])

    tt = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    user1.remaining_time = tt
    user1.save()
    return render(request,'gheaven/apps.html',{
        "user" : user1,
        "apps" : apps,
        "appsgenre" : appsgenre,
        "timer" : timer
    })

def tagwiseapps(request, user, genreid, timer):
    apps = App.objects.filter(app_genre=genreid)
    appsgenre = AppsGenre.objects.all()
    user1 = User.objects.get(username=user)
    time = str(timer)
    time_parts = time.split(":")

    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2])

    tt = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    user1.remaining_time = tt
    user1.save()
    return render(request,'gheaven/apps.html',{
         "user" : user1,
        "apps" : apps,
        "appsgenre" : appsgenre,
        "timer" : timer,
    })

def searchapp(request, timer):
    user = request.GET['username']
    appname = request.GET['appname']
    apps = App.objects.filter(app_name=appname)
    user1 = User.objects.get(username=user)
    appsgenre = AppsGenre.objects.all()
    time = str(timer)
    time_parts = time.split(":")

    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2])

    tt = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    user1.remaining_time = tt
    user1.save()
    if apps.exists:
        return render(request,'gheaven/apps.html',{
       "user" : user1,
        "apps" : apps,
        "appsgenre" : appsgenre,
        "timer" : timer
    })

def shop(request, user, timer):
    prices = {
        "one" : 70,
        "two" : 130,
        "three" : 250,
    }
    user1 = User.objects.get(username=user) 
    time = str(timer)
    time_parts = time.split(":")

    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2])

    tt = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    user1.remaining_time = tt
    user1.save() 
    return render(request, "gheaven/shop.html", {
        "user" : user1,
        "packageprice" : prices,
        "timer" : timer
    })

def shopAddTime(request, user, timer):
    if request.method == 'POST':
        user = User.objects.get(username=user)
        my_values = request.POST['amount']
        time = request.POST['time']
        return render(request, "gheaven/lowtimepayment.html", {
            "user" : user,
            "amount" : my_values,
            "time" : time,
            "timer" : timer
        })
    

def shoppayment(request, user, timer):
    if request.method == 'POST':
        user = User.objects.get(username=user)
        my_values = request.POST['amount']
        time = request.POST['time']
        return render(request, "gheaven/payment.html", {
            "user" : user,
            "amount" : my_values,
            "time" : time,
            "timer" : timer
        })
    
def lowtimepayment(request, user, timer):
    if request.method == 'POST':
        user = User.objects.get(username=user)
        my_values = request.POST['amount']
        time = request.POST['time']
        return render(request, "gheaven/payment.html", {
            "user" : user,
            "amount" : my_values,
            "time" : time,
            "timer" : timer
        })
    
def paynow(request, user, timer):
    if request.method == 'POST':
        user =User.objects.get(username=user)
        totalamount = int(request.POST['totalamount'])
        time = str(request.POST['totaltime'])
        time_parts = time.split(":")

        hours = int(time_parts[0])
        minutes = int(time_parts[1])
        seconds = int(time_parts[2])

        tt = timedelta(hours=hours, minutes=minutes, seconds=seconds)


        prevTimer = str(timer)
        prev_time_parts = prevTimer.split(":")

        p_hours = int(prev_time_parts[0])
        p_minutes = int(prev_time_parts[1])
        p_seconds = int(prev_time_parts[2]) 

        p_tt = timedelta(hours=p_hours, minutes=p_minutes, seconds=p_seconds)
        nt = p_tt + tt


        ordertype = request.POST['ordertype']
        if user.account_balance > totalamount :
            neworder = Order.objects.create(user = user,total_amount = totalamount,total_time = tt,order_type = ordertype)

            neworder.save()
            msg = "Payment Successful"
            return render(request, "gheaven/payalert.html", {"msg" : msg, "user" : user, "timer" : nt})

        else :
            msg = "Payment Unsuccessful"
            return render(request, "gheaven/payalert.html", {"msg" : msg, "user" : user, "timer" : nt})
    


def account(request, user, timer):
    user1 = User.objects.get(username=user)
    time = str(timer)
    time_parts = time.split(":")

    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2])

    tt = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    user1.remaining_time = tt
    user1.save()
    return render(request,'gheaven/account.html',{
        "user" : user1,
        "timer" : timer
    })

def alert(request):
    return render(request, "gheaven/alert.html")

def payalert(request):
    return render(request, "gheaven/payalert.html")


def paymenthistory(request, user, timer):
    user1 = User.objects.get(username=user)
    orders = Order.objects.filter(user=user1)
    time = str(timer)
    time_parts = time.split(":")

    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2])

    tt = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    user1.remaining_time = tt
    user1.save()
    return render(request,'gheaven/paymenthistory.html',{
        "user" : user1,
        "orders" : orders,
        "timer" : timer
    })

def editaccount(request, user, timer):
    user1 = User.objects.get(username=user)
    time = str(timer)
    time_parts = time.split(":")

    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2])

    tt = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    user1.remaining_time = tt
    user1.save()
    return render(request,'gheaven/editaccount.html',{
        "user" : user1,
        "timer" : timer
    })

def editdetails(request, user, timer):
    
    if request.method == "POST":
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phonenumber = request.POST['phonenumber']
        dob = request.POST['dob']

        user1 = User.objects.get(username=user)

        user1.email = email
        user1.first_name = firstname
        user1.last_name = lastname
        user1.phone_number = phonenumber
        user1.date_of_birth = dob
        user1.save()

        return render(request,'gheaven/account.html',{
        "user" : user1,
        "timer" : timer
        })

    
    
    # return render(request,'gheaven/games.html',{
    #     "user" : user1,
    #     "games" : games,
    #     "genre" : genre,
    # })


# Admin views
def dashboard(request):
    today = date.today()
    current_month = datetime.now().month
    orders = Order.objects.filter(date_and_time = today)
    thismonthorders = Order.objects.filter(date_and_time__month= current_month)
    allpc = PC.objects.all()
    pccount = PC.objects.count()
    ord_amt = []
    tmo = []
    
    for order in orders :
        ord_amt.append(order.total_amount)
    if orders.exists() :
        todaysincome = sum(ord_amt)
    else :
        todaysincome = 0

    for ords in thismonthorders :
        tmo.append(ords.total_amount)
    
    if thismonthorders.exists():
        monthsincome = sum(tmo)
    else : 
        monthsincome = 0

    return render(request, "gheaven/admin/dashboard.html", {
        "todaysincome" : todaysincome,
        "monthsincome" : monthsincome,
        "allpc" : allpc,
        "pccount" : pccount
    })


def orders(request):
    payments = Payment.objects.all().order_by('-id')

    return render(request, "gheaven/admin/orders.html", {
        "payments" : payments
    })

def users(request):
    allusers = User.objects.all().order_by('-id')
    return render(request, "gheaven/admin/users.html", {
        "allusers" : allusers
    })

def activity(request):
    allactivity = Activity.objects.all().order_by('-id')
    return render(request, "gheaven/admin/activity.html",{
        "allactivities" : allactivity
    })


def addUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phonenumber = request.POST['phonenumber']
        dob = request.POST['dob']

        if User.objects.filter(username = username).exists():
            messages.warning(request, "Username already exists")
            return HttpResponseRedirect(request.path_info)

        newuser = User.objects.create()
        newuser.first_name = firstname
        newuser.last_name = lastname
        newuser.email = email
        newuser.password = password
        newuser.username = username
        newuser.phone_number = phonenumber
        newuser.date_of_birth = dob

        try :
            newuser.save()


        except Exception as e:
            print("An error occurred while saving:", str(e))        

            return redirect('addUSer')
        
    return render(request, "gheaven/admin/addUser.html")
    

