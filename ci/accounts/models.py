from django.db import models
from django.contrib.auth.models import User

class Skills(models.Model):
	description = models.CharField(max_length=3000)

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='images', blank=True)
    skills  = models.ManyToManyField(Skills)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

    REQUIRED_FIELDS = []

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])