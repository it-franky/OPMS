from django.contrib import admin

import xadmin
from xadmin import views
# Register your models here.


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "OPMS 个人管理系统"
    site_footer = "OPMS"
    menu_style = "accordion"


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)