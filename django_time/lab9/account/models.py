from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    userprofile = models.OneToOneField(User)

    # The additional attributes we wish to include.
    userprofile_website = models.URLField(blank=True)
    userprofile_picture = models.ImageField(upload_to='profile_images', blank=True)
    userprofile_identfication = models.CharField(max_length=24,
                                    unique=True,
                                    verbose_name='Identificacion',
                                    help_text='Numero de Identficacion')

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.userprofile.username
