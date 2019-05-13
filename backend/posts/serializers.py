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
        fields = ('listnumber','listname','contentid')
        model = models.Checklist

#Calender
class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('indexnumber','startdate','starttime','duedate','duetime','contentid','isoverlap')
        model = models.Calender

#Comment
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('comnumber','comcomment','contentid')
        model = models.Comment

#Content
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('contentid','contentname','contentinfo','iscomment','ischecklist','contentpos','contentheight','contentstate',)
        model = models.Content

#Contentstate
class ContentstateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('statenumber','statename',)
        model = models.Contentstate

#Enroll
class EnrollSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('enrollid','memberid','titleid')
        model = models.Enroll

#File
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('fileaddress','filename','fileformat','contentid',)
        model = models.File

#Member
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('memberid','membername','memberpwd','memberemail',)
        model = models.Member

#Permission
class PermissionstateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('perstatenumber','perstatename',)
        model = models.Permissionstate

#Permission
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('priority','memberid','contentid','fileaddress','permissionid',)
        model = models.Permission

#Section
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('sectionid','titleid')
        model = models.Section

#Title
class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('titleid','titlename','titleinfo',)
        model = models.Title