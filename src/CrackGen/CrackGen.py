import os
import shutil
import time
import GlobalSettings
from pathlib import *

import PySimpleGUI as sg

from CodeBuilder import generateCM
from CrackGenPaths import *

#######
# GUI #
#######

sg.theme('SystemDefault')

# Frames in mainWindow
cmConfigFrame = [ [sg.Text('\n运算次数：'), sg.Slider(range=(1, 30), default_value=1, orientation='horizontal', key="algCount")] ]

exportCofigFrame = [ [sg.Text('CrackMe 命名：'), sg.In(key="cm_name", default_text="CrackGenCM")], 
                     [sg.Text('CrackMe 模版依赖：'), sg.In(key="cm_template_dir"), sg.FolderBrowse(target="cm_template_dir")],
                     [sg.Text('导出目录：'), sg.In(key="export_path"), sg.FolderBrowse(target="export_path")] ]

# Main Window
layout = [ [sg.Text('CrackGen', font=("Avenir Next", 30)), sg.VerticalSeparator(pad=None), sg.Text('CrackMe & KeyGemMe 自动生成\n作者：@TLHorse，WwW.52PoJiE.cN', font=("Avenir Next", 18))],
           [sg.Frame('CrackMe 配置', cmConfigFrame, font=("苹方-简", 15), title_color='black')],
           [sg.Frame('生成选项', exportCofigFrame, font=("苹方-简", 15), title_color='black')],
           [sg.Button('生成', key="gen"), sg.CloseButton('退出')] ]
mainWindow = sg.Window('CrackGen', layout, font=("苹方-简", 15))

##############################
# Settings for CodeGenerator #
##############################

while True:
    event, values = mainWindow.read()
    if event == 'gen':
        if not Path(values['cm_template_dir']).exists():
            sg.popup_error('CrackMe 模版依赖填写错误！', title="参数错误", font=("苹方-简", 15))
        else:
            projectPath = str(values['cm_template_dir'])
            # try:
            GlobalSettings.GUIAlgorithmsCount = int(values['algCount'])
            generateCM(newCMPath=values['export_path'], newCMName=values['cm_name'])
            # except OSError as err:
            #     sg.popup_error(f'操作异常：{err}。\n\n请将此错误反馈给作者！', title="生成失败", font=("苹方-简", 15))