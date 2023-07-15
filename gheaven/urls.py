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
    path('payment/<user>/<timer>', views.shoppayment, name='payment'),
    path("lowtimepayment/<user>/<timer>", views.shopAddTime, name="lowtimepayment"),
    path('paynow/<user>/<timer>',views.paynow, name="paynow"),
    path("account/<user>/<timer>", views.account, name="account"),
    path("alert", views.alert, name="alert"),
    path("payalert/<timer>", views.payalert, name="payalert"),
    path("games/<user>/<genreid>/<timer>", views.tagwisegames, name="tagwisegames"), 
    path("games/<timer>", views.searchgame, name="searchgame"), 
    path("apps/<user>/<genreid>/<timer>", views.tagwiseapps, name="tagwiseapps"),
    path("apps/<timer>", views.searchapp, name="searchapp"), 
    path("paymenthistory/<user>/<timer>", views.paymenthistory, name="paymenthistory"),
    path("editaccount/<user>/<timer>", views.editaccount, name="editaccount"),
    path("editdetails/<user>/<timer>",views.editdetails, name="editdetails"),
    path('logout/', views.logout_view, name='logout'),

    #admin below
    path("dashboard", views.dashboard, name="dashboard"),
    path("activity", views.activity, name="activity"),
    path("addUser", views.addUser, name="addUser"),
    path("orders", views.orders, name="orders"),
    path("users", views.users, name="users"),
]
