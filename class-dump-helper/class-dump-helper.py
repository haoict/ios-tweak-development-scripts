#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author : Hao Nguyen

import sys
import os
import magic
import subprocess
from pathlib import Path

classDumpExec = './class-dump-with-swift-support'
FNULL = open(os.devnull, 'w')

def traverseDir(rootDir='.'):
    mime = magic.Magic(mime=True)
    for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
        # print('Found directory: %s' % dirName)
        for fname in fileList:
            # print('\t%s/%s' % (dirName, fname))
            filePath = '%s/%s' % (dirName, fname)
            fmimeType = mime.from_file(filePath)
            if (fmimeType == 'application/x-mach-binary'):
                # print(filePath)
                classDumpExecArg = ' -H "%s" -o "%s/header/%s"' % (filePath, rootDir, fname)
                print([classDumpExec, classDumpExecArg])
                subprocess.call([classDumpExec + classDumpExecArg], shell=True)



if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print('Argument is missing. Example: ./class-dump-helper.py ~/Desktop/ipa-dump/facebook')

    print('Checking binary files in dir: ', sys.argv[1])
    # os.mkdir(sys.argv[1] + '/header')
    Path(sys.argv[1] + '/header').mkdir(parents=True, exist_ok=True)
    traverseDir(sys.argv[1])
