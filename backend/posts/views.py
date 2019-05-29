import jwt
import datetime
import json

from posts import regex, token,searchfunc
from pytz import timezone

from rest_framework import generics, permissions
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Assign,Checklist,Calender,Comment,Content,Contentstate,Enroll,File,Member,Permission,Section,Title, Permissionstate, Session
from .serializers import AssignSerializer,ChecklistSerializer,CalenderSerializer,CommentSerializer,ContentSerializer,ContentstateSerializer,EnrollSerializer,FileSerializer,MemberSerializer,PermissionSerializer,SectionSerializer,TitleSerializer,PermissionstateSerializer,SessionSerializer

# Create your views here.
#Assign
class AssignList(generics.ListAPIView):
    queryset = Assign.objects.all()
    serializer_class = AssignSerializer

class AssignCreate(APIView):
    parser_classes = (JSONParser,)
    def post(self, request, format=None):
        input_contentid =request.data["contentid"]
        input_token = str(request.data["token"])
        get_memberid = token.earn_memberid(input_token)
        try:
            member = Member.objects.get(memberid=get_memberid)
            content = Content.objects.get(contentid=input_contentid)
            Assign.objects.create(memberid = member, contentid = content)
            token.extend_token(input_token)
            return JsonResponse({'create': 'success'}) 
        except:
            return JsonResponse({'create': 'fail'})

class AssignSearchMember(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_token = str(request.data["token"])
        if Session.objects.filter(token = input_token).exists():
            get_memberid = token.earn_memberid(input_token)
            assign_list= searchfunc.assign_searchmember(get_memberid)
            token.extend_token(input_token)
            return HttpResponse(assign_list, content_type="application/json")
        else:
            assign_list = []
            token.extend_token(input_token)
            return HttpResponse(assign_list, content_type="application/json")
        
class AssignSearchContent(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_contentid = str(request.data["contentid"])
        input_token = str(request.data["token"])
        assign_list = searchfunc.assign_searchcontent(input_contentid)
        token.extend_token(input_token)
        return HttpResponse(assign_list, content_type="application/json")

class AssignDelete(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_token = str(request.data["token"])
        get_memberid = token.earn_memberid(input_token)
        input_contentid = str(request.data["contentid"])
        try:
            del_assign = Assign.objects.all().filter(memberid = get_memberid, contentid = input_contentid)
            str_data = str(del_assign)
            power_list = regex.parse_assign(str_data)
            acquire_assigncid = str(power_list[0][0])
            acquire_assignid = str(power_list[0][1])
            if((acquire_assignid == get_memberid) and (acquire_assigncid == input_contentid)):
                del_assign.delete()
                token.extend_token(input_token)
                return JsonResponse({'delete': 'success'})
            else:
                token.extend_token(input_token)
                return JsonResponse({'delete': 'Not matched'})
        except:
            token.extend_token(input_token)
            return JsonResponse({'delete': 'fail'})

#Checklist
class ChecklistList(generics.ListAPIView):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

class ChecklistCreate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_listname = request.data["listname"]
        input_contentid = request.data["contentid"]
        input_token = str(request.data["token"])
        try:
            content = Content.objects.get(contentid=input_contentid)
            Checklist.objects.create(listname = input_listname, contentid = content, checked= 0)
            token.extend_token(input_token)
            return JsonResponse({'create': 'success'}) 
        except:
            token.extend_token(input_token)
            return JsonResponse({'create': 'fail'})

class ChecklistSearch(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):    
        input_contentid = request.data["contentid"]
        input_token = str(request.data["token"])
        comment_list = searchfunc.check_list_search(input_contentid)
        token.extend_token(input_token)
        return HttpResponse(comment_list, content_type="application/json")


class ChecklistDelete(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_listnumber = request.data["listnumber"]
        input_token = str(request.data["token"])
        try:
            del_checklist = Checklist.objects.all().filter(listnumber = input_listnumber)    
            del_checklist.delete()
            token.extend_token(input_token)
            return JsonResponse({'delete': 'Delete success'})
        except:
            token.extend_token(input_token)
            return JsonResponse({'delete': 'fail'})

class ChecklistUpdate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_listname = request.data["listname"]
        input_listnumber = request.data["listnumber"]
        input_checked = request.data["checked"]
        input_token = str(request.data["token"])
        try:
            update_checklist = Checklist.objects.all().filter(listnumber = input_listnumber)
            update_checklist.update(listname = input_listname, checked = input_checked)
            token.extend_token(input_token)
            return JsonResponse({'update': 'success'})
        except:
            token.extend_token(input_token)
            return JsonResponse({'update': 'fail'})

#Calender
class CalenderList(generics.ListAPIView):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer

class CalenderCreate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_starttime=request.data["starttime"]
        input_duetime = request.data["duetime"]
        input_contentid = request.data["contentid"]
        input_token = str(request.data["token"])
        try:
            contentid = Content.objects.get(contentid=input_contentid)
            Calender.objects.create(starttime = input_starttime, duetime = input_duetime, contentid = contentid)
            token.extend_token(input_token)
            return JsonResponse({'create': 'success'}) 
        except:
            token.extend_token(input_token)
            return JsonResponse({'create': 'fail'})

class CalenderSearch(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):    
        input_contentid = request.data["contentid"]
        input_token = str(request.data["token"])
        calender_list = searchfunc.calender_searhch(input_contentid)
        token.extend_token(input_token)
        return HttpResponse(calender_list, content_type="application/json")


class CalenderDelete(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_indexnumber = str(request.data["indexnumber"])
        input_contentid = str(request.data["contentid"])
        input_token = str(request.data["token"])
        try:
            del_calender = Calender.objects.all().filter(indexnumber = input_indexnumber, contentid = input_contentid)
            str_data = str(del_calender)
            power_list = regex.parse_calender(str_data)
            acquire_contentid = str(power_list[0][2])
            acquire_indexnumber = str(power_list[0][3])
            if((acquire_indexnumber == input_indexnumber) and ( acquire_contentid == input_contentid)):
                del_calender.delete()
                token.extend_token(input_token)
                return JsonResponse({'delete': 'Delete success'})
            else:
                token.extend_token(input_token)
                return JsonResponse({'delete': 'Not Matched'}) 
        except:
            token.extend_token(input_token)
            return JsonResponse({'delete': 'fail'})


class CalenderUpdate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_contentid = request.data["contentid"]
        input_starttime = request.data["starttime"]
        input_duetime = request.data["duetime"]
        input_isoverlap = request.data["isoverlap"]
        input_token = str(request.data["token"])
        try:
            str_data2 = str(input_starttime)
            power_list2 = regex.parse_midbar(str_data2)
            day = int(power_list2[0][2])
            if(day < 29):
                print("29일 미만 ok")
                update_contentid = Calender.objects.all().filter(contentid = input_contentid)
                str_data = str(update_contentid)
                power_list = regex.parse_calender(str_data)
                print(power_list)
                acquire_contentid = power_list[0][2]
                if(acquire_contentid == input_contentid):
                    update_contentid.update(starttime = input_starttime, duetime = input_duetime, isoverlap = input_isoverlap)
                    token.extend_token(input_token)
                    return JsonResponse({'update': 'success'})
                else:
                    token.extend_token(input_token)
                    return JsonResponse({'update': 'Not Matched'})

            else:
                token.extend_token(input_token)
                print("요일이 이상합니다.")
        except:
            token.extend_token(input_token)
            return JsonResponse({'update': 'fail'})



#Comment
class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentCreate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_token = str(request.data["token"])
        input_comcomment = request.data["comcomment"]
        input_memberid=request.data["memberid"]
        input_contentid = request.data["contentid"]
        cur_time = datetime.datetime.now()
        try:
            content = Content.objects.get(contentid=input_contentid)
            member = Member.objects.get(memberid=input_memberid)
            Comment.objects.create(comcomment=input_comcomment, contentid = content, memberid = member, commenttime = cur_time)
            token.extend_token(input_token)
            return JsonResponse({'create': 'success'}) 
        except:
            token.extend_token(input_token)
            return JsonResponse({'create': 'fail'})

class CommentDelete(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_token = str(request.data["token"])
        input_comnumber = request.data["comnumber"]
        input_memberid=request.data["memberid"]
        try:
            del_comment = Comment.objects.all().filter(comnumber = input_comnumber)
            str_data = str(del_comment)
            power_list = regex.parse_text(str_data)
            acquire_memberid = power_list[0][1]
            if acquire_memberid == input_memberid:
                del_comment.delete()
                token.extend_token(input_token)
                return JsonResponse({'delete': 'Delete success'})
            else:
                token.extend_token(input_token)
                return JsonResponse({'delete': 'Not Matched'}) 
        except:
            token.extend_token(input_token)
            return JsonResponse({'delete': 'fail'})

class CommentUpdate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_token = str(request.data["token"])
        input_comnumber = request.data["comnumber"]
        input_memberid=request.data["memberid"]
        input_comcomment = request.data["comcomment"]
        cur_time = datetime.datetime.now()
        try:
            update_comment = Comment.objects.all().filter(comnumber = input_comnumber)
            str_data = str(update_comment)
            power_list = regex.parse_text(str_data)
            acquire_memberid = power_list[0][1]
            if acquire_memberid == input_memberid:
                update_comment.update(comcomment = input_comcomment,commenttime = cur_time)
                token.extend_token(input_token)
                return JsonResponse({'delete': 'Update success'})
            else:
                token.extend_token(input_token)
                return JsonResponse({'delete': 'Not Matched'}) 
        except:
            token.extend_token(input_token)
            return JsonResponse({'delete': 'fail'})

class CheckComment(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_token = str(request.data["token"])    
        input_contentid = request.data["contentid"]
        comment_list = []
        data = list(Comment.objects.all().filter(contentid = input_contentid))
        str_data = str(data)
        power_list = regex.parse_text(str_data)
        for i in power_list:
            json_tmp = {}
            json_tmp['comnumber'] = i[0]
            json_tmp['memberid'] = i[1]
            json_tmp['comcomment'] = i[2]
            json_tmp['commenttime'] = i[3]
            comment_list.append(json_tmp)
        comment_list=json.dumps(comment_list)
        token.extend_token(input_token)
        return HttpResponse(comment_list, content_type="application/json")
#Content
class ContentList(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentCreate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_token = str(request.data["token"])  
        input_contentname = request.data["contentname"]
        input_contentinfo = request.data["contentinfo"]
        input_contentstate = request.data["contentstate"]
        input_sectionid = request.data["sectionid"]
        try:
            contentstatename = Contentstate.objects.get(statenumber=input_contentstate)
            if(input_sectionid == "NULL"):
                Content.objects.create(contentname=input_contentname, contentinfo = input_contentinfo, contentstate = contentstatename)
                token.extend_token(input_token)
            else:
                section = Section.objects.get(sectionid = input_sectionid)
                Content.objects.create(contentname=input_contentname, contentinfo = input_contentinfo, contentstate = contentstatename, sectionid =section)
                token.extend_token(input_token)
            return JsonResponse({'Create': 'Create success'})
        except:
            token.extend_token(input_token)
            return JsonResponse({'Create': 'fail'})
    
class ContentSearch(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):    
        input_token = str(request.data["token"])  
        input_contentid = request.data["contentid"]
        content_list=searchfunc.content_search(input_contentid)
        token.extend_token(input_token)
        return HttpResponse(content_list, content_type="application/json")

class ContentDelete(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_contentid = request.data["contentid"]
        input_token = str(request.data["token"])  
        try:
            del_content = Content.objects.all().filter(contentid = input_contentid)
            del_content.delete()
            token.extend_token(input_token)
            return JsonResponse({'delete': 'Delete success'})
        except:
            token.extend_token(input_token)
            return JsonResponse({'delete': 'fail'})

class ContentUpdate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_contentid = request.data["contentid"]
        input_contentname = request.data["contentname"]
        input_contentinfo = request.data["contentinfo"]
        input_contentstate = request.data["contentstate"]
        input_token = str(request.data["token"])  
        try:
            update_content = Content.objects.all().filter(contentid = input_contentid)
            update_content.update(contentname = input_contentname,contentinfo = input_contentinfo, contentstate = input_contentstate)
            token.extend_token(input_token)
            return JsonResponse({'update': 'update success'})
        except:
            token.extend_token(input_token)
            return JsonResponse({'update': 'fail'})

#Contentstate
class ContentstateList(generics.ListAPIView):
    queryset = Contentstate.objects.all()
    serializer_class = ContentstateSerializer

class ContentstateCreate(generics.CreateAPIView):
    queryset = Contentstate.objects.all()
    serializer_class = ContentstateSerializer

class ContentstateSearch(generics.RetrieveAPIView):
    queryset = Contentstate.objects.all()
    serializer_class = ContentstateSerializer

class ContentstateDelete(generics.DestroyAPIView):
    queryset = Contentstate.objects.all()
    serializer_class = ContentstateSerializer

class ContentstateUpdate(generics.UpdateAPIView):
    queryset = Contentstate.objects.all()
    serializer_class = ContentstateSerializer

#Enroll
class EnrollList(generics.ListAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer

class EnrollCreate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_titleid = str(request.data["titleid"])
        input_token = str(request.data["token"])
        get_memberid = token.earn_memberid(input_token)
        try:
            member = Member.objects.get(memberid=get_memberid)
            title = Title.objects.get(titleid=input_titleid)
            Enroll.objects.create(memberid=member, titleid=title)
            token.extend_token(input_token)
            return JsonResponse({'create': 'success'}) 
        except:
            token.extend_token(input_token)
            return JsonResponse({'create': 'fail'})

class EnrollSearchTitle(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):  
        input_titleid = str(request.data["titleid"])
        input_token = str(request.data["token"])
        comment_list = searchfunc.enroll_searchtitle(input_titleid)
        token.extend_token(input_token)
        return HttpResponse(comment_list, content_type="application/json")

class EnrollSearchMember(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):   
        input_token = str(request.data["token"])
        enroll_list = searchfunc.enroll_searchmember(input_token)
        token.extend_token(input_token)
        return HttpResponse(enroll_list, content_type="application/json")

class EnrollDelete(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_titleid = str(request.data["titleid"])
        input_token = str(request.data["token"])
        get_memberid = token.earn_memberid(input_token)
        try:
            del_enroll = Enroll.objects.all().filter(memberid = get_memberid, titleid = input_titleid)
            str_data = str(del_enroll)
            power_list = regex.parse_enroll(str_data)
            ac_titleid = str(power_list[0][0])
            ac_memberid = str(power_list[0][3])
            if((ac_memberid == get_memberid) and (ac_titleid == input_titleid)):
                del_enroll.delete()
                token.extend_token(input_token)
                return JsonResponse({'delete': 'success'})
            else:
                token.extend_token(input_token)
                return JsonResponse({'delete': 'Not matched'})
        except:
            token.extend_token(input_token)
            return JsonResponse({'delete': 'fail'})

#File
class FileList(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileCreate(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileSearch(generics.RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileDelete(generics.DestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileUpdate(generics.UpdateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

#Member
class MemberList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberCreate(APIView):
    parser_classes = (JSONParser,)
    def post(self, request, format=None):
        input_memberid = request.data["memberid"]
        input_memberpwd = request.data["memberpwd"]
        input_membername = request.data["membername"]
        input_memberemail = request.data["memberemail"]
        try:
            Member.objects.create(memberid = input_memberid, memberpwd = input_memberpwd, membername = input_membername, memberemail= input_memberemail)
            return JsonResponse({'create': 'success'}) 
        except:
            return JsonResponse({'create': 'fail'})

class MemberDelete(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_memberid = request.data["memberid"]
        input_memberpwd = request.data["memberpwd"]
        try:
            del_member = Member.objects.all().filter(memberid = input_memberid, memberpwd = input_memberpwd)
            str_data = str(del_member)
            power_list = regex.parse_member(str_data)
            ac_memberid = str(power_list[0][0])
            ac_memberpwd = str(power_list[0][1])
            if((ac_memberid == input_memberid) and (ac_memberpwd == input_memberpwd)):
               del_member.delete()
               return JsonResponse({'delete': 'success'})
            else:
                return JsonResponse({'delete': 'Not matched'})
        except:
            return JsonResponse({'delete': 'fail'})

class MemberUpdate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_memberid = request.data["memberid"]
        input_memberpwd = request.data["memberpwd"]
        input_membername = request.data["membername"]
        input_memberemail = request.data["memberemail"]
        try:
            update_member = Member.objects.all().filter(memberid = input_memberid)
            str_data = str(update_member)
            power_list = regex.parse_member(str_data)
            ac_memberid = str(power_list[0][0])
            if ac_memberid == input_memberid:
               update_member.update(membername = input_membername, memberemail = input_memberemail, memberpwd = input_memberpwd)
               return JsonResponse({'update': 'success'})
            else:
                return JsonResponse({'update': 'Not matched'})
        except:
            return JsonResponse({'update': 'fail'})

class MemberSearch(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_token = str(request.data["token"])
        login_list = searchfunc.member_search(input_token)
        token.extend_token(input_token)
        return HttpResponse(login_list, content_type="application/json")

#Permission
class PermissionList(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class PermissionCreate(APIView):
    parser_classes = (JSONParser,)
    def post(self, request, format = None):
        input_priority = request.data["priority"]
        input_memberid = request.data["memberid"]
        input_contentid = request.data["contentid"]
        input_fileid = request.data["fileid"]
        try:
            priority = Permissionstate.objects.get(perstatenumber=input_priority)
            member = Member.objects.get(memberid=input_memberid)
            content = Content.objects.get(contentid=input_contentid)
            fileid = File.objects.get(fileid=input_fileid)
            Permission.objects.create(priority = priority, memberid = member, contentid = content, fileid = fileid)
            return JsonResponse({'create': 'success'}) 
        except:
            return JsonResponse({'create': 'fail'})

class PermissionSearchMember(APIView):
     parser_classes = (JSONParser,)

     def post(self, request, format=None):
        input_memberid = str(request.data["memberid"])
        Permission_list=searchfunc.permission_searchmember(input_memberid)
        return HttpResponse(Permission_list, content_type="application/json")

class PermissionSearchContent(APIView):
     parser_classes = (JSONParser,)

     def post(self, request, format=None):
        input_contentid = str(request.data["contentid"])
        Permission_list=searchfunc.permission_searchcontent(input_contentid)
        return HttpResponse(Permission_list, content_type="application/json")

class PermissionDelete(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_fileid = request.data["fileid"]
        try:
            del_per = Permission.objects.all().filter(fileid = input_fileid)
            del_per.delete()
            return JsonResponse({'delete': 'Delete success'})
        except:
            return JsonResponse({'delete': 'fail'})

#Permissionstate
class PermissionstateList(generics.ListAPIView):
    queryset = Permissionstate.objects.all()
    serializer_class =PermissionstateSerializer

class PermissionstateCreate(generics.CreateAPIView):
    queryset = Permissionstate.objects.all()
    serializer_class = PermissionstateSerializer

class PermissionstateSearch(generics.RetrieveAPIView):
    queryset = Permissionstate.objects.all()
    serializer_class = PermissionstateSerializer

class PermissionstateDelete(generics.DestroyAPIView):
    queryset = Permissionstate.objects.all()
    serializer_class = PermissionstateSerializer

class PermissionstateUpdate(generics.UpdateAPIView):
    queryset = Permissionstate.objects.all()
    serializer_class = PermissionstateSerializer

#Section
class SectionList(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionCreate(APIView):
    parser_classes = (JSONParser,)
    def post(self, request, format=None):
        input_titleid = request.data["titleid"]
        input_sectionname = request.data["sectionname"]
        input_token = str(request.data["token"])
        try:
            thistitle = Title.objects.get(titleid=input_titleid)
            Section.objects.create(titleid = thistitle, sectionname = input_sectionname)
            token.extend_token(input_token)
            return JsonResponse({'create': 'success'}) 
        except:
            token.extend_token(input_token)
            return JsonResponse({'create': 'fail'})

class SectionSearch(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):    
        input_sectionid = request.data["sectionid"]
        input_token = str(request.data["token"])
        comment_list=searchfunc.section_search(input_sectionid)
        token.extend_token(input_token)
        return HttpResponse(comment_list, content_type="application/json")

class SectionDelete(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_sectionid = request.data["sectionid"]
        input_token = str(request.data["token"])
        try:
            del_sec = Section.objects.all().filter(sectionid = input_sectionid)
            del_sec.delete()
            token.extend_token(input_token)
            return JsonResponse({'delete': 'Delete success'})
        except:
            token.extend_token(input_token)
            return JsonResponse({'delete': 'fail'})

class SectionUpdate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_sectionid = request.data["sectionid"]
        input_sectionname = request.data["sectionname"]
        input_token = str(request.data["token"])
        try:
            update_section = Section.objects.all().filter(sectionid = input_sectionid)
            update_section.update(sectionname = input_sectionname)
            token.extend_token(input_token)
            return JsonResponse({'update': 'success'})
        except:
            token.extend_token(input_token)
            return JsonResponse({'update': 'fail'})

#Session
class SessionList(generics.ListAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class SessionCreate(APIView):
    def post(self, request, format=None):
        input_memberid=request.data["memberid"]
        input_memberpwd=request.data["memberpwd"]
        if Member.objects.filter(memberid=input_memberid, memberpwd=input_memberpwd).exists():
            if Session.objects.filter(memberid=input_memberid).exists():
                login_list= token.create_token(input_memberid)
                return HttpResponse(login_list, content_type="application/json")
            else:
                login_list= token.create_token(input_memberid)
                return HttpResponse(login_list, content_type="application/json")
        else: 
            login_list = []
            login_tmp = {}
            login_tmp['token'] = "Not Matched"
            login_list.append(login_tmp)
            login_list=json.dumps(login_list)
            return HttpResponse(login_list, content_type="application/json")

#Title
class TitleList(generics.ListAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

class TitleCreate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_titlename=request.data["titlename"]
        input_titleinfo = request.data["titleinfo"]
        input_token = str(request.data["token"])
        get_memberid = token.earn_memberid(input_token)

        try:
            model_instance = Title(titlename = input_titlename, titleinfo = input_titleinfo)
            model_instance.save()
            member = Member.objects.get(memberid=get_memberid)
            Enroll.objects.create(memberid=member, titleid=model_instance)
            token.extend_token(input_token)
            return JsonResponse({'create': 'success'}) 
        except:
            token.extend_token(input_token)
            return JsonResponse({'create': 'fail'})

class TitleSearch(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):    
        input_titleid = request.data["titleid"]
        input_token = str(request.data["token"])
        comment_list=searchfunc.title_search(input_titleid)
        token.extend_token(input_token)
        return HttpResponse(comment_list, content_type="application/json")

class TitleDelete(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_titleid = request.data["titleid"]
        input_token = str(request.data["token"])
        try:
            del_title = Title.objects.all().filter(titleid = input_titleid)
            del_title.delete()
            token.extend_token(input_token)
            return JsonResponse({'delete': 'Delete success'})
        except:
            token.extend_token(input_token)
            return JsonResponse({'delete': 'fail'})

class TitleUpdate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_titlename=request.data["titlename"]
        input_titleinfo = request.data["titleinfo"]
        input_titleid = request.data["titleid"]
        input_token = str(request.data["token"])
        try:
            update_title = Title.objects.all().filter(titleid = input_titleid)
            update_title.update(titlename = input_titlename, titleinfo = input_titleinfo)
            token.extend_token(input_token)
            return JsonResponse({'update': 'success'})
        except:
            token.extend_token(input_token)
            return JsonResponse({'update': 'fail'})

class SearchAll(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):    
        input_titleid = request.data["titleid"]
        input_token = str(request.data["token"])
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
        token.extend_token(input_token)
        return HttpResponse(section_jlist, content_type="application/json")