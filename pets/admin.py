from django.contrib import admin
from .models import *


class PetAdmin(admin.ModelAdmin):
    list_display = ["name", "birthday", "animal_kind"]
    fields = ["name", "birthday", "animal_kind"]

    class Meta:
        model = Pet

    def get_queryset(self, request):
        qs = super(PetAdmin, self).get_queryset(request)
        user = request.user
        if not user.is_superuser:
            return qs.filter(owner=user)
        else:
            return qs

admin.site.register(Pet, PetAdmin)
