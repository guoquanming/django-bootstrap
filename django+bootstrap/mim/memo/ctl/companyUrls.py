
from django.conf.urls import url
from django.contrib import admin

from memo.ctl import companyApi

urlpatterns = [
    url(r'^jsonx/', companyApi.jsonx),
    url("companyinfolist",companyApi.companyInfoList),
    url("companyjoblist",companyApi.companyJobList)
]
    # url(r'^index/',views.display_companyIntrdouction),