from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100,null=True)
	content = models.TextField(null = True)
	date_posted = models.DateTimeField(default = timezone.now, null = True)
	author      = models.ForeignKey(User, on_delete = models.CASCADE)


	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "Posts"

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'pk':self.id})
		
		


# def save(self, *args, **kwargs):
# 	super().save(*args, **kwargs)
# 	img = Image.open(self.image.path)
# 	if img.width >300 and img.height > 300:
# 		output_size = (300, 300)
# 		img.thumbnail(output_size)
# 		img.save(self.image.path)