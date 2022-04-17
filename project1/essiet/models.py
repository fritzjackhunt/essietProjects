from django.db import models
from django.http import HttpResponse, JsonResponse
#from .utils import SendSubscribeMail
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


#class Subscribe(models.Model):
 #   email_id = models.EmailField(null = True, blank = True)
  #  timestamp = models.DateTimeField(default=timezone.now)
	
  #  def __str__(self):
	#	    return self.email_id


class Job(models.Model):
  title = models.CharField(max_length=255)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  description = models.TextField()

  def __str__(self):
    return self.title + " job by " + str(self.author)

  def get_absolute_url(self):
    return reverse('job-detail', args=(str(self.id)))

  
class UserProfile(models.Model):
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  bio = models.TextField()
  profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
  website_url = models.CharField(max_length=255, null=True, blank=True)
  fb_url = models.CharField(max_length=255, null=True, blank=True)
  instagram_url = models.CharField(max_length=255, null=True, blank=True)
  twitter_url = models.CharField(max_length=255, null=True, blank=True)
  linkedin_url = models.CharField(max_length=255, null=True, blank=True)
  github_url = models.CharField(max_length=255, null=True, blank=True)


  def __str__(self):
    return str(self.user)