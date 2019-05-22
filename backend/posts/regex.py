import re
def parse_text(text):
    field =  re.compile("<Comment: (\d+)isp(\w+)who([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2][:-19],i[2][-19:]))
        
    return true_result

#return '{}sp{}where{}{}'.format(self.listnumber, self.listname, self.contentid, self.checked)
def parse_checklist(text):
    field = re.compile("<Checklist: (\d+)sp([ㄱ-힣\\w\\s -=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)where(\d+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2][:-1],i[2][-1:]))
        
    return true_result