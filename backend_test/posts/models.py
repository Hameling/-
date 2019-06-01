# -*- encoding: utf-8 -*-
import datetime
from django.db import models

# Create your models here.

class Assign(models.Model):
    memberid = models.ForeignKey('Member', on_delete=models.CASCADE, db_column='memberid')
    contentid = models.ForeignKey('Content', on_delete=models.CASCADE, db_column='contentid')
    assignid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Assign'
        unique_together = (('memberid','contentid'),)
    def __str__(self):
        return '{}msp{}isp{}'.format(self.contentid, self.memberid, self.assignid)

class Calender(models.Model):
    indexnumber = models.AutoField(primary_key=True)
    starttime = models.DateTimeField()
    duetime = models.DateTimeField()
    contentid = models.ForeignKey('Content', on_delete=models.CASCADE, db_column='contentid')
    isoverlap = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        managed = False
        db_table = 'Calender'
    def __str__(self):
        return '{}to{}csp{}isp{}lsp{}'.format(self.starttime, self.duetime, self.contentid, self.indexnumber, self.isoverlap)


class Checklist(models.Model):
    listnumber = models.AutoField(primary_key=True)
    listname = models.CharField(max_length=45)
    contentid = models.ForeignKey('Content', on_delete=models.CASCADE, db_column='contentid')
    checked = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Checklist'
    def __str__(self):
        return '{}na{}ck{}cid{}'.format(self.listnumber, self.listname,self.checked, self.contentid)


class Comment(models.Model):
    comnumber = models.AutoField(primary_key=True)
    comcomment = models.CharField(max_length=45)
    contentid = models.ForeignKey('Content', on_delete=models.CASCADE, db_column='contentid')
    memberid = models.ForeignKey('Member', on_delete=models.CASCADE, db_column='memberid', blank=True, null=True)
    commenttime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Comment'
    def __str__(self):
        return '{}isp{}who{}{}'.format(self.comnumber,self.memberid,self.comcomment,self.commenttime)


class Content(models.Model):
    contentid = models.AutoField(primary_key=True)
    contentname = models.CharField(max_length=45, blank=True, null=True)
    contentinfo = models.CharField(max_length=200, blank=True, null=True)
    contentstate = models.ForeignKey('Contentstate', on_delete=models.CASCADE, db_column='contentstate')
    sectionid = models.ForeignKey('Section', on_delete=models.CASCADE, db_column='sectionid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Content'
    def __str__(self):
        return '{}na{}in{}st{}sec{}'.format(self.contentid,self.contentname,self.contentinfo, self.contentstate, self.sectionid)


class Contentstate(models.Model):
    statenumber = models.IntegerField(primary_key=True)
    statename = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Contentstate'
    def __str__(self):
        return self.statename
        
class Enroll(models.Model):
    memberid = models.ForeignKey('Member', on_delete=models.CASCADE, db_column='memberid')
    titleid = models.ForeignKey('Title', on_delete=models.CASCADE, db_column='titleid')
    enrollid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Enroll'
        unique_together = (('memberid','titleid'),)
    def __str__(self):
        return '{}id{}idd{}'.format(self.titleid, self.memberid, self.enrollid)

class File(models.Model):
    contentid = models.ForeignKey(Content, on_delete=models.CASCADE, db_column='contentid')
    fileid = models.AutoField(primary_key=True)
    filename = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'File'
    def __str__(self):
        return self.filename


class Member(models.Model):
    memberid = models.CharField(primary_key=True, max_length=45)
    membername = models.CharField(max_length=45)
    memberpwd = models.CharField(max_length=45)
    memberemail = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Member'
    def __str__(self):
        return '{}ps{}na{}em{}'.format(self.memberid, self.memberpwd, self.membername, self.memberemail)

class Permissionstate(models.Model):
    perstatenumber = models.IntegerField(primary_key=True)
    perstatename = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Permissionstate'
    def __str__(self):
        return self.perstatename

class Permission(models.Model):
    priority = models.ForeignKey('Permissionstate', on_delete=models.CASCADE, db_column='priority')
    contentid = models.ForeignKey(Content, on_delete=models.CASCADE, db_column='contentid')
    memberid = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='memberid')
    fileid = models.ForeignKey(File, on_delete=models.CASCADE, db_column='fileid')
    permissionid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Permission'
    def __str__(self):
        return '{}cid{}mid{}fid{}per{}'.format(self.priority,self.contentid, self.memberid, self.fileid, self.permissionid)

class Section(models.Model):
    sectionid = models.AutoField(primary_key=True)
    titleid = models.ForeignKey('Title', on_delete=models.CASCADE, db_column='titleid')
    sectionname = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Section'
    def __str__(self):
        return '{}na{}id{}'.format(self.sectionid,self.sectionname, self.titleid)


class Session(models.Model):
    memberid = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='memberid')
    token = models.CharField(max_length=120)
    expiretime = models.DateTimeField()
    sessionid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Session'
    def __str__(self):
        return '{}mid{}exp{}'.format(self.sessionid,self.memberid,self.expiretime)

class Title(models.Model):
    titleid = models.AutoField(primary_key=True)
    titlename = models.CharField(max_length=45)
    titleinfo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Title'
    def __str__(self):
        return '{}sp{}na{}'.format(self.titleid,self.titlename, self.titleinfo)

class Uploadfilemodel(models.Model):
    fileid = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=32)
    fileex = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UploadFileModel'