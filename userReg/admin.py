from django.contrib import admin
from userReg.models import User,Content,Comment
# Register your models here.
admin.site.register([User,Content,Comment])