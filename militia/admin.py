from django.contrib import admin

from tkinter import *
from cryptography.fernet import Fernet
import base64
import logging
import traceback
from dais import settings


from militia.models import Tip


class TipAdmin(admin.ModelAdmin):
    def response_change(self, request, obj):

        if "decrypt" in request.POST:
            msg = obj.message

            def decrypt(txt):
                try:
                    txt = base64.urlsafe_b64decode(txt)
                    cipher_suite = Fernet(settings.ENCRYPT_KEY)
                    decoded_text = cipher_suite.decrypt(txt).decode("ascii")
                    return decoded_text
                except Exception as e:
                    logging.getLogger("error_logger").error(traceback.format_exc())
                    return None

            def delete():
                root.destroy()

            root = Tk()
            root.title("message")
            window = Label(root, text=decrypt(msg))
            window.pack()

            root.after(60000, delete)
            root.mainloop()
        return super().response_change(request, obj)


admin.site.register(Tip, TipAdmin)
