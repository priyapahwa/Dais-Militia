from django.contrib import admin

from tkinter import *
from tkinter import messagebox as mb
from cryptography.fernet import Fernet
import base64
import logging
import traceback
from dais import settings


from militia.models import Tip


class TipAdmin(admin.ModelAdmin):

    list_display = ["title", "location", "pin_code", "date"]
    list_filter = ["title", "pin_code"]
    search_fields = ["title", "location", "pin_code"]

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
                app.destroy()

            def deletetop():
                app.destroy()

            def show():
                verify_password = password.get()
                # Password is hard coded for the time being
                if verify_password == "12345":
                    top = Toplevel()
                    top.title("")
                    Label(top, text=decrypt(msg)).pack()
                    top.after(10000, deletetop)
                else:
                    pass

            app = Tk()
            password = StringVar()
            passEntry = Entry(app, textvariable=password, show="*")
            submit = Button(app, text="Verify", command=show)

            passEntry.pack()
            submit.pack()
            app.after(60000, delete)
            app.mainloop()

        return super().response_change(request, obj)


admin.site.register(Tip, TipAdmin)
