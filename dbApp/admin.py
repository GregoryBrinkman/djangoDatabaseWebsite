from django.contrib import admin

# Register your models here.
from django.apps import apps
from .models import *

app = apps.get_app_config('dbApp')
for model_name,model in app.models.items():
    admin.site.register(model)

