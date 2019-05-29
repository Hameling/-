import jwt
import datetime
import json

from posts import regex
from .models import Session, Member

def earn_memberid(input_token):
    session_member = Session.objects.get(token = input_token)
    str_sessiondata = str(session_member)
    rejex_session = regex.parse_session(str_sessiondata)
    earn_memberid = rejex_session[0][1]
    return earn_memberid

def create_token(input_memberid):
    expiretime = datetime.datetime.now() + datetime.timedelta(hours=1)
    key = str(expiretime)
    encoded = jwt.encode({'memberid': input_memberid}, key, algorithm='HS256')
    encoded = encoded.decode('utf-8') 
    member = Member.objects.get(memberid=input_memberid)
    Session.objects.filter(memberid= member).update(memberid= member,token=encoded, expiretime = expiretime)
    login_list = []
    login_json = {}
    login_json['token'] = encoded
    login_list.append(login_json)
    login_list=json.dumps(login_list)
    return login_list

def extend_token(input_token):
    expiretime = datetime.datetime.now() + datetime.timedelta(hours=1)
    Session.objects.filter(token = input_token).update(expiretime = expiretime)