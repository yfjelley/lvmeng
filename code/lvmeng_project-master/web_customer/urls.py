from django.conf.urls import url
from web_customer import views
urlpatterns = [
    url(r'lv_announcement_process/$',views.lv_announcement_process),
    url(r'lv_announcement_list/$',views.lv_announcement_list),
    url(r'check_announcement/$',views.check_announcement),
    url(r'announcement/$',views.lv_announment),
    url(r'product/$',views.product),
    url(r'redi_to_index/$',views.redi_to_index),
    url(r'web_customer_headline_list/$',views.web_customer_headline_list),
    url(r'web_customer_headline_detail/$',views.web_customer_headline_detail),
    url(r'noticelist/$',views.noticelist),
    url(r'notice/$',views.notice),
    url(r'personal_info/$',views.personal_info),
    url(r'^customer_business_search/$',views.customer_business_search),
    url(r'^show_product_by_type/$',views.show_product_by_type),


	# url(r'^ie8', views.homePage_ie8),
    # url(r'^', views.homePage),
    # url(r'^mobi', views.mobile_homePage),
]