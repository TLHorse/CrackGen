import os
import shutil
from pathlib import *

import PySimpleGUI as sg

import CodeGenerator
from CrackGenPaths import *

def buildCM():
    """
    Write code, then build the CrackMe via shell script.
    """
    CodeGenerator.writeCode()
    os.chdir(projectPath) #  + '/CrackGenCM.xcodeproj'
    # os.system("xcodebuild build -quiet -project " + projectPath + '/CrackGenCM.xcodeproj')
    os.system("xcodebuild -quiet -target " + "CrackGenCM")
    CodeGenerator.clearCode()

def productCM(newCMPath, newCMName='CrackGenCM'):
    """
    Move the CrackMe product to the expected distance.
    """
    os.rename(src=f'{cwd}/CMTemplate/CrackGenCM/build/Release/CrackGenCM', dst=f'{cwd}/CMTemplate/CrackGenCM/build/Release/{newCMName}')
    cmPathWithName = Path(newCMPath + "/" + newCMName)
    if not cmPathWithName.exists():
        shutil.move(src=f'{cwd}/CMTemplate/CrackGenCM/build/Release/{newCMName}', dst=newCMPath)
        shutil.rmtree(f'{cwd}/CMTemplate/CrackGenCM/build')
        if sg.popup_ok_cancel(f"CrackMe 生成成功：{newCMPath}/{newCMName}。\n是否打开 CrackMe 所在的文件夹？", title="生成成功", font=("苹方-简", 15)) == "OK":
            cmDirectory = str(newCMPath)
            os.system('open ' + cmDirectory)
    else:
        if sg.popup_yes_no("在目录下已经存在同名文件。是否覆盖？如果不覆盖，将丢失您生成的 CrackMe。", title="文件已存在", font=("苹方-简", 15)) == "No":
            shutil.rmtree(f'{cwd}/CMTemplate/CrackGenCM/build')
        else:
            os.remove(newCMPath + "/" + newCMName)
            shutil.move(src=f'{cwd}/CMTemplate/CrackGenCM/build/Release/{newCMName}', dst=newCMPath)
            shutil.rmtree(f'{cwd}/CMTemplate/CrackGenCM/build')
            if sg.popup_ok_cancel(f"CrackMe 生成成功：{newCMPath}/{newCMName}。\n是否打开 CrackMe 所在的文件夹？", title="生成成功", font=("苹方-简", 15)) == "OK":
                cmDirectory = str(newCMPath)
                os.system('open ' + cmDirectory)

def generateCM(newCMPath, newCMName):
    """
    The final function to generate a CrackMe.
    """
    buildCM()
    productCM(newCMPath=newCMPath, newCMName=newCMName)
