from django.contrib import admin
from .models import Package, Client, Recipient, FailureReason, FormItem, Form

# Register your models here.

admin.site.register(Package)
admin.site.register(Recipient)
admin.site.register(Client)
admin.site.register(FailureReason)
admin.site.register(Form)
admin.site.register(FormItem)