from django.contrib import admin
from .models import Articles,Author
# Register your models here.
admin.site.register(Author)
admin.site.register(Articles)