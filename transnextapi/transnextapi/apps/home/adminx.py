import xadmin
from xadmin import views
from .models import Banner, Nav, Menu, MainBanner, CenterBanner, Message


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


# 导航菜单
class NavModelAdmin(object):
    list_display = ["title", "link", "position", "is_site"]


xadmin.site.register(Nav, NavModelAdmin)


# 二级菜单
class MenuModelAdmin(object):
    list_display = ["title", "link", "parent"]


xadmin.site.register(Menu, MenuModelAdmin)


# 横幅广告
class MainBannerModelAdmin(object):
    list_display = ["title", "link", "position", "is_show"]
    ordering = ["order"]


xadmin.site.register(MainBanner, MainBannerModelAdmin)


# 中间广告
class CenterBannerModelAdmin(object):
    list_display = ["title", "link", "position", "is_show"]
    ordering = ["order"]
    # model_icon = 'fa fa-user'


xadmin.site.register(CenterBanner, CenterBannerModelAdmin)


# 留言板
class MessageModelAdmin(object):
    list_display = ["name", "email", "msg", "created_time"]
    readonly_fields = ["name", "email", "msg", "created_time"]
    ordering = ["id"]
    list_per_page = 10

    def has_delete_permission(self, request=None):
        return False

    def has_add_permission(self, request=None):
        # Disable delete
        return False


xadmin.site.register(Message, MessageModelAdmin)
