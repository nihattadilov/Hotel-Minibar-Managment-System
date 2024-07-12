from django.contrib import admin
from .models import Room,Product,Sale
# Register your models here.

admin.site.register(Room)
admin.site.register(Product)
admin.site.register(Sale)


admin.site.site_header='Nohur Hotel Minibar Managment System'


