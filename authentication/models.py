from enum import unique

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import ValidationError

# Create your models here.

"""3 (Model.objects.create) Luo objectin kantaan"""


class UserPicture(models.Model):
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 1.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError(
                'Invalid image size: %(value)s MB. Max size for image is: %(max_size)s MB. Please select new file.',
                params={'value': "{0:.4f}".format(filesize/(1024*1024)), 'max_size': megabyte_limit},
            )

    profile_picture = models.ImageField(upload_to='profile_pictures/', validators=[validate_image])
    user = models.OneToOneField(User, related_name='user_picture', unique=True)

    def __str__(self):
        return "/static/img/" + self.profile_picture.name
