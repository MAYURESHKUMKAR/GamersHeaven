from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import User, Game, Genre, App, AppsGenre
from django.contrib import messages
# Create your views here.

# User Views

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        games = Game.objects.all()
        user = User.objects.get(username=username)
        if user :
            if user.password == password:
                return render(request, "gheaven/home.html", {
                    "user" : user,
                    "games" : games,
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

        userobj = User.objects.filter(username = username)

        if userobj.exists:
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

        
    return render(request, "gheaven/register.html")


def home(request, user):
    user1 = User.objects.get(username=user)
    games = Game.objects.all()
    return render(request,'gheaven/home.html',{
        "user" : user1,
        "games" : games,
    })

def games(request, user):
    genre = Genre.objects.all()
    games = Game.objects.all()
    user1 = User.objects.get(username=user)
    return render(request,'gheaven/games.html',{
        "user" : user1,
        "games" : games,
        "genre" : genre,
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

def apps(request, user):
    appsgenre = AppsGenre.objects.all()
    apps = App.objects.all()
    user1 = User.objects.get(username=user)
    return render(request,'gheaven/apps.html',{
        "user" : user1,
        "apps" : apps,
        "appsgenre" : appsgenre,
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

def shop(request, user):
    user1 = User.objects.get(username=user)  
    return render(request, "gheaven/shop.html", {
        "user" : user1,
    })

def account(request, user):
    user1 = User.objects.get(username=user)
    return render(request,'gheaven/account.html',{
        "user" : user1
    })

def alert(request):
    return render(request, "gheaven/alert.html")




    
    
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