#coding:utf-8
from django.shortcuts import HttpResponseRedirect

permission_dict = {
    '/erp/show_business_base_info/':'auth.business_info_modify',             #查看机构详细信息 1
    '/erp/modify_business_base_info/':'auth.business_info_modify',           #修改机构信息1
    '/erp/business_carousel_list_delete/':'auth.business_info_modify',       #机构轮播图列表1
    '/erp/business_carousel_add/':'auth.business_info_modify',               #机构轮播图添加1
    '/erp/agent_list/':'auth.employee_show',                                 #员工列表
    '/erp/agent_process/':'auth.employee_process',                           #员工操作2
    '/erp/agent_customer_allot/':'auth.employee_process',                    #员工删除2
    '/erp/position_list/':'auth.employee_process',                           #职位列表2
    '/erp/position_add_modify/':'auth.employee_process',                     #职位添加和修改2
    '/erp/picture_logos/':'auth.business_announcement_out',                  #添加/修改机构公告信息(对外)3
    '/erp/product_process/':'auth.product_process',                          #产品修改/添加4
    '/oa/check_table/':'auth.check_work',                                    #考勤表5
    '/oa/employee_distribution/':'auth.check_work',                          #员工分布图5
    '/oa/employee_position/':'auth.check_work',                              #员工位置查询5
    '/oa/employee_history_position/':'auth.check_work',                      #员工轨迹回放5
    '/oa/announcement_add_modify/':'auth.business_announcement_inner',       #添加/修改机构公告信息(对内)6
    '/erp/income_inquiry/':'auth.financial_management',                      #财务管理7
    'type_employee':'auth.employee_show',                                    #员工查看8
    '/oa/check_time_setting/':'auth.check_time_setting',                           #考勤时间设定

}

class QtsPermissionMiddleware(object):
    def process_request(self, request):
        request.session.set_expiry(120*60) #session时间，如果用户在2个小时之内对页面无操作，则需要重新登录，防止用户离开未退出

        if not request.user.is_anonymous() and request.user.is_authenticated and request.user.last_name !=u"客户":
        # if not request.user.is_anonymous() and request.user.is_authenticated and not request.user.customer:
            permissions = get_permissions(request)
            url = request.path
            try:
                if permission_dict[url] in permissions:
                    pass
                else:
                    return HttpResponseRedirect("/erp/no_permission/")
            except:
                url = request.get_full_path()
                if 'type=agent' in url:
                    if 'auth.employee_show' in permissions:
                        pass
                    else:
                        return HttpResponseRedirect("/erp/no_permission/")


def get_permissions(request):
    permissions = []
    try:
        user_agent = request.user.agent
    except:
        user_agent = None
    # if request.user.last_name == u"员工":
    if user_agent:
        for permission in request.user.agent.permissions.all():
            permissions.append('auth.'+permission.codename)
    else:
        for permission in request.user.get_all_permissions():
            permissions.append(permission)

    return permissions