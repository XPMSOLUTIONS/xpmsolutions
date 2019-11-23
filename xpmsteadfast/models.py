from django.db import models





class Register(models.Model):
	full_name = models.CharField(max_length=200)
	user_id = models.CharField(max_length=100)
	email =  models.EmailField()
	password = models.CharField(max_length=100)
	re_password = models.CharField(max_length=100)


class Login(models.Model):
	user_id = models.CharField(max_length=100)
	password = models.CharField(max_length=100)



class Cards (models.Model):
	name = models.CharField(max_length=50)
	desc = models.CharField(max_length=200)
	date = models.DateField()
	img = models.ImageField(upload_to='images')


