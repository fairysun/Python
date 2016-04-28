#It's a practise to extract dependencies name and version from npm-shrinkwrap.json file
#Author: sunyb@cn.ibm.com  @2016-04-28

import simplejson
import sys

fo = open(sys.argv[1],"wb")
with open('npm-shrinkwrap.json') as data_file: 
    data=simplejson.load(data_file)

dependency = data['dependencies']
for item in dependency.items(): 
    fo.write("name: " + item[0] + ", version: " + item[1]['version'] + '\n')

fo.close()
