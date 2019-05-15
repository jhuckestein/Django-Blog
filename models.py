from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)  #mapping to User model with 1:1 relationship
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	
	#Setting how we want this to be diplayed instead of profile object
	def __str__(self):
		return f'{self.user.username} Profile'
		
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		
		img = Image.open(self.image.path)
		
		#This next block checks to see if either dimension is greater than 300
		#pixels.  If so, resize with thumbnail, and then save back to the path.
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)