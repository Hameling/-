import jwt
import datetime
import json

from posts import regex
from pytz import timezone

from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render
from rest_framework import generics, permissions
from django.views.generic import DetailView

from .models import Assign,Checklist,Calender,Comment,Content,Contentstate,Enroll,File,Member,Permission,Section,Title, Permissionstate, Session
from .serializers import AssignSerializer,ChecklistSerializer,CalenderSerializer,CommentSerializer,ContentSerializer,ContentstateSerializer,EnrollSerializer,FileSerializer,MemberSerializer,PermissionSerializer,SectionSerializer,TitleSerializer,PermissionstateSerializer,MembeUpdaterSerializer,ChecklistUpdateSerializer,CalenderUpdateSerializer,CommentUpdateSerializer,ContentUpdateSerializer,FileUpdateSerializer,PermissionUpdateSerializer,SectionUpdateSerializer,TitleUpdateSerializer, SessionSerializer

# Create your views here.
#Assign
class AssignList(generics.ListAPIView):
    queryset = Assign.objects.all()
    serializer_class = AssignSerializer

class AssignCreate(APIView):
    parser_classes = (JSONParser,)
    def post(self, request, format=None):
        input_memberid = request.data["memberid"]
        input_contentid =request.data["contentid"]

        try:
            member = Member.objects.get(memberid=input_memberid)
            content = Content.objects.get(contentid=input_contentid)
            Assign.objects.create(memberid = member, contentid = content)
            return JsonResponse({'create': 'success'}) 
        except:
            return JsonResponse({'create': 'fail'})

class AssignSearchMember(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_memberid = str(request.data["memberid"])
        data = list(Assign.objects.all().filter(memberid = input_memberid))
        assign_list = []

        str_data = str(data)
        power_list = regex.parse_assign(str_data)

        for i in power_list:
            json_tmp = {}
            json_tmp['contentid'] = i[0]
            json_tmp['memberid'] = i[1]
            json_tmp['assignid'] = i[2]
            assign_list.append(json_tmp)
        assign_list=json.dumps(assign_list)
        return HttpResponse(assign_list, content_type="application/json")
class AssignSearchContent(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_contentid = str(request.data["contentid"])
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
        return HttpResponse(assign_list, content_type="application/json")

class AssignDelete(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_memberid = str(request.data["memberid"])
        input_contentid = str(request.data["contentid"])
        try:
            del_assign = Assign.objects.all().filter(memberid = input_memberid, contentid = input_contentid)
            str_data = str(del_assign)
            print("str",str_data)
            power_list = regex.parse_assign(str_data)
            print("power",power_list)
            acquire_assigncid = str(power_list[0][0])
            acquire_assignid = str(power_list[0][1])
            if((acquire_assignid == input_memberid) and (acquire_assigncid == input_contentid)):
                del_assign.delete()
                return JsonResponse({'delete': 'success'})
            else:
                return JsonResponse({'delete': 'Not matched'})
        except:
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

        try:
            content = Content.objects.get(contentid=input_contentid)
            Checklist.objects.create(listname = input_listname, contentid = content, checked= 0)
            return JsonResponse({'create': 'success'}) 
        except:
            return JsonResponse({'create': 'fail'})

class ChecklistSearch(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):    
        input_contentid = request.data["contentid"]
        comment_list = []
    
        data = list(Checklist.objects.all().filter(contentid = input_contentid))
        str_data = str(data)
        power_list = regex.parse_checklist(str_data)
        for i in power_list:
            json_tmp = {}
            json_tmp['listnumber'] = i[0]
            json_tmp['listname'] = i[1]
            json_tmp['contentid'] = i[2]
            json_tmp['checked'] = i[3]
            comment_list.append(json_tmp)
        comment_list=json.dumps(comment_list)
        return HttpResponse(comment_list, content_type="application/json")


class ChecklistDelete(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_listnumber = request.data["listnumber"]
        try:
            del_checklist = Checklist.objects.all().filter(listnumber = input_listnumber)    
            del_checklist.delete()
            return JsonResponse({'delete': 'Delete success'})
        except:
            return JsonResponse({'delete': 'fail'})

class ChecklistUpdate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_listname = request.data["listname"]
        input_listnumber = request.data["listnumber"]
        input_checked = request.data["checked"]
        try:
            update_checklist = Checklist.objects.all().filter(listnumber = input_listnumber)
            update_checklist.update(listname = input_listname, checked = input_checked)
            return JsonResponse({'update': 'success'})
        except:
            return JsonResponse({'update': 'fail'})

#Calender
class CalenderList(generics.ListAPIView):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer

class CalenderCreate(generics.CreateAPIView):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer

class CalenderSearch(generics.RetrieveAPIView):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer

class CalenderDelete(generics.DestroyAPIView):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer

class CalenderUpdate(generics.UpdateAPIView):
    queryset = Calender.objects.all()
    serializer_class = CalenderUpdateSerializer

#Comment
class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentCreate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_comcomment = request.data["comcomment"]
        input_memberid=request.data["memberid"]
        input_contentid = request.data["contentid"]
        cur_time = datetime.datetime.now()

        try:
            content = Content.objects.get(contentid=input_contentid)
            member = Member.objects.get(memberid=input_memberid)
            Comment.objects.create(comcomment=input_comcomment, contentid = content, memberid = member, commenttime = cur_time)
            return JsonResponse({'create': 'success'}) 
        except:
            return JsonResponse({'create': 'fail'})

class CommentDelete(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_comnumber = request.data["comnumber"]
        input_memberid=request.data["memberid"]
        try:
            del_comment = Comment.objects.all().filter(comnumber = input_comnumber)
            str_data = str(del_comment)
            power_list = regex.parse_text(str_data)
            acquire_memberid = power_list[0][1]
            if acquire_memberid == input_memberid:
                del_comment.delete()
                return JsonResponse({'delete': 'Delete success'})
            return JsonResponse({'delete': 'Not Matched'}) 
        except:
            return JsonResponse({'delete': 'fail'})

class CommentUpdate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
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
                return JsonResponse({'delete': 'Update success'})
            return JsonResponse({'delete': 'Not Matched'}) 
        except:
            return JsonResponse({'delete': 'fail'})

class CheckComment(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):    
        input_memberid=request.data["memberid"]
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
        return HttpResponse(comment_list, content_type="application/json")
#Content
class ContentList(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentCreate(generics.CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    
class ContentSearch(generics.RetrieveAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentDelete(generics.DestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentUpdate(generics.UpdateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentUpdateSerializer

class MyContent(generics.ListAPIView):
    serializer_class = ContentSerializer
    lookup_url_kwarg = "sectionid"
    def get_queryset(self):
        sectionid = self.kwargs.get(self.lookup_url_kwarg)
        mysectionid = Content.objects.filter(sectionid=sectionid)
        print(mysectionid)
        return mysectionid

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
        input_memberid = str(request.data["memberid"])
        try:
            member = Member.objects.get(memberid=input_memberid)
            title = Title.objects.get(titleid=input_titleid)
            Enroll.objects.create(memberid=member, titleid=title)
            return JsonResponse({'create': 'success'}) 
        except:
            return JsonResponse({'create': 'fail'})

class EnrollSearchTitle(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):  
        input_memberid = str(request.data["memberid"])
        data = list(Enroll.objects.all().filter(memberid = input_memberid))
        comment_list = []
        str_data = str(data)
        power_list = regex.parse_enroll(str_data)
        for i in power_list:
            json_tmp = {}
            json_tmp['titleid'] = i[0]
            json_tmp['memeberid'] = i[1]
            json_tmp['enrollid'] = i[2]
            comment_list.append(json_tmp)
        comment_list=json.dumps(comment_list)
        return HttpResponse(comment_list, content_type="application/json")

class EnrollSearchMember(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):   
        input_titleid = str(request.data["titleid"]) 
        data = list(Enroll.objects.all().filter(titleid = input_titleid))
        comment_list = []
        str_data = str(data)
        power_list = regex.parse_enroll(str_data)
        for i in power_list:
            json_tmp = {}
            json_tmp['titleid'] = i[0]
            json_tmp['memeberid'] = i[1]
            json_tmp['enrollid'] = i[2]
            comment_list.append(json_tmp)
        comment_list=json.dumps(comment_list)
        return HttpResponse(comment_list, content_type="application/json")

class EnrollDelete(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_titleid = str(request.data["titleid"])
        input_memberid = str(request.data["memberid"])
        try:
            del_enroll = Enroll.objects.all().filter(memberid = input_memberid, titleid = input_titleid)
            str_data = str(del_enroll)
            power_list = regex.parse_enroll(str_data)
            ac_titleid = str(power_list[0][0])
            ac_memberid = str(power_list[0][1])
            if((ac_memberid == input_memberid) and (ac_titleid == input_titleid)):
                del_enroll.delete()
                return JsonResponse({'delete': 'success'})
            else:
                return JsonResponse({'delete': 'Not matched'})
        except:
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
    serializer_class = FileUpdateSerializer

#Member
class MemberList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberCreate(generics.CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberSearch(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberDelete(generics.DestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberUpdate(generics.UpdateAPIView):
    queryset = Member.objects.all()
    serializer_class = MembeUpdaterSerializer

class Login(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        expiretime = datetime.datetime.now() + datetime.timedelta(hours=2)
        key = str(expiretime)
        
        encoded = ""
        input_memberid=request.data["memberid"]
        input_memberpwd=request.data["memberpwd"]

        #session member가 존재할 경우.
        if Session.objects.filter(memberid=input_memberid).exists():
            encoded = jwt.encode({'memberid': input_memberid}, key, algorithm='HS256')
            member = Member.objects.get(memberid=input_memberid)
            queryset = Session.objects.filter(memberid= member).update(memberid= member,token=encoded, expiretime = expiretime)
            return JsonResponse({'token': encoded.decode('utf-8')}) 
        #session member가 없을 경우.
        else :
            if Member.objects.filter(memberid=input_memberid, memberpwd=input_memberpwd).exists():
                encoded = jwt.encode({'memberid': input_memberid}, key, algorithm='HS256')
                member = Member.objects.get(memberid=input_memberid)
                queryset = Session.objects.create(memberid =member, token=encoded, expiretime=expiretime)
                return JsonResponse({'token': encoded.decode('utf-8')}) 
        return JsonResponse({'token': encoded})

#Permission
class PermissionList(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class PermissionCreate(generics.CreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class PermissionSearch(generics.RetrieveAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class PermissionDelete(generics.DestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class PermissionUpdate(generics.UpdateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionUpdateSerializer

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

        try:
            thistitle = Title.objects.get(titleid=input_titleid)
            Section.objects.create(titleid = thistitle, sectionname = input_sectionname)
            return JsonResponse({'create': 'success'}) 
        except:
            return JsonResponse({'create': 'fail'})

class SectionSearch(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):    
        input_sectionid = request.data["sectionid"]
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
        return HttpResponse(comment_list, content_type="application/json")

class SectionDelete(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_sectionid = request.data["sectionid"]
        try:
            del_sec = Section.objects.all().filter(sectionid = input_sectionid)
            del_sec.delete()
            return JsonResponse({'delete': 'Delete success'})
        except:
            return JsonResponse({'delete': 'fail'})

class SectionUpdate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_sectionid = request.data["sectionid"]
        input_sectionname = request.data["sectionname"]
        try:
            update_section = Section.objects.all().filter(sectionid = input_sectionid)
            update_section.update(sectionname = input_sectionname)
            return JsonResponse({'update': 'success'})
        except:
            return JsonResponse({'update': 'fail'})

#Session
class SessionList(generics.ListAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class SessionCreate(generics.CreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class SessionSearch(generics.RetrieveAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class SessionDelete(generics.DestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

#Title
class TitleList(generics.ListAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

class TitleCreate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_titlename=request.data["titlename"]
        input_titleinfo = request.data["titleinfo"]

        try:
            Title.objects.create(titlename = input_titlename, titleinfo = input_titleinfo)
            return JsonResponse({'create': 'success'}) 
        except:
            return JsonResponse({'create': 'fail'})

class TitleSearch(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):    
        input_titleid = request.data["titleid"]
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
        return HttpResponse(comment_list, content_type="application/json")

class TitleDelete(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_titleid = request.data["titleid"]
        try:
            del_title = Title.objects.all().filter(titleid = input_titleid)
            del_title.delete()
            return JsonResponse({'delete': 'Delete success'})
        except:
            return JsonResponse({'delete': 'fail'})

class TitleUpdate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        input_titlename=request.data["titlename"]
        input_titleinfo = request.data["titleinfo"]
        input_titleid = request.data["titleid"]
        try:
            update_title = Title.objects.all().filter(titleid = input_titleid)
            update_title.update(titlename = input_titlename, titleinfo = input_titleinfo)
            return JsonResponse({'update': 'success'})
        except:
            return JsonResponse({'update': 'fail'})


class SearchAll(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, format=None):    
        input_titleid = request.data["titleid"]
        section_list = []
        data = list(Section.objects.all().filter(titleid = input_titleid))
        str_data = str(data)
        power_list = regex.parse_section(str_data)
        for i in power_list:
            json_tmp = {}
            json_tmp['sectionid'] = i[0]
            json_tmp['sectionname'] = i[1]
            content_list = []
            con_data = list(Content.objects.all().filter(sectionid = i[0]))
            str_condata = str(con_data)
            content_regex= regex.parse_content(str_condata)
            print(content_regex)
            for j in content_regex:
                json_stmp = {}
                json_stmp['contentid'] = j[0]
                json_stmp['contentname'] = j[1]
                json_stmp['contentinfo'] = j[2]
                print(json_stmp)
                content_list.append(json_stmp)
            json_tmp['includeContent'] = content_list
            section_list.append(json_tmp)
        section_list=json.dumps(section_list)
        return HttpResponse(section_list, content_type="application/json")