from django.contrib import admin
from .models import Post

class DisplayDate(admin.ModelAdmin):
    readonly_fields = ('createDate',)

# Register your models here.
admin.site.register(Post, DisplayDate)
