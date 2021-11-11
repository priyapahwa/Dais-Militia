from django.db import models


class Tip(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    location = models.TextField()
    pin_code = models.CharField(max_length=100, null=True, blank= True)
    date = models.DateTimeField()

    def __str__(self):
        return self.title
