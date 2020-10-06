from django.contrib import admin

from .models import Question, Choice, CactusType, Cactus

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(CactusType)
admin.site.register(Cactus)