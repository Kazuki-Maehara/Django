from django.contrib import admin

# Register your models here.
from .models import Blog, Entry, Author, Dog

admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Author)
admin.site.register(Dog)
