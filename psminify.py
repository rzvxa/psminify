import sys
import os
import re
import ntpath as ntp
fname = sys.argv[1]
try:
    fout = sys.argv[2]
except IndexError:
    fout = None
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
result = ''
lastToken = None
for token in content:
    token = re.sub('\s\s+(".*?"|.*?)*?', " ", token)
    if lastToken is not None and lastToken != '{' and lastToken != '}' and token != '{' and token != '}':
        result += ';'
    result += token
    lastToken = token
if fout is None:
    basenameObj =  os.path.splitext(ntp.basename(fname))
    fout = basenameObj[0] + '.min' + basenameObj[1]
with open(fout,"w+") as f:
    f.write(result)
