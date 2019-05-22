import re
def parse_text(text):
    field =  re.compile("<Comment: (\d+)isp([ 0-9a-zA-Z-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘\'…]+)>")
    result = field.findall(text)
    true_result = []

    for i in result:
        true_result.append((i[0],i[1][:-19],i[1][-19:]))

    #print(true_result)
    return true_result