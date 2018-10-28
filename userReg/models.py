from django.db import models
import datetime
# Create your models here.

Class User(models.Model):
		uid = models.IntegerField(primary_key=True)
		uname=models.CharField(max_lenth=50)
		upassword=models.CharField(max_lenth=16)
		gender=models.CharField(max_lenth=6)
        regTime=models.DateField(_("Date"),default=datetime.date.today)
        email=models.CharField(max_length=50)


Class Content(models.Model):
		cid=models
