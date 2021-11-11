from django.db import models
from django_cryptography.fields import encrypt
from cryptography.fernet import Fernet


class Tip(models.Model):
    title = models.CharField(max_length=200)
    message = encrypt(models.TextField())
    location = models.TextField()
    pin_code = models.CharField(max_length=100, null=True, blank= True)
    date = models.DateTimeField()
    file = encrypt(models.FileField(upload_to='documents/', null=True, blank=True))

    def save(self, *args, **kwargs):
        key = Fernet.generate_key()
        encrypted_key = Fernet(key)
        encrypted_message = encrypted_key.encrypt(bytes(self.message, 'utf-8'))
        self.message = encrypted_message
        super(Tip, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
