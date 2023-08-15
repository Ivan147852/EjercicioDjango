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

class FormItemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 
                    'position', 
                    #'delete_link'
                    )  # Agrega aquí los campos que deseas mostrar
    actions = ['delete_selected', 
               'add_form_item', 
               #'delete_form_item',
               'change_package_state_to_distribucion'
               ]

    #def deleteLink(self, obj):
    #    return format_html('<a href="{}">Delete</a>', reverse('admin:deleteFormItem', args=[obj.form.formNumber, obj.position]))

    #deleteLink.short_description = "Delete Link"

    def add_form_item(self, request, queryset):
        # Lógica para agregar un nuevo ítem de formulario aquí
        # Puedes usar el método HttpResponseRedirect para redirigir a la página correcta después de la acción
        # Puedes usar el método messages.success para mostrar un mensaje de éxito
        pass
    add_form_item.short_description = "Add Form Item"
    """
    def delete_form_item(self, request, queryset):
        # Lógica para eliminar un ítem de formulario aquí
        pass
    delete_form_item.short_description = "Delete Form Item"
    """

    def change_package_state_to_distribucion(self, request, queryset):
        self.change_package_state(queryset , StatesEnum.EN_DISTRIBUCION)

    def change_package_state(self, queryset, new_state):
        count = 0
        for form_item in queryset:  
            package = form_item.package
            package.state = new_state
            package.save()
            count += 1
        
        return HttpResponseRedirect(reverse('admin:sistema_logistica_app_formitem_changelist'))
    
    change_package_state_to_distribucion.short_description = "Change Package State To Distribution"
    
    

stormtechAdmin = StormetchAdminArea(name = 'StormtechAdmin')

models_to_register = django.apps.apps.get_models()

admin.site.register(Client)
admin.site.register(Package)
admin.site.register(Recipient)
admin.site.register(Form)
admin.site.register(FormItem, FormItemAdmin)
admin.site.register(FailureReason)
stormtechAdmin.register(Client)
stormtechAdmin.register(Package)
stormtechAdmin.register(Recipient)
stormtechAdmin.register(Form)
stormtechAdmin.register(FormItem, FormItemAdmin)
stormtechAdmin.register(FailureReason)

admin.site = stormtechAdmin
admin.site.register = stormtechAdmin.register