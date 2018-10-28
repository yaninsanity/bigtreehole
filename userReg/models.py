from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class User(models.Model):
		uid = models.IntegerField(primary_key=True)
		uname=models.CharField(max_length=50)
		upassword=models.CharField(max_length=16)
		gender=(
				(0,"male"),
				(1,"female"),
				(2,"unknown")
			)
		regTime=models.DateField('regDate',auto_now=True)
		email=models.EmailField(max_length=50)
		img= models.ImageField(upload_to='upload')


class Content(models.Model):
		cid=models.IntegerField(primary_key=True)
		uid=models.ForeignKey('User',on_delete=models.CASCADE)
		contentword=models.CharField(max_length=300)

class Comment(models.Model):
		commentID=models.IntegerField(primary_key=True)
		cid=models.ForeignKey('Content',on_delete=models.CASCADE)
		commentword=models.CharField(max_length=150)
		uid=models.ForeignKey('User',on_delete=models.CASCADE)
