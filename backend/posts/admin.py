from django.contrib import admin
from . models import Member
from . models import Title
from . models import Assign
from . models import Calender
from . models import Checklist
from . models import Comment 
from . models import Content
from . models import Contentstate
from . models import Enroll
from . models import File
from . models import Permission
from . models import Section
from . models import Permissionstate
from . models import Setion

# Register your models here.

admin.site.register(Member)
admin.site.register(Title)
admin.site.register(Assign)
admin.site.register(Calender)
admin.site.register(Checklist)
admin.site.register(Comment)
admin.site.register(Content)
admin.site.register(Contentstate)
admin.site.register(Enroll)
admin.site.register(File)
admin.site.register(Permission)
admin.site.register(Section)
admin.site.register(Permissionstate)
admin.site.register(Setion)