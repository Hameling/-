import jwt
import datetime

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

class AssignCreate(generics.CreateAPIView):
    queryset = Assign.objects.all()
    serializer_class = AssignSerializer

class AssignSearch(generics.RetrieveAPIView):
    queryset = Assign.objects.all()
    serializer_class = AssignSerializer

class AssignDelete(generics.DestroyAPIView):
    queryset = Assign.objects.all()
    serializer_class = AssignSerializer

class AssignUpdate(generics.UpdateAPIView):
    queryset = Assign.objects.all()
    serializer_class = AssignSerializer

class MyAssign(generics.ListAPIView):
    serializer_class = AssignSerializer
    lookup_url_kwarg = "memberid"
    def get_queryset(self):
        memberid = self.kwargs.get(self.lookup_url_kwarg)
        mymemberid = Assign.objects.filter(memberid=memberid)
        print(mymemberid)
        return mymemberid

#Checklist
class ChecklistList(generics.ListAPIView):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

class ChecklistCreate(generics.CreateAPIView):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

class ChecklistSearch(generics.RetrieveAPIView):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

class ChecklistDelete(generics.DestroyAPIView):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

class ChecklistUpdate(generics.UpdateAPIView):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistUpdateSerializer

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

class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentSearch(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDelete(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentUpdate(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

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

class EnrollCreate(generics.CreateAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer

class EnrollSearch(generics.RetrieveAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer

class EnrollDelete(generics.DestroyAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer

class EnrollUpdate(generics.UpdateAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer

class MyEnroll(generics.ListAPIView):
    serializer_class = EnrollSerializer
    lookup_url_kwarg = "memberid"
    def get_queryset(self):
        memberid = self.kwargs.get(self.lookup_url_kwarg)
        mymemberid = Enroll.objects.filter(memberid=memberid)
        print(mymemberid)
        return mymemberid

class InTitle(generics.ListAPIView):
    serializer_class = EnrollSerializer
    lookup_url_kwarg = "titleid"
    def get_queryset(self):
        titleid = self.kwargs.get(self.lookup_url_kwarg)
        mytitleid = Enroll.objects.filter(titleid=titleid)
        print(mytitleid)
        return mytitleid

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

class SectionCreate(generics.CreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionSearch(generics.RetrieveAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionDelete(generics.DestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionUpdate(generics.UpdateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionUpdateSerializer

class MySection(generics.ListAPIView):
    serializer_class = SectionSerializer
    lookup_url_kwarg = "titleid"
    def get_queryset(self):
        titleid = self.kwargs.get(self.lookup_url_kwarg)
        mytitleid = Section.objects.filter(titleid=titleid)
        print(mytitleid)
        return mytitleid

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

class TitleCreate(generics.CreateAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

class TitleSearch(generics.RetrieveAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

class TitleDelete(generics.DestroyAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

class TitleUpdate(generics.UpdateAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleUpdateSerializer

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
         