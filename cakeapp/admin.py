from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Index_start)
class Index_startAdmin(admin.ModelAdmin):
    list_display = ['name1']
    prepopulated_fields = {"slug": ('name1',)}

@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Wedding)
class WeddingAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Custom)
class CustomAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['name1']
    prepopulated_fields = {"slug": ('name1',)}

@admin.register(Client)
class CLientAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ('name',)}

admin.site.register(About)
admin.site.register(Contact)