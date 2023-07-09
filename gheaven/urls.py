from django.urls import path
from . import views


urlpatterns = [
    #user below
    path("", views.login, name="login-page"),
    path("register",views.register, name="register-page"),
    path("home/<user>", views.home, name="home"),
    path("games/<user>", views.games, name="games"),
    path("apps/<user>", views.apps, name="apps"),
    path("shop/<user>", views.shop, name="shop"),
    path("account/<user>", views.account, name="account"),
    path("alert/<msg>", views.alert, name="alert"),
    path("games/<user>/<genreid>", views.tagwisegames, name="tagwisegames"), 
    path("games", views.searchgame, name="searchgame"), 
    path("apps/<user>/<genreid>", views.tagwiseapps, name="tagwiseapps"),
    path("apps", views.searchapp, name="searchapp"), 
    #admin below
    path("dashboard", views.dashboard, name="dashboard"),
    path("activity", views.activity, name="activity"),
    path("addGame", views.addGame, name="addGame"),
    path("addUser", views.addUser, name="addUser"),
    path("orders", views.orders, name="orders"),
    path("statistics", views.statistics, name="statistics"),
    path("users", views.users, name="users"),
]
