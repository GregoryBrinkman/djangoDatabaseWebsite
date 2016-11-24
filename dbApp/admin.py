from django.contrib import admin

# Register your models here.
from django.apps import apps
from .models import *

# class MembershipInline(admin.TabularInline):
#     model=Plays
#     extra = 1

# class PerformsInline(admin.TabularInline):
#     model = Performs
#     extra = 1

# class SongAppearsAdmin(admin.ModelAdmin):
#     inlines = (PerformsInline,)

# class InstrumentsAdmin(admin.ModelAdmin):
#     inlines = (MembershipInline,)

# class MusiciansAdmin(admin.ModelAdmin):
#     inlines = (MembershipInline,)

# admin.site.register(Musicians,MusiciansAdmin)
# admin.site.register(Instruments, InstrumentsAdmin)
# admin.site.register(SongAppears,SongAppearsAdmin)

app = apps.get_app_config('dbApp')
for model_name,model in app.models.items():
    # print(model,model_name)
    # if ('musicians' not in model_name and 'instruments' not in model_name and 'songappears' not in model_name):
    admin.site.register(model)
    print("REGISTERED " + str(model_name))
