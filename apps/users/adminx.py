# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 11:22
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : adminx.py
# @Software: PyCharm

from xadmin import views
import xadmin


class BaseSetting(object):
    # 主题切换
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    # 系统标题
    site_title = '易数宝智能营销支撑系统'
    # 底部栏
    site_footer = '易数宝智能营销支撑系统'
    menu_style = 'accordion'




xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.LoginView,
                     login_template="xadmin/views/xadmin_login.html"
                     )