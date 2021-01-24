"""interface_test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from MyApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # 2020/12/30觉得这个没用就注解了
    path('welcome/', welcome),  # 获取菜单
    path('home/',home),  # 进入首页
    path('home2/',home2),
    # django3正则表达式需要用re_path   .表示任意单个字符 +表示前一个字符1次或无限次扩展 *表0或无限次  ？表示0或者1次
    re_path('child/(?P<eid>.+)/(?P<oid>.*)/(?P<ooid>.*)/$', child),  # 返回子菜单
    path('login/', login),  # 进入登录页面
    path('login_action/',login_action),  # 登录
    path('register_action/', register_action),  # 注册
    # 这里写成login返回login.html会导致图片和js依赖导入失败，所以重新写了一个映射，重定向"/login/"
    re_path('^accounts/login/$',login2), # 非登录状态 进入登录页
    path('logout/', logout), # 登出
    path('pei/', pei), # 吐槽
    # path('show_user/', show_user), # 自己写的主页显示当前的用户
    path('help/', api_help),  # 进入帮助文档
    path('project_list/', project_list),  # 项目列表
    path('delete_project/',delete_project),  # 根据项目id去删除项目
    path('add_project/', add_project),  # 新增项目
    re_path('^apis/(?P<project_id>.*)/$', open_apis),  # 进入接口库
    re_path('^cases/(?P<project_id>.*)/$', open_cases),  # 进入用例库
    re_path('^project_set/(?P<project_id>.*)/$', open_project_set),  # 进入项目设置
    re_path('^project_set_save/(?P<project_id>.*)/$', project_set_save),  # 项目设置保存
    re_path('^project_api_add/(?P<project_id>.*)/$', project_api_add),  # 新增接口
    re_path('^delete_apis/(?P<api_id>.*)/$', delete_apis),  # 删除接口
    path('save_bz/', save_bz),  # 保存备注
    path('get_bz/', get_bz),  # 获取备注
    path('api_save/', api_save),  # 保存接口
    path('get_api_data/',api_data),  # 获取接口信息
    path('api_send/', api_send),  # 发送接口请求
    path('copy_api/', api_copy),  # 复制接口
    path('error_request/', error_request),  # 调用异常测试接口
    re_path('^add_case/(?P<project_id>.*)/$', add_case),  # 增加用例
    re_path('del_case/(?P<case_id>.*)/(?P<project_id>.*)/$', del_case),  # 删除用例
    re_path('^copy_case/(?P<case_id>.*)/(?P<project_id>.*)/$', copy_case),  # 复制用例
    path('get_small/', get_small),  # 获取小用例步骤的列表数据
    path('add_new_step/', add_new_step),  # 新增小用例
    re_path('^delete_step/(?P<step_id>.*)/$', delete_step),  # 删除小用例
    path('user_upload/', user_upload),  # 上传头像
    path('api_send_home/', api_send_home),  # 首页发送接口请求
    path('get_home_log/', get_home_log),  # 获得最近请求记录
    path('get_api_log_home/', get_api_log_home),  # 获得完整的一条的测试记录
    re_path('^home_log/(?P<log_id>.*)/$', home2),  # 再次进入首页，这次带着请求记录的id
]
