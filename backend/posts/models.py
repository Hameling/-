# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.

class Assign(models.Model):
    memberid = models.ForeignKey('Member', models.DO_NOTHING, db_column='memberid')
    contentid = models.ForeignKey('Content', models.DO_NOTHING, db_column='contentid')
    assignid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'assign'


class Calender(models.Model):
    indexnumber = models.AutoField(primary_key=True)
    startdate = models.DateField()
    starttime = models.DateTimeField()
    duedate = models.DateField()
    duetime = models.DateTimeField()
    contentid = models.ForeignKey('Content', models.DO_NOTHING, db_column='contentid')
    isoverlap = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Calender'


class Checklist(models.Model):
    listnumber = models.AutoField(primary_key=True)
    listname = models.CharField(max_length=45)
    contentid = models.ForeignKey('Content', models.DO_NOTHING, db_column='contentid')

    class Meta:
        managed = False
        db_table = 'Checklist'


class Comment(models.Model):
    comnumber = models.AutoField(primary_key=True)
    comcomment = models.CharField(max_length=45)
    contentid = models.ForeignKey('Content', models.DO_NOTHING, db_column='contentid')

    class Meta:
        managed = False
        db_table = 'Comment'
    def __str__(self):
        return self.comcomment


class Content(models.Model):
    contentid = models.CharField(primary_key=True, max_length=45)
    contentname = models.CharField(max_length=45, blank=True, null=True)
    contentinfo = models.CharField(max_length=200, blank=True, null=True)
    iscomment = models.IntegerField(blank=True, null=True)
    ischecklist = models.IntegerField(blank=True, null=True)
    contentpos = models.IntegerField(blank=True, null=True)
    contentheight = models.IntegerField(blank=True, null=True)
    contentstate = models.ForeignKey('Contentstate', models.DO_NOTHING, db_column='contentstate', blank=True, null=True)
    sectionid = models.ForeignKey('Section', models.DO_NOTHING, db_column='sectionid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Content'
    def __str__(self):
        return self.contentname


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
        db_table = 'enroll'
        unique_together = (('memberid', 'titleid'),)

class File(models.Model):
    fileaddress = models.CharField(primary_key=True, max_length=45)
    filename = models.CharField(max_length=45, blank=True, null=True)
    fileformat = models.CharField(max_length=45, blank=True, null=True)
    contentid = models.ForeignKey(Content, models.DO_NOTHING, db_column='contentid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'File'


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
    priority = models.IntegerField()
    memberid = models.ForeignKey(Assign, models.DO_NOTHING, db_column='memberid')
    contentid = models.ForeignKey(Content, models.DO_NOTHING, db_column='contentid')
    fileaddress = models.ForeignKey(File, models.DO_NOTHING, db_column='fileaddress')
    permissionid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Permission'


class Section(models.Model):
    sectionid = models.CharField(db_column='sectionId', primary_key=True, max_length=45)  # Field name made lowercase.
    titleid = models.ForeignKey('Title', models.DO_NOTHING, db_column='titleId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Section'


class Title(models.Model):
    titleid = models.CharField(db_column='titleId', primary_key=True, max_length=45)  # Field name made lowercase.
    titlename = models.CharField(db_column='titleName', max_length=45)  # Field name made lowercase.
    titleinfo = models.CharField(db_column='titleInfo', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Title'
    def __str__(self):
        return self.titleid