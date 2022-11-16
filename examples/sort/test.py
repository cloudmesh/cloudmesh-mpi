#!/usr/bin/env python
from distutils.log import debug
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import argparse
import psutil

from cloudmesh.common.Shell import Shell
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.dotdict import dotdict

def main():
   
    folder = "log"
    for count, filename in enumerate(os.listdir(folder)):
        dst = filename
        words = dst.split("-")
        dst = f"{'-'.join(words[0:4])}-1-{words[4]}.log"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"

        # rename() function will
        # rename all the files
        os.rename(src, dst)
 
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()