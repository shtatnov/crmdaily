#!/usr/bin/python

## michael pinus 10/05/2015
## Credits to Phillip at https://pw999.wordpress.com/2013/08/19/mass-convert-a-project-to-utf-8-using-notepad/ for original implementation of the folder\file iterations
## Credits to vitperov at http://stackoverflow.com/questions/5202648/adding-bom-unicode-signature-while-saving-file-in-python for the addUTF8bom function

## TODO add comments and usage instructions
## TODO command line usage http://www.cyberciti.biz/faq/python-command-line-arguments-argv-example/;
## TODO add drag and drop box

import codecs
import sys
import os

def addUTF8Bom(filename):
  f = codecs.open(filename, 'r', 'utf-8')
  content = f.read()
  f.close()
  f2 = codecs.open(filename, 'w', 'utf-8')
  f2.write(u'\ufeff')
  f2.write(content)
  f2.close()

filePathSrc = 'D:\python' 
for root, dirs, files in os.walk(filePathSrc):
    for fn in files:
      if fn[-4:] == '.csv':
          addUTF8Bom(filePathSrc + '\\' + fn)
          print(filePathSrc + '\\' + fn + ' converted to UTF with BOM')
input("done. press any key to continue... all converted files should be listed above. if none were listed, check spelling of source directroy and that they are CSV")

        

