from django.db import models
from django_cryptography.fields import encrypt
from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings


class Tip(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    location = models.TextField()
    pin_code = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField()
    file = encrypt(models.FileField(upload_to="documents/", null=True, blank=True))

    def save(self, *args, **kwargs):
        if self.message and self.pk is None:

            def encrypt(txt):
                try:
                    txt = str(txt)
                    cipher_suite = Fernet(settings.ENCRYPT_KEY)
                    encrypted_text = cipher_suite.encrypt(txt.encode("ascii"))
                    encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode(
                        "ascii"
                    )
                    return encrypted_text
                except Exception as e:
                    logging.getLogger("error_logger").error(traceback.format_exc())
                    return None

            self.message = encrypt(self.message)
            super(Tip, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
