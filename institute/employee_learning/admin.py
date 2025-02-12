from django.contrib import admin

# Register your models here.
from .models import Employee
from .models import Division
from .models import PersonalInfo
from .models import LearningCourse

admin.site.register(Employee)
admin.site.register(Division)
admin.site.register(PersonalInfo)
admin.site.register(LearningCourse)
