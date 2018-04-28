import sys
import os
import re
import ntpath as ntp
import argparse
parser = argparse.ArgumentParser(description='PowerShell Minifier')
parser.add_argument('fin', metavar='input file', type=file, nargs=1, help='input PowerShell source')
parser.add_argument('--fout', metavar='output file', type=argparse.FileType('w+'), nargs='?', help='output file of minified version')
args = parser.parse_args()
fin = args.fin[0]
fout = args.fout
content = fin.readlines()
content = [x.strip() for x in content]
result = ''
lastToken = None
# remove all whitespaces and just add ; where ever needed
for token in content:
    token = re.sub('\s\s+(".*?"|.*?)*?', " ", token)
    if lastToken is not None and lastToken != '{' and lastToken != '}' and token != '{' and token != '}':
        result += ';'
    result += token
    lastToken = token
# if there is no output path just save output in same directory with the name format like this [orginal_name].min.[format]
if fout is None:
    basenameObj =  os.path.splitext(ntp.basename(fin.name))
    fout = open(basenameObj[0] + '.min' + basenameObj[1], "w+")
fout.write(result)
