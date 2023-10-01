import re

pattern = "usun_to"
string = "python2020@gusun_tomail.com"
if re.search(pattern,string):
    print(re.sub(pattern, '', string))