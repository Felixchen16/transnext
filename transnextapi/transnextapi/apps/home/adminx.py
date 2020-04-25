import xadmin
from xadmin import views
from .models import Banner


class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSetting(object):
    """xadmin的全局配置"""
    site_title = "TransNext"
    site_footer = "TransNext Technology Ltd"
    menu_style = "accordion"


xadmin.site.register(views.CommAdminView, GlobalSetting)


# 轮播图
class BannerModelAdmin(object):
    list_display = ["title", "order", "is_show"]


xadmin.site.register(Banner, BannerModelAdmin)
