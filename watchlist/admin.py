# Register your models here.
from django.contrib import admin
from .models import WatchList, NewComentarios

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
  readonly_fields = ('id',)

class TaskAdmin2(admin.ModelAdmin):
  readonly_fields = ('id',)  

admin.site.register(WatchList, TaskAdmin)
admin.site.register(NewComentarios, TaskAdmin2)		