from django.urls import path
from . import views


urlpatterns = [
    #user below
    path("", views.login, name="login-page"),
    path("register",views.register, name="register-page"),
    path("home/<user>/<timer>", views.home, name="home"),
    path("games/<user>/<timer>", views.games, name="games"),
    path("apps/<user>/<timer>", views.apps, name="apps"),
    path("shop/<user>/<timer>", views.shop, name="shop"),
    path('payment/<user>', views.shoppayment, name='payment'),
    path("lowtimepayment/<user>/<timer>", views.shopAddTime, name="lowtimepayment"),
    path('paynow/<user>/<timer>',views.paynow, name="paynow"),
    path("account/<user>/<timer>", views.account, name="account"),
    path("alert/<msg>", views.alert, name="alert"),
    path("payalert/<timer>", views.payalert, name="payalert"),
    path("games/<user>/<genreid>", views.tagwisegames, name="tagwisegames"), 
    path("games", views.searchgame, name="searchgame"), 
    path("apps/<user>/<genreid>", views.tagwiseapps, name="tagwiseapps"),
    path("apps", views.searchapp, name="searchapp"), 
    path("paymenthistory/<user>", views.paymenthistory, name="paymenthistory"),
    path('logout/', views.logout_view, name='logout'),

    #admin below
    path("dashboard", views.dashboard, name="dashboard"),
    path("activity", views.activity, name="activity"),
    path("addGame", views.addGame, name="addGame"),
    path("addUser", views.addUser, name="addUser"),
    path("orders", views.orders, name="orders"),
    path("statistics", views.statistics, name="statistics"),
    path("users", views.users, name="users"),
]
