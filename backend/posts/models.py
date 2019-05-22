# -*- encoding: utf-8 -*-
import datetime
from django.db import models

# Create your models here.

class Assign(models.Model):
    memberid = models.ForeignKey('Member', models.DO_NOTHING, db_column='memberid')
    contentid = models.ForeignKey('Content', models.DO_NOTHING, db_column='contentid')
    assignid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Assign'
        unique_together = (('memberid'),)
    def __str__(self):
        return '[{}] {}'.format(self.contentid, self.memberid)

class Calender(models.Model):
    indexnumber = models.AutoField(primary_key=True)
    starttime = models.DateTimeField()
    duetime = models.DateTimeField()
    contentid = models.ForeignKey('Content', models.DO_NOTHING, db_column='contentid')
    isoverlap = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Calender'
    def __str__(self):
        return '[{}] ~ [{}] {}'.format(self.starttime, self.duetime, self.contentid)


class Checklist(models.Model):
    listnumber = models.AutoField(primary_key=True)
    listname = models.CharField(max_length=45)
    contentid = models.ForeignKey('Content', models.DO_NOTHING, db_column='contentid')
    checked = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Checklist'
    def __str__(self):
        return '{}sp{}where{}{}'.format(self.listnumber, self.listname, self.contentid, self.checked)


class Comment(models.Model):
    comnumber = models.AutoField(primary_key=True)
    comcomment = models.CharField(max_length=45)
    contentid = models.ForeignKey('Content', models.DO_NOTHING, db_column='contentid')
    memberid = models.ForeignKey('Member', models.DO_NOTHING, db_column='memberid', blank=True, null=True)
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
    iscomment = models.IntegerField(blank=True, null=True)
    ischecklist = models.IntegerField(blank=True, null=True)
    contentpos = models.IntegerField(blank=True, null=True)
    contentheight = models.IntegerField(blank=True, null=True)
    contentstate = models.ForeignKey('Contentstate', models.DO_NOTHING, db_column='contentstate')
    sectionid = models.ForeignKey('Section', models.DO_NOTHING, db_column='sectionid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Content'
    def __str__(self):
        return str(self.contentid)


class Contentstate(models.Model):
    statenumber = models.IntegerField(primary_key=True)
    statename = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Contentstate'
    def __str__(self):
        return self.statename
        
class Enroll(models.Model):
    memberid = models.ForeignKey('Member', models.DO_NOTHING, db_column='memberid')
    titleid = models.ForeignKey('Title', models.DO_NOTHING, db_column='titleid')
    enrollid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Enroll'
        unique_together = (('memberid','titleid'),)
    def __str__(self):
        return '[{}] {}'.format(self.titleid, self.memberid)

class File(models.Model):
    fileaddress = models.CharField(primary_key=True, max_length=45)
    filename = models.CharField(max_length=45, blank=True, null=True)
    fileformat = models.CharField(max_length=45, blank=True, null=True)
    contentid = models.ForeignKey(Content, models.DO_NOTHING, db_column='contentid', blank=True, null=True)

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
        return self.memberid


class Permission(models.Model):
    priority = models.ForeignKey('Permissionstate', models.DO_NOTHING, db_column='priority')
    memberid = models.ForeignKey(Member, models.DO_NOTHING, db_column='memberid')
    contentid = models.ForeignKey(Content, models.DO_NOTHING, db_column='contentid')
    fileaddress = models.ForeignKey(File, models.DO_NOTHING, db_column='fileaddress')
    permissionid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Permission'
    def __str__(self):
        return '<{}>[{}] {}'.format(self.priority,self.contentid, self.memberid)


class Permissionstate(models.Model):
    perstatenumber = models.IntegerField(primary_key=True)
    perstatename = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Permissionstate'
    def __str__(self):
        return self.perstatename


class Section(models.Model):
    sectionid = models.AutoField(primary_key=True)
    titleid = models.ForeignKey('Title', models.DO_NOTHING, db_column='titleid')
    sectionname = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Section'
    def __str__(self):
        return self.sectionname


class Session(models.Model):
    memberid = models.ForeignKey(Member, models.DO_NOTHING, db_column='memberid')
    token = models.CharField(max_length=120)
    expiretime = models.DateTimeField()
    sessionid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Session'

class Title(models.Model):
    titleid = models.AutoField(primary_key=True)
    titlename = models.CharField(max_length=45)
    titleinfo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Title'
    def __str__(self):
        return self.titlename

    