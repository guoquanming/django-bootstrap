# -*- coding: utf-8 -*-
from itertools import chain

from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
# from memo import views
from memo import models


import urllib2

# 此模块实现在数据注册表中查找文件名字返回该文件中的具体信息



# def search(key,back):
#     content = {}
#     a = models.DataInfo.objects.all().values()
#     search = a.filter(title=key)
#     for b in search:
#         fo1 = urllib2.urlopen(b['data_store'], "rb")
#         b['data_store'] = fo1.read()
#         content[back] = b
#     return content


# 获取广告信息
def adv_search():
    list_adv = []
    content = {}
    adv = models.TAdvertisement.objects.all().filter(dispaly='1')

    for i in range(0, len(adv)):
        search_key = adv[i]['md5']
        data = models.DoaTDrc.objects.all().values().filter(md5=search_key)
        content['test'] = chain(adv[i], data[0])
        a = dict(adv[i].items() + data[0].items())
        list_adv.append(a)
        # # 把获取到的广告信息放在content['adv']中
        # content['adv'] = list_adv
    return list_adv



# 获取公司信息
def company_position_search(key):
    company = models.TCompanyInfo.objects.all().values().filter(provence__contains=key)
    return company



# 获取职位信息
def job_category_search(key):
    content = {}
    job_list = []
    # key = '技术'
    job = models.TJobPublish.objects.all().values().filter(job_category=key)
    content['job'] = job
    # 查询发布职位的公司
    for i in range(0, len(job)):
        search_key = job[i]['company_id']
        company = models.TCompanyInfo.objects.all().values().filter(company_id=search_key)

        # 查询公司logo
        logo = models.DoaTDrc.objects.all().filter(md5=company[0]['md5'])
        # content['test'] = chain(job[i], company[0],logo[0])
        a = dict(job[i].items() +company[0].items()+ logo[0].items())
        job_list.append(a)
    return job_list




# 获取活动信息
def activ():
    list_activ = []
    activ = models.TActivity.objects.all().filter(dispaly='1')

    for i in range(0, len(activ)):
        search_key = activ[i]['md5']
        data = models.DoaTDrc.objects.all().values().filter(md5=search_key)
        # content['test'] = chain(activ[i], data[0])
        a = dict(activ[i].items() + data[0].items())
        list_activ.append(a)
        # 把获取到的活动信息放在content['active']中
    return list_activ


# 搜索框的模糊搜索(实现输入关键字进行自动匹配职位名称和公司名称的功能)
def search(key):
    content = {}

    job = models.TJobPublish.objects.all().values().filter(job__contains=key)
    content['job'] = job

    company = models.TCompanyInfo.objects.all().values().filter(company_name__contains=key)
    content['company'] = company

    return content


