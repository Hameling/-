from rest_framework import serializers
from . import models

#Assign
class AssignSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('memberid','contentid','assignid')
        model = models.Assign

#Checklist
class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('listnumber','listname','contentid','checked')
        model = models.Checklist

class ChecklistUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('listname',)
        model = models.Checklist

#Calender
class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('indexnumber','starttime','duetime','contentid','isoverlap')
        model = models.Calender

class CalenderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('starttime','duetime','isoverlap')
        model = models.Calender

#Comment
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('comnumber','comcomment','contentid','memberid')
        model = models.Comment

class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('comcomment',)
        model = models.Comment

#Content
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('contentid','contentname','contentinfo','iscomment','ischecklist','contentpos','contentheight','contentstate','sectionid')
        model = models.Content

class ContentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('contentname','contentinfo','iscomment','ischecklist','contentpos','contentheight','contentstate',)
        model = models.Content

#Contentstate
class ContentstateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('statenumber','statename',)
        model = models.Contentstate

#Enroll
class EnrollSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('memberid','titleid','enrollid')
        model = models.Enroll

#File
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('fileaddress','filename','fileformat','contentid',)
        model = models.File

class FileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('filename',)
        model = models.File

#Member
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('memberid','membername','memberpwd','memberemail',)
        model = models.Member

class MembeUpdaterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('membername','memberpwd','memberemail',)
        model = models.Member

#Permission
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('priority','memberid','contentid','fileaddress','permissionid',)
        model = models.Permission

class PermissionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('priority',)
        model = models.Permission

#PermissionState
class PermissionstateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('perstatenumber','perstatename',)
        model = models.Permissionstate

#Section
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('titleid','sectionname',)
        model = models.Section

class SectionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('sectionname',)
        model = models.Section

#Session
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('memberid','token','expiretime',)
        model = models.Session

#Title
class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('titleid','titlename','titleinfo',)
        model = models.Title

class TitleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('titlename','titleinfo',)
        model = models.Title

#테스트
class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Upload
        fields = "__all__"

class FileuploadSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = models.Upload
        fields = "__all__"