from django.db import models
from django.contrib.auth.models import User
from crequest.middleware import CrequestMiddleware


ANIMAL_KIND = (
    ("dog", "dog"),
    ("cat", "cat")
)


class Pet(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=256)
    birthday = models.DateField()
    animal_kind = models.CharField(max_length=3, choices=ANIMAL_KIND, verbose_name="kind of animal")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            current_request = CrequestMiddleware.get_request()
            self.owner = current_request.user
        super(Pet, self).save(*args, **kwargs)
