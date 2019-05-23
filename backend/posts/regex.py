import re
def parse_text(text):
    field =  re.compile("<Comment: (\d+)isp(\w+)who([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2][:-19],i[2][-19:]))
        
    return true_result

def parse_checklist(text):
    field = re.compile("<Checklist: (\d+)sp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)where(\d+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2][:-1],i[2][-1:]))
        
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

#<QuerySet [<Enroll: 8sp종합 프로젝트na소프트웨어 개발idjjhw9882idd8>]>
def parse_enroll(text):
    field = re.compile("<Enroll: (\d+)sp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)id(\w+)idd(\d+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[3],i[4]))
    return true_result

#[<Content: 8na사전조사(1)in현재 운영중인 회사 정보>]
def parse_content(text):
    field = re.compile("<Content: ([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)in([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2]))
    return true_result

#[<Assign: 8na사전조사(1)in현재 운영중인 회사 정보mspjjhw9883isp3>]
def parse_assign(text):
    field = re.compile("<Assign: (\d+)na([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)in([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)msp(\w+)isp(\w+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[3],i[4]))
    return true_result