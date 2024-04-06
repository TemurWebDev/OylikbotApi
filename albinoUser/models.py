from django.db import models

class TelegramUser(models.Model):
    STATUS_CHOICES = [
        ('aktiv', 'aktiv'),
        ('no_aktiv', 'No_aktiv'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, default='no_aktiv', max_length=20,null=True,blank=True)
    first_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,null=True,blank=True)
    user_id = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    passport = models.CharField(max_length=10)


    def __str__(self):
        return self.name



class Sana(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name



class Oylik(models.Model):
    sana = models.ForeignKey(Sana, on_delete=models.CASCADE)
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    jami_oylik = models.FloatField()
    karobka_puli = models.FloatField()
    bonus = models.FloatField()
    avans = models.FloatField()
    shtraf = models.FloatField()
    ishlamagan_kun = models.FloatField()
    forma = models.FloatField()
    korpa_tushak = models.FloatField()
    qushimcha= models.FloatField()
    
    berildi = models.FloatField()


    def __str__(self):
        return self.user.name + ' ' + self.sana.name if self.user else "Oylik"
    



