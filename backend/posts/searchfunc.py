import json

from posts import regex
from .models import Assign

def assign_searchmember(get_memberid):
    data = list(Assign.objects.all().filter(memberid = get_memberid))
    str_data = str(data)
    power_list = regex.parse_assign(str_data)
    assign_list = []
    for i in power_list:
        json_tmp = {}
        json_tmp['contentid'] = i[0]
        json_tmp['memberid'] = i[1]
        json_tmp['assignid'] = i[2]
        assign_list.append(json_tmp)
    assign_list=json.dumps(assign_list)
    return assign_list

def assign_searchcontent(input_contentid):
    data = list(Assign.objects.all().filter(contentid = input_contentid))
    assign_list = []
    str_data = str(data)
    power_list = regex.parse_assign(str_data)
    for i in power_list:
        json_tmp = {}
        json_tmp['contentid'] = i[0]
        json_tmp['memberid'] = i[1]
        json_tmp['assignid'] = i[2]
        assign_list.append(json_tmp)
    assign_list = json.dumps(assign_list)
    return assign_list