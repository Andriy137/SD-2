from django.contrib import admin

from polls.models import Question, Choice


# Register your models here.
@admin.register(Question)
class Questionadmin(admin.ModelAdmin):
    pass



@admin.register(Choice)
class Choiseadmin(admin.ModelAdmin):
    pass

