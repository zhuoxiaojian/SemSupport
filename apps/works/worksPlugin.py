# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 9:18
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : discountPlugin.py
# @Software: PyCharm
import xadmin
from xadmin.views import BaseAdminPlugin, ListAdminView
from django.template import loader
from xadmin.plugins.utils import get_context_dict


class DiscountPlugin(BaseAdminPlugin):
    works_show = False

    # 这个函数返回true or false。如果为true会加载插件。
    def init_request(self, *args, **kwargs):
        return bool(self.works_show)

    def block_top_toolbar(self, context, nodes):
        # 指定我们渲染使用的模板html
        nodes.append(loader.render_to_string('xadmin/worksShow.html',
                                             context=get_context_dict(context)))


xadmin.site.register_plugin(DiscountPlugin, ListAdminView)
