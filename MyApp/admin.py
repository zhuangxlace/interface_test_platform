from django.contrib import admin

# Register your models here.

from MyApp.models import *
# 要想后台管理平台可以看的到models中创建的表 并且可以控制，需要进行admin注册
admin.site.register(DB_tucao)
admin.site.register(DB_home_href)
admin.site.register(DB_project)
admin.site.register(DB_apis)
admin.site.register(DB_apis_log)
admin.site.register(DB_cases)
admin.site.register(DB_step)
