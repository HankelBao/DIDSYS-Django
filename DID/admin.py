from django.contrib import admin
from .models import Subject
from .models import Clas
from .models import Scorer
from .models import Record

# Register your models here.
admin.site.register(Subject)
admin.site.register(Clas)
admin.site.register(Scorer)
admin.site.register(Record)
