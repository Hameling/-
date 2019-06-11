import re
#[<Comment: 63ispjjhw9882psm4321na테스트2emtest02@naver.comwho이얏2019-05-24 17:10:10>
#return '{}isp{}who{}{}'.format(self.comnumber,self.memberid,self.comcomment,self.commenttime)
def parse_text(text):
    field =  re.compile("<Comment: (\d+)isp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)ps([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)em([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)who([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[5][:-19],i[5][-19:]))
        
    return true_result

#return '{}na{}ck{}cid{}'.format(self.listnumber, self.listname,self.checked, self.contentid)
#[<Checklist: 1na업데이트 성공!ck1cid8na사전조사(1)in현재 운영중인 회사 정보pos1he1st신규>]
def parse_checklist(text):
    field = re.compile("<Checklist: (\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)ck(\d+)cid(\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)in([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]*)st([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2],i[3]))
        
    return true_result

#[<Title: 10spcreate 테스트nacreate 테스트>]
def parse_title(text):
    field = re.compile("<Title: (\d+)sp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]*)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2]))
        
    return true_result

#[<Section: 24nasfsdfid37spProject2naProject 2>]
#return '{}na{}id{}'.format(self.sectionid,self.sectionname, self.titleid)
def parse_section(text):
    field = re.compile("<Section: (\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)id(\d+)sp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]*)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2]))
    return true_result

#<QuerySet [<Enroll: 8sp종합 프로젝트na소프트웨어 개발idjjhw9882idd8>]>
#[<Enroll: 8sp종합 프로젝트na소프트웨어 개발idjjhw9882psm4321na테스트2emtest02@naver.comidd27>]
def parse_enroll(text):
    field = re.compile("<Enroll: (\d+)sp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]*)id([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)ps([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)em([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)idd(\d+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2],i[3],i[7]))
    return true_result

#return '{}na{}in{}st{}sec{}'.format(self.contentid,self.contentname,self.contentinfo, self.contentstate, self.sectionid)
# [<Content: 8na사전조사(1)in현재 운영중인 회사 정보 st신규 sec6 na사전조사 id8 sp종합 프로젝트na 소프트웨어 개발>]>
# [<Content: 32 na오늘할일 inasdf st신규 sec33 na오늘할일 id50 spProject 4na>]
def parse_content(text):
    field = re.compile("<Content: (\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)in([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]*)st([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)sec(\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)id(\d+)sp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]*)>")
    result = field.findall(text)
    true_result = []
    for i in result:
        true_result.append((i[0],i[1],i[2],i[3],i[4]))
    return true_result

#return '{}msp{}isp{}'.format(self.contentid, self.memberid, self.assignid)
#<Assign: 37na asdfin st신규 sec36 naa sdf id 49 sp Project3 na msp hameli ps m4321 na백승한ema@1234.comisp23>
def parse_assign(text):
    field = re.compile("<Assign: (\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)in([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]*)st([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)sec(\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)id(\d+)sp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]*)msp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)ps([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)em([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)isp(\d+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[9],i[13],i[1],i[2]))
    return true_result

#return '{}ps{}na{}em{}'.format(self.memberid, self.memberpwd, self.membername, self.memberemail)
#[<Member: testidpwdtestpwd123na테스트emtest@naver.com>]
def parse_member(text):
    field = re.compile("<Member: ([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)ps([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)em([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2],i[3]))
    return true_result

#return '{}to{}csp{}isp{}lsp{}name{}'.format(self.starttime, self.duetime, self.contentid, self.indexnumber, self.isoverlap, self.calendername)
#[<Calender: 2019-06-08 17:16:00to2019-06-21 17:16:00csp30naNew Contentin내용아 생겨라st신규sec32naNew Sectionid49spProject3naisp51lsp0nameㄴㅇㄹㄴㅇ>
def parse_calender(text):
    field = re.compile("<Calender: ([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)to([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)csp(\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)in([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]*)st([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)sec(\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)id(\d+)sp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]*)isp(\d+)lsp(\d+)name([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2],i[11],i[13]))
    return true_result

#return '{}cid{}mid{}fid{}per{}'.format(self.priority,self.contentid, self.memberid, self.fileid, self.permissionid)
#[<Permission: 나만cid8na사전조사(1)in현재 운영중인 회사 정보st신규sec6na사전조사id8sp종합 프로젝트na소프트웨어 개발midjjhw9882psm4321na테스트2emtest02@naver.comfid가랏per2>]
def parse_Permission(text):
    field = re.compile("<Permission: ([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)cid(\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)in([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)st([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)sec([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)mid([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)ps([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)em([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)fid(\w+)per(\w+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[6],i[10],i[11]))
    return true_result

#29midjjhw9882psm4321na테스트2emtest02@naver.comexp2019-05-29 19:23:03
def parse_session(text):
    field = re.compile("(\d+)mid([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)ps([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)em([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)exp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[5]))
    return true_result