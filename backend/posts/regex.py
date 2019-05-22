import re
def parse_text(text):
    field =  re.compile("<Comment: (\d+)isp(\w+)who([ 0-9a-zA-Z-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1],i[2][:-19],i[2][-19:]))
        
    return true_result