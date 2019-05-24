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
    field = re.compile("<Checklist: (\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)ck(\d+)cid(\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)in([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)pos(\d+)he(\d+)st([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2],i[3]))
        
    return true_result

#[<Title: 10spcreate 테스트nacreate 테스트>]
def parse_title(text):
    field = re.compile("<Title: (\d+)sp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2]))
        
    return true_result

#[<Section: 10na변경되냐?id14sp이상한데?na뭐지>]
#return '{}na{}id{}'.format(self.sectionid,self.sectionname, self.titleid)
def parse_section(text):
    field = re.compile("<Section: (\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)id(\d+)sp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2]))
    return true_result

def parse_getsectionid(text):
    field = re.compile("(\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)id(\d+)sp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2]))
    return true_result

#<QuerySet [<Enroll: 8sp종합 프로젝트na소프트웨어 개발idjjhw9882idd8>]>
def parse_enroll(text):
    field = re.compile("<Enroll: (\d+)sp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)id(\w+)idd(\d+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[3],i[4]))
    return true_result

#return '{}na{}in{}pos{}he{}st{}sec{}'.format(self.contentid,self.contentname,self.contentinfo, self.contentpos, self.contentheight, self.contentstate)
#[<Content: 8na사전조사(1)in현재 운영중인 회사 정보pos1he1st신규>]
def parse_content(text):
    field = re.compile("<Content: (\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)in([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)pos(\d+)he(\d+)st([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)sec([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    return true_result

#[<Assign: 8na사전조사(1)in현재 운영중인 회사 정보mspjjhw9883isp3>]
def parse_assign(text):
    field = re.compile("<Assign: (\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)in([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)msp(\w+)isp(\w+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[3],i[4]))
    return true_result

#return '{}pwd{}na{}em{}'.format(self.memberid, self.memberpwd, self.membername, self.memberemail)
#[<Member: testidpwdtestpwd123na테스트emtest@naver.com>]
def parse_member(text):
    field = re.compile("<Member: ([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)ps([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)em([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2],i[3]))
    return true_result

#return '[{}] ~ [{}]csp{}isp{}lsp{}'.format(self.starttime, self.duetime, self.contentid, self.indexnumber, self.isoverlap)
#[Calender: [2019-05-24 00:00:00] ~ [2019-05-25 00:00:00]csp8na사전조사(1)in현재 운영중인 회사 정보pos1he1st신규sec6na사전조사id8sp종합 프로젝트na소프트웨어 개발isp14lsp0]
def parse_calender(text):
    field = re.compile("<Calender: [([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)] ~ [([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)]csp(\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)in([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)pos(\d+)he(\d+)st([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)sec([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)isp(\d+)lsp(\d+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        #true_result.append((i[0],i[1],i[2],i[13],i[14]))
        true_result.append((i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14]))
    return true_result