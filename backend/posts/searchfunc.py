import json

from posts import regex,token
from .models import Assign,Title,Section,Permission,Member,Enroll,Content,Checklist,Comment,Calender

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

def title_search(input_titleid):
    comment_list = []
    data = list(Title.objects.all().filter(titleid = input_titleid))
    str_data = str(data)
    power_list = regex.parse_title(str_data)
    for i in power_list:
        json_tmp = {}
        json_tmp['titleid'] = i[0]
        json_tmp['titlename'] = i[1]
        json_tmp['titleinfo'] = i[2]
        comment_list.append(json_tmp)
    comment_list=json.dumps(comment_list)
    return comment_list

def section_search(input_sectionid):
    comment_list = []
    data = list(Section.objects.all().filter(sectionid = input_sectionid))
    str_data = str(data)
    power_list = regex.parse_section(str_data)
    for i in power_list:
        json_tmp = {}
        json_tmp['sectionid'] = i[0]
        json_tmp['sectionname'] = i[1]
        json_tmp['titleid'] = i[2]
        comment_list.append(json_tmp)
    comment_list=json.dumps(comment_list)
    return comment_list

def permission_searchcontent(input_contentid):
    data = list(Permission.objects.all().filter(contentid = input_contentid))
    Permission_list = []
    str_data = str(data)
    power_list = regex.parse_Permission(str_data)
    for i in power_list:
        json_tmp = {}
        json_tmp['priority'] = i[0]
        json_tmp['contentid'] = i[1]
        json_tmp['memeberid'] = i[2]
        json_tmp['filename'] = i[3]
        json_tmp['fileid'] = i[4]
        Permission_list.append(json_tmp)
    Permission_list = json.dumps(Permission_list)
    return Permission_list

def permission_searchmember(input_memberid):
    data = list(Permission.objects.all().filter(memberid = input_memberid))
    Permission_list = []
    str_data = str(data)
    power_list = regex.parse_Permission(str_data)
    for i in power_list:
        json_tmp = {}
        json_tmp['priority'] = i[0]
        json_tmp['contentid'] = i[1]
        json_tmp['memeberid'] = i[2]
        json_tmp['filename'] = i[3]
        json_tmp['fileid'] = i[4]
        Permission_list.append(json_tmp)
    Permission_list=json.dumps(Permission_list)
    return Permission_list

def member_search(input_token):
    get_memberid = token.earn_memberid(input_token)
    login_list = []
    login_json = {}
    data = list(Enroll.objects.all().filter(memberid = get_memberid))
    str_data = str(data)
    enrolltitle_list = regex.parse_enroll(str_data)
    enroll_list = []
    for i in enrolltitle_list:
        json_tmp = {}
        json_tmp['titleid'] = i[0]
        json_tmp['titlename'] = i[1]
        json_tmp['titleinfo'] = i[2]
        json_tmp['enrollid'] = i[4]
        enroll_list.append(json_tmp)
    login_json['enrollTitle'] = enroll_list
    assign_data = list(Assign.objects.all().filter(memberid = get_memberid))
    str_assigndata = str(assign_data)
    assigncontent_list = regex.parse_assign(str_assigndata)
    assign_list = []
    for j in assigncontent_list:
        json_assigntmp = {}
        json_assigntmp['contentid'] = j[0]
        json_assigntmp['assignid'] = j[2]
        json_assigntmp['contentname'] = j[3]
        json_assigntmp['contentinfo'] = j[4]
        calender_data = list(Calender.objects.all().filter(contentid = j[0]))
        str_calenerdata = str(calender_data)
        calender_list = regex.parse_calender(str_calenerdata)
        calender_jlist = []
        for l in calender_list:
            json_catmp = {}
            json_catmp['indexnumber'] = l[3]
            json_catmp['starttime'] = l[0]
            json_catmp['duetime'] = l[1]
            calender_jlist.append(json_catmp)
        json_assigntmp['calender'] = calender_jlist
        assign_list.append(json_assigntmp)
    login_json['assignContent'] = assign_list
    login_list.append(login_json)
    login_list=json.dumps(login_list)
    return login_list

def enroll_searchmember(input_token):
    get_memberid = token.earn_memberid(input_token)
    data = list(Enroll.objects.all().filter(memberid = get_memberid))
    enroll_list = []
    str_data = str(data)
    power_list = regex.parse_enroll(str_data)
    for i in power_list:
        json_tmp = {}
        json_tmp['titleid'] = i[0]
        json_tmp['memeberid'] = i[3]
        json_tmp['enrollid'] = i[4]
        enroll_list.append(json_tmp)
    enroll_list=json.dumps(enroll_list)
    return enroll_list

def enroll_searchtitle(input_titleid):
    data = list(Enroll.objects.all().filter(titleid = input_titleid))
    comment_list = []
    str_data = str(data)
    power_list = regex.parse_enroll(str_data)
    for i in power_list:
        json_tmp = {}
        json_tmp['titleid'] = i[0]
        json_tmp['memeberid'] = i[3]
        json_tmp['enrollid'] = i[4]
        comment_list.append(json_tmp)
    comment_list=json.dumps(comment_list)
    return comment_list

def content_search(input_contentid):
    content_list = []
    data = Content.objects.all().filter(contentid = input_contentid)
    str_data = str(data)
    power_list = regex.parse_content(str_data)
    for i in power_list:
        json_tmp = {}
        json_tmp['contentid'] = i[0]
        json_tmp['contentname'] = i[1]
        json_tmp['contentinfo'] = i[2]
        json_tmp['contentstate'] = i[3]
        str_sectionid = str(i[4])
        print(str_sectionid)
        only_sectionid = regex.parse_section(str_sectionid)
        print(only_sectionid)
        json_tmp['sectionid'] = i[4]
        comment_data = list(Comment.objects.all().filter(contentid = input_contentid))
        str_commentdata = str(comment_data)
        comment_list = regex.parse_text(str_commentdata)
        comment_jlist = []
        for j in comment_list:
            json_ctmp = {}
            json_ctmp['comnumber'] = j[0]
            json_ctmp['memberid'] = j[1]
            json_ctmp['comcomment'] = j[2]
            json_ctmp['commenttime'] = j[3]
            comment_jlist.append(json_ctmp)
        json_tmp['commentlist'] = comment_jlist
        checklist_data = list(Checklist.objects.all().filter(contentid = input_contentid))
        str_cheklistdata = str(checklist_data)
        check_list = regex.parse_checklist(str_cheklistdata)
        cheklist_list = []
        for k in check_list:
            json_cktmp = {}
            json_cktmp['listnumber'] = k[0]
            json_cktmp['listname'] = k[1]
            json_cktmp['checked'] = k[2]
            cheklist_list.append(json_cktmp)
        json_tmp['checklistlist'] = cheklist_list
        content_list.append(json_tmp)
        calender_data = list(Calender.objects.all().filter(contentid = input_contentid))
        str_calenerdata = str(calender_data)
        calender_list = regex.parse_calender(str_calenerdata)
        calender_jlist = []
        for l in calender_list:
            json_catmp = {}
            json_catmp['indexnumber'] = l[3]
            json_catmp['starttime'] = l[0]
            json_catmp['duetime'] = l[1]
            calender_jlist.append(json_catmp)
        json_tmp['calender'] = calender_jlist
    content_list=json.dumps(content_list)
    return content_list

def calender_searhch(input_contentid):
    calender_list = []
    data = list(Calender.objects.all().filter(contentid = input_contentid))
    str_data = str(data)
    power_list = regex.parse_calender(str_data)
    for i in power_list:
        json_tmp = {}
        json_tmp['indexnumber'] = i[3]
        json_tmp['starttime'] = i[0]
        json_tmp['duetime'] = i[1]
        json_tmp['contentid'] = i[2]
        calender_list.append(json_tmp)
    calender_list=json.dumps(calender_list)
    return calender_list

def check_list_search(input_contentid):
    comment_list = []
    data = list(Checklist.objects.all().filter(contentid = input_contentid))
    str_data = str(data)
    power_list = regex.parse_checklist(str_data)
    for i in power_list:
        json_tmp = {}
        json_tmp['listnumber'] = i[0]
        json_tmp['listname'] = i[1]
        json_tmp['checked'] = i[2]
        comment_list.append(json_tmp)
    comment_list=json.dumps(comment_list)
    return comment_list

def search_all(input_titleid):
    section_data = list(Section.objects.all().filter(titleid = input_titleid))
    str_sectiondata = str(section_data)
    section_list = regex.parse_section(str_sectiondata)
    section_jlist = []
    for j in section_list:
        json_section = {}
        json_section['sectionid'] = j[0]
        json_section['sectionname'] = j[1]
        content_data = list(Content.objects.all().filter(sectionid = j[0]))
        str_contentdata = str(content_data)
        content_list= regex.parse_content(str_contentdata)
        content_jlist = []
        for k in content_list:
            json_content = {}
            json_content['contentid'] = k[0]
            json_content['contentname'] = k[1]
            json_content['contentinfo'] = k[2]
            json_content['state'] = k[3]
            checklist_data = list(Checklist.objects.all().filter(contentid = k[0]))
            str_cheklistdata = str(checklist_data)
            checklist_list = regex.parse_checklist(str_cheklistdata)
            checklist_jlist = []
            for l in checklist_list:
                json_checktmp = {}
                json_checktmp['listnumber'] = l[0]
                json_checktmp['listname'] = l[1]
                json_checktmp['checked'] = l[2]
                checklist_jlist.append(json_checktmp)
            json_content['includeChecklist'] = checklist_jlist
            comment_data = list(Comment.objects.all().filter(contentid = k[0]))
            str_commentdata = str(comment_data)
            comment_list = regex.parse_text(str_commentdata)
            comment_jlist = []
            for m in comment_list:
                json_comment = {}
                json_comment['comnumber'] = m[0]
                json_comment['memberid'] = m[1]
                json_comment['comcomment'] = m[2]
                json_comment['commenttime'] = m[3]
                comment_jlist.append(json_comment)
            json_content['includeComment'] = comment_jlist
            calender_data = list(Calender.objects.all().filter(contentid = k[0]))
            str_calenerdata = str(calender_data)
            calender_list = regex.parse_calender(str_calenerdata)
            calender_jlist = []
            for n in calender_list:
                json_calender = {}
                json_calender['indexnumber'] = n[3]
                json_calender['starttime'] = n[0]
                json_calender['duetime'] = n[1]
                calender_jlist.append(json_calender)
            json_content['includeCalender'] = calender_jlist
            content_jlist.append(json_content)
        json_section['includeContent'] = content_jlist
        section_jlist.append(json_section)
    section_jlist=json.dumps(section_jlist)
    return section_jlist
