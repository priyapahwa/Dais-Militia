from django.contrib import admin
from django.shortcuts import redirect


from militia.models import Tip

class TipAdmin(admin.ModelAdmin):
    def response_change(self, request, obj):
        if "decrypt" in request.POST:
            print("hi")
        return  super().response_change(request, obj)

admin.site.register(Tip, TipAdmin)