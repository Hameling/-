from django.shortcuts import render
from rest_framework import generics, permissions
from django.views.generic import DetailView

from .models import Assign,Checklist,Calender,Comment,Content,Contentstate,Enroll,File,Member,Permission,Section,Title
from .serializers import AssignSerializer,ChecklistSerializer,CalenderSerializer,CommentSerializer,ContentSerializer,ContentstateSerializer,EnrollSerializer,FileSerializer,MemberSerializer,PermissionSerializer,SectionSerializer,TitleSerializer

# Create your views here.
#Assign
class AssignList(generics.ListAPIView):
    queryset = Assign.objects.all()
    serializer_class = AssignSerializer

class AssignDetail(generics.RetrieveAPIView):
    queryset = Assign.objects.all()
    serializer_class = AssignSerializer

class AssignCreate(generics.CreateAPIView):
    queryset = Assign.objects.all()
    serializer_class = AssignSerializer

#Checklist
class ChecklistList(generics.ListAPIView):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

class ChecklistDetail(generics.RetrieveAPIView):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

class ChecklistCreate(generics.CreateAPIView):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

#Calender
class CalenderList(generics.ListAPIView):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer

class CalenderDetail(generics.RetrieveAPIView):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer

class CalenderCreate(generics.CreateAPIView):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer

#Comment
class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

#Content
class ContentList(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentDetail(generics.RetrieveAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentCreate(generics.CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

#Contentstate
class ContentstateList(generics.ListAPIView):
    queryset = Contentstate.objects.all()
    serializer_class = ContentstateSerializer

class ContentstateDetail(generics.RetrieveAPIView):
    queryset = Contentstate.objects.all()
    serializer_class = ContentstateSerializer

class ContentstateCreate(generics.CreateAPIView):
    queryset = Contentstate.objects.all()
    serializer_class = ContentstateSerializer

#Enroll
class EnrollList(generics.ListAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer

class EnrollDetail(generics.RetrieveAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer

class EnrollCreate(generics.CreateAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer

#File
class FileList(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileDetail(generics.RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileCreate(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

#Member
class MemberList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberDetail(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberCreate(generics.CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberSearch(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

#Permission
class PermissionList(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class PermissionDetail(generics.RetrieveAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class PermissionCreate(generics.CreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

#Section
class SectionList(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionDetail(generics.RetrieveAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionCreate(generics.CreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

#Title
class TitleList(generics.ListAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

class TitleDetail(generics.RetrieveAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

class TitleCreate(generics.CreateAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer