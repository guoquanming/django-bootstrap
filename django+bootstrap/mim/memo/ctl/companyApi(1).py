
# -*- coding: utf-8 -*-


from __future__ import print_function
from __future__ import print_function
from __future__ import unicode_literals

import json
import random
import sys

import datetime
from itertools import chain

from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from memo.functionalModule import search
from memo import models
import memo.dto.ret as ret

reload(sys)
sys.setdefaultencoding('utf8')


# 公司主页 相似职位
def companyJobLike(res):
    job=res.GET.get("job_category")
    if job:
        pass
    else:
        return ret.Error(ret.txtArgu)
    jobLike=models.TJobPublish.objects.all().filter(job_category=job)[:5]
    return ret.Success(ret.enjson(jobLike))



# 公司主页 职位列表
def companyJobList(res):
    companyId=res.GET.get("company_id")
    page = res.GET.get('pageIndex')

    if companyId:
        pass
    else:
        companyId=1
        # return ret.Error(ret.txtArgu)


    jobList = models.TJobPublish.objects.all().filter(company_id=int(companyId))
    if jobList:
        pass
    else:
        return ret.pageError(ret.txtNoPage)
    paginator = Paginator(jobList, 20)


    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    # pageCount=paginator.count
    # pageNum=paginator.num_pages
    # contacts = ret.json(contacts)
    return ret.pageSuccess(pageIndex=page,pageNum=paginator.num_pages,pageCount=paginator.count,content=contacts)





# 修改公司相关信息
def companyInfo(res):
    return "111"

# 返回公司信息
def companyInfoList(request):
    # 返回所有
    infolist=models.TCompanyInfo.objects.all().filter(company_id=1)[:20]
    # infolist = serializers.serialize("json", infolist)

    # 返回一些
    # infolist=models.TCompanyInfo.objects.values('company_id','company_name').filter(company_id=1)[:20]
    # infolist=list(infolist)

    if infolist:
        pass
    else:
        return ret.Error("没有数据")
    print (infolist)
    return ret.enjson(infolist)

def jsonx(request):
    return ret.ret(ret.retSuccess(), "yes")