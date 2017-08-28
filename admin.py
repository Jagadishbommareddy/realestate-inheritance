from django.contrib import admin
from .models import Person
from .models import ContactInfo


class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)


class ContactInfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(ContactInfo, ContactInfoAdmin)
