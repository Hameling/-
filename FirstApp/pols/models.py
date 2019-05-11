# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Assign(models.Model):
    memberid = models.ForeignKey('Member', models.DO_NOTHING, db_column='memberId', primary_key=True)  # Field name made lowercase.
    contentid = models.ForeignKey('Content', models.DO_NOTHING, db_column='contentId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Assign'
        unique_together = (('memberid', 'contentid'),)


class Calender(models.Model):
    indexnumber = models.AutoField(db_column='indexNumber', primary_key=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='startTime')  # Field name made lowercase.
    duedate = models.DateField(db_column='dueDate')  # Field name made lowercase.
    duetime = models.DateTimeField(db_column='dueTime')  # Field name made lowercase.
    contentid = models.ForeignKey('Content', models.DO_NOTHING, db_column='contentId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Calender'


class Checklist(models.Model):
    listnumber = models.AutoField(db_column='listNumber', primary_key=True)  # Field name made lowercase.
    listname = models.CharField(db_column='listName', max_length=45)  # Field name made lowercase.
    contentid = models.ForeignKey('Content', models.DO_NOTHING, db_column='contentId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CheckList'


class Comment(models.Model):
    comnumber = models.AutoField(db_column='comNumber', primary_key=True)  # Field name made lowercase.
    comcomment = models.CharField(db_column='comComment', max_length=45)  # Field name made lowercase.
    contentid = models.ForeignKey('Content', models.DO_NOTHING, db_column='contentId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comment'


class Content(models.Model):
    contentid = models.CharField(db_column='contentId', primary_key=True, max_length=45)  # Field name made lowercase.
    contentname = models.CharField(db_column='contentName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contentinfo = models.CharField(db_column='contentInfo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    iscomment = models.TextField(db_column='isComment', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ischecklist = models.TextField(db_column='isCheckList', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contentpos = models.IntegerField(db_column='contentPos')  # Field name made lowercase.
    contentheight = models.IntegerField(db_column='contentHeight')  # Field name made lowercase.
    contentstate = models.ForeignKey('Contentstate', models.DO_NOTHING, db_column='contentState', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Content'


class Contentstate(models.Model):
    statenumber = models.IntegerField(db_column='StateNumber', primary_key=True)  # Field name made lowercase.
    statename = models.CharField(db_column='StateName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContentState'


class Enroll(models.Model):
    memberid = models.ForeignKey('Member', models.DO_NOTHING, db_column='memberId', primary_key=True)  # Field name made lowercase.
    storyid = models.ForeignKey('Story', models.DO_NOTHING, db_column='storyId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Enroll'
        unique_together = (('memberid', 'storyid'),)


class File(models.Model):
    fileaddress = models.CharField(db_column='fileAddress', primary_key=True, max_length=45)  # Field name made lowercase.
    filename = models.CharField(db_column='fileName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fileformat = models.CharField(db_column='fileFormat', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contentid = models.ForeignKey(Content, models.DO_NOTHING, db_column='contentId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'File'


class Member(models.Model):
    memberid = models.CharField(db_column='memberId', primary_key=True, max_length=45)  # Field name made lowercase.
    membername = models.CharField(db_column='memberName', max_length=45)  # Field name made lowercase.
    pwd = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Member'


class Permission(models.Model):
    rank = models.IntegerField(primary_key=True)
    memberid = models.ForeignKey(Assign, models.DO_NOTHING, db_column='memberId')  # Field name made lowercase.
    contentid = models.ForeignKey(Content, models.DO_NOTHING, db_column='contentId')  # Field name made lowercase.
    fileaddress = models.ForeignKey(File, models.DO_NOTHING, db_column='fileAddress')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Permission'
        unique_together = (('rank', 'memberid', 'contentid', 'fileaddress'),)


class Section(models.Model):
    sectionid = models.CharField(db_column='sectionId', primary_key=True, max_length=45)  # Field name made lowercase.
    titleid = models.ForeignKey('Title', models.DO_NOTHING, db_column='titleId', blank=True, null=True)  # Field name made lowercase.
    contentid = models.ForeignKey(Content, models.DO_NOTHING, db_column='contentId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Section'


class Story(models.Model):
    storyid = models.CharField(db_column='storyId', primary_key=True, max_length=45)  # Field name made lowercase.
    storyname = models.CharField(db_column='storyName', max_length=45)  # Field name made lowercase.
    storyinfo = models.CharField(db_column='storyInfo', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Story'


class Title(models.Model):
    titleid = models.CharField(db_column='titleId', primary_key=True, max_length=45)  # Field name made lowercase.
    titlename = models.CharField(db_column='titleName', max_length=45)  # Field name made lowercase.
    titlenumber = models.IntegerField(db_column='titleNumber')  # Field name made lowercase.
    storyid = models.ForeignKey(Story, models.DO_NOTHING, db_column='storyId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Title'
