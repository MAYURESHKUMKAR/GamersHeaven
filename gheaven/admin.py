from django.contrib import admin

# admin username : mayur password : root
# Register your models here.

from .models import PC,User,Activity,App,Game,Order,Payment,Genre,AppsGenre

class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name", "username", "remaining_time")

class PcAdmin(admin.ModelAdmin):
    list_display = ("pc_number","availability_status","username","remaining_time")

class AppAdmin(admin.ModelAdmin):
    list_display = ("app_name",)

class GameAdmin(admin.ModelAdmin):
    list_display = ("name",)

class OrderAdmin(admin.ModelAdmin):
    list_display = ("user","total_amount","total_time","order_type")

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order","amount","status")

class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)

class AppsGenreAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(PC, PcAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Activity)
admin.site.register(App, AppAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(AppsGenre, AppsGenreAdmin)
