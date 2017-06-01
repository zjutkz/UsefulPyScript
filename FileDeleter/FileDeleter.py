#!/usr/bin/env python
#-*-coding:utf-8-*- 

import os
import sys
import logging

def delete(path):
  delFile(path)

def changeEnv(path):
  os.chdir(path)

def delFile(path):
  if len(path) != 4:
      logging.error('Please input the right paramters')
      sys.exit(0)
  changeEnv(path[1])
  hitCount = 0
  for parent, dirnames, filenames in os.walk(path[1]):
      for fileName in filenames:
        if path[2] == 'prefix' and fileName.startswith(path[3]):
          os.remove(fileName)
          hitCount = hitCount + 1
        elif path[2] == 'normal' and fileName.find(path[3]) != -1:
          os.remove(fileName)
          hitCount = hitCount + 1
        elif path[2] == 'suffix':
          nameWithOutFormat = fileName.split('.')[0]
          if nameWithOutFormat.endswith(path[3]):
            os.remove(fileName)
            hitCount = hitCount + 1
        elif path[2] != 'prefix' and path[2] != 'normal' and path[2] != 'suffix':
          logging.error('Please input the right matches')
          sys.exit(0)
  if hitCount == 0:
      logging.warning('Not find the file with given matches')

if __name__ == "__main__":
    delete(sys.argv)


