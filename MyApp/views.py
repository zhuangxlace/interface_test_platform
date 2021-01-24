from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json
from django.http import HttpResponse,HttpResponseRedirect
from MyApp.models import *
import json
import requests


# Create your views here.
# 2020.12.30觉得没有用就注解
@login_required()
def welcome(request):
    # return HttpResponse("你好")
    return render(request, "welcome.html")


@login_required
def home(request):
    return render(request, "welcome.html", {"whichHTML": "home.html", "oid": request.user.username, "username": request.user.username, "userimg": str(request.user.id) + ".jpg"})


@login_required
def home2(request, log_id=""):
    return render(request, "welcome.html", {"whichHTML": "home2.html", "oid": request.user.id, "ooid": log_id, "username": request.user.username, "userimg": str(request.user.id) + ".jpg"})


# 返回子页面  后面两个入参是urls.py中的path中的值
def child(request, eid, oid, ooid):
    res = child_json(eid, oid, ooid)
    return render(request, eid, res)


def child_json(eid, oid, ooid=""):
    res = {}
    if eid == "home.html":
        data = DB_home_href.objects.all()
        home_username = oid
        res["hrefs"] = data
        res["username"] = home_username
    if eid == "home2.html":
        data = DB_apis_log.objects.filter(user_id=oid)[::-1]
        if ooid == "":
            res["home_log"] = data
        else:
            log = DB_apis_log.objects.filter(id=ooid)[0]
            res["home_log"] = data
            res["log"] = log
    if eid == "project_list.html":
        data = DB_project.objects.all()
        res["project"] = data
    if eid == "P_apis.html":
        # 写法一
        # data = DB_project.objects.filter(id=oid)
        # 写法二  这里取到的数据是根据 models.py中orm映射类中的__str__()函数定义的格式来的
        # data = DB_project.objects.filter(id=oid)[0]
        # 写法三 这里的data是QuerySet 类型 ,所以用[0]把数据取出来 .指定字段可以定向返回数据 ，不然就用第二种方法在__str__中控制
        data = DB_project.objects.filter(id=oid)[0]
        apis = DB_apis.objects.filter(project_id=oid)
        res["project"] = data
        res["apis"] = apis
    if eid == "P_cases.html":
        cases = DB_cases.objects.filter(project_id=oid)
        data = DB_project.objects.filter(id=oid)[0]
        res["project"] = data
        res["cases"] = cases
    if eid == "P_project_set.html":
        data = DB_project.objects.filter(id=oid)[0]
        res["project"] = data
    return res


def login(request):
    return render(request, "login.html")


def login2(request):
    return HttpResponseRedirect("/login/")


def login_action(request):
    user_name = request.GET['username']
    pass_word = request.GET['password']
    # 开始联通django用户库，查看用户名或密码是否正确
    from django.contrib import auth
    user = auth.authenticate(username=user_name, password=pass_word)
    # 判断user是用户实体还是一个none
    if user is not None:
        auth.login(request, user)
        request.session['user'] = user_name
        return HttpResponse("成功")
    else:
        return HttpResponse("失败")
    # post请求
    # concat = requests.POST
    # postBody = requests.body
    # print("concat",concat)
    # print("类型",type(postBody))
    # print("postBody",postBody)
    # print("111111111111")
    # json_result = json.loads(postBody)
    # print(json_result)


def register_action(request):
    user_name = request.GET['username']
    pass_word = request.GET['password']
    # 开始联通django用户库
    from django.contrib.auth.models import User
    try:
        user = User.objects.create_user(username=user_name, password=pass_word)
        user.save()
        return HttpResponse("注册成功")
    except:
        return HttpResponse("注册失败 用户已存在")


def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return HttpResponseRedirect("/login/")


def pei(request):
    tucao = request.POST["tucao_text"]
    # DB_tucao就是创建的orm映射类。create方法就是创建数据库记录
    DB_tucao.objects.create(user=request.user.username, text=tucao)
    return HttpResponse("👍")


# def show_user(request):
#     username = request.user.username
#     return render(request, "home.html", {"username": username})


def api_help(request):
    return render(request, "welcome.html", {"whichHTML": "help.html", "oid": "", "username": request.user.username, "userimg": str(request.user.id) + ".jpg"})


def project_list(request):
    return render(request, "welcome.html", {"whichHTML": "project_list.html", "oid": "", "username": request.user.username, "userimg": str(request.user.id) + ".jpg"})


def delete_project(request):
    project_id = request.GET["id"]
    DB_project.objects.filter(id=project_id).delete()
    # 删除项目的时候把接口表中与项目id关联的接口也都删掉
    DB_apis.objects.filter(project_id=project_id).delete()
    # 删除项目的时候把用例表中与项目id关联的用例也都删掉,以及与用例id关联的小步骤用例
    all_cases = DB_cases.objects.filter(project_id=project_id)
    for i in all_cases.values():
        DB_step.objects.filter(Case_id=i["id"]).delete()  # 删除小步骤
    all_cases.delete()  # 删除所有的用例
    return HttpResponse("👍")


def add_project(request):
    project_name = request.GET['name']
    remark = request.GET['remark']
    user = request.user.username
    DB_project.objects.create(name=project_name, remark=remark, user=user, other_user="")
    return HttpResponse("👍")


def open_apis(request, project_id):
    return render(request, "welcome.html", {"whichHTML": "P_apis.html", "oid": project_id, "username": request.user.username, "userimg": str(request.user.id) + ".jpg"})


def open_cases(request, project_id):
    return render(request, "welcome.html", {"whichHTML": "P_cases.html", "oid": project_id, "username": request.user.username, "userimg": str(request.user.id) + ".jpg"})


def open_project_set(request, project_id):
    return render(request, "welcome.html", {"whichHTML": "P_project_set.html", "oid": project_id, "username": request.user.username, "userimg": str(request.user.id) + ".jpg"})


def project_set_save(request, project_id):
    name = request.POST["name"]
    remark = request.POST["remark"]
    user = request.user.username
    other_user = request.POST["other_user"]
    DB_project.objects.filter(id=project_id).update(name=name, remark=remark, user=user, other_user=other_user)
    return HttpResponse("👍")


def project_api_add(request, project_id):
    # api_method="none" 这样前台的select的value为none就会默认取第一只option的value
    DB_apis.objects.create(project_id=project_id, name="", api_method="none")
    # 写法一
    # return HttpResponseRedirect("/apis/" + project_id + "/")
    # 写法二
    return HttpResponseRedirect("/apis/%s/" % project_id)


def delete_apis(request, api_id):
    project_id = DB_apis.objects.filter(id=api_id)[0].project_id
    DB_apis.objects.filter(id=api_id).delete()
    return HttpResponseRedirect("/apis/%s/" % project_id)


def save_bz(request):
    api_id = request.POST["id"]
    des = request.POST["des"]
    DB_apis.objects.filter(id=api_id).update(des=des)
    return HttpResponse("👍")


def get_bz(request):
    api_id = request.POST["api_id"]
    des = DB_apis.objects.filter(id=api_id)[0].des
    return HttpResponse(des)


def api_save(request):
    api_name = request.POST["api_name"]
    api_id = request.POST['api_id']
    ts_method = request.POST['api_method']
    ts_url = request.POST['api_url']
    ts_host = request.POST['api_hosts']
    ts_header = request.POST['api_headers']
    ts_body_method = request.POST['api_body_type']
    # 请求体类型在返回体的情况
    if ts_body_method == "返回体":
        ts_body_method = DB_apis.objects.filter(id=api_id)[0].last_body_method
        ts_api_body = DB_apis.objects.filter(id=api_id)[0].last_api_body
    else:
        ts_api_body = request.POST["api_body"]
    # 保存数据
    DB_apis.objects.filter(id=api_id).update(
        name=api_name,
        api_method=ts_method,
        api_url=ts_url,
        api_header=ts_header,
        api_host=ts_host,
        body_method=ts_body_method,
        api_body=ts_api_body
    )
    # 返回
    return HttpResponse('success')


def api_data(request):
    api_id = request.POST["api_id"]
    # 拿到这个接口的字典格式数据  type 'dict'
    data_dic = DB_apis.objects.filter(id=api_id).values()[0]
    data_json = json.dumps(data_dic)
    # 返回给前端字符串，格式得是json
    return HttpResponse(data_json, content_type="application/json")


def api_send(request):
    api_name = request.POST["api_name"]
    api_id = request.POST['api_id']
    ts_method = request.POST['api_method']
    ts_url = request.POST['api_url']
    ts_host = request.POST['api_hosts']
    ts_header = request.POST['api_headers']
    ts_body_method = request.POST['api_body_type']
    # 获取正确的请求体编码和请求体body
    if ts_body_method == "返回体":
        api = DB_apis.objects.filter(id=api_id)[0]
        ts_body_method = api.last_body_method
        ts_api_body = api.last_api_body
        if ts_api_body is None or ts_api_body == "":
            return HttpResponse('请先设置好请求体编码格式和请求体，再点击"Send"按钮发送请求')
        pass
    else:
        ts_api_body = request.POST['api_body']
        DB_apis.objects.filter(id=api_id).update(last_body_method=ts_body_method, last_api_body=ts_api_body)
        pass
    # 发送请求获取返回值
    ts_header = json.loads(ts_header)  # 把前台传来的str类型header转换成dic类型
    # 拼接完整的url hosts+url  注意：hosts结尾没有'/'，url开头有'/'
    if ts_host[-1] == "/":
        ts_host = ts_host[:-1]
    if ts_url[0] != "/":
        ts_url = "/" + ts_url
    complete_url = ts_host + ts_url
    try:
        if ts_body_method == "none":
            response = requests.request(method=ts_body_method, url=complete_url, headers=ts_header, data={})
        elif ts_body_method == "form-data":
            files = []  # 文件流
            data = json.loads(ts_api_body)  # 把前台传过来的str类型body转换成dic类型
            response = requests.request(method=ts_method, url=complete_url, headers=ts_header, data=data, files=files)
        elif ts_body_method == "x-www-form-urlencoded":
            ts_header["Content-Type"] = "application/x-www-form-urlencoded"  # 在headers中添加一个参数
            data = json.loads(ts_api_body)  # 把前台传过来的str类型body转换成dic类型
            response = requests.request(method=ts_method, url=complete_url, headers=ts_header, data=data)
        else:
            # 五个raw类型请求编码处理
            if ts_body_method == "Text":
                ts_header["Content-Type"] = "text/plain"
            if ts_body_method == "Json":
                ts_header["Content-Type"] = "text/plain"
                # 判断是否为json格式
                try:
                    json.loads(ts_api_body)
                except:
                    return HttpResponse("请求体不符合json格式")
            if ts_body_method == "JavaScript":
                ts_header["Content-Type"] = "text/plain"
            if ts_body_method == "Xml":
                ts_header["Content-Type"] = "text/plain"
            if ts_body_method == "Html":
                ts_header["Content-Type"] = "text/plain"
            response = requests.request(method=ts_method, url=complete_url, headers=ts_header,
                                        data=ts_api_body.encode("utf-8"))
            response.encoding = "utf-8"
            pass
        return HttpResponse(response.text)
    except Exception as e:
        print(str(e))


def api_copy(request):
    api_id = request.POST["api_id"]
    old_api = DB_apis.objects.filter(id=api_id)[0]
    DB_apis.objects.create(project_id=old_api.project_id,
                           name=old_api.name + "副本",
                           api_method=old_api.api_method,
                           api_url=old_api.api_url,
                           api_header=old_api.api_header,
                           api_login=old_api.api_login,
                           api_host=old_api.api_host,
                           des=old_api.des,
                           body_method=old_api.body_method,
                           api_body=old_api.api_body,
                           result=old_api.result,
                           sign=old_api.sign,
                           file_key=old_api.file_key,
                           file_name=old_api.file_name,
                           public_header=old_api.public_header,
                           last_body_method=old_api.last_body_method,
                           last_api_body=old_api.last_api_body
                           )
    return HttpResponse("👍")


def error_request(request):
    api_id = request.POST['api_id']
    new_body = request.POST['new_body']
    span_text = request.POST['span_text']
    api = DB_apis.objects.filter(id=api_id)[0]
    method = api.api_method
    url = api.api_url
    host = api.api_host
    header = api.api_header
    # 非空就把前台传来的str类型header转换成dic类型
    header = {} if header == "" else json.loads(header)
    body_method = api.body_method
    # 把前台传来的str类型header转换成dic类型
    # 拼接完整的url hosts+url  注意：hosts结尾没有'/'，url开头有'/'
    if host[-1] == "/":
        host = host[:-1]
    if url[0] != "/":
        url = "/" + url
    complete_url = host + url
    try:
        if body_method == 'form-data':
            files = []
            data = json.loads(new_body)
            response = requests.request(method.upper(), complete_url, headers=header, data=data, files=files)
        elif body_method == 'x-www-form-urlencoded':
            header['Content-Type'] = 'application/x-www-form-urlencoded'
            data = json.loads(new_body)
            response = requests.request(method.upper(), complete_url, headers=header, data=data)
        elif body_method == 'Json':
            header['Content-Type'] = 'text/plain'
            response = requests.request(method.upper(), complete_url, headers=header, data=new_body.encode('utf-8'))
        else:
            return HttpResponse('非法的请求体类型')
            # 把返回值传递给前端页面
        response.encoding = "utf-8"
        res_json = {
            "response": response.text,
            "span_text": span_text
        }
        return HttpResponse(json.dumps(res_json), content_type="application/json")
    except:
        res_json = {
            "response": "接口没调通",
            "span_text": span_text
        }
        return HttpResponse(json.dumps(res_json), content_type="application/json")


def add_case(request, project_id):
    DB_cases.objects.create(project_id=project_id, name="未命名的用例")
    #  可写成 return HttpResponseRedirect("/cases/%s/" % project_id)
    return HttpResponseRedirect("/cases/" + project_id + "/")


def del_case(request, case_id, project_id):
    DB_cases.objects.filter(id=case_id).delete()
    DB_step.objects.filter(Case_id=case_id).delete()
    return HttpResponseRedirect("/cases/%s/" % project_id)


def copy_case(request, case_id, project_id):
    case = DB_cases.objects.filter(id=case_id)[0]
    DB_cases.objects.create(project_id=project_id, name=case.name + "_复制")
    return HttpResponseRedirect("/cases/%s/" % project_id)


def get_small(request):
    case_id = request.POST['case_id']
    # 可以只获取部分字段如：values("Case_id","index","name")
    steps = DB_step.objects.filter(Case_id=case_id).order_by("index").values()
    res = {
        "all_steps": list(steps)
    }
    return HttpResponse(json.dumps(res), content_type="application/json")


def add_new_step(request):
    case_id = request.POST["case_id"]
    step_num = len(DB_step.objects.filter(Case_id=case_id))
    DB_step.objects.create(Case_id=case_id, name="我是新步骤", index=step_num + 1)
    return HttpResponse("👍")


def delete_step(request, step_id):
    del_step = DB_step.objects.filter(id=step_id)
    del_step_case_id = del_step[0].Case_id
    del_step_index = del_step[0].index
    del_step.delete()
    # 将被删除小用例的后续小用例顺序向前1个  字段__gt==2 相当于 大于2
    # 写法1 F()可用于数字字段的自增减
    # from django.db.models import F
    # DB_step.objects.filter(Case_id=del_step_case_id).filter(index__gt=del_step_index).update(index=F("index")-1)
    # 写法2
    for i in DB_step.objects.filter(Case_id=del_step_case_id).filter(index__gt=del_step_index):
        i.index -= 1
        i.save()
    return HttpResponse("👍")


def api_send_home(request):
    ts_method = request.POST['ts_method']
    ts_url = request.POST['ts_url']
    ts_host = request.POST['ts_host']
    ts_header = request.POST['ts_header']
    ts_body_method = request.POST['ts_body_type']
    ts_api_body = request.POST['ts_body']
    # 发送请求获取返回值
    ts_header = json.loads(ts_header)  # 把前台传来的str类型header转换成dic类型
    # 拼接完整的url hosts+url  注意：hosts结尾没有'/'，url开头有'/'
    if ts_host[-1] == "/":
        ts_host = ts_host[:-1]
    if ts_url[0] != "/":
        ts_url = "/" + ts_url
    complete_url = ts_host + ts_url
    # 写入到数据库请求记录表中
    DB_apis_log.objects.create(user_id=request.user.id,
                               api_method=ts_method,
                               api_url=ts_url,
                               api_header=ts_header,
                               api_host=ts_host,
                               body_method=ts_body_method,
                               api_body=ts_api_body)
    try:
        if ts_body_method == "none":
            response = requests.request(method=ts_body_method, url=complete_url, headers=ts_header, data={})
        elif ts_body_method == "form-data":
            files = []  # 文件流
            data = json.loads(ts_api_body)  # 把前台传过来的str类型body转换成dic类型
            response = requests.request(method=ts_method, url=complete_url, headers=ts_header, data=data, files=files)
        elif ts_body_method == "x-www-form-urlencoded":
            ts_header["Content-Type"] = "application/x-www-form-urlencoded"  # 在headers中添加一个参数
            data = json.loads(ts_api_body)  # 把前台传过来的str类型body转换成dic类型
            response = requests.request(method=ts_method, url=complete_url, headers=ts_header, data=data)
        else:
            # 五个raw类型请求编码处理
            if ts_body_method == "Text":
                ts_header["Content-Type"] = "text/plain"
            if ts_body_method == "Json":
                ts_header["Content-Type"] = "text/plain"
                # 判断是否为json格式
                try:
                    json.loads(ts_api_body)
                except:
                    return HttpResponse("请求体不符合json格式")
            if ts_body_method == "JavaScript":
                ts_header["Content-Type"] = "text/plain"
            if ts_body_method == "Xml":
                ts_header["Content-Type"] = "text/plain"
            if ts_body_method == "Html":
                ts_header["Content-Type"] = "text/plain"
            response = requests.request(method=ts_method, url=complete_url, headers=ts_header,
                                        data=ts_api_body.encode("utf-8"))
            response.encoding = "utf-8"
            pass
        return HttpResponse(response.text)
    except Exception as e:
        return HttpResponse(str(e))


def get_home_log(request):
    user_id = request.user.id
    # QuerySet类型转换为字典
    res = DB_apis_log.objects.filter(user_id=user_id).values()
    # 切片倒序是为了把最新的请求记录放在页面最上面
    return HttpResponse(json.dumps(list(res)[::-1]), content_type="application/json")


def get_api_log_home(request):
    log_id = request.POST["log_id"]
    res = DB_apis_log.objects.filter(id=log_id).values()
    return HttpResponse(json.dumps(res[0]), content_type="application/json")


# 上传用户头像
def user_upload(request):
    file = request.FILES.get("fileUpload",None)  # 靠name获取上传的文件，如果没有，避免报错，设置成None
    if not file:
        return HttpResponseRedirect('/home/')  # 如果没有则返回到首页
    new_name = str(request.user.id) + '.jpg'  # 设置好这个新图片的名字
    destination = open("MyApp/static/user_img/"+new_name, 'wb+')  # 打开特定的文件进行二进制的写操作
    for chunk in file.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()
    return HttpResponseRedirect('/home/')  # 返回到首页