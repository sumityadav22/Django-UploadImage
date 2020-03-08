from django.db import models


class Hotel(models.Model): 
	name = models.CharField(max_length=50) 
	hotel_Main_Img = models.ImageField(upload_to='images/')

''' 
Here upload_to will specify, to which directory the images should reside,
by default django creates the directory under media directory which will be 
automatically created when we upload an image. No need of explicit creation of media directory.
'''