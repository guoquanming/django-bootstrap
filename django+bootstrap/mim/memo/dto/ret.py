# -*- coding: utf-8 -*-
import json

import sys
from django.core import serializers
from django.http import HttpResponse

reload(sys)
sys.setdefaultencoding('utf8')


txtIntnet="网络错误"
txtErr="错误"
txtArgu="参数错误"
txtNoPage="没有数据"
retSuccess=1
retError=0




def ret(code,content):
    resp = {
        "success":code,
        "content":content
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")




def page(code,pageIndex,pageNum,pageCount,content):
    resp = {
        "success": code,
        "pageIndex":pageIndex,
        "pageNum":pageNum,
        "pageCount":pageCount,
        "content": content
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

def pageSuccess(pageIndex,pageNum,pageCount,content):
    resp = {
        "success": retSuccess,
        "pageIndex": pageIndex,
        "pageNum": pageNum,
        "pageCount": pageCount,
        "content": content
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

def pageError(content):
    resp = {
        "success": retError,
        "pageIndex": 0,
        "pageNum": 0,
        "pageCount": 0,
        "content": content
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")





def Success(content):
    return ret(retSuccess,content)

def Error(content):
    return ret(retError,content)

def enjson(content):
    return HttpResponse(serializers.serialize("json",content), content_type="application/json")

