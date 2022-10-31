#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
bit = platform.architecture()[0]
if bit == '64bit':
    import Sarfraz
elif bit == '32bit':
    print("Device Not Supported!!;")