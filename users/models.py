from django.db import models
from django.contrib.auth.models import User
from tutor.models import TutorProfile
from PIL import Image


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.TextChoices('Type of Account', (('REGULAR USER', 'Regular User'), ('TUTOR', 'Tutor')))
    is_tutor = models.CharField("Type of Account: (Tutor/Regular)", max_length=15,
                                choices=account_type.choices, default=None)
    created_tutorprofile = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    tutorprofiles = models.ManyToManyField(TutorProfile, verbose_name="My Tutors", default=None)

    def __str__(self):
        return f"{self.user}'s Account"

    def save(self, *args, **kwargs):
        super(Account, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        # change the image resizing part of the method
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
