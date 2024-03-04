from django.contrib import admin
from appfolder.models import *
# Register your models here.


class AdminServer(admin.ModelAdmin):
    list_display = ['nm','malumot']

admin.site.register(Service,AdminServer)

class AdminPortfolio(admin.ModelAdmin):
    list_display = ['nom','tur','rasm','data']

admin.site.register(Portfolio,AdminPortfolio)

class AdminTeam(admin.ModelAdmin):
    list_display = ['ismi','fam','yosh','rasm','lavozimi']

admin.site.register(Team,AdminTeam)

class AdminTur(admin.ModelAdmin):
    list_display =['id','nomi']
admin.site.register(Type,AdminTur)
