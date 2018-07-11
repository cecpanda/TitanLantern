import xadmin
from xadmin import views

from .models import GroupSetting


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'Lantern Backend'
    site_footer = 'cecpanda'
    menu_style = 'accordion'


class GroupSettingAdmin(object):
    list_display = ['group', 'code']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(GroupSetting, GroupSettingAdmin)
