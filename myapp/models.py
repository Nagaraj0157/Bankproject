from django.db import models
class acc_details(models.Model):
    name=models.CharField(max_length=30)
    account_num=models.CharField(max_length=20)
    ifsc=models.CharField(max_length=20)
    mob_no=models.IntegerField()
    location=models.CharField(max_length=20)
    amount=models.FloatField()
 
