from django.contrib import admin
import django.apps
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.html import format_html
from .models import *
from .enums import StatesEnum

class StormetchAdminArea(admin.AdminSite):
    site_header = "Stormtech Admin Area"

class FormItemInline(admin.TabularInline):
    model = FormItem
    extra = 0

class FormAdmin(admin.ModelAdmin):
    inlines = [FormItemInline]

    list_display = ('__str__', 
                    'date', 
                    ) 
    list_filter = ('formitem__package__state',
                   )
    actions = ['delete_selected', 
               'changePackageStateToDistribucion'
               ]

    def changePackageStateToDistribucion(self, request, queryset):
        self.changePackageState(queryset , StatesEnum.EN_DISTRIBUCION.value)

    def changePackageState(self, queryset, new_state):
        count = 0
        for form in queryset:
            for formItem in form.formitem_set.all():  
                package = formItem.package
                package.state = new_state
                package.save()
                count += 1
        
        return HttpResponseRedirect(reverse('admin:sistema_logistica_app_formitem_changelist'))
    
    changePackageStateToDistribucion.short_description = "Change Package State To Distribution"

stormtechAdmin = StormetchAdminArea(name = 'StormtechAdmin')

models_to_register = django.apps.apps.get_models()

admin.site.register(Client)
admin.site.register(Package)
admin.site.register(Recipient)
admin.site.register(Form, FormAdmin)
admin.site.register(FormItem)
admin.site.register(FailureReason)
stormtechAdmin.register(Client)
stormtechAdmin.register(Package)
stormtechAdmin.register(Recipient)
stormtechAdmin.register(Form, FormAdmin)
stormtechAdmin.register(FormItem)
stormtechAdmin.register(FailureReason)

admin.site = stormtechAdmin
admin.site.register = stormtechAdmin.register