from django.contrib import admin
from .models import Orders, StatusCrm, Comments

# Register your models here.
admin.site.register(Orders)
admin.site.register(StatusCrm)
admin.site.register(Comments)