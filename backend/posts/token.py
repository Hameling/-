from posts import regex
from .models import Session

def earn_memberid(input_token):
    session_member = Session.objects.get(token = input_token)
    str_sessiondata = str(session_member)
    rejex_session = regex.parse_session(str_sessiondata)
    earn_memberid = rejex_session[0][1]
    return earn_memberid