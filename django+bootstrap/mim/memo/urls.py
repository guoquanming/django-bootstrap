
from django.conf.urls import url,include
from django.contrib import admin
from memo import views
import url_sign

urlpatterns = [

    url(r'^sign/', include(url_sign)),




    # url(r'^$',views.display_companyIntrdouction ),
    # url(r'^sign/',views.sign_htm),
    # url(r'^regist/',views.regist),
    # url(r'^sign_in/', views.sign_in),
    # url(r'^search/', views.search),
    url(r'^job_search/', views.job_search),
    url(r'^job_category/', views.job_category),
    url(r'^company_sort_search/', views.company_sort_search),
    # url(r'^jsonx/',views.jsonx),
    url(r'^shouye/', views.shouye),
    url(r'^gongsijieshao/', views.gongsijieshao),
    url(r'^zhiweixinxi/', views.zhiweixinxi),
    url(r'^ecs/', views.enterprise_condition_search),
    url(r'^jcs/', views.job_condition_search),

    url(r'^zhiweixinxi/',views.zhiweixinxi),
]
    # url(r'^index/',views.display_companyIntrdouction),