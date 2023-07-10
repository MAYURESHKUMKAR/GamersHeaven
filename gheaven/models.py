from django.db import models


class PC(models.Model):
    pc_number = models.IntegerField()
    availability_status = models.BooleanField()
    username = models.CharField(max_length=255, blank=True)
    remaining_time = models.DurationField(blank=True, null=True)



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_coins = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=20)
    remaining_time = models.DurationField(null=True, blank=True)


class Genre(models.Model):
    name = models.CharField(max_length=255)
      
    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon_url = models.FileField()
    video_url = models.FileField()
    url = models.FileField()
    genres = models.ManyToManyField(Genre)

class AppsGenre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class App(models.Model):
    app_name = models.CharField(max_length=255)
    app_icon_url = models.FileField()
    app_url = models.FileField(blank=True)
    app_genre = models.ManyToManyField(AppsGenre)


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    activity_type = models.CharField(max_length=10)
    duration = models.IntegerField()

    


class Order(models.Model):
    TYPE_CHOICES = [
        ('package', 'Package'),
        ('price', 'Price'),
    ]

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_time = models.DurationField()
    package_names = models.CharField(max_length=255, blank=True)
    date_and_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def save(self, *args, **kwargs):
        self.user.remaining_time += (self.total_time/2)
        self.user.account_balance -= self.total_amount
        super().save(*args, **kwargs)
        self.user.save()

        if self.order_type == 'package' and not hasattr(self, 'payment'):
            payment = Payment.objects.create(order=self, amount=self.total_amount, status='Success')


class Payment(models.Model):
    
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        limit_choices_to={'order_type': 'package'}
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
