
# -*- coding: utf-8 -*-


from __future__ import print_function
from __future__ import print_function
from __future__ import unicode_literals

import json
import random
import sys

import datetime
from itertools import chain

from django.db.models import Manager
from django.db import connection
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from memo import models
import functionalModule


from memo.tools import demo
from memo.tools.demo import send_sms
import dto.ret as ret

reload(sys)
sys.setdefaultencoding('utf8')


# Create your views here.




#显示注册登录页面
# author=chaim
# type=get，param=null
def display_sign_html(request):
    content = {}
    return render(request,'1.html',content)


# 发送验证码功能
# author=chaim
# type=get，param=phoneNum
def regNum(request):
    phone = request.GET['phoneNum']
    # phone = '18286691619'
    regNum = str(random.randint(100000, 999999))

    request.session['phoneNum'] = phone
    request.session['regNum'] = regNum

# 调用阿里云发送验证码接口
    __business_id = demo.uuid.uuid1()
    # params = "{\"code\":\"\"}"
    params = '{"code":"' + regNum + '"}'
    print(send_sms(__business_id, phone, "gxq网站用户注册测试", "SMS_99935016", params))
    request.session['regNum'] = regNum
    # 验证码已发送返回'200'
    return HttpResponse('200')


# 注册功能
# author=chaim
# type=post，param=phoneNum,password,regNum
def register(request):
    phone = request.POST['usuaPhoneNum']
    password = request.POST['password']
    regNum = request.POST['identifyCode']
    print (phone)
    print(password)
    print(regNum)
    if regNum == request.session['regNum']:
        models.DoaTUser(
            phone = phone,
            regist_passwd = password,
                ).save()

        return HttpResponse('注册成功')
    else:
        # 验证码错误返回'2'
        return HttpResponse('验证码错误')









# 登录功能
# author=chaim
# type=post，param=username,password
def login(request):
    name = request.POST['username']
    password = request.POST['password']
    data = models.DoaTUser.objects.all().filter(name=name)
    if data:
        if password == data[0]['regist_passwd']:
            return HttpResponse('登陆成功')
        else:
            return HttpResponse('密码错误，请重新输入')
    else:
        return HttpResponse('用户名不存在，请前往注册')







# 首页显示
# author=chaim
# type=null，param=null
def index_diaplay(request):

    # 获取用户登录信息
    content ={}
    content['username'] = request.session['username']

    # 获取广告信息
    content['adv'] = functionalModule.adv_search()

    # 获取公司信息
    # company_position = request.POST['company_position']
    company_position = '高新'
    content['company'] = functionalModule.company_position_search(company_position)

    # 获取职位信息
    # key = request.POST['job_category']
    key = '技术'
    content['job'] = functionalModule.job_category_search(key)

    # 获取活动信息
    content['active'] = functionalModule.activ()

    return render(request, '2.html', content)







# 主搜索功能(实现输入关键字进行自动匹配职位名称和公司名称的功能)
def search(request):
    content = {}
    key = request.POST['search_key']
    content['result'] = functionalModule.search(key)
    return render(request, '###.html', content)







# # 公司介绍功能
# def display_companyIntrdouction(request):
#     content = search('公司介绍','companyIntrdouction')
#     content['username'] = request.session['username']
#     return render(request,'index.html',content)




# def sign_in(request):
#     name = request.POST['username']
#     password = request.POST['password']
#     if regNum:
#         if regNum==request.session['regNum']:
#             pass
#         else:
#             return ret.ret(ret.retError(),"验证码错误")
#     a = models.TCompanyRegister.objects.all().values().filter(register_id = name)
#     if a:
#         for b in a:
#             if password ==b['passwd']:
#                 content = {}
#                 content['succeed'] = {'report':'succeed'}
#                 request.session['username'] = name
#                 content['username'] = request.session['username']
#                 return index_diaplay(request)
#             else:
#                 content = {}
#                 content['error'] = {'report': '密码错误,请重新输入！'}
#                 return ret.ret(ret.retError(), "密码错误")
#                 # return render(request, 'sign.html', content)
#
#     else:
#         models.TCompanyRegister(
#         register_id = name,
#         passwd = password,
#         ).save()
#         content = {}
#         content['name_null'] = {'report': '注册成功！'}
#         # Json
#         request.session['username'] = name
#         return index_diaplay(request)


#
# # 手机注册验证码
# def regist(request):
#     __name__ = 'query'
#     phone=request.POST['username']
#     if phone:
#         phone=str(phone)
#     else:
#         return ret.ret(ret.retError(),"手机号错误")
#     # phone=str('13281282010')
#     regNum=str(random.randint(100000,999999))
#     timeNow=str(datetime.datetime.now().strftime('%Y%m%d'))
#     if __name__ == 'send':
#         pass
#
#     if __name__ == 'query':
#         print(regNum)
#         __business_id = demo.uuid.uuid1()
#         print(__business_id)
#         # params = "{\"code\":\"\"}"
#         params = '{"code":"'+regNum+'"}'
#         print(send_sms(__business_id, phone, "gxq网站用户注册测试", "SMS_99935016", params))
#         request.session['regNum']=regNum
#         return ret.ret(ret.retSuccess(),"已发送验证码")
#
# def jsonx(request):
#     print("jsonx click")
#     return ret.ret(200,"noods")







# def search(request):
#     content = {}
#     key = request.POST['search_content']
#     content['username'] = request.session['username']
#
#     if key:
#         search_result = models.TJobPublish.objects.all().values().filter(job__contains=key)
#         content['position'] = search_result
#
#         search_result2 = models.TCompanyInfo.objects.all().values().filter(company_name__contains=key)
#         content['company'] = search_result2
#
#         return render(request, 'searchreturn.html', content)
#     else:
#         kong = {}
#         return render(request, 'searchreturn.html', kong)




# 首页职位的直接搜索
def job_search(request):
    content = {}
    key = request.POST['job_name']
    if key:
        search_result = models.TJobPublish.objects.all().values().filter(job__contains=key)
        content['position'] = search_result
        return render(request, 'searchreturn.html', content)
    else:
        kong = {}
        return render(request, 'index.html', kong)






# 首页职位的分类搜索
# ****************************************
def job_category(request):
    content = {}
    qwe = []
    i = 0
    key = request.POST['job_category']
    if key:
        search_result = models.TJobPublish.objects.all().values().filter(job_category=key)
        for i in range(0,len(search_result)):
            search_key = search_result[i]['company_name']
            company = models.TCompanyInfo .objects.all().values().filter(company_name=search_key)
            content['test']= chain(search_result[i],company[0])
            a = dict(search_result[i].items()+company[0].items())
            qwe.append(a)
            content['test'] = qwe
            print (content['test'])
        return render(request, 'index.html', content)
        # return HttpResponse(a)
    else:
        kong = {}
        return render(request, 'index.html', kong)




# 首页公司位置的分类搜索
def company_sort_search(request):
    content = {}
    key = request.POST['company_sort_search']
    if key:
        search_result = models.TCompanyInfo.objects.all().values().filter(provence__contains=key)
        content['company'] = search_result
        return render(request, 'index.html', content)
    else:
        kong = {}
        return render(request, 'index.html', kong)



# 首页内容
def shouye(request):

# 职位推荐
    content = {}
    qwe = []
    i = 0

    search_result = models.TJobPublish.objects.all().values().filter(is_exigency='1')
    for i in range(0, len(search_result)):
        search_key = search_result[i]['company_name']
        company = models.TCompanyInfo.objects.all().values().filter(company_name=search_key)
        content['job'] = chain(search_result[i], company[0])
        a = dict(search_result[i].items() + company[0].items())
        qwe.append(a)
        content['job'] = qwe


# 公司推荐

    company = models.TCompanyInfo.objects.all().values()
    # content['company'] = company


    content['company'] = company



# 活动推荐
    active = models.TActivity.objects.all().values()
    print (active)
    huodong = []
    for i in range(0, len(active)):
        search_key = active[i]['md5']
        data = models.DoaTDrc.objects.all().values().filter(md5=search_key)
        content['active'] = chain(active[i], data[0])
        a = dict(active[i].items() + data[0].items())
        huodong.append(a)
        content['active'] = huodong


    content['username'] = request.session['username']

    return render(request, 'shouye.html', content)



# 公司介绍
def gongsijieshao(request):

    # 查询公司信息
    content = {}
    # search_key = request.POST['company_name']
    search_key = 'ssa'
    company = models.TCompanyInfo.objects.all().values().filter(company_name__contains=search_key)
    if company:
        content['company'] = company[0]

        # 查询公司logo
        data = models.DoaTDrc.objects.all().values().filter(md5=company[0]['logo'])
        content['data']=data[0]
        # 查询公司发布的职位
        job = models.TJobPublish.objects.all().values().filter(company_name__contains=search_key)
        content['job']=job

        # 面试评价
        pingjia = models.TInterviewEvaluation.objects.all().filter(company_name=search_key)
        content['pingjia'] = pingjia

        # 相似职位

    else:
        content['null'] = '查询结果为空！'

    return render(request, 'gongsijieshao.html', content)



# 职位信息
def zhiweixinxi(request):
    # 查询职位信息
    content = {}
    # search_key = request.GET['job_id']
    search_key = '1'
    job = models.TJobPublish.objects.all().values().filter(id = search_key)
    content['job'] = job[0]

# 查询发布职位的公司
    company = models.TCompanyInfo.objects.all().values().filter(company_id=job[0]['company_id'])
    print (company[0])
    content['company'] = company[0]
    # 查询logo
    data = models.DoaTDrc.objects.all().values().filter(md5=company[0]['logo'])
    content['data']=data[0]
    return render(request,'4.html',content)




# 企业的条件搜索
def enterprise_condition_search(request):
    content = {}
    qwe = []
    # # 写字楼区域
    # postion = request.POST['postion']
    # # 行业领域
    # field = request.POST['field']
    # # 企业规模
    # scale = request.POST['scale']
    # # 企业性质
    # company_nature = request.POST['Company_nature']
    postion ='高新'
    field = '生物'
    scale = '200'
    company_nature = '外资'

    company = models.TCompanyInfo.objects.all().values().filter(company_type__contains=company_nature).filter(company_scale__contains=scale).filter(industry_categroy__contains=field).filter(provence__contains=postion)
    # content['company'] = company
    for i in range(0, len(company)):
        search_key = company[i]['logo']
        data = models.DoaTDrc.objects.all().values().filter(md5=search_key)
        content['test'] = chain(company[i], data[0])
        a = dict(company[i].items() + data[0].items())
        qwe.append(a)
        content['company'] = qwe
    return render(request, 'enterprise_condition_search.html', content)
    # return HttpResponse(qwe)




# 职位的条件搜索,(未完成，待完善)
# def job_condition_search(request):
#     content = {}
#     qwe = []
#
#     # # 写字楼区域
#     # postion = request.POST['postion']
#     # # 职位分类
#     # job_category = request.POST['job_category']
#     # 薪资
#     # money = request.POST['money']
#     #  工作年限
#     # experience_required = request.POST['experience_required']
#     #  学历要求
#     # education_required = request.POST['education_required']
#     #  发布日期
#     # release_time = request.POST['release_time']
#
#     postion ='高新'
#     job_category = '技术'
#     salary = '1000'
#     experience_required = '0'
#     education_required = '初高中'
#     # release_time = '2012-12-12 00:00:00'
#     company = models.TCompanyInfo.objects.all().values().filter(provence__contains=postion)
#
#     for i in range(0, len(company)):
#         key = company[i]['company_id']
#         job = models.TJobPublish.objects.all().values().filter(company_id=key)
#         print (job)
#         job2 = job.filter(education_required=education_required).filter(experience_required=experience_required).filter(salary=salary).filter(job_category=job_category)
#         print (job2)
#         # content['test'] = chain(company[i],job2[i])
#         a = dict(company[i].items()+job2[i].items())
#         qwe.append(a)
#         content['job'] = qwe
#         # content['job']=job2
#     return render(request, 'job_condition_search.html', content)
    # return HttpResponse(qwe)



def job_condition_search(request):
    # postion = '高新'
    # job_category = '技术'
    # salary = '1000'
    # experience_required = '0'
    # education_required = '初高中'

    job = models.TCompanyInfo.objects.filter(company_id='10010').values('TJobPublish__job')
    print (job)
    return (job)



    # django中使用原生sql语句的方法
#     cursor = connection.cursor()
#     cursor.execute('''select * FROM T_COMPANY_INFO,T_JOB_PUBLISH WHERE T_COMPANY_INFO.company_id = T_JOB_PUBLISH.company_id AND provence = '成都高新西' AND education_required = '初高中' AND experience_required = '0'AND salary = '1000'AND job_category = '技术'
# ''')
#     # raw = cursor.fetchone()  # 返回结果行游标直读向前，读取一条
#     print (cursor.fetchall()) # 读取所有
