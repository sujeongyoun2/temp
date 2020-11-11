from django.db import models

# Heroku connect
# from sqlalchemy import create_engine
# DB_URL = 'mysql://b1479fa2d58dc2:37b1aa35@us-cdbr-east-02.cleardb.com/heroku_91f73732ea80247?reconnect=true'
# engine = create_engine(DB_URL)


# Create your models here.
# Question for DB (Use MariaDB)
class Member(models.Model):
    member_no = models.AutoField(db_column='member_no', primary_key=True)
    member_id = models.CharField(db_column='member_id', max_length=20)
    member_pwd = models.CharField(db_column='member_pwd', max_length=255)
    member_name = models.CharField(db_column='member_name', max_length=50)
    member_email = models.CharField(db_column='member_email', max_length=255)
    member_type = models.CharField(db_column='member_type', max_length=20)
    usage_flag = models.CharField(
        db_column='usage_flag', max_length=10, default='1')
    register_date = models.DateTimeField(db_column='register_date', )
    access_latest = models.DateTimeField(db_column='access_latest',)

    class Meta:
        managed = False
        db_table = 'member'


class Member_two(models.Model):
    member_no = models.AutoField(db_column='member_no', primary_key=True)
    member_id = models.CharField(db_column='member_id', max_length=20)
    member_pwd = models.CharField(db_column='member_pwd', max_length=255)
    member_name = models.CharField(db_column='member_name', max_length=50)
    member_email = models.CharField(db_column='member_email', max_length=255)
    usage_flag = models.CharField(
        db_column='usage_flag', max_length=10, default='1')
    register_date = models.DateTimeField(db_column='register_date', )

    class Meta:
        managed = False
        db_table = 'membertwo'


class Forsitter(models.Model):
    b_id = models.AutoField(db_column='no', primary_key=True)
    Name = models.CharField(db_column='Name', max_length=255)
    Title = models.CharField(db_column='Title', max_length=255)
    Location = models.CharField(db_column='Location', max_length=50)
    Date = models.DateTimeField(db_column='Date', )

    class Meta:
        managed = False
        db_table = 'forsitter'


class Forparent(models.Model):
    b_id = models.AutoField(db_column='no', primary_key=True)
    parent_Name = models.CharField(db_column='parent_Name', max_length=255)
    parent_Title = models.CharField(db_column='parent_Title', max_length=255)
    parent_Location = models.CharField(
        db_column='parent_Location', max_length=50)
    parent_Payrate = models.IntegerField(
        db_column='parent_Payrate',)
    parent_Note = models.CharField(db_column='parent_Note', max_length=255)
    parent_Service = models.CharField(
        db_column='parent_Service', max_length=255)
    parent_Workperiod = models.CharField(
        db_column='parent_Workperiod', max_length=255)
    parent_Timefrom = models.CharField(
        db_column='parent_Timefrom', max_length=50)
    parent_Workto = models.CharField(db_column='parent_Workto', max_length=50)
    parent_Gender = models.CharField(db_column='parent_Gender', max_length=255)
    parent_Date = models.DateTimeField(db_column='parent_Date', )

    class Meta:
        managed = False
        db_table = 'forparent'


class Question1(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    Title = models.CharField(db_column='Title', max_length=255)
    Date = models.DateTimeField(db_column='Date', )
    Text = models.CharField(db_column='Text', max_length=255)

    class Meta:
        managed = False
        db_table = 'question'


class Mypost(models.Model):
    mp_id = models.AutoField(db_column='mp_no', primary_key=True)
    mp_Name = models.CharField(db_column='mp_Name', max_length=255)
    mp_Title = models.CharField(db_column='mp_Title', max_length=255)
    mp_Location = models.CharField(
        db_column='mp_Location', max_length=50)
    mp_Payrate = models.IntegerField(
        db_column='mp_Payrate',)
    mp_Note = models.CharField(db_column='mp_Note', max_length=255)
    mp_Service = models.CharField(
        db_column='mp_Service', max_length=255)
    mp_Workperiod = models.CharField(
        db_column='mp_Workperiod', max_length=255)
    mp_Timefrom = models.CharField(
        db_column='mp_Timefrom', max_length=50)
    mp_Workto = models.CharField(db_column='mp_Workto', max_length=50)
    mp_Gender = models.CharField(db_column='mp_Gender', max_length=255)
    mp_Date = models.DateTimeField(db_column='mp_Date', )

    class Meta:
        managed = False
        db_table = 'mypost'
