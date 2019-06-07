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

#Calender
class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('indexnumber','calendername','starttime','duetime','contentid','isoverlap')
        model = models.Calender

#Comment
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('comnumber','comcomment','contentid','memberid','commenttime')
        model = models.Comment

#Content
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('contentid','contentname','contentinfo','contentstate','sectionid')
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
        fields = ('contentid','fileid','filename')
        model = models.File

class FileSerializer2(serializers.ModelSerializer):
    class Meta:
        fields = ('token','contentid','filename')
        model = models.Download

class FileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('filename',)
        model = models.File

#Member
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('memberid','membername','memberpwd','memberemail',)
        model = models.Member

#Permission
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('priority','memberid','fileid','permissionid','contentid',)
        model = models.Permission


#PermissionState
class PermissionstateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('perstatenumber','perstatename',)
        model = models.Permissionstate

#Section
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('titleid','sectionname','sectionid')
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
