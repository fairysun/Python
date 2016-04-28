#It's a practise to extract dependencies name and version from package.json file
#Author: sunyb@cn.ibm.com  @2016-04-28

import simplejson
import sys

fo = open(sys.argv[1],"wb")
with open('package.json') as data_file: 
    data=simplejson.load(data_file)

dependency = data['dependencies']
for (name, version) in dependency.items(): 
    fo.write("name: " + name + ", version: " + str(version)[1::] + '\n')
fo.close()
