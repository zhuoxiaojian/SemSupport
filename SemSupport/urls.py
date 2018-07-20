"""SemSupport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.conf.urls import url, include
from django.views.generic import RedirectView
from customers.views import formCustomerHandle, seoCustomerHandle
import xadmin
# 导入x admin，替换admin
from django.views.static import serve
from speechcraft.views import speechcraftshow, getSpeechcraftInfo, checkLoginInfo
from SemSupport.settings import MEDIA_ROOT


urlpatterns = [
    url('^admin/', xadmin.site.urls),
    url('^$', RedirectView.as_view(url='/admin'), name='login'),
    # path('refleshAdData/', xadmin.site.urls),
    url('^login/', RedirectView.as_view(url='/admin'), name='login'),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    url(r'^media/(?P<path>.*)$',  serve, {"document_root": MEDIA_ROOT}),
    # url('^captcha/', include('captcha.urls')),
    # 配置静态文件访问
    # url('(?P<path>.*)$', serve, {'document_root': STATICFILES_DIRS}),
    url('^admin/customers/formcustomer/formCustomerHandle', formCustomerHandle.as_view(), name='formCustomerHandle'),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/favicon.ico')),
    url(r'^admin/speechcraftshow', speechcraftshow, name='speechcraftshow'),
    url(r'^getSpeechcraftInfo', getSpeechcraftInfo, name="getSpeechcraftInfo"),
    url(r'^checkLoginInfo', checkLoginInfo, name="checkLoginInfo"),
    url('^admin/customers/seosalework/seoCustomerHandle', seoCustomerHandle.as_view(), name='seoCustomerHandle'),
]

# 全局 404 500 页面配置（django 会自动调用这个变量）
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
