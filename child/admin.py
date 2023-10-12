from django.contrib import admin
from .models import Post
from .models import students
from .models import login

# Register your models here.
admin.site.register(Post),
admin.site.register(students),
admin.site.register(login)

