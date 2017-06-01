#!/usr/bin/env python
#-*-coding:utf-8-*- 

import os
import sys
import logging

def changeEnv(path):
    os.chdir(path)

def changeFileName(path):
    if len(path) != 5:
      logging.error('Please input the right paramters')
      sys.exit(0)
    dirPath = path[1]
    wantToChange = path[2]
    toBeChanged = path[4]
    changeEnv(dirPath)
    hitCount = 0
    for parent, dirnames, filenames in os.walk(dirPath):
      for fileName in filenames:
        if path[3] == 'prefix' and fileName.startswith(wantToChange):
          newName = fileName.replace(wantToChange,toBeChanged,1)
          print fileName + " =====> " + newName
          os.renames(fileName,newName)
          hitCount = hitCount + 1
        elif path[3] == 'normal' and fileName.find(wantToChange) != -1:
          newName = fileName.replace(wantToChange,toBeChanged)
          print fileName + " =====> " + newName
          os.renames(fileName,newName)
          hitCount = hitCount + 1
        elif path[3] == 'suffix':
          nameWithOutFormat = fileName.split('.')[0]
          if nameWithOutFormat.endswith(wantToChange):
            count = nameWithOutFormat.count(wantToChange, 0, len(nameWithOutFormat))
            changeAll = fileName.replace(wantToChange,toBeChanged)
            newName = changeAll.replace(toBeChanged,wantToChange,count - 1)
            print fileName + " =====> " + newName
            os.renames(fileName,newName)
            hitCount = hitCount + 1
        elif path[3] != 'prefix' and path[3] != 'normal' and path[3] != 'suffix':
          logging.error('Please input the right matches')
          sys.exit(0)

    if hitCount == 0:
      logging.warning('Not find the file with given matches')

def changeFile(path):
  changeFileName(path)

if __name__ == "__main__":
  changeFile(sys.argv)


