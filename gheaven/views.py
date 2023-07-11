from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import User, Game, Genre, App, AppsGenre, Order, Payment
from django.contrib import messages
from datetime import datetime,time, timedelta
from django.contrib.auth import logout
# Create your views here.

# User Views

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        et = timedelta(minutes=5)
        games = Game.objects.all()
        user = User.objects.get(username=username)
        apps = App.objects.all()
        if user :
            if user.password == password:
                if user.remaining_time > et :
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
            return redirect('alert', args=(msg))


        except Exception as e:
            print("An error occurred while saving:", str(e))        

            return redirect('register-page')

    # return render(request, "gheaven/register.html")

def logout_view(request):
    if request.method == "POST":
        usernm = request.POST['username']
        time = str(request.POST['timer'])
        time_parts = time.split(":")

        days = int(time_parts[0])
        hours = int(time_parts[1])
        minutes = int(time_parts[2])
        seconds = int(time_parts[3])
        tt = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

        user = User.objects.get(username=usernm)
        user.remaining_time = tt
        user.save()

        logout(request)

        return redirect('login-page')

def home(request, user, timer):

    user1 = User.objects.get(username=user)
    time = str(timer)
    time_parts = time.split(":")

    days = int(time_parts[0])
    hours = int(time_parts[1])
    minutes = int(time_parts[2])

    tt = timedelta(days=days, hours=hours, minutes=minutes)
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

    days = int(time_parts[0])
    hours = int(time_parts[1])
    minutes = int(time_parts[2])
    seconds = int(time_parts[3])

    tt = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    user1.remaining_time = tt
    user1.save()
    return render(request,'gheaven/games.html',{
        "user" : user1,
        "games" : games,
        "genre" : genre,
        "timer" : timer
    })

def tagwisegames(request, user, genreid):
    games = Game.objects.filter(genres=genreid)
    genre = Genre.objects.all()
    user1 = User.objects.get(username=user)
    return render(request,'gheaven/games.html',{
        "user" : user1,
        "games" : games,
        "genre" : genre,
    })

def searchgame(request):
    user = request.GET['username']
    gamename = request.GET['gamename']
    game = Game.objects.filter(name=gamename)
    user1 = User.objects.get(username=user)
    genre = Genre.objects.all()
    if game.exists:
        return render(request,'gheaven/games.html',{
        "user" : user1,
        "games" : game,
        "genre" : genre,
    })

def apps(request, user, timer):
    appsgenre = AppsGenre.objects.all()
    apps = App.objects.all()
    user1 = User.objects.get(username=user)
    time = str(timer)
    time_parts = time.split(":")

    days = int(time_parts[0])
    hours = int(time_parts[1])
    minutes = int(time_parts[2])
    seconds = int(time_parts[3])

    tt = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    user1.remaining_time = tt
    user1.save()
    return render(request,'gheaven/apps.html',{
        "user" : user1,
        "apps" : apps,
        "appsgenre" : appsgenre,
        "timer" : timer
    })

def tagwiseapps(request, user, genreid):
    apps = App.objects.filter(app_genre=genreid)
    appsgenre = AppsGenre.objects.all()
    user1 = User.objects.get(username=user)
    return render(request,'gheaven/apps.html',{
         "user" : user1,
        "apps" : apps,
        "appsgenre" : appsgenre,
    })

def searchapp(request):
    user = request.GET['username']
    appname = request.GET['appname']
    apps = App.objects.filter(app_name=appname)
    user1 = User.objects.get(username=user)
    appsgenre = AppsGenre.objects.all()
    if apps.exists:
        return render(request,'gheaven/apps.html',{
       "user" : user1,
        "apps" : apps,
        "appsgenre" : appsgenre,
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

    days = int(time_parts[0])
    hours = int(time_parts[1])
    minutes = int(time_parts[2])
    seconds = int(time_parts[3])

    tt = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
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
    

def shoppayment(request, user):
    if request.method == 'POST':
        user = User.objects.get(username=user)
        my_values = request.POST['amount']
        time = request.POST['time']
        return render(request, "gheaven/payment.html", {
            "user" : user,
            "amount" : my_values,
            "time" : time,
        })
    
def lowtimepayment(request, user):
    if request.method == 'POST':
        user = User.objects.get(username=user)
        my_values = request.POST['amount']
        time = request.POST['time']
        return render(request, "gheaven/payment.html", {
            "user" : user,
            "amount" : my_values,
            "time" : time,
        })
    
def paynow(request, user, timer):
    if request.method == 'POST':
        user =User.objects.get(username=user)
        totalamount = int(request.POST['totalamount'])
        totaltime = int(request.POST['totaltime'])
        tt = timedelta(hours=totaltime)
       
        ordertype = request.POST['ordertype']
        if user.account_balance > totalamount :
            neworder = Order.objects.create(user = user,total_amount = totalamount,total_time = tt,order_type = ordertype)

            neworder.save()
            msg = "Payment Successful"
            return render(request, "gheaven/payalert.html", {"msg" : msg, "user" : user.username, "timer" : timer})

        else :
            msg = "Payment Unsuccessful(low balance add from admin)"
            return render(request, "gheaven/payalert.html", {"msg" : msg, "user" : user.username, "timer" : timer})
    


def account(request, user, timer):
    user1 = User.objects.get(username=user)
    time = str(timer)
    time_parts = time.split(":")

    days = int(time_parts[0])
    hours = int(time_parts[1])
    minutes = int(time_parts[2])
    seconds = int(time_parts[3])

    tt = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
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


def paymenthistory(request, user):
    user1 = User.objects.get(username=user)
    orders = Order.objects.filter(user=user1)
    return render(request,'gheaven/paymenthistory.html',{
        "user" : user1,
        "orders" : orders
    })

def editdetails(request, user):
    user1 = User.objects.get(username=user)
    return render(request,'gheaven/paymenthistory.html',{
        "user" : user1,
    })

    
    
    # return render(request,'gheaven/games.html',{
    #     "user" : user1,
    #     "games" : games,
    #     "genre" : genre,
    # })


# Admin views

def activity(request):
    return render(request, "gheaven/admin/activity.html")

def addGame(request):
    return render(request, "gheaven/admin/addGame.html")

def addUser(request):
    return render(request, "gheaven/admin/addUser.html")

def dashboard(request):
    return render(request, "gheaven/admin/dashboard.html")

def orders(request):
    return render(request, "gheaven/admin/orders.html")

def statistics(request):
    return render(request, "gheaven/admin/statistics.html")

def users(request):
    return render(request, "gheaven/admin/users.html")