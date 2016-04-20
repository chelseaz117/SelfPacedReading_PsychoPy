#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Mon Apr  4 18:26:01 2016
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'CHN'  # from the Builder filename that created this script
expInfo = {u'Last Name': u'', u'First Name': u'', u'From which course?': u'', u'First Language': u'', u'Session': u'001', u'Student ID': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['First Language'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'\u6b22\u8fce\u53c2\u52a0\u5b9e\u9a8c\u3002\n\u5728\u672c\u5b9e\u9a8c\u4e2d\u4f60\u4f1a\u5728\u5c4f\u5e55\u4e0a\u8bfb\u5230\u4e00\u4e9b\u53e5\u5b50\u3002\u9996\u5148\u4f60\u4f1a\u5728\u5c4f\u5e55\n\u6b63\u4e2d\u592e\u770b\u5230\u4e00\u4e2a\u5341\u5b57\u6807\u5fd7\uff1a',    font='Arial',
    pos=[0, 0.4], height=0.1, wrapWidth=0.1,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=0.1,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text=u'\u5f53\u4f60\u6309\u4e0b\u7a7a\u683c\u952e\u65f6\uff0c\u5341\u5b57\u6807\u5fd7\u4f1a\u6d88\u5931\uff0c\u540c\u65f6\u7b2c\u4e00\u4e2a\u8bcd\u4f1a\u51fa\n\u73b0\u3002\u6bcf\u6309\u4e0b\u4e00\u6b21\u7a7a\u683c\u952e\uff0c\u4e00\u4e2a\u65b0\u7684\u8bcd\u4fbf\u4f1a\u51fa\u73b0\u5728\u5c4f\u5e55\u6b63\u4e2d\n\u53d6\u4ee3\u524d\u4e00\u4e2a\u8bcd\u3002\n\n\u73b0\u5728\u6309\u4e0b\u7a7a\u683c\u952e\u7ee7\u7eed\u3002',    font='Arial',
    pos=[0, -0.4], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "instru2"
instru2Clock = core.Clock()
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text=u'\u5f53\u4f60\u8bfb\u5b8c\u53e5\u5b50\u7684\u6700\u540e\u4e00\u4e2a\u8bcd\uff0c\u518d\u6b21\u6309\u4e0b\u7a7a\u683c\u952e\u3002\u4e00\u5bf9\u56fe\u7247\n\u4f1a\u51fa\u73b0\u5728\u5c4f\u5e55\u4e0a\uff0c\u5e76\u4e14\u4f60\u4f1a\u770b\u5230\u4e00\u4e2a\u95ee\u9898\uff0c\u95ee\u4f60\u8fd9\u5bf9\u56fe\u7247\n\u7684\u5185\u5bb9\u548c\u53e5\u5b50\u5185\u5bb9\u662f\u5426\u76f8\u7b26\u3002\n\n\u56de\u7b54\u95ee\u9898\u65f6\uff0c\u5982\u679c\u56fe\u7247\u4e0e\u53e5\u5b50\u5185\u5bb9\u76f8\u7b26\uff0c\u6309\u201cY\u201d\u952e\uff1b\u5982\u679c\n\u56fe\u7247\u4e0e\u53e5\u5b50\u5185\u5bb9\u4e0d\u76f8\u7b26\uff0c\u6309\u201cN\u201d\u952e\u3002\n\n\u73b0\u5728\u6309\u4e0b\u7a7a\u683c\u952e\u7ee7\u7eed\u3002',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instru3"
instru3Clock = core.Clock()
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text=u'\u4e3a\u4e86\u9605\u8bfb\u548c\u56de\u7b54\u7684\u4fbf\u5229\uff0c\u4f60\u53ef\u4ee5\u628a\u624b\u6307\u653e\u5728\u201cY\u201d\u3001\u201cN\u201d\u548c\n\u7a7a\u683c\u952e\u4e0a\u3002\u8bf7\u5c3d\u91cf\u4ee5\u81ea\u7136\u901f\u5ea6\u9605\u8bfb\uff0c\u5e76\u4e14\u786e\u4fdd\u4f60\u7406\u89e3\u4e86\u4f60\n\u6240\u9605\u8bfb\u7684\u5185\u5bb9\u3002\n\n\u5728\u5b9e\u9a8c\u4e2d\u4f60\u53ef\u4ee5\u4f11\u606f\uff0c\u4f46\u662f\u8bf7\u4e0d\u8981\u5728\u8bfb\u4e00\u4e2a\u53e5\u5b50\u7684\u4e2d\u95f4\u4f11\n\u606f\uff0c\u4e5f\u5c31\u662f\u8bf4\uff0c\u8bf7\u53ea\u5728\u770b\u5230\u5341\u5b57\u6807\u8bb0\u201c+\u201d\u7684\u65f6\u5019\u4f11\u606f\u3002\n\n\u5f53\u5b9e\u9a8c\u7ed3\u675f\u7684\u65f6\u5019\uff0c\u4f60\u4f1a\u770b\u5230\u4e00\u4e2a\u611f\u8c22\u754c\u9762\uff0c\u8bf7\u544a\u77e5\u4e3b\u8bd5\n\u4f60\u5df2\u7ecf\u5b8c\u6210\u4e86\u5b9e\u9a8c\u3002\n\n\u73b0\u5728\u6309\u4e0b\u7a7a\u683c\u952e\u7ee7\u7eed\u3002',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instru4"
instru4Clock = core.Clock()
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text=u'\u73b0\u5728\u8ba9\u6211\u4eec\u518d\u56de\u987e\u4e00\u4e0b\u672c\u5b9e\u9a8c\u7684\u6d41\u7a0b\u2026\n\n1.\u4f60\u901a\u8fc7\u6309\u4e0b\u7a7a\u683c\u952e\u6765\u9605\u8bfb\u5b9e\u9a8c\u53e5\u5b50\u3002\u53e5\u5b50\u8bfb\u5b8c\u540e\u4f1a\u51fa\u73b0\n\u4e00\u5bf9\u56fe\u7247\uff0c\u56fe\u7247\u4ece\u5de6\u5230\u53f3\u63cf\u8ff0\u53e5\u5b50\u4e2d\u7684\u4e24\u4e2a\u4e8b\u4ef6\u3002\n2.\u4f60\u4f1a\u9047\u5230\u4ee5\u4e0b\u51e0\u79cd\u60c5\u51b5\u4e4b\u4e00\uff1a\n(a)\u53e5\u5b50\u4e2d\u63cf\u8ff0\u7684\u5185\u5bb9\u548c\u56fe\u7247\u4e2d\u63cf\u8ff0\u7684\u5185\u5bb9\u76f8\u5339\u914d\u3002\u4e5f\u5c31\n\u662f\u8bf4\uff0c\u5de6\u8fb9\u7684\u56fe\u7247\u63cf\u8ff0\u53e5\u5b50\u4e2d\u7684\u7b2c\u4e00\u4e2a\u4e8b\u4ef6\uff0c\u53f3\u8fb9\u7684\u56fe\u7247\n\u63cf\u8ff0\u53e5\u5b50\u4e2d\u7684\u7b2c\u4e8c\u4e2a\u4e8b\u4ef6\u3002\u8fd9\u65f6\u4f60\u5e94\u8be5\u6309"Y"\u952e\u3002\n(b)\u5de6\u8fb9\u7684\u56fe\u7247\u63cf\u8ff0\u7684\u4e8b\u4ef6\u4e0e\u53e5\u5b50\u4e2d\u7684\u7b2c\u4e00\u4e2a\u4e8b\u4ef6\u4e0d\u5339\u914d\u3002\n\u8fd9\u65f6\u4f60\u5e94\u8be5\u6309"N"\u952e\u3002\n(c)\u53f3\u8fb9\u7684\u56fe\u7247\u63cf\u8ff0\u7684\u4e8b\u4ef6\u4e0e\u53e5\u5b50\u4e2d\u7684\u7b2c\u4e8c\u4e2a\u4e8b\u4ef6\u4e0d\u5339\u914d\u3002\n\u8fd9\u65f6\u4f60\u5e94\u8be5\u6309"N"\u952e\u3002\n\u8bf7\u8bb0\u4f4f\uff0c\u5de6\u8fb9\u6216\u8005\u53f3\u8fb9\u7684\u56fe\u7247\u90fd\u6709\u53ef\u80fd\u4e0e\u53e5\u5b50\u4e0d\u5339\u914d\u3002\n3.\u4f60\u4f1a\u770b\u5230\u4e00\u4e2a\u95ee\u9898\uff0c\u95ee\u4f60\u521a\u770b\u5230\u7684\u4e00\u5bf9\u56fe\u7247\u662f\u5426\u5339\u914d\u4f60\n\u521a\u521a\u8bfb\u8fc7\u7684\u53e5\u5b50\u3002\n\n\u73b0\u5728\u6309\u4e0b\u7a7a\u683c\u952e\u7ee7\u7eed\u3002',    font='Arial',
    pos=[0, 0], height=0.09, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "fixation0"
fixation0Clock = core.Clock()
illustrationS_fixation = visual.TextStim(win=win, ori=0, name='illustrationS_fixation',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "illustration"
illustrationClock = core.Clock()
illustrationS_text = visual.TextStim(win=win, ori=0, name='illustrationS_text',
    text='default text',    font=u'Arial',
    pos=[0, 0.65], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
illustrationS_phrase_1 = visual.TextStim(win=win, ori=0, name='illustrationS_phrase_1',
    text='default text',    font=u'Arial',
    pos=[-0.5, 0.42], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)
illustrationS_phrase_2 = visual.TextStim(win=win, ori=0, name='illustrationS_phrase_2',
    text='default text',    font=u'Arial',
    pos=[0.5, 0.42], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)
illustrationS_pic_1 = visual.ImageStim(win=win, name='illustrationS_pic_1',
    image='sin', mask=None,
    ori=0, pos=[-0.5, 0], size=[0.7, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
illustrationS_pic_2 = visual.ImageStim(win=win, name='illustrationS_pic_2',
    image='sin', mask=None,
    ori=0, pos=[0.5, 0], size=[0.7, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
illustrationS_question_text = visual.TextStim(win=win, ori=0, name='illustrationS_question_text',
    text='default text',    font=u'Arial',
    pos=[0, -0.6], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0)

# Initialize components for Routine "feedback_2"
feedback_2Clock = core.Clock()
illustrationS_feedback_text = visual.TextStim(win=win, ori=0, name='illustrationS_feedback_text',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
illustrationS_feedback_pressToContinue = visual.TextStim(win=win, ori=0, name='illustrationS_feedback_pressToContinue',
    text='default text',    font=u'Arial',
    pos=[0, -0.3], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "instru5"
instru5Clock = core.Clock()
instru_5_text = visual.TextStim(win=win, ori=0, name='instru_5_text',
    text=u'\u8bf7\u518d\u6b21\u6ce8\u610f\uff0c\u6216\u8005\u5de6\u8fb9\u6216\u8005\u53f3\u8fb9\u7684\u56fe\u7247\u4f1a\u8ddf\u53e5\u5b50\u4e0d\u5339\u914d\u3002\n\n\u73b0\u5728\u6309\u4e0b\u7a7a\u683c\u952e\u7ee7\u7eed\u3002',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instru6"
instru6Clock = core.Clock()
instru_6_text = visual.TextStim(win=win, ori=0, name='instru_6_text',
    text=u'\u4f46\u662f\u5728\u771f\u6b63\u7684\u5b9e\u9a8c\u4e2d\uff0c\u53bb\u5b8c\u6210\u9605\u8bfb\u6574\u4e2a\u53e5\u5b50\uff0c\u4f60\u9700\u8981\u4e0d\u65ad\n\u5730\u6309\u4e0b\u7a7a\u683c\u952e\u3002\u6bcf\u6309\u4e00\u6b21\u7a7a\u683c\u952e\uff0c\u53e5\u5b50\u4e2d\u7684\u4e00\u4e2a\u6216\u8005\u51e0\u4e2a\n\u8bcd\u51fa\u73b0\u3002\u4e0b\u9762\u4f60\u4f1a\u770b\u5230\u4f60\u521a\u521a\u8bfb\u8fc7\u7684\u4f8b\u5b50\u51fa\u73b0\u5728\u771f\u6b63\u7684\u5b9e\n\u9a8c\u4e2d\u7684\u573a\u666f\u3002\n\n\u73b0\u5728\u6309\u4e0b\u7a7a\u683c\u952e\u7ee7\u7eed\u3002',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "fixation1"
fixation1Clock = core.Clock()
illustrationSP_fixation = visual.TextStim(win=win, ori=0, name='illustrationSP_fixation',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region1"
region1Clock = core.Clock()
regionSP_text_1 = visual.TextStim(win=win, ori=0, name='regionSP_text_1',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region2"
region2Clock = core.Clock()
regionSP_text_2 = visual.TextStim(win=win, ori=0, name='regionSP_text_2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region3"
region3Clock = core.Clock()
regionSP_text_3 = visual.TextStim(win=win, ori=0, name='regionSP_text_3',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region4"
region4Clock = core.Clock()
regionSP_text_4 = visual.TextStim(win=win, ori=0, name='regionSP_text_4',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region5"
region5Clock = core.Clock()
regionSP_text_5 = visual.TextStim(win=win, ori=0, name='regionSP_text_5',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region6"
region6Clock = core.Clock()
regionSP_text_6 = visual.TextStim(win=win, ori=0, name='regionSP_text_6',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region7"
region7Clock = core.Clock()
regionSP_text_7 = visual.TextStim(win=win, ori=0, name='regionSP_text_7',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region8"
region8Clock = core.Clock()
regionSP_text_8 = visual.TextStim(win=win, ori=0, name='regionSP_text_8',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region9"
region9Clock = core.Clock()
regionSP_text_9 = visual.TextStim(win=win, ori=0, name='regionSP_text_9',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region10"
region10Clock = core.Clock()
regionSP_text_10 = visual.TextStim(win=win, ori=0, name='regionSP_text_10',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region11"
region11Clock = core.Clock()
regionSP_text_11 = visual.TextStim(win=win, ori=0, name='regionSP_text_11',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region12"
region12Clock = core.Clock()
regionSP_text_12 = visual.TextStim(win=win, ori=0, name='regionSP_text_12',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "response1"
response1Clock = core.Clock()
phraseSP_text_1 = visual.TextStim(win=win, ori=0, name='phraseSP_text_1',
    text='default text',    font='Arial',
    pos=[-0.5, 0.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
phraseSP_text_2 = visual.TextStim(win=win, ori=0, name='phraseSP_text_2',
    text='default text',    font='Arial',
    pos=[0.5, 0.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
picSP_1 = visual.ImageStim(win=win, name='picSP_1',
    image='sin', mask=None,
    ori=0, pos=[-0.5, 0], size=[0.7, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
picSP_2 = visual.ImageStim(win=win, name='picSP_2',
    image='sin', mask=None,
    ori=0, pos=[0.5, 0], size=[0.7, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Q_SP = visual.TextStim(win=win, ori=0, name='Q_SP',
    text='default text',    font=u'Arial',
    pos=[0, -0.6], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "feedback_SP"
feedback_SPClock = core.Clock()
feedback_SP_text = visual.TextStim(win=win, ori=0, name='feedback_SP_text',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
feedback_SP_pressToContinue = visual.TextStim(win=win, ori=0, name='feedback_SP_pressToContinue',
    text='default text',    font=u'Arial',
    pos=[0, -0.3], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "instru_prac"
instru_pracClock = core.Clock()
instruction_Prac = visual.TextStim(win=win, ori=0, name='instruction_Prac',
    text=u'\u5982\u679c\u4f60\u6709\u95ee\u9898\uff0c\u8bf7\u73b0\u5728\u8be2\u95ee\u4e3b\u8bd5\u3002\u5982\u679c\u4f60\u4e86\u89e3\u4e86\u5b9e\u9a8c\u4efb\u52a1\n\u5e76\u4e14\u6ca1\u6709\u95ee\u9898\uff0c\u9996\u5148\u4f60\u4f1a\u505a\u4e00\u8f6e\u7ec3\u4e60\u53e5\u3002\u7ec3\u4e60\u53e5\u4f1a\u548c\u771f\u6b63\n\u7684\u5b9e\u9a8c\u5b8c\u5168\u4e00\u6837\uff0c\u552f\u4e00\u7684\u533a\u522b\u662f\u5728\u6bcf\u4e2a\u7ec3\u4e60\u53e5\u7ed3\u675f\u540e\uff0c\u4f60\n\u4f1a\u770b\u5230\u53cd\u9988\u6765\u544a\u8bc9\u4f60\u6b63\u786e\u7b54\u6848\u662f\u4ec0\u4e48\u3002\n\n\u73b0\u5728\u6309\u4e0b\u7a7a\u683c\u952e\u7ee7\u7eed\u3002',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "fixation2_2"
fixation2_2Clock = core.Clock()
practice_fixation = visual.TextStim(win=win, ori=0, name='practice_fixation',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region1_2"
region1_2Clock = core.Clock()
region_prac_1 = visual.TextStim(win=win, ori=0, name='region_prac_1',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region2_2"
region2_2Clock = core.Clock()
region_prac_2 = visual.TextStim(win=win, ori=0, name='region_prac_2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region3_2"
region3_2Clock = core.Clock()
region_prac_3 = visual.TextStim(win=win, ori=0, name='region_prac_3',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region4_2"
region4_2Clock = core.Clock()
region_prac_4 = visual.TextStim(win=win, ori=0, name='region_prac_4',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region5_2"
region5_2Clock = core.Clock()
region_prac_5 = visual.TextStim(win=win, ori=0, name='region_prac_5',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region6_2"
region6_2Clock = core.Clock()
region_prac_6 = visual.TextStim(win=win, ori=0, name='region_prac_6',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region7_2"
region7_2Clock = core.Clock()
region_prac_7 = visual.TextStim(win=win, ori=0, name='region_prac_7',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region8_2"
region8_2Clock = core.Clock()
region_prac_8 = visual.TextStim(win=win, ori=0, name='region_prac_8',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region9_2"
region9_2Clock = core.Clock()
region_prac_9 = visual.TextStim(win=win, ori=0, name='region_prac_9',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region10_2"
region10_2Clock = core.Clock()
region_prac_10 = visual.TextStim(win=win, ori=0, name='region_prac_10',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region11_2"
region11_2Clock = core.Clock()
region_prac_11 = visual.TextStim(win=win, ori=0, name='region_prac_11',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region12_2"
region12_2Clock = core.Clock()
region_prac_12 = visual.TextStim(win=win, ori=0, name='region_prac_12',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "response_Prac"
response_PracClock = core.Clock()
phrase_prac_1 = visual.TextStim(win=win, ori=0, name='phrase_prac_1',
    text='default text',    font='Arial',
    pos=[-0.5, 0.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
phrase_prac_2 = visual.TextStim(win=win, ori=0, name='phrase_prac_2',
    text='default text',    font='Arial',
    pos=[0.5, 0.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
image_prac_1 = visual.ImageStim(win=win, name='image_prac_1',
    image='sin', mask=None,
    ori=0, pos=[-0.5, 0], size=[0.7, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_prac_2 = visual.ImageStim(win=win, name='image_prac_2',
    image='sin', mask=None,
    ori=0, pos=[0.5, 0], size=[0.7, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Q_prac_text = visual.TextStim(win=win, ori=0, name='Q_prac_text',
    text='default text',    font=u'Arial',
    pos=[0, -0.6], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "feedback_prac"
feedback_pracClock = core.Clock()
feedback_prac_text = visual.TextStim(win=win, ori=0, name='feedback_prac_text',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
feedback_prac_pressToContinue = visual.TextStim(win=win, ori=0, name='feedback_prac_pressToContinue',
    text='default text',    font=u'Arial',
    pos=[0, -0.3], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "pracEnd"
pracEndClock = core.Clock()
pracEnd_text = visual.TextStim(win=win, ori=0, name='pracEnd_text',
    text=u'\u8fd9\u5c31\u662f\u5168\u90e8\u7684\u7ec3\u4e60\u53e5\u3002\n\n\u5982\u679c\u6709\u7591\u95ee\uff0c\u8bf7\u73b0\u5728\u8be2\u95ee\u4e3b\u8bd5\u3002\n\n\u5982\u679c\u6ca1\u6709\u7591\u95ee\uff0c\u4f60\u53ef\u4ee5\u5f00\u59cb\u5b9e\u9a8c\u4e86\u3002',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "ExpBegin"
ExpBeginClock = core.Clock()
ExpBegin_text = visual.TextStim(win=win, ori=0, name='ExpBegin_text',
    text=u'\u73b0\u5728\u5f00\u59cb\u5b9e\u9a8c...',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "fixationExp"
fixationExpClock = core.Clock()
Exp_fixation = visual.TextStim(win=win, ori=0, name='Exp_fixation',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region1_Exp"
region1_ExpClock = core.Clock()
regionExp_text_1 = visual.TextStim(win=win, ori=0, name='regionExp_text_1',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region2_Exp"
region2_ExpClock = core.Clock()
regionExp_text_2 = visual.TextStim(win=win, ori=0, name='regionExp_text_2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region3_Exp"
region3_ExpClock = core.Clock()
regionExp_text_3 = visual.TextStim(win=win, ori=0, name='regionExp_text_3',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region4_Exp"
region4_ExpClock = core.Clock()
regionExp_text_4 = visual.TextStim(win=win, ori=0, name='regionExp_text_4',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region5_Exp"
region5_ExpClock = core.Clock()
regionExp_text_5 = visual.TextStim(win=win, ori=0, name='regionExp_text_5',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region6_Exp"
region6_ExpClock = core.Clock()
regionExp_text_6 = visual.TextStim(win=win, ori=0, name='regionExp_text_6',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region7_Exp"
region7_ExpClock = core.Clock()
regionExp_text_7 = visual.TextStim(win=win, ori=0, name='regionExp_text_7',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region8_Exp"
region8_ExpClock = core.Clock()
regionExp_text_8 = visual.TextStim(win=win, ori=0, name='regionExp_text_8',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region9_Exp"
region9_ExpClock = core.Clock()
regionExp_text_9 = visual.TextStim(win=win, ori=0, name='regionExp_text_9',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region10_Exp"
region10_ExpClock = core.Clock()
regionExp_text_10 = visual.TextStim(win=win, ori=0, name='regionExp_text_10',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region11_Exp"
region11_ExpClock = core.Clock()
regionExp_text_11 = visual.TextStim(win=win, ori=0, name='regionExp_text_11',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region12_Exp"
region12_ExpClock = core.Clock()
regionExp_text_12 = visual.TextStim(win=win, ori=0, name='regionExp_text_12',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "response_Exp"
response_ExpClock = core.Clock()
phraseExp_text_1 = visual.TextStim(win=win, ori=0, name='phraseExp_text_1',
    text='default text',    font='Arial',
    pos=[-0.5, 0.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
phraseExp_text_2 = visual.TextStim(win=win, ori=0, name='phraseExp_text_2',
    text='default text',    font='Arial',
    pos=[0.5, 0.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
picExp_text_1 = visual.ImageStim(win=win, name='picExp_text_1',
    image='sin', mask=None,
    ori=0, pos=[-0.5, 0], size=[0.7, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
picExp_text_2 = visual.ImageStim(win=win, name='picExp_text_2',
    image='sin', mask=None,
    ori=0, pos=[0.5, 0], size=[0.7, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Q_Exp_text_1 = visual.TextStim(win=win, ori=0, name='Q_Exp_text_1',
    text='default text',    font=u'Arial',
    pos=[0, -0.6], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "ExpEnd"
ExpEndClock = core.Clock()
ExpEnd_text = visual.TextStim(win=win, ori=0, name='ExpEnd_text',
    text=u'\u8fd9\u5c31\u662f\u5168\u90e8\u7684\u5b9e\u9a8c\u3002\n\n\u611f\u8c22\u4f60\u7684\u53c2\u4e0e\uff01',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instr1"-------
t = 0
instr1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
instr1Components = []
instr1Components.append(text)
instr1Components.append(text_2)
instr1Components.append(text_3)
instr1Components.append(key_resp_2)
for thisComponent in instr1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instru2"-------
t = 0
instru2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
instru2Components = []
instru2Components.append(text_4)
instru2Components.append(key_resp_3)
for thisComponent in instru2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instru2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instru2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t  # underestimates by a little under one frame
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instru2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instru2"-------
for thisComponent in instru2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instru2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instru3"-------
t = 0
instru3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
instru3Components = []
instru3Components.append(text_5)
instru3Components.append(key_resp_4)
for thisComponent in instru3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instru3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instru3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # underestimates by a little under one frame
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instru3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instru3"-------
for thisComponent in instru3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instru3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instru4"-------
t = 0
instru4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
instru4Components = []
instru4Components.append(text_6)
instru4Components.append(key_resp_5)
for thisComponent in instru4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instru4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instru4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # underestimates by a little under one frame
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instru4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instru4"-------
for thisComponent in instru4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instru4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
illustrationSentence = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('illustration1.xlsx'),
    seed=None, name='illustrationSentence')
thisExp.addLoop(illustrationSentence)  # add the loop to the experiment
thisIllustrationSentence = illustrationSentence.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisIllustrationSentence.rgb)
if thisIllustrationSentence != None:
    for paramName in thisIllustrationSentence.keys():
        exec(paramName + '= thisIllustrationSentence.' + paramName)

for thisIllustrationSentence in illustrationSentence:
    currentLoop = illustrationSentence
    # abbreviate parameter names if possible (e.g. rgb = thisIllustrationSentence.rgb)
    if thisIllustrationSentence != None:
        for paramName in thisIllustrationSentence.keys():
            exec(paramName + '= thisIllustrationSentence.' + paramName)
    
    #------Prepare to start Routine "fixation0"-------
    t = 0
    fixation0Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    illustrationS_fixation.setText(u'+')
    illustrationS_fixation_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    illustrationS_fixation_response.status = NOT_STARTED
    # keep track of which components have finished
    fixation0Components = []
    fixation0Components.append(illustrationS_fixation)
    fixation0Components.append(illustrationS_fixation_response)
    for thisComponent in fixation0Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fixation0"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = fixation0Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *illustrationS_fixation* updates
        if t >= 0.0 and illustrationS_fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationS_fixation.tStart = t  # underestimates by a little under one frame
            illustrationS_fixation.frameNStart = frameN  # exact frame index
            illustrationS_fixation.setAutoDraw(True)
        
        # *illustrationS_fixation_response* updates
        if t >= 0.0 and illustrationS_fixation_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationS_fixation_response.tStart = t  # underestimates by a little under one frame
            illustrationS_fixation_response.frameNStart = frameN  # exact frame index
            illustrationS_fixation_response.status = STARTED
            # keyboard checking is just starting
            illustrationS_fixation_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if illustrationS_fixation_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                illustrationS_fixation_response.keys = theseKeys[-1]  # just the last key pressed
                illustrationS_fixation_response.rt = illustrationS_fixation_response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation0Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "fixation0"-------
    for thisComponent in fixation0Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if illustrationS_fixation_response.keys in ['', [], None]:  # No response was made
       illustrationS_fixation_response.keys=None
    # store data for illustrationSentence (TrialHandler)
    illustrationSentence.addData('illustrationS_fixation_response.keys',illustrationS_fixation_response.keys)
    if illustrationS_fixation_response.keys != None:  # we had a response
        illustrationSentence.addData('illustrationS_fixation_response.rt', illustrationS_fixation_response.rt)
    # the Routine "fixation0" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "illustration"-------
    t = 0
    illustrationClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    illustrationS_text.setText(sentence)
    illustrationS_phrase_1.setText(phrase1)
    illustrationS_phrase_2.setText(phrase2)
    illustrationS_pic_1.setImage(pic1)
    illustrationS_pic_2.setImage(pic2)
    illustrationS_question_text.setText(question)
    illustrationS_question_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    illustrationS_question_response.status = NOT_STARTED
    # keep track of which components have finished
    illustrationComponents = []
    illustrationComponents.append(illustrationS_text)
    illustrationComponents.append(illustrationS_phrase_1)
    illustrationComponents.append(illustrationS_phrase_2)
    illustrationComponents.append(illustrationS_pic_1)
    illustrationComponents.append(illustrationS_pic_2)
    illustrationComponents.append(illustrationS_question_text)
    illustrationComponents.append(illustrationS_question_response)
    for thisComponent in illustrationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "illustration"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = illustrationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *illustrationS_text* updates
        if t >= 0.0 and illustrationS_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationS_text.tStart = t  # underestimates by a little under one frame
            illustrationS_text.frameNStart = frameN  # exact frame index
            illustrationS_text.setAutoDraw(True)
        
        # *illustrationS_phrase_1* updates
        if t >= 0.0 and illustrationS_phrase_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationS_phrase_1.tStart = t  # underestimates by a little under one frame
            illustrationS_phrase_1.frameNStart = frameN  # exact frame index
            illustrationS_phrase_1.setAutoDraw(True)
        
        # *illustrationS_phrase_2* updates
        if t >= 0.0 and illustrationS_phrase_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationS_phrase_2.tStart = t  # underestimates by a little under one frame
            illustrationS_phrase_2.frameNStart = frameN  # exact frame index
            illustrationS_phrase_2.setAutoDraw(True)
        
        # *illustrationS_pic_1* updates
        if t >= 0.0 and illustrationS_pic_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationS_pic_1.tStart = t  # underestimates by a little under one frame
            illustrationS_pic_1.frameNStart = frameN  # exact frame index
            illustrationS_pic_1.setAutoDraw(True)
        
        # *illustrationS_pic_2* updates
        if t >= 0.0 and illustrationS_pic_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationS_pic_2.tStart = t  # underestimates by a little under one frame
            illustrationS_pic_2.frameNStart = frameN  # exact frame index
            illustrationS_pic_2.setAutoDraw(True)
        
        # *illustrationS_question_text* updates
        if t >= 0.0 and illustrationS_question_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationS_question_text.tStart = t  # underestimates by a little under one frame
            illustrationS_question_text.frameNStart = frameN  # exact frame index
            illustrationS_question_text.setAutoDraw(True)
        
        # *illustrationS_question_response* updates
        if t >= 0.0 and illustrationS_question_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationS_question_response.tStart = t  # underestimates by a little under one frame
            illustrationS_question_response.frameNStart = frameN  # exact frame index
            illustrationS_question_response.status = STARTED
            # keyboard checking is just starting
            illustrationS_question_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if illustrationS_question_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                illustrationS_question_response.keys = theseKeys[-1]  # just the last key pressed
                illustrationS_question_response.rt = illustrationS_question_response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in illustrationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "illustration"-------
    for thisComponent in illustrationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if illustrationS_question_response.keys in ['', [], None]:  # No response was made
       illustrationS_question_response.keys=None
    # store data for illustrationSentence (TrialHandler)
    illustrationSentence.addData('illustrationS_question_response.keys',illustrationS_question_response.keys)
    if illustrationS_question_response.keys != None:  # we had a response
        illustrationSentence.addData('illustrationS_question_response.rt', illustrationS_question_response.rt)
    # the Routine "illustration" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "feedback_2"-------
    t = 0
    feedback_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    illustrationS_feedback_text.setText(feedback)
    illustrationS_feedback_pressToContinue.setText(u'\u73b0\u5728\u6309\u4e0b\u7a7a\u683c\u952e\u7ee7\u7eed\u3002')
    illustrationS_feedback_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    illustrationS_feedback_response.status = NOT_STARTED
    # keep track of which components have finished
    feedback_2Components = []
    feedback_2Components.append(illustrationS_feedback_text)
    feedback_2Components.append(illustrationS_feedback_pressToContinue)
    feedback_2Components.append(illustrationS_feedback_response)
    for thisComponent in feedback_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedback_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = feedback_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *illustrationS_feedback_text* updates
        if t >= 0.0 and illustrationS_feedback_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationS_feedback_text.tStart = t  # underestimates by a little under one frame
            illustrationS_feedback_text.frameNStart = frameN  # exact frame index
            illustrationS_feedback_text.setAutoDraw(True)
        
        # *illustrationS_feedback_pressToContinue* updates
        if t >= 0.0 and illustrationS_feedback_pressToContinue.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationS_feedback_pressToContinue.tStart = t  # underestimates by a little under one frame
            illustrationS_feedback_pressToContinue.frameNStart = frameN  # exact frame index
            illustrationS_feedback_pressToContinue.setAutoDraw(True)
        
        # *illustrationS_feedback_response* updates
        if t >= 0.0 and illustrationS_feedback_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationS_feedback_response.tStart = t  # underestimates by a little under one frame
            illustrationS_feedback_response.frameNStart = frameN  # exact frame index
            illustrationS_feedback_response.status = STARTED
            # keyboard checking is just starting
            illustrationS_feedback_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if illustrationS_feedback_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                illustrationS_feedback_response.keys = theseKeys[-1]  # just the last key pressed
                illustrationS_feedback_response.rt = illustrationS_feedback_response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "feedback_2"-------
    for thisComponent in feedback_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if illustrationS_feedback_response.keys in ['', [], None]:  # No response was made
       illustrationS_feedback_response.keys=None
    # store data for illustrationSentence (TrialHandler)
    illustrationSentence.addData('illustrationS_feedback_response.keys',illustrationS_feedback_response.keys)
    if illustrationS_feedback_response.keys != None:  # we had a response
        illustrationSentence.addData('illustrationS_feedback_response.rt', illustrationS_feedback_response.rt)
    # the Routine "feedback_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'illustrationSentence'


#------Prepare to start Routine "instru5"-------
t = 0
instru5Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instru_5_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
instru_5_response.status = NOT_STARTED
# keep track of which components have finished
instru5Components = []
instru5Components.append(instru_5_text)
instru5Components.append(instru_5_response)
for thisComponent in instru5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instru5"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instru5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instru_5_text* updates
    if t >= 0.0 and instru_5_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instru_5_text.tStart = t  # underestimates by a little under one frame
        instru_5_text.frameNStart = frameN  # exact frame index
        instru_5_text.setAutoDraw(True)
    
    # *instru_5_response* updates
    if t >= 0.0 and instru_5_response.status == NOT_STARTED:
        # keep track of start time/frame for later
        instru_5_response.tStart = t  # underestimates by a little under one frame
        instru_5_response.frameNStart = frameN  # exact frame index
        instru_5_response.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if instru_5_response.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instru5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instru5"-------
for thisComponent in instru5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instru5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instru6"-------
t = 0
instru6Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instru_6_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
instru_6_response.status = NOT_STARTED
# keep track of which components have finished
instru6Components = []
instru6Components.append(instru_6_text)
instru6Components.append(instru_6_response)
for thisComponent in instru6Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instru6"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instru6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instru_6_text* updates
    if t >= 0.0 and instru_6_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instru_6_text.tStart = t  # underestimates by a little under one frame
        instru_6_text.frameNStart = frameN  # exact frame index
        instru_6_text.setAutoDraw(True)
    
    # *instru_6_response* updates
    if t >= 0.0 and instru_6_response.status == NOT_STARTED:
        # keep track of start time/frame for later
        instru_6_response.tStart = t  # underestimates by a little under one frame
        instru_6_response.frameNStart = frameN  # exact frame index
        instru_6_response.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if instru_6_response.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instru6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instru6"-------
for thisComponent in instru6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instru6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
illustration_SP = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('illustration_SP_1.xlsx'),
    seed=None, name='illustration_SP')
thisExp.addLoop(illustration_SP)  # add the loop to the experiment
thisIllustration_SP = illustration_SP.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisIllustration_SP.rgb)
if thisIllustration_SP != None:
    for paramName in thisIllustration_SP.keys():
        exec(paramName + '= thisIllustration_SP.' + paramName)

for thisIllustration_SP in illustration_SP:
    currentLoop = illustration_SP
    # abbreviate parameter names if possible (e.g. rgb = thisIllustration_SP.rgb)
    if thisIllustration_SP != None:
        for paramName in thisIllustration_SP.keys():
            exec(paramName + '= thisIllustration_SP.' + paramName)
    
    #------Prepare to start Routine "fixation1"-------
    t = 0
    fixation1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    illustrationSP_fixation.setText(u'+')
    illustrationSP_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    illustrationSP_response.status = NOT_STARTED
    # keep track of which components have finished
    fixation1Components = []
    fixation1Components.append(illustrationSP_fixation)
    fixation1Components.append(illustrationSP_response)
    for thisComponent in fixation1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fixation1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = fixation1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *illustrationSP_fixation* updates
        if t >= 0.0 and illustrationSP_fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationSP_fixation.tStart = t  # underestimates by a little under one frame
            illustrationSP_fixation.frameNStart = frameN  # exact frame index
            illustrationSP_fixation.setAutoDraw(True)
        
        # *illustrationSP_response* updates
        if t >= 0.0 and illustrationSP_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationSP_response.tStart = t  # underestimates by a little under one frame
            illustrationSP_response.frameNStart = frameN  # exact frame index
            illustrationSP_response.status = STARTED
            # keyboard checking is just starting
            illustrationSP_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if illustrationSP_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                illustrationSP_response.keys = theseKeys[-1]  # just the last key pressed
                illustrationSP_response.rt = illustrationSP_response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "fixation1"-------
    for thisComponent in fixation1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if illustrationSP_response.keys in ['', [], None]:  # No response was made
       illustrationSP_response.keys=None
    # store data for illustration_SP (TrialHandler)
    illustration_SP.addData('illustrationSP_response.keys',illustrationSP_response.keys)
    if illustrationSP_response.keys != None:  # we had a response
        illustration_SP.addData('illustrationSP_response.rt', illustrationSP_response.rt)
    # the Routine "fixation1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region1"-------
    t = 0
    region1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionSP_text_1.setText(region1)
    regionSP_response_1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionSP_response_1.status = NOT_STARTED
    # keep track of which components have finished
    region1Components = []
    region1Components.append(regionSP_text_1)
    region1Components.append(regionSP_response_1)
    for thisComponent in region1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionSP_text_1* updates
        if t >= 0.0 and regionSP_text_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_text_1.tStart = t  # underestimates by a little under one frame
            regionSP_text_1.frameNStart = frameN  # exact frame index
            regionSP_text_1.setAutoDraw(True)
        
        # *regionSP_response_1* updates
        if t >= 0.0 and regionSP_response_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_response_1.tStart = t  # underestimates by a little under one frame
            regionSP_response_1.frameNStart = frameN  # exact frame index
            regionSP_response_1.status = STARTED
            # keyboard checking is just starting
            regionSP_response_1.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionSP_response_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionSP_response_1.keys = theseKeys[-1]  # just the last key pressed
                regionSP_response_1.rt = regionSP_response_1.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region1"-------
    for thisComponent in region1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionSP_response_1.keys in ['', [], None]:  # No response was made
       regionSP_response_1.keys=None
    # store data for illustration_SP (TrialHandler)
    illustration_SP.addData('regionSP_response_1.keys',regionSP_response_1.keys)
    if regionSP_response_1.keys != None:  # we had a response
        illustration_SP.addData('regionSP_response_1.rt', regionSP_response_1.rt)
    # the Routine "region1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region2"-------
    t = 0
    region2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionSP_text_2.setText(region2)
    regionSP_response_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionSP_response_2.status = NOT_STARTED
    # keep track of which components have finished
    region2Components = []
    region2Components.append(regionSP_text_2)
    region2Components.append(regionSP_response_2)
    for thisComponent in region2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionSP_text_2* updates
        if t >= 0.0 and regionSP_text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_text_2.tStart = t  # underestimates by a little under one frame
            regionSP_text_2.frameNStart = frameN  # exact frame index
            regionSP_text_2.setAutoDraw(True)
        
        # *regionSP_response_2* updates
        if t >= 0.0 and regionSP_response_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_response_2.tStart = t  # underestimates by a little under one frame
            regionSP_response_2.frameNStart = frameN  # exact frame index
            regionSP_response_2.status = STARTED
            # keyboard checking is just starting
            regionSP_response_2.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionSP_response_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionSP_response_2.keys = theseKeys[-1]  # just the last key pressed
                regionSP_response_2.rt = regionSP_response_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region2"-------
    for thisComponent in region2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionSP_response_2.keys in ['', [], None]:  # No response was made
       regionSP_response_2.keys=None
    # store data for illustration_SP (TrialHandler)
    illustration_SP.addData('regionSP_response_2.keys',regionSP_response_2.keys)
    if regionSP_response_2.keys != None:  # we had a response
        illustration_SP.addData('regionSP_response_2.rt', regionSP_response_2.rt)
    # the Routine "region2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region3"-------
    t = 0
    region3Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionSP_text_3.setText(region3)
    regionSP_response_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionSP_response_3.status = NOT_STARTED
    # keep track of which components have finished
    region3Components = []
    region3Components.append(regionSP_text_3)
    region3Components.append(regionSP_response_3)
    for thisComponent in region3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region3"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionSP_text_3* updates
        if t >= 0.0 and regionSP_text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_text_3.tStart = t  # underestimates by a little under one frame
            regionSP_text_3.frameNStart = frameN  # exact frame index
            regionSP_text_3.setAutoDraw(True)
        
        # *regionSP_response_3* updates
        if t >= 0.0 and regionSP_response_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_response_3.tStart = t  # underestimates by a little under one frame
            regionSP_response_3.frameNStart = frameN  # exact frame index
            regionSP_response_3.status = STARTED
            # keyboard checking is just starting
            regionSP_response_3.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionSP_response_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionSP_response_3.keys = theseKeys[-1]  # just the last key pressed
                regionSP_response_3.rt = regionSP_response_3.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region3"-------
    for thisComponent in region3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionSP_response_3.keys in ['', [], None]:  # No response was made
       regionSP_response_3.keys=None
    # store data for illustration_SP (TrialHandler)
    illustration_SP.addData('regionSP_response_3.keys',regionSP_response_3.keys)
    if regionSP_response_3.keys != None:  # we had a response
        illustration_SP.addData('regionSP_response_3.rt', regionSP_response_3.rt)
    # the Routine "region3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region4"-------
    t = 0
    region4Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionSP_text_4.setText(region4)
    regionSP_response_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionSP_response_4.status = NOT_STARTED
    # keep track of which components have finished
    region4Components = []
    region4Components.append(regionSP_text_4)
    region4Components.append(regionSP_response_4)
    for thisComponent in region4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region4"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionSP_text_4* updates
        if t >= 0.0 and regionSP_text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_text_4.tStart = t  # underestimates by a little under one frame
            regionSP_text_4.frameNStart = frameN  # exact frame index
            regionSP_text_4.setAutoDraw(True)
        
        # *regionSP_response_4* updates
        if t >= 0.0 and regionSP_response_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_response_4.tStart = t  # underestimates by a little under one frame
            regionSP_response_4.frameNStart = frameN  # exact frame index
            regionSP_response_4.status = STARTED
            # keyboard checking is just starting
            regionSP_response_4.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionSP_response_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionSP_response_4.keys = theseKeys[-1]  # just the last key pressed
                regionSP_response_4.rt = regionSP_response_4.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region4"-------
    for thisComponent in region4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionSP_response_4.keys in ['', [], None]:  # No response was made
       regionSP_response_4.keys=None
    # store data for illustration_SP (TrialHandler)
    illustration_SP.addData('regionSP_response_4.keys',regionSP_response_4.keys)
    if regionSP_response_4.keys != None:  # we had a response
        illustration_SP.addData('regionSP_response_4.rt', regionSP_response_4.rt)
    # the Routine "region4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region5"-------
    t = 0
    region5Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionSP_text_5.setText(region5)
    regionSP_response_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionSP_response_5.status = NOT_STARTED
    # keep track of which components have finished
    region5Components = []
    region5Components.append(regionSP_text_5)
    region5Components.append(regionSP_response_5)
    for thisComponent in region5Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region5"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region5Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionSP_text_5* updates
        if t >= 0.0 and regionSP_text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_text_5.tStart = t  # underestimates by a little under one frame
            regionSP_text_5.frameNStart = frameN  # exact frame index
            regionSP_text_5.setAutoDraw(True)
        
        # *regionSP_response_5* updates
        if t >= 0.0 and regionSP_response_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_response_5.tStart = t  # underestimates by a little under one frame
            regionSP_response_5.frameNStart = frameN  # exact frame index
            regionSP_response_5.status = STARTED
            # keyboard checking is just starting
            regionSP_response_5.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionSP_response_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionSP_response_5.keys = theseKeys[-1]  # just the last key pressed
                regionSP_response_5.rt = regionSP_response_5.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region5"-------
    for thisComponent in region5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionSP_response_5.keys in ['', [], None]:  # No response was made
       regionSP_response_5.keys=None
    # store data for illustration_SP (TrialHandler)
    illustration_SP.addData('regionSP_response_5.keys',regionSP_response_5.keys)
    if regionSP_response_5.keys != None:  # we had a response
        illustration_SP.addData('regionSP_response_5.rt', regionSP_response_5.rt)
    # the Routine "region5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region6"-------
    t = 0
    region6Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionSP_text_6.setText(region6)
    regionSP_response_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionSP_response_6.status = NOT_STARTED
    # keep track of which components have finished
    region6Components = []
    region6Components.append(regionSP_text_6)
    region6Components.append(regionSP_response_6)
    for thisComponent in region6Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region6"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region6Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionSP_text_6* updates
        if t >= 0.0 and regionSP_text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_text_6.tStart = t  # underestimates by a little under one frame
            regionSP_text_6.frameNStart = frameN  # exact frame index
            regionSP_text_6.setAutoDraw(True)
        
        # *regionSP_response_6* updates
        if t >= 0.0 and regionSP_response_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_response_6.tStart = t  # underestimates by a little under one frame
            regionSP_response_6.frameNStart = frameN  # exact frame index
            regionSP_response_6.status = STARTED
            # keyboard checking is just starting
            regionSP_response_6.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionSP_response_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionSP_response_6.keys = theseKeys[-1]  # just the last key pressed
                regionSP_response_6.rt = regionSP_response_6.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region6"-------
    for thisComponent in region6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionSP_response_6.keys in ['', [], None]:  # No response was made
       regionSP_response_6.keys=None
    # store data for illustration_SP (TrialHandler)
    illustration_SP.addData('regionSP_response_6.keys',regionSP_response_6.keys)
    if regionSP_response_6.keys != None:  # we had a response
        illustration_SP.addData('regionSP_response_6.rt', regionSP_response_6.rt)
    # the Routine "region6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region7"-------
    t = 0
    region7Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionSP_text_7.setText(region7)
    regionSP_response_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionSP_response_7.status = NOT_STARTED
    # keep track of which components have finished
    region7Components = []
    region7Components.append(regionSP_text_7)
    region7Components.append(regionSP_response_7)
    for thisComponent in region7Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region7"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region7Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionSP_text_7* updates
        if t >= 0.0 and regionSP_text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_text_7.tStart = t  # underestimates by a little under one frame
            regionSP_text_7.frameNStart = frameN  # exact frame index
            regionSP_text_7.setAutoDraw(True)
        
        # *regionSP_response_7* updates
        if t >= 0.0 and regionSP_response_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_response_7.tStart = t  # underestimates by a little under one frame
            regionSP_response_7.frameNStart = frameN  # exact frame index
            regionSP_response_7.status = STARTED
            # keyboard checking is just starting
            regionSP_response_7.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionSP_response_7.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionSP_response_7.keys = theseKeys[-1]  # just the last key pressed
                regionSP_response_7.rt = regionSP_response_7.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region7"-------
    for thisComponent in region7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionSP_response_7.keys in ['', [], None]:  # No response was made
       regionSP_response_7.keys=None
    # store data for illustration_SP (TrialHandler)
    illustration_SP.addData('regionSP_response_7.keys',regionSP_response_7.keys)
    if regionSP_response_7.keys != None:  # we had a response
        illustration_SP.addData('regionSP_response_7.rt', regionSP_response_7.rt)
    # the Routine "region7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region8"-------
    t = 0
    region8Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionSP_text_8.setText(region8)
    regionSP_response_8 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionSP_response_8.status = NOT_STARTED
    # keep track of which components have finished
    region8Components = []
    region8Components.append(regionSP_text_8)
    region8Components.append(regionSP_response_8)
    for thisComponent in region8Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region8"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region8Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionSP_text_8* updates
        if t >= 0.0 and regionSP_text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_text_8.tStart = t  # underestimates by a little under one frame
            regionSP_text_8.frameNStart = frameN  # exact frame index
            regionSP_text_8.setAutoDraw(True)
        
        # *regionSP_response_8* updates
        if t >= 0.0 and regionSP_response_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_response_8.tStart = t  # underestimates by a little under one frame
            regionSP_response_8.frameNStart = frameN  # exact frame index
            regionSP_response_8.status = STARTED
            # keyboard checking is just starting
            regionSP_response_8.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionSP_response_8.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionSP_response_8.keys = theseKeys[-1]  # just the last key pressed
                regionSP_response_8.rt = regionSP_response_8.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region8"-------
    for thisComponent in region8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionSP_response_8.keys in ['', [], None]:  # No response was made
       regionSP_response_8.keys=None
    # store data for illustration_SP (TrialHandler)
    illustration_SP.addData('regionSP_response_8.keys',regionSP_response_8.keys)
    if regionSP_response_8.keys != None:  # we had a response
        illustration_SP.addData('regionSP_response_8.rt', regionSP_response_8.rt)
    # the Routine "region8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region9"-------
    t = 0
    region9Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionSP_text_9.setText(region9)
    regionSP_response_9 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionSP_response_9.status = NOT_STARTED
    # keep track of which components have finished
    region9Components = []
    region9Components.append(regionSP_text_9)
    region9Components.append(regionSP_response_9)
    for thisComponent in region9Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region9"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region9Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionSP_text_9* updates
        if t >= 0.0 and regionSP_text_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_text_9.tStart = t  # underestimates by a little under one frame
            regionSP_text_9.frameNStart = frameN  # exact frame index
            regionSP_text_9.setAutoDraw(True)
        
        # *regionSP_response_9* updates
        if t >= 0.0 and regionSP_response_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_response_9.tStart = t  # underestimates by a little under one frame
            regionSP_response_9.frameNStart = frameN  # exact frame index
            regionSP_response_9.status = STARTED
            # keyboard checking is just starting
            regionSP_response_9.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionSP_response_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionSP_response_9.keys = theseKeys[-1]  # just the last key pressed
                regionSP_response_9.rt = regionSP_response_9.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region9Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region9"-------
    for thisComponent in region9Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionSP_response_9.keys in ['', [], None]:  # No response was made
       regionSP_response_9.keys=None
    # store data for illustration_SP (TrialHandler)
    illustration_SP.addData('regionSP_response_9.keys',regionSP_response_9.keys)
    if regionSP_response_9.keys != None:  # we had a response
        illustration_SP.addData('regionSP_response_9.rt', regionSP_response_9.rt)
    # the Routine "region9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region10"-------
    t = 0
    region10Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionSP_text_10.setText(region10)
    regionSP_response_10 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionSP_response_10.status = NOT_STARTED
    # keep track of which components have finished
    region10Components = []
    region10Components.append(regionSP_text_10)
    region10Components.append(regionSP_response_10)
    for thisComponent in region10Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region10"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region10Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionSP_text_10* updates
        if t >= 0.0 and regionSP_text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_text_10.tStart = t  # underestimates by a little under one frame
            regionSP_text_10.frameNStart = frameN  # exact frame index
            regionSP_text_10.setAutoDraw(True)
        
        # *regionSP_response_10* updates
        if t >= 0.0 and regionSP_response_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionSP_response_10.tStart = t  # underestimates by a little under one frame
            regionSP_response_10.frameNStart = frameN  # exact frame index
            regionSP_response_10.status = STARTED
            # keyboard checking is just starting
            regionSP_response_10.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionSP_response_10.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionSP_response_10.keys = theseKeys[-1]  # just the last key pressed
                regionSP_response_10.rt = regionSP_response_10.clock.getTime()
                # was this 'correct'?
                if (regionSP_response_10.keys == str(u'')) or (regionSP_response_10.keys == u''):
                    regionSP_response_10.corr = 1
                else:
                    regionSP_response_10.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region10"-------
    for thisComponent in region10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionSP_response_10.keys in ['', [], None]:  # No response was made
       regionSP_response_10.keys=None
       # was no response the correct answer?!
       if str(u'').lower() == 'none': regionSP_response_10.corr = 1  # correct non-response
       else: regionSP_response_10.corr = 0  # failed to respond (incorrectly)
    # store data for illustration_SP (TrialHandler)
    illustration_SP.addData('regionSP_response_10.keys',regionSP_response_10.keys)
    illustration_SP.addData('regionSP_response_10.corr', regionSP_response_10.corr)
    if regionSP_response_10.keys != None:  # we had a response
        illustration_SP.addData('regionSP_response_10.rt', regionSP_response_10.rt)
    # the Routine "region10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region11"-------
    t = 0
    region11Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionSP_text_11.setText(region11)
    regionSP_response_11 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionSP_response_11.status = NOT_STARTED
    # keep track of which components have finished
    region11Components = []
    region11Components.append(regionSP_text_11)
    region11Components.append(regionSP_response_11)
    for thisComponent in region11Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------uneven number of cells in excel----------------

    if region11 == "xyz":

        #------Prepare to start Routine "response1"-------
        t = 0
        response1Clock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        phraseSP_text_1.setText(phrase1)
        phraseSP_text_2.setText(phrase2)
        picSP_1.setImage(pic1)
        picSP_2.setImage(pic2)
        Q_SP.setText(question)
        Q_SP_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
        Q_SP_response.status = NOT_STARTED
        # keep track of which components have finished
        response1Components = []
        response1Components.append(phraseSP_text_1)
        response1Components.append(phraseSP_text_2)
        response1Components.append(picSP_1)
        response1Components.append(picSP_2)
        response1Components.append(Q_SP)
        response1Components.append(Q_SP_response)
        for thisComponent in response1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "response1"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = response1Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *phraseSP_text_1* updates
            if t >= 0.0 and phraseSP_text_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                phraseSP_text_1.tStart = t  # underestimates by a little under one frame
                phraseSP_text_1.frameNStart = frameN  # exact frame index
                phraseSP_text_1.setAutoDraw(True)
            
            # *phraseSP_text_2* updates
            if t >= 0.0 and phraseSP_text_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                phraseSP_text_2.tStart = t  # underestimates by a little under one frame
                phraseSP_text_2.frameNStart = frameN  # exact frame index
                phraseSP_text_2.setAutoDraw(True)
            
            # *picSP_1* updates
            if t >= 0.0 and picSP_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                picSP_1.tStart = t  # underestimates by a little under one frame
                picSP_1.frameNStart = frameN  # exact frame index
                picSP_1.setAutoDraw(True)
            
            # *picSP_2* updates
            if t >= 0.0 and picSP_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                picSP_2.tStart = t  # underestimates by a little under one frame
                picSP_2.frameNStart = frameN  # exact frame index
                picSP_2.setAutoDraw(True)
            
            # *Q_SP* updates
            if t >= 0.0 and Q_SP.status == NOT_STARTED:
                # keep track of start time/frame for later
                Q_SP.tStart = t  # underestimates by a little under one frame
                Q_SP.frameNStart = frameN  # exact frame index
                Q_SP.setAutoDraw(True)
            
            # *Q_SP_response* updates
            if t >= 0.0 and Q_SP_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                Q_SP_response.tStart = t  # underestimates by a little under one frame
                Q_SP_response.frameNStart = frameN  # exact frame index
                Q_SP_response.status = STARTED
                # keyboard checking is just starting
                Q_SP_response.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if Q_SP_response.status == STARTED:
                theseKeys = event.getKeys(keyList=['y', 'n'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Q_SP_response.keys = theseKeys[-1]  # just the last key pressed
                    Q_SP_response.rt = Q_SP_response.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in response1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "response1"-------
        for thisComponent in response1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Q_SP_response.keys in ['', [], None]:  # No response was made
           Q_SP_response.keys=None
        # store data for illustration_SP (TrialHandler)
        illustration_SP.addData('Q_SP_response.keys',Q_SP_response.keys)
        if Q_SP_response.keys != None:  # we had a response
            illustration_SP.addData('Q_SP_response.rt', Q_SP_response.rt)
        # the Routine "response1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

    else:
    
        #-------Start Routine "region11"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = region11Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *regionSP_text_11* updates
            if t >= 0.0 and regionSP_text_11.status == NOT_STARTED:
                # keep track of start time/frame for later
                regionSP_text_11.tStart = t  # underestimates by a little under one frame
                regionSP_text_11.frameNStart = frameN  # exact frame index
                regionSP_text_11.setAutoDraw(True)
            
            # *regionSP_response_11* updates
            if t >= 0.0 and regionSP_response_11.status == NOT_STARTED:
                # keep track of start time/frame for later
                regionSP_response_11.tStart = t  # underestimates by a little under one frame
                regionSP_response_11.frameNStart = frameN  # exact frame index
                regionSP_response_11.status = STARTED
                # keyboard checking is just starting
                regionSP_response_11.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if regionSP_response_11.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    regionSP_response_11.keys = theseKeys[-1]  # just the last key pressed
                    regionSP_response_11.rt = regionSP_response_11.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in region11Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "region11"-------
        for thisComponent in region11Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if regionSP_response_11.keys in ['', [], None]:  # No response was made
           regionSP_response_11.keys=None
        # store data for illustration_SP (TrialHandler)
        illustration_SP.addData('regionSP_response_11.keys',regionSP_response_11.keys)
        if regionSP_response_11.keys != None:  # we had a response
            illustration_SP.addData('regionSP_response_11.rt', regionSP_response_11.rt)
        # the Routine "region11" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        #------Prepare to start Routine "region12"-------
        t = 0
        region12Clock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        regionSP_text_12.setText(region12)
        regionSP_response_12 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        regionSP_response_12.status = NOT_STARTED
        # keep track of which components have finished
        region12Components = []
        region12Components.append(regionSP_text_12)
        region12Components.append(regionSP_response_12)
        for thisComponent in region12Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "region12"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = region12Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *regionSP_text_12* updates
            if t >= 0.0 and regionSP_text_12.status == NOT_STARTED:
                # keep track of start time/frame for later
                regionSP_text_12.tStart = t  # underestimates by a little under one frame
                regionSP_text_12.frameNStart = frameN  # exact frame index
                regionSP_text_12.setAutoDraw(True)
            
            # *regionSP_response_12* updates
            if t >= 0.0 and regionSP_response_12.status == NOT_STARTED:
                # keep track of start time/frame for later
                regionSP_response_12.tStart = t  # underestimates by a little under one frame
                regionSP_response_12.frameNStart = frameN  # exact frame index
                regionSP_response_12.status = STARTED
                # keyboard checking is just starting
                regionSP_response_12.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if regionSP_response_12.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    regionSP_response_12.keys = theseKeys[-1]  # just the last key pressed
                    regionSP_response_12.rt = regionSP_response_12.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in region12Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "region12"-------
        for thisComponent in region12Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if regionSP_response_12.keys in ['', [], None]:  # No response was made
           regionSP_response_12.keys=None
        # store data for illustration_SP (TrialHandler)
        illustration_SP.addData('regionSP_response_12.keys',regionSP_response_12.keys)
        if regionSP_response_12.keys != None:  # we had a response
            illustration_SP.addData('regionSP_response_12.rt', regionSP_response_12.rt)
        # the Routine "region12" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    
    #------Prepare to start Routine "response1"-------
    t = 0
    response1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    phraseSP_text_1.setText(phrase1)
    phraseSP_text_2.setText(phrase2)
    picSP_1.setImage(pic1)
    picSP_2.setImage(pic2)
    Q_SP.setText(question)
    Q_SP_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Q_SP_response.status = NOT_STARTED
    # keep track of which components have finished
    response1Components = []
    response1Components.append(phraseSP_text_1)
    response1Components.append(phraseSP_text_2)
    response1Components.append(picSP_1)
    response1Components.append(picSP_2)
    response1Components.append(Q_SP)
    response1Components.append(Q_SP_response)
    for thisComponent in response1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "response1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = response1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *phraseSP_text_1* updates
        if t >= 0.0 and phraseSP_text_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            phraseSP_text_1.tStart = t  # underestimates by a little under one frame
            phraseSP_text_1.frameNStart = frameN  # exact frame index
            phraseSP_text_1.setAutoDraw(True)
        
        # *phraseSP_text_2* updates
        if t >= 0.0 and phraseSP_text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            phraseSP_text_2.tStart = t  # underestimates by a little under one frame
            phraseSP_text_2.frameNStart = frameN  # exact frame index
            phraseSP_text_2.setAutoDraw(True)
        
        # *picSP_1* updates
        if t >= 0.0 and picSP_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            picSP_1.tStart = t  # underestimates by a little under one frame
            picSP_1.frameNStart = frameN  # exact frame index
            picSP_1.setAutoDraw(True)
        
        # *picSP_2* updates
        if t >= 0.0 and picSP_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            picSP_2.tStart = t  # underestimates by a little under one frame
            picSP_2.frameNStart = frameN  # exact frame index
            picSP_2.setAutoDraw(True)
        
        # *Q_SP* updates
        if t >= 0.0 and Q_SP.status == NOT_STARTED:
            # keep track of start time/frame for later
            Q_SP.tStart = t  # underestimates by a little under one frame
            Q_SP.frameNStart = frameN  # exact frame index
            Q_SP.setAutoDraw(True)
        
        # *Q_SP_response* updates
        if t >= 0.0 and Q_SP_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            Q_SP_response.tStart = t  # underestimates by a little under one frame
            Q_SP_response.frameNStart = frameN  # exact frame index
            Q_SP_response.status = STARTED
            # keyboard checking is just starting
            Q_SP_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Q_SP_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Q_SP_response.keys = theseKeys[-1]  # just the last key pressed
                Q_SP_response.rt = Q_SP_response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in response1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "response1"-------
    for thisComponent in response1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Q_SP_response.keys in ['', [], None]:  # No response was made
       Q_SP_response.keys=None
    # store data for illustration_SP (TrialHandler)
    illustration_SP.addData('Q_SP_response.keys',Q_SP_response.keys)
    if Q_SP_response.keys != None:  # we had a response
        illustration_SP.addData('Q_SP_response.rt', Q_SP_response.rt)
    # the Routine "response1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "feedback_SP"-------
    t = 0
    feedback_SPClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    feedback_SP_text.setText(feedback)
    feedback_SP_pressToContinue.setText(u'\u73b0\u5728\u6309\u4e0b\u7a7a\u683c\u952e\u7ee7\u7eed\u3002')
    feedback_SP_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    feedback_SP_response.status = NOT_STARTED
    # keep track of which components have finished
    feedback_SPComponents = []
    feedback_SPComponents.append(feedback_SP_text)
    feedback_SPComponents.append(feedback_SP_pressToContinue)
    feedback_SPComponents.append(feedback_SP_response)
    for thisComponent in feedback_SPComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedback_SP"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = feedback_SPClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_SP_text* updates
        if t >= 0.0 and feedback_SP_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_SP_text.tStart = t  # underestimates by a little under one frame
            feedback_SP_text.frameNStart = frameN  # exact frame index
            feedback_SP_text.setAutoDraw(True)
        
        # *feedback_SP_pressToContinue* updates
        if t >= 0.0 and feedback_SP_pressToContinue.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_SP_pressToContinue.tStart = t  # underestimates by a little under one frame
            feedback_SP_pressToContinue.frameNStart = frameN  # exact frame index
            feedback_SP_pressToContinue.setAutoDraw(True)
        
        # *feedback_SP_response* updates
        if t >= 0.0 and feedback_SP_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_SP_response.tStart = t  # underestimates by a little under one frame
            feedback_SP_response.frameNStart = frameN  # exact frame index
            feedback_SP_response.status = STARTED
            # keyboard checking is just starting
            feedback_SP_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if feedback_SP_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                feedback_SP_response.keys = theseKeys[-1]  # just the last key pressed
                feedback_SP_response.rt = feedback_SP_response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_SPComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "feedback_SP"-------
    for thisComponent in feedback_SPComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if feedback_SP_response.keys in ['', [], None]:  # No response was made
       feedback_SP_response.keys=None
    # store data for illustration_SP (TrialHandler)
    illustration_SP.addData('feedback_SP_response.keys',feedback_SP_response.keys)
    if feedback_SP_response.keys != None:  # we had a response
        illustration_SP.addData('feedback_SP_response.rt', feedback_SP_response.rt)
    # the Routine "feedback_SP" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'illustration_SP'


#------Prepare to start Routine "instru_prac"-------
t = 0
instru_pracClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_26 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_26.status = NOT_STARTED
# keep track of which components have finished
instru_pracComponents = []
instru_pracComponents.append(instruction_Prac)
instru_pracComponents.append(key_resp_26)
for thisComponent in instru_pracComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instru_prac"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instru_pracClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_Prac* updates
    if t >= 0.0 and instruction_Prac.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruction_Prac.tStart = t  # underestimates by a little under one frame
        instruction_Prac.frameNStart = frameN  # exact frame index
        instruction_Prac.setAutoDraw(True)
    
    # *key_resp_26* updates
    if t >= 0.0 and key_resp_26.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_26.tStart = t  # underestimates by a little under one frame
        key_resp_26.frameNStart = frameN  # exact frame index
        key_resp_26.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_26.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instru_pracComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instru_prac"-------
for thisComponent in instru_pracComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instru_prac" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_prac = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('prac1_CHN.xlsx'),
    seed=None, name='trials_prac')
thisExp.addLoop(trials_prac)  # add the loop to the experiment
thisTrials_prac = trials_prac.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrials_prac.rgb)
if thisTrials_prac != None:
    for paramName in thisTrials_prac.keys():
        exec(paramName + '= thisTrials_prac.' + paramName)

for thisTrials_prac in trials_prac:
    currentLoop = trials_prac
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_prac.rgb)
    if thisTrials_prac != None:
        for paramName in thisTrials_prac.keys():
            exec(paramName + '= thisTrials_prac.' + paramName)
    
    #------Prepare to start Routine "fixation2_2"-------
    t = 0
    fixation2_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    practice_fixation.setText(u'+')
    practice_fixation_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    practice_fixation_response.status = NOT_STARTED
    # keep track of which components have finished
    fixation2_2Components = []
    fixation2_2Components.append(practice_fixation)
    fixation2_2Components.append(practice_fixation_response)
    for thisComponent in fixation2_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fixation2_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = fixation2_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_fixation* updates
        if t >= 0.0 and practice_fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_fixation.tStart = t  # underestimates by a little under one frame
            practice_fixation.frameNStart = frameN  # exact frame index
            practice_fixation.setAutoDraw(True)
        
        # *practice_fixation_response* updates
        if t >= 0.0 and practice_fixation_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_fixation_response.tStart = t  # underestimates by a little under one frame
            practice_fixation_response.frameNStart = frameN  # exact frame index
            practice_fixation_response.status = STARTED
            # keyboard checking is just starting
            practice_fixation_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if practice_fixation_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                practice_fixation_response.keys = theseKeys[-1]  # just the last key pressed
                practice_fixation_response.rt = practice_fixation_response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation2_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "fixation2_2"-------
    for thisComponent in fixation2_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if practice_fixation_response.keys in ['', [], None]:  # No response was made
       practice_fixation_response.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('practice_fixation_response.keys',practice_fixation_response.keys)
    if practice_fixation_response.keys != None:  # we had a response
        trials_prac.addData('practice_fixation_response.rt', practice_fixation_response.rt)
    # the Routine "fixation2_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region1_2"-------
    t = 0
    region1_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_1.setText(region1)
    region_response_1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_response_1.status = NOT_STARTED
    # keep track of which components have finished
    region1_2Components = []
    region1_2Components.append(region_prac_1)
    region1_2Components.append(region_response_1)
    for thisComponent in region1_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region1_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region1_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *region_prac_1* updates
        if t >= 0.0 and region_prac_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_1.tStart = t  # underestimates by a little under one frame
            region_prac_1.frameNStart = frameN  # exact frame index
            region_prac_1.setAutoDraw(True)
        
        # *region_response_1* updates
        if t >= 0.0 and region_response_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_response_1.tStart = t  # underestimates by a little under one frame
            region_response_1.frameNStart = frameN  # exact frame index
            region_response_1.status = STARTED
            # keyboard checking is just starting
            region_response_1.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_response_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_response_1.keys = theseKeys[-1]  # just the last key pressed
                region_response_1.rt = region_response_1.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region1_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region1_2"-------
    for thisComponent in region1_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if region_response_1.keys in ['', [], None]:  # No response was made
       region_response_1.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_response_1.keys',region_response_1.keys)
    if region_response_1.keys != None:  # we had a response
        trials_prac.addData('region_response_1.rt', region_response_1.rt)
    # the Routine "region1_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region2_2"-------
    t = 0
    region2_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_2.setText(region2)
    region_response_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_response_2.status = NOT_STARTED
    # keep track of which components have finished
    region2_2Components = []
    region2_2Components.append(region_prac_2)
    region2_2Components.append(region_response_2)
    for thisComponent in region2_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region2_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region2_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *region_prac_2* updates
        if t >= 0.0 and region_prac_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_2.tStart = t  # underestimates by a little under one frame
            region_prac_2.frameNStart = frameN  # exact frame index
            region_prac_2.setAutoDraw(True)
        
        # *region_response_2* updates
        if t >= 0.0 and region_response_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_response_2.tStart = t  # underestimates by a little under one frame
            region_response_2.frameNStart = frameN  # exact frame index
            region_response_2.status = STARTED
            # keyboard checking is just starting
            region_response_2.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_response_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_response_2.keys = theseKeys[-1]  # just the last key pressed
                region_response_2.rt = region_response_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region2_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region2_2"-------
    for thisComponent in region2_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if region_response_2.keys in ['', [], None]:  # No response was made
       region_response_2.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_response_2.keys',region_response_2.keys)
    if region_response_2.keys != None:  # we had a response
        trials_prac.addData('region_response_2.rt', region_response_2.rt)
    # the Routine "region2_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region3_2"-------
    t = 0
    region3_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_3.setText(region3)
    region_response_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_response_3.status = NOT_STARTED
    # keep track of which components have finished
    region3_2Components = []
    region3_2Components.append(region_prac_3)
    region3_2Components.append(region_response_3)
    for thisComponent in region3_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region3_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region3_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *region_prac_3* updates
        if t >= 0.0 and region_prac_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_3.tStart = t  # underestimates by a little under one frame
            region_prac_3.frameNStart = frameN  # exact frame index
            region_prac_3.setAutoDraw(True)
        
        # *region_response_3* updates
        if t >= 0.0 and region_response_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_response_3.tStart = t  # underestimates by a little under one frame
            region_response_3.frameNStart = frameN  # exact frame index
            region_response_3.status = STARTED
            # keyboard checking is just starting
            region_response_3.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_response_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_response_3.keys = theseKeys[-1]  # just the last key pressed
                region_response_3.rt = region_response_3.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region3_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region3_2"-------
    for thisComponent in region3_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if region_response_3.keys in ['', [], None]:  # No response was made
       region_response_3.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_response_3.keys',region_response_3.keys)
    if region_response_3.keys != None:  # we had a response
        trials_prac.addData('region_response_3.rt', region_response_3.rt)
    # the Routine "region3_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region4_2"-------
    t = 0
    region4_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_4.setText(region4)
    region_response_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_response_4.status = NOT_STARTED
    # keep track of which components have finished
    region4_2Components = []
    region4_2Components.append(region_prac_4)
    region4_2Components.append(region_response_4)
    for thisComponent in region4_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region4_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region4_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *region_prac_4* updates
        if t >= 0.0 and region_prac_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_4.tStart = t  # underestimates by a little under one frame
            region_prac_4.frameNStart = frameN  # exact frame index
            region_prac_4.setAutoDraw(True)
        
        # *region_response_4* updates
        if t >= 0.0 and region_response_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_response_4.tStart = t  # underestimates by a little under one frame
            region_response_4.frameNStart = frameN  # exact frame index
            region_response_4.status = STARTED
            # keyboard checking is just starting
            region_response_4.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_response_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_response_4.keys = theseKeys[-1]  # just the last key pressed
                region_response_4.rt = region_response_4.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region4_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region4_2"-------
    for thisComponent in region4_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if region_response_4.keys in ['', [], None]:  # No response was made
       region_response_4.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_response_4.keys',region_response_4.keys)
    if region_response_4.keys != None:  # we had a response
        trials_prac.addData('region_response_4.rt', region_response_4.rt)
    # the Routine "region4_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region5_2"-------
    t = 0
    region5_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_5.setText(region5)
    region_response_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_response_5.status = NOT_STARTED
    # keep track of which components have finished
    region5_2Components = []
    region5_2Components.append(region_prac_5)
    region5_2Components.append(region_response_5)
    for thisComponent in region5_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region5_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region5_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *region_prac_5* updates
        if t >= 0.0 and region_prac_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_5.tStart = t  # underestimates by a little under one frame
            region_prac_5.frameNStart = frameN  # exact frame index
            region_prac_5.setAutoDraw(True)
        
        # *region_response_5* updates
        if t >= 0.0 and region_response_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_response_5.tStart = t  # underestimates by a little under one frame
            region_response_5.frameNStart = frameN  # exact frame index
            region_response_5.status = STARTED
            # keyboard checking is just starting
            region_response_5.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_response_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_response_5.keys = theseKeys[-1]  # just the last key pressed
                region_response_5.rt = region_response_5.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region5_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region5_2"-------
    for thisComponent in region5_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if region_response_5.keys in ['', [], None]:  # No response was made
       region_response_5.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_response_5.keys',region_response_5.keys)
    if region_response_5.keys != None:  # we had a response
        trials_prac.addData('region_response_5.rt', region_response_5.rt)
    # the Routine "region5_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region6_2"-------
    t = 0
    region6_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_6.setText(region6)
    region_response_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_response_6.status = NOT_STARTED
    # keep track of which components have finished
    region6_2Components = []
    region6_2Components.append(region_prac_6)
    region6_2Components.append(region_response_6)
    for thisComponent in region6_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region6_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region6_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *region_prac_6* updates
        if t >= 0.0 and region_prac_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_6.tStart = t  # underestimates by a little under one frame
            region_prac_6.frameNStart = frameN  # exact frame index
            region_prac_6.setAutoDraw(True)
        
        # *region_response_6* updates
        if t >= 0.0 and region_response_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_response_6.tStart = t  # underestimates by a little under one frame
            region_response_6.frameNStart = frameN  # exact frame index
            region_response_6.status = STARTED
            # keyboard checking is just starting
            region_response_6.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_response_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_response_6.keys = theseKeys[-1]  # just the last key pressed
                region_response_6.rt = region_response_6.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region6_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region6_2"-------
    for thisComponent in region6_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if region_response_6.keys in ['', [], None]:  # No response was made
       region_response_6.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_response_6.keys',region_response_6.keys)
    if region_response_6.keys != None:  # we had a response
        trials_prac.addData('region_response_6.rt', region_response_6.rt)
    # the Routine "region6_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region7_2"-------
    t = 0
    region7_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_7.setText(region7)
    region_response_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_response_7.status = NOT_STARTED
    # keep track of which components have finished
    region7_2Components = []
    region7_2Components.append(region_prac_7)
    region7_2Components.append(region_response_7)
    for thisComponent in region7_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region7_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region7_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *region_prac_7* updates
        if t >= 0.0 and region_prac_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_7.tStart = t  # underestimates by a little under one frame
            region_prac_7.frameNStart = frameN  # exact frame index
            region_prac_7.setAutoDraw(True)
        
        # *region_response_7* updates
        if t >= 0.0 and region_response_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_response_7.tStart = t  # underestimates by a little under one frame
            region_response_7.frameNStart = frameN  # exact frame index
            region_response_7.status = STARTED
            # keyboard checking is just starting
            region_response_7.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_response_7.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_response_7.keys = theseKeys[-1]  # just the last key pressed
                region_response_7.rt = region_response_7.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region7_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region7_2"-------
    for thisComponent in region7_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if region_response_7.keys in ['', [], None]:  # No response was made
       region_response_7.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_response_7.keys',region_response_7.keys)
    if region_response_7.keys != None:  # we had a response
        trials_prac.addData('region_response_7.rt', region_response_7.rt)
    # the Routine "region7_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region8_2"-------
    t = 0
    region8_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_8.setText(region8)
    region_response_8 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_response_8.status = NOT_STARTED
    # keep track of which components have finished
    region8_2Components = []
    region8_2Components.append(region_prac_8)
    region8_2Components.append(region_response_8)
    for thisComponent in region8_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region8_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region8_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *region_prac_8* updates
        if t >= 0.0 and region_prac_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_8.tStart = t  # underestimates by a little under one frame
            region_prac_8.frameNStart = frameN  # exact frame index
            region_prac_8.setAutoDraw(True)
        
        # *region_response_8* updates
        if t >= 0.0 and region_response_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_response_8.tStart = t  # underestimates by a little under one frame
            region_response_8.frameNStart = frameN  # exact frame index
            region_response_8.status = STARTED
            # keyboard checking is just starting
            region_response_8.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_response_8.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_response_8.keys = theseKeys[-1]  # just the last key pressed
                region_response_8.rt = region_response_8.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region8_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region8_2"-------
    for thisComponent in region8_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if region_response_8.keys in ['', [], None]:  # No response was made
       region_response_8.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_response_8.keys',region_response_8.keys)
    if region_response_8.keys != None:  # we had a response
        trials_prac.addData('region_response_8.rt', region_response_8.rt)
    # the Routine "region8_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region9_2"-------
    t = 0
    region9_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_9.setText(region9)
    region_response_9 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_response_9.status = NOT_STARTED
    # keep track of which components have finished
    region9_2Components = []
    region9_2Components.append(region_prac_9)
    region9_2Components.append(region_response_9)
    for thisComponent in region9_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region9_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region9_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *region_prac_9* updates
        if t >= 0.0 and region_prac_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_9.tStart = t  # underestimates by a little under one frame
            region_prac_9.frameNStart = frameN  # exact frame index
            region_prac_9.setAutoDraw(True)
        
        # *region_response_9* updates
        if t >= 0.0 and region_response_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_response_9.tStart = t  # underestimates by a little under one frame
            region_response_9.frameNStart = frameN  # exact frame index
            region_response_9.status = STARTED
            # keyboard checking is just starting
            region_response_9.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_response_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_response_9.keys = theseKeys[-1]  # just the last key pressed
                region_response_9.rt = region_response_9.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region9_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region9_2"-------
    for thisComponent in region9_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if region_response_9.keys in ['', [], None]:  # No response was made
       region_response_9.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_response_9.keys',region_response_9.keys)
    if region_response_9.keys != None:  # we had a response
        trials_prac.addData('region_response_9.rt', region_response_9.rt)
    # the Routine "region9_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region10_2"-------
    t = 0
    region10_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_10.setText(region10)
    region_response_10 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_response_10.status = NOT_STARTED
    # keep track of which components have finished
    region10_2Components = []
    region10_2Components.append(region_prac_10)
    region10_2Components.append(region_response_10)
    for thisComponent in region10_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region10_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region10_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *region_prac_10* updates
        if t >= 0.0 and region_prac_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_10.tStart = t  # underestimates by a little under one frame
            region_prac_10.frameNStart = frameN  # exact frame index
            region_prac_10.setAutoDraw(True)
        
        # *region_response_10* updates
        if t >= 0.0 and region_response_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_response_10.tStart = t  # underestimates by a little under one frame
            region_response_10.frameNStart = frameN  # exact frame index
            region_response_10.status = STARTED
            # keyboard checking is just starting
            region_response_10.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_response_10.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_response_10.keys = theseKeys[-1]  # just the last key pressed
                region_response_10.rt = region_response_10.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region10_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region10_2"-------
    for thisComponent in region10_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if region_response_10.keys in ['', [], None]:  # No response was made
       region_response_10.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_response_10.keys',region_response_10.keys)
    if region_response_10.keys != None:  # we had a response
        trials_prac.addData('region_response_10.rt', region_response_10.rt)
    # the Routine "region10_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region11_2"-------
    t = 0
    region11_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_11.setText(region11)
    region_response_11 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_response_11.status = NOT_STARTED
    # keep track of which components have finished
    region11_2Components = []
    region11_2Components.append(region_prac_11)
    region11_2Components.append(region_response_11)
    for thisComponent in region11_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------uneven number of cells in excel----------------

    if region11 == "xyz":

        #------Prepare to start Routine "response_Prac"-------
        t = 0
        response_PracClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        phrase_prac_1.setText(phrase1)
        phrase_prac_2.setText(phrase2)
        image_prac_1.setImage(pic1)
        image_prac_2.setImage(pic2)
        Q_prac_text.setText(question)
        Q_prac_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
        Q_prac_response.status = NOT_STARTED
        # keep track of which components have finished
        response_PracComponents = []
        response_PracComponents.append(phrase_prac_1)
        response_PracComponents.append(phrase_prac_2)
        response_PracComponents.append(image_prac_1)
        response_PracComponents.append(image_prac_2)
        response_PracComponents.append(Q_prac_text)
        response_PracComponents.append(Q_prac_response)
        for thisComponent in response_PracComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "response_Prac"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = response_PracClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *phrase_prac_1* updates
            if t >= 0.0 and phrase_prac_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                phrase_prac_1.tStart = t  # underestimates by a little under one frame
                phrase_prac_1.frameNStart = frameN  # exact frame index
                phrase_prac_1.setAutoDraw(True)
            
            # *phrase_prac_2* updates
            if t >= 0.0 and phrase_prac_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                phrase_prac_2.tStart = t  # underestimates by a little under one frame
                phrase_prac_2.frameNStart = frameN  # exact frame index
                phrase_prac_2.setAutoDraw(True)
            
            # *image_prac_1* updates
            if t >= 0.0 and image_prac_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_prac_1.tStart = t  # underestimates by a little under one frame
                image_prac_1.frameNStart = frameN  # exact frame index
                image_prac_1.setAutoDraw(True)
            
            # *image_prac_2* updates
            if t >= 0.0 and image_prac_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_prac_2.tStart = t  # underestimates by a little under one frame
                image_prac_2.frameNStart = frameN  # exact frame index
                image_prac_2.setAutoDraw(True)
            
            # *Q_prac_text* updates
            if t >= 0.0 and Q_prac_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                Q_prac_text.tStart = t  # underestimates by a little under one frame
                Q_prac_text.frameNStart = frameN  # exact frame index
                Q_prac_text.setAutoDraw(True)
            
            # *Q_prac_response* updates
            if t >= 0.0 and Q_prac_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                Q_prac_response.tStart = t  # underestimates by a little under one frame
                Q_prac_response.frameNStart = frameN  # exact frame index
                Q_prac_response.status = STARTED
                # keyboard checking is just starting
                Q_prac_response.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if Q_prac_response.status == STARTED:
                theseKeys = event.getKeys(keyList=['y', 'n'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Q_prac_response.keys = theseKeys[-1]  # just the last key pressed
                    Q_prac_response.rt = Q_prac_response.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in response_PracComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "response_Prac"-------
        for thisComponent in response_PracComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Q_prac_response.keys in ['', [], None]:  # No response was made
           Q_prac_response.keys=None
        # store data for trials_prac (TrialHandler)
        trials_prac.addData('Q_prac_response.keys',Q_prac_response.keys)
        if Q_prac_response.keys != None:  # we had a response
            trials_prac.addData('Q_prac_response.rt', Q_prac_response.rt)
        # the Routine "response_Prac" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

    else:
    
        #-------Start Routine "region11_2"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = region11_2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *region_prac_11* updates
            if t >= 0.0 and region_prac_11.status == NOT_STARTED:
                # keep track of start time/frame for later
                region_prac_11.tStart = t  # underestimates by a little under one frame
                region_prac_11.frameNStart = frameN  # exact frame index
                region_prac_11.setAutoDraw(True)
            
            # *region_response_11* updates
            if t >= 0.0 and region_response_11.status == NOT_STARTED:
                # keep track of start time/frame for later
                region_response_11.tStart = t  # underestimates by a little under one frame
                region_response_11.frameNStart = frameN  # exact frame index
                region_response_11.status = STARTED
                # keyboard checking is just starting
                region_response_11.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if region_response_11.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    region_response_11.keys = theseKeys[-1]  # just the last key pressed
                    region_response_11.rt = region_response_11.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in region11_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "region11_2"-------
        for thisComponent in region11_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if region_response_11.keys in ['', [], None]:  # No response was made
           region_response_11.keys=None
        # store data for trials_prac (TrialHandler)
        trials_prac.addData('region_response_11.keys',region_response_11.keys)
        if region_response_11.keys != None:  # we had a response
            trials_prac.addData('region_response_11.rt', region_response_11.rt)
        # the Routine "region11_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        #------Prepare to start Routine "region12_2"-------
        t = 0
        region12_2Clock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        region_prac_12.setText(region12)
        region_response_12 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        region_response_12.status = NOT_STARTED
        # keep track of which components have finished
        region12_2Components = []
        region12_2Components.append(region_prac_12)
        region12_2Components.append(region_response_12)
        for thisComponent in region12_2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "region12_2"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = region12_2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *region_prac_12* updates
            if t >= 0.0 and region_prac_12.status == NOT_STARTED:
                # keep track of start time/frame for later
                region_prac_12.tStart = t  # underestimates by a little under one frame
                region_prac_12.frameNStart = frameN  # exact frame index
                region_prac_12.setAutoDraw(True)
            
            # *region_response_12* updates
            if t >= 0.0 and region_response_12.status == NOT_STARTED:
                # keep track of start time/frame for later
                region_response_12.tStart = t  # underestimates by a little under one frame
                region_response_12.frameNStart = frameN  # exact frame index
                region_response_12.status = STARTED
                # keyboard checking is just starting
                region_response_12.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if region_response_12.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    region_response_12.keys = theseKeys[-1]  # just the last key pressed
                    region_response_12.rt = region_response_12.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in region12_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "region12_2"-------
        for thisComponent in region12_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if region_response_12.keys in ['', [], None]:  # No response was made
           region_response_12.keys=None
        # store data for trials_prac (TrialHandler)
        trials_prac.addData('region_response_12.keys',region_response_12.keys)
        if region_response_12.keys != None:  # we had a response
            trials_prac.addData('region_response_12.rt', region_response_12.rt)
        # the Routine "region12_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    
    #------Prepare to start Routine "response_Prac"-------
    t = 0
    response_PracClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    phrase_prac_1.setText(phrase1)
    phrase_prac_2.setText(phrase2)
    image_prac_1.setImage(pic1)
    image_prac_2.setImage(pic2)
    Q_prac_text.setText(question)
    Q_prac_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Q_prac_response.status = NOT_STARTED
    # keep track of which components have finished
    response_PracComponents = []
    response_PracComponents.append(phrase_prac_1)
    response_PracComponents.append(phrase_prac_2)
    response_PracComponents.append(image_prac_1)
    response_PracComponents.append(image_prac_2)
    response_PracComponents.append(Q_prac_text)
    response_PracComponents.append(Q_prac_response)
    for thisComponent in response_PracComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "response_Prac"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = response_PracClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *phrase_prac_1* updates
        if t >= 0.0 and phrase_prac_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            phrase_prac_1.tStart = t  # underestimates by a little under one frame
            phrase_prac_1.frameNStart = frameN  # exact frame index
            phrase_prac_1.setAutoDraw(True)
        
        # *phrase_prac_2* updates
        if t >= 0.0 and phrase_prac_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            phrase_prac_2.tStart = t  # underestimates by a little under one frame
            phrase_prac_2.frameNStart = frameN  # exact frame index
            phrase_prac_2.setAutoDraw(True)
        
        # *image_prac_1* updates
        if t >= 0.0 and image_prac_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_prac_1.tStart = t  # underestimates by a little under one frame
            image_prac_1.frameNStart = frameN  # exact frame index
            image_prac_1.setAutoDraw(True)
        
        # *image_prac_2* updates
        if t >= 0.0 and image_prac_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_prac_2.tStart = t  # underestimates by a little under one frame
            image_prac_2.frameNStart = frameN  # exact frame index
            image_prac_2.setAutoDraw(True)
        
        # *Q_prac_text* updates
        if t >= 0.0 and Q_prac_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            Q_prac_text.tStart = t  # underestimates by a little under one frame
            Q_prac_text.frameNStart = frameN  # exact frame index
            Q_prac_text.setAutoDraw(True)
        
        # *Q_prac_response* updates
        if t >= 0.0 and Q_prac_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            Q_prac_response.tStart = t  # underestimates by a little under one frame
            Q_prac_response.frameNStart = frameN  # exact frame index
            Q_prac_response.status = STARTED
            # keyboard checking is just starting
            Q_prac_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Q_prac_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Q_prac_response.keys = theseKeys[-1]  # just the last key pressed
                Q_prac_response.rt = Q_prac_response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in response_PracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "response_Prac"-------
    for thisComponent in response_PracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Q_prac_response.keys in ['', [], None]:  # No response was made
       Q_prac_response.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('Q_prac_response.keys',Q_prac_response.keys)
    if Q_prac_response.keys != None:  # we had a response
        trials_prac.addData('Q_prac_response.rt', Q_prac_response.rt)
    # the Routine "response_Prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "feedback_prac"-------
    t = 0
    feedback_pracClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    feedback_prac_text.setText(feedback)
    feedback_prac_pressToContinue.setText(u'\u73b0\u5728\u8bf7\u6309\u4e0b\u7a7a\u683c\u952e\u7ee7\u7eed\u3002')
    feedback_prac_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    feedback_prac_response.status = NOT_STARTED
    # keep track of which components have finished
    feedback_pracComponents = []
    feedback_pracComponents.append(feedback_prac_text)
    feedback_pracComponents.append(feedback_prac_pressToContinue)
    feedback_pracComponents.append(feedback_prac_response)
    for thisComponent in feedback_pracComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedback_prac"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = feedback_pracClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_prac_text* updates
        if t >= 0.0 and feedback_prac_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_prac_text.tStart = t  # underestimates by a little under one frame
            feedback_prac_text.frameNStart = frameN  # exact frame index
            feedback_prac_text.setAutoDraw(True)
        
        # *feedback_prac_pressToContinue* updates
        if t >= 0.0 and feedback_prac_pressToContinue.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_prac_pressToContinue.tStart = t  # underestimates by a little under one frame
            feedback_prac_pressToContinue.frameNStart = frameN  # exact frame index
            feedback_prac_pressToContinue.setAutoDraw(True)
        
        # *feedback_prac_response* updates
        if t >= 0.0 and feedback_prac_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_prac_response.tStart = t  # underestimates by a little under one frame
            feedback_prac_response.frameNStart = frameN  # exact frame index
            feedback_prac_response.status = STARTED
            # keyboard checking is just starting
            feedback_prac_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if feedback_prac_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                feedback_prac_response.keys = theseKeys[-1]  # just the last key pressed
                feedback_prac_response.rt = feedback_prac_response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "feedback_prac"-------
    for thisComponent in feedback_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if feedback_prac_response.keys in ['', [], None]:  # No response was made
       feedback_prac_response.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('feedback_prac_response.keys',feedback_prac_response.keys)
    if feedback_prac_response.keys != None:  # we had a response
        trials_prac.addData('feedback_prac_response.rt', feedback_prac_response.rt)
    # the Routine "feedback_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_prac'


#------Prepare to start Routine "pracEnd"-------
t = 0
pracEndClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
pracEnd_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
pracEnd_response.status = NOT_STARTED
# keep track of which components have finished
pracEndComponents = []
pracEndComponents.append(pracEnd_text)
pracEndComponents.append(pracEnd_response)
for thisComponent in pracEndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "pracEnd"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = pracEndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pracEnd_text* updates
    if t >= 0.0 and pracEnd_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        pracEnd_text.tStart = t  # underestimates by a little under one frame
        pracEnd_text.frameNStart = frameN  # exact frame index
        pracEnd_text.setAutoDraw(True)
    
    # *pracEnd_response* updates
    if t >= 0.0 and pracEnd_response.status == NOT_STARTED:
        # keep track of start time/frame for later
        pracEnd_response.tStart = t  # underestimates by a little under one frame
        pracEnd_response.frameNStart = frameN  # exact frame index
        pracEnd_response.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if pracEnd_response.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pracEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "pracEnd"-------
for thisComponent in pracEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pracEnd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "ExpBegin"-------
t = 0
ExpBeginClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
ExpBegin_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
ExpBegin_response.status = NOT_STARTED
# keep track of which components have finished
ExpBeginComponents = []
ExpBeginComponents.append(ExpBegin_text)
ExpBeginComponents.append(ExpBegin_response)
for thisComponent in ExpBeginComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "ExpBegin"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = ExpBeginClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ExpBegin_text* updates
    if t >= 0.0 and ExpBegin_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        ExpBegin_text.tStart = t  # underestimates by a little under one frame
        ExpBegin_text.frameNStart = frameN  # exact frame index
        ExpBegin_text.setAutoDraw(True)
    
    # *ExpBegin_response* updates
    if t >= 0.0 and ExpBegin_response.status == NOT_STARTED:
        # keep track of start time/frame for later
        ExpBegin_response.tStart = t  # underestimates by a little under one frame
        ExpBegin_response.frameNStart = frameN  # exact frame index
        ExpBegin_response.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if ExpBegin_response.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExpBeginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "ExpBegin"-------
for thisComponent in ExpBeginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "ExpBegin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_exp = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('List1CHN.xlsx'),
    seed=None, name='trials_exp')
thisExp.addLoop(trials_exp)  # add the loop to the experiment
thisTrials_exp = trials_exp.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrials_exp.rgb)
if thisTrials_exp != None:
    for paramName in thisTrials_exp.keys():
        exec(paramName + '= thisTrials_exp.' + paramName)

for thisTrials_exp in trials_exp:
    currentLoop = trials_exp
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_exp.rgb)
    if thisTrials_exp != None:
        for paramName in thisTrials_exp.keys():
            exec(paramName + '= thisTrials_exp.' + paramName)
    
    #------Prepare to start Routine "fixationExp"-------
    t = 0
    fixationExpClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    Exp_fixation.setText(u'+')
    Exp_fixation_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Exp_fixation_response.status = NOT_STARTED
    # keep track of which components have finished
    fixationExpComponents = []
    fixationExpComponents.append(Exp_fixation)
    fixationExpComponents.append(Exp_fixation_response)
    for thisComponent in fixationExpComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fixationExp"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = fixationExpClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Exp_fixation* updates
        if t >= 0.0 and Exp_fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            Exp_fixation.tStart = t  # underestimates by a little under one frame
            Exp_fixation.frameNStart = frameN  # exact frame index
            Exp_fixation.setAutoDraw(True)
        
        # *Exp_fixation_response* updates
        if t >= 0.0 and Exp_fixation_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            Exp_fixation_response.tStart = t  # underestimates by a little under one frame
            Exp_fixation_response.frameNStart = frameN  # exact frame index
            Exp_fixation_response.status = STARTED
            # keyboard checking is just starting
            Exp_fixation_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Exp_fixation_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Exp_fixation_response.keys = theseKeys[-1]  # just the last key pressed
                Exp_fixation_response.rt = Exp_fixation_response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationExpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "fixationExp"-------
    for thisComponent in fixationExpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Exp_fixation_response.keys in ['', [], None]:  # No response was made
       Exp_fixation_response.keys=None
    # store data for trials_exp (TrialHandler)
    trials_exp.addData('Exp_fixation_response.keys',Exp_fixation_response.keys)
    if Exp_fixation_response.keys != None:  # we had a response
        trials_exp.addData('Exp_fixation_response.rt', Exp_fixation_response.rt)
    # the Routine "fixationExp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region1_Exp"-------
    t = 0
    region1_ExpClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionExp_text_1.setText(region1)
    regionExp_response_1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionExp_response_1.status = NOT_STARTED
    # keep track of which components have finished
    region1_ExpComponents = []
    region1_ExpComponents.append(regionExp_text_1)
    region1_ExpComponents.append(regionExp_response_1)
    for thisComponent in region1_ExpComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region1_Exp"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region1_ExpClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionExp_text_1* updates
        if t >= 0.0 and regionExp_text_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_text_1.tStart = t  # underestimates by a little under one frame
            regionExp_text_1.frameNStart = frameN  # exact frame index
            regionExp_text_1.setAutoDraw(True)
        
        # *regionExp_response_1* updates
        if t >= 0.0 and regionExp_response_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_response_1.tStart = t  # underestimates by a little under one frame
            regionExp_response_1.frameNStart = frameN  # exact frame index
            regionExp_response_1.status = STARTED
            # keyboard checking is just starting
            regionExp_response_1.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionExp_response_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionExp_response_1.keys = theseKeys[-1]  # just the last key pressed
                regionExp_response_1.rt = regionExp_response_1.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region1_ExpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region1_Exp"-------
    for thisComponent in region1_ExpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionExp_response_1.keys in ['', [], None]:  # No response was made
       regionExp_response_1.keys=None
    # store data for trials_exp (TrialHandler)
    trials_exp.addData('regionExp_response_1.keys',regionExp_response_1.keys)
    if regionExp_response_1.keys != None:  # we had a response
        trials_exp.addData('regionExp_response_1.rt', regionExp_response_1.rt)
    # the Routine "region1_Exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region2_Exp"-------
    t = 0
    region2_ExpClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionExp_text_2.setText(region2)
    regionExp_response_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionExp_response_2.status = NOT_STARTED
    # keep track of which components have finished
    region2_ExpComponents = []
    region2_ExpComponents.append(regionExp_text_2)
    region2_ExpComponents.append(regionExp_response_2)
    for thisComponent in region2_ExpComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region2_Exp"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region2_ExpClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionExp_text_2* updates
        if t >= 0.0 and regionExp_text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_text_2.tStart = t  # underestimates by a little under one frame
            regionExp_text_2.frameNStart = frameN  # exact frame index
            regionExp_text_2.setAutoDraw(True)
        
        # *regionExp_response_2* updates
        if t >= 0.0 and regionExp_response_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_response_2.tStart = t  # underestimates by a little under one frame
            regionExp_response_2.frameNStart = frameN  # exact frame index
            regionExp_response_2.status = STARTED
            # keyboard checking is just starting
            regionExp_response_2.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionExp_response_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionExp_response_2.keys = theseKeys[-1]  # just the last key pressed
                regionExp_response_2.rt = regionExp_response_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region2_ExpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region2_Exp"-------
    for thisComponent in region2_ExpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionExp_response_2.keys in ['', [], None]:  # No response was made
       regionExp_response_2.keys=None
    # store data for trials_exp (TrialHandler)
    trials_exp.addData('regionExp_response_2.keys',regionExp_response_2.keys)
    if regionExp_response_2.keys != None:  # we had a response
        trials_exp.addData('regionExp_response_2.rt', regionExp_response_2.rt)
    # the Routine "region2_Exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region3_Exp"-------
    t = 0
    region3_ExpClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionExp_text_3.setText(region3)
    regionExp_response_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionExp_response_3.status = NOT_STARTED
    # keep track of which components have finished
    region3_ExpComponents = []
    region3_ExpComponents.append(regionExp_text_3)
    region3_ExpComponents.append(regionExp_response_3)
    for thisComponent in region3_ExpComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region3_Exp"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region3_ExpClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionExp_text_3* updates
        if t >= 0.0 and regionExp_text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_text_3.tStart = t  # underestimates by a little under one frame
            regionExp_text_3.frameNStart = frameN  # exact frame index
            regionExp_text_3.setAutoDraw(True)
        
        # *regionExp_response_3* updates
        if t >= 0.0 and regionExp_response_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_response_3.tStart = t  # underestimates by a little under one frame
            regionExp_response_3.frameNStart = frameN  # exact frame index
            regionExp_response_3.status = STARTED
            # keyboard checking is just starting
            regionExp_response_3.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionExp_response_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionExp_response_3.keys = theseKeys[-1]  # just the last key pressed
                regionExp_response_3.rt = regionExp_response_3.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region3_ExpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region3_Exp"-------
    for thisComponent in region3_ExpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionExp_response_3.keys in ['', [], None]:  # No response was made
       regionExp_response_3.keys=None
    # store data for trials_exp (TrialHandler)
    trials_exp.addData('regionExp_response_3.keys',regionExp_response_3.keys)
    if regionExp_response_3.keys != None:  # we had a response
        trials_exp.addData('regionExp_response_3.rt', regionExp_response_3.rt)
    # the Routine "region3_Exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region4_Exp"-------
    t = 0
    region4_ExpClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionExp_text_4.setText(region4)
    regionExp_response_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionExp_response_4.status = NOT_STARTED
    # keep track of which components have finished
    region4_ExpComponents = []
    region4_ExpComponents.append(regionExp_text_4)
    region4_ExpComponents.append(regionExp_response_4)
    for thisComponent in region4_ExpComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region4_Exp"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region4_ExpClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionExp_text_4* updates
        if t >= 0.0 and regionExp_text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_text_4.tStart = t  # underestimates by a little under one frame
            regionExp_text_4.frameNStart = frameN  # exact frame index
            regionExp_text_4.setAutoDraw(True)
        
        # *regionExp_response_4* updates
        if t >= 0.0 and regionExp_response_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_response_4.tStart = t  # underestimates by a little under one frame
            regionExp_response_4.frameNStart = frameN  # exact frame index
            regionExp_response_4.status = STARTED
            # keyboard checking is just starting
            regionExp_response_4.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionExp_response_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionExp_response_4.keys = theseKeys[-1]  # just the last key pressed
                regionExp_response_4.rt = regionExp_response_4.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region4_ExpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region4_Exp"-------
    for thisComponent in region4_ExpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionExp_response_4.keys in ['', [], None]:  # No response was made
       regionExp_response_4.keys=None
    # store data for trials_exp (TrialHandler)
    trials_exp.addData('regionExp_response_4.keys',regionExp_response_4.keys)
    if regionExp_response_4.keys != None:  # we had a response
        trials_exp.addData('regionExp_response_4.rt', regionExp_response_4.rt)
    # the Routine "region4_Exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region5_Exp"-------
    t = 0
    region5_ExpClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionExp_text_5.setText(region5)
    regionExp_response_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionExp_response_5.status = NOT_STARTED
    # keep track of which components have finished
    region5_ExpComponents = []
    region5_ExpComponents.append(regionExp_text_5)
    region5_ExpComponents.append(regionExp_response_5)
    for thisComponent in region5_ExpComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region5_Exp"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region5_ExpClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionExp_text_5* updates
        if t >= 0.0 and regionExp_text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_text_5.tStart = t  # underestimates by a little under one frame
            regionExp_text_5.frameNStart = frameN  # exact frame index
            regionExp_text_5.setAutoDraw(True)
        
        # *regionExp_response_5* updates
        if t >= 0.0 and regionExp_response_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_response_5.tStart = t  # underestimates by a little under one frame
            regionExp_response_5.frameNStart = frameN  # exact frame index
            regionExp_response_5.status = STARTED
            # keyboard checking is just starting
            regionExp_response_5.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionExp_response_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionExp_response_5.keys = theseKeys[-1]  # just the last key pressed
                regionExp_response_5.rt = regionExp_response_5.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region5_ExpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region5_Exp"-------
    for thisComponent in region5_ExpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionExp_response_5.keys in ['', [], None]:  # No response was made
       regionExp_response_5.keys=None
    # store data for trials_exp (TrialHandler)
    trials_exp.addData('regionExp_response_5.keys',regionExp_response_5.keys)
    if regionExp_response_5.keys != None:  # we had a response
        trials_exp.addData('regionExp_response_5.rt', regionExp_response_5.rt)
    # the Routine "region5_Exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region6_Exp"-------
    t = 0
    region6_ExpClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionExp_text_6.setText(region6)
    regionExp_response_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionExp_response_6.status = NOT_STARTED
    # keep track of which components have finished
    region6_ExpComponents = []
    region6_ExpComponents.append(regionExp_text_6)
    region6_ExpComponents.append(regionExp_response_6)
    for thisComponent in region6_ExpComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region6_Exp"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region6_ExpClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionExp_text_6* updates
        if t >= 0.0 and regionExp_text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_text_6.tStart = t  # underestimates by a little under one frame
            regionExp_text_6.frameNStart = frameN  # exact frame index
            regionExp_text_6.setAutoDraw(True)
        
        # *regionExp_response_6* updates
        if t >= 0.0 and regionExp_response_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_response_6.tStart = t  # underestimates by a little under one frame
            regionExp_response_6.frameNStart = frameN  # exact frame index
            regionExp_response_6.status = STARTED
            # keyboard checking is just starting
            regionExp_response_6.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionExp_response_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionExp_response_6.keys = theseKeys[-1]  # just the last key pressed
                regionExp_response_6.rt = regionExp_response_6.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region6_ExpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region6_Exp"-------
    for thisComponent in region6_ExpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionExp_response_6.keys in ['', [], None]:  # No response was made
       regionExp_response_6.keys=None
    # store data for trials_exp (TrialHandler)
    trials_exp.addData('regionExp_response_6.keys',regionExp_response_6.keys)
    if regionExp_response_6.keys != None:  # we had a response
        trials_exp.addData('regionExp_response_6.rt', regionExp_response_6.rt)
    # the Routine "region6_Exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region7_Exp"-------
    t = 0
    region7_ExpClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionExp_text_7.setText(region7)
    regionExp_response_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionExp_response_7.status = NOT_STARTED
    # keep track of which components have finished
    region7_ExpComponents = []
    region7_ExpComponents.append(regionExp_text_7)
    region7_ExpComponents.append(regionExp_response_7)
    for thisComponent in region7_ExpComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region7_Exp"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region7_ExpClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionExp_text_7* updates
        if t >= 0.0 and regionExp_text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_text_7.tStart = t  # underestimates by a little under one frame
            regionExp_text_7.frameNStart = frameN  # exact frame index
            regionExp_text_7.setAutoDraw(True)
        
        # *regionExp_response_7* updates
        if t >= 0.0 and regionExp_response_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_response_7.tStart = t  # underestimates by a little under one frame
            regionExp_response_7.frameNStart = frameN  # exact frame index
            regionExp_response_7.status = STARTED
            # keyboard checking is just starting
            regionExp_response_7.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionExp_response_7.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionExp_response_7.keys = theseKeys[-1]  # just the last key pressed
                regionExp_response_7.rt = regionExp_response_7.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region7_ExpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region7_Exp"-------
    for thisComponent in region7_ExpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionExp_response_7.keys in ['', [], None]:  # No response was made
       regionExp_response_7.keys=None
    # store data for trials_exp (TrialHandler)
    trials_exp.addData('regionExp_response_7.keys',regionExp_response_7.keys)
    if regionExp_response_7.keys != None:  # we had a response
        trials_exp.addData('regionExp_response_7.rt', regionExp_response_7.rt)
    # the Routine "region7_Exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region8_Exp"-------
    t = 0
    region8_ExpClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionExp_text_8.setText(region8)
    regionExp_response_8 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionExp_response_8.status = NOT_STARTED
    # keep track of which components have finished
    region8_ExpComponents = []
    region8_ExpComponents.append(regionExp_text_8)
    region8_ExpComponents.append(regionExp_response_8)
    for thisComponent in region8_ExpComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region8_Exp"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region8_ExpClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionExp_text_8* updates
        if t >= 0.0 and regionExp_text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_text_8.tStart = t  # underestimates by a little under one frame
            regionExp_text_8.frameNStart = frameN  # exact frame index
            regionExp_text_8.setAutoDraw(True)
        
        # *regionExp_response_8* updates
        if t >= 0.0 and regionExp_response_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_response_8.tStart = t  # underestimates by a little under one frame
            regionExp_response_8.frameNStart = frameN  # exact frame index
            regionExp_response_8.status = STARTED
            # keyboard checking is just starting
            regionExp_response_8.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionExp_response_8.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionExp_response_8.keys = theseKeys[-1]  # just the last key pressed
                regionExp_response_8.rt = regionExp_response_8.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region8_ExpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region8_Exp"-------
    for thisComponent in region8_ExpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionExp_response_8.keys in ['', [], None]:  # No response was made
       regionExp_response_8.keys=None
    # store data for trials_exp (TrialHandler)
    trials_exp.addData('regionExp_response_8.keys',regionExp_response_8.keys)
    if regionExp_response_8.keys != None:  # we had a response
        trials_exp.addData('regionExp_response_8.rt', regionExp_response_8.rt)
    # the Routine "region8_Exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region9_Exp"-------
    t = 0
    region9_ExpClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionExp_text_9.setText(region9)
    regionExp_response_9 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionExp_response_9.status = NOT_STARTED
    # keep track of which components have finished
    region9_ExpComponents = []
    region9_ExpComponents.append(regionExp_text_9)
    region9_ExpComponents.append(regionExp_response_9)
    for thisComponent in region9_ExpComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region9_Exp"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region9_ExpClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionExp_text_9* updates
        if t >= 0.0 and regionExp_text_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_text_9.tStart = t  # underestimates by a little under one frame
            regionExp_text_9.frameNStart = frameN  # exact frame index
            regionExp_text_9.setAutoDraw(True)
        
        # *regionExp_response_9* updates
        if t >= 0.0 and regionExp_response_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_response_9.tStart = t  # underestimates by a little under one frame
            regionExp_response_9.frameNStart = frameN  # exact frame index
            regionExp_response_9.status = STARTED
            # keyboard checking is just starting
            regionExp_response_9.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionExp_response_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionExp_response_9.keys = theseKeys[-1]  # just the last key pressed
                regionExp_response_9.rt = regionExp_response_9.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region9_ExpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region9_Exp"-------
    for thisComponent in region9_ExpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionExp_response_9.keys in ['', [], None]:  # No response was made
       regionExp_response_9.keys=None
    # store data for trials_exp (TrialHandler)
    trials_exp.addData('regionExp_response_9.keys',regionExp_response_9.keys)
    if regionExp_response_9.keys != None:  # we had a response
        trials_exp.addData('regionExp_response_9.rt', regionExp_response_9.rt)
    # the Routine "region9_Exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region10_Exp"-------
    t = 0
    region10_ExpClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionExp_text_10.setText(region10)
    regionExp_response_10 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionExp_response_10.status = NOT_STARTED
    # keep track of which components have finished
    region10_ExpComponents = []
    region10_ExpComponents.append(regionExp_text_10)
    region10_ExpComponents.append(regionExp_response_10)
    for thisComponent in region10_ExpComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "region10_Exp"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = region10_ExpClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *regionExp_text_10* updates
        if t >= 0.0 and regionExp_text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_text_10.tStart = t  # underestimates by a little under one frame
            regionExp_text_10.frameNStart = frameN  # exact frame index
            regionExp_text_10.setAutoDraw(True)
        
        # *regionExp_response_10* updates
        if t >= 0.0 and regionExp_response_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            regionExp_response_10.tStart = t  # underestimates by a little under one frame
            regionExp_response_10.frameNStart = frameN  # exact frame index
            regionExp_response_10.status = STARTED
            # keyboard checking is just starting
            regionExp_response_10.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if regionExp_response_10.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                regionExp_response_10.keys = theseKeys[-1]  # just the last key pressed
                regionExp_response_10.rt = regionExp_response_10.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in region10_ExpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "region10_Exp"-------
    for thisComponent in region10_ExpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if regionExp_response_10.keys in ['', [], None]:  # No response was made
       regionExp_response_10.keys=None
    # store data for trials_exp (TrialHandler)
    trials_exp.addData('regionExp_response_10.keys',regionExp_response_10.keys)
    if regionExp_response_10.keys != None:  # we had a response
        trials_exp.addData('regionExp_response_10.rt', regionExp_response_10.rt)
    # the Routine "region10_Exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region11_Exp"-------
    t = 0
    region11_ExpClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    regionExp_text_11.setText(region11)
    regionExp_response_11 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    regionExp_response_11.status = NOT_STARTED
    # keep track of which components have finished
    region11_ExpComponents = []
    region11_ExpComponents.append(regionExp_text_11)
    region11_ExpComponents.append(regionExp_response_11)
    for thisComponent in region11_ExpComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------uneven number of cells in excel----------------

    if region11 == "xyz":

        #------Prepare to start Routine "response_Exp"-------
        t = 0
        response_ExpClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        phraseExp_text_1.setText(phrase1)
        phraseExp_text_2.setText(phrase2)
        picExp_text_1.setImage(pic1)
        picExp_text_2.setImage(pic2)
        Q_Exp_text_1.setText(question)
        Q_Exp_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
        Q_Exp_response.status = NOT_STARTED
        # keep track of which components have finished
        response_ExpComponents = []
        response_ExpComponents.append(phraseExp_text_1)
        response_ExpComponents.append(phraseExp_text_2)
        response_ExpComponents.append(picExp_text_1)
        response_ExpComponents.append(picExp_text_2)
        response_ExpComponents.append(Q_Exp_text_1)
        response_ExpComponents.append(Q_Exp_response)
        for thisComponent in response_ExpComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "response_Exp"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = response_ExpClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *phraseExp_text_1* updates
            if t >= 0.0 and phraseExp_text_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                phraseExp_text_1.tStart = t  # underestimates by a little under one frame
                phraseExp_text_1.frameNStart = frameN  # exact frame index
                phraseExp_text_1.setAutoDraw(True)
            
            # *phraseExp_text_2* updates
            if t >= 0.0 and phraseExp_text_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                phraseExp_text_2.tStart = t  # underestimates by a little under one frame
                phraseExp_text_2.frameNStart = frameN  # exact frame index
                phraseExp_text_2.setAutoDraw(True)
            
            # *picExp_text_1* updates
            if t >= 0.0 and picExp_text_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                picExp_text_1.tStart = t  # underestimates by a little under one frame
                picExp_text_1.frameNStart = frameN  # exact frame index
                picExp_text_1.setAutoDraw(True)
            
            # *picExp_text_2* updates
            if t >= 0.0 and picExp_text_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                picExp_text_2.tStart = t  # underestimates by a little under one frame
                picExp_text_2.frameNStart = frameN  # exact frame index
                picExp_text_2.setAutoDraw(True)
            
            # *Q_Exp_text_1* updates
            if t >= 0.0 and Q_Exp_text_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                Q_Exp_text_1.tStart = t  # underestimates by a little under one frame
                Q_Exp_text_1.frameNStart = frameN  # exact frame index
                Q_Exp_text_1.setAutoDraw(True)
            
            # *Q_Exp_response* updates
            if t >= 0.0 and Q_Exp_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                Q_Exp_response.tStart = t  # underestimates by a little under one frame
                Q_Exp_response.frameNStart = frameN  # exact frame index
                Q_Exp_response.status = STARTED
                # keyboard checking is just starting
                Q_Exp_response.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if Q_Exp_response.status == STARTED:
                theseKeys = event.getKeys(keyList=['y', 'n'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Q_Exp_response.keys = theseKeys[-1]  # just the last key pressed
                    Q_Exp_response.rt = Q_Exp_response.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in response_ExpComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "response_Exp"-------
        for thisComponent in response_ExpComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Q_Exp_response.keys in ['', [], None]:  # No response was made
           Q_Exp_response.keys=None
        # store data for trials_exp (TrialHandler)
        trials_exp.addData('Q_Exp_response.keys',Q_Exp_response.keys)
        if Q_Exp_response.keys != None:  # we had a response
            trials_exp.addData('Q_Exp_response.rt', Q_Exp_response.rt)
        # the Routine "response_Exp" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

    else:

        #-------Start Routine "region11_Exp"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = region11_ExpClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *regionExp_text_11* updates
            if t >= 0.0 and regionExp_text_11.status == NOT_STARTED:
                # keep track of start time/frame for later
                regionExp_text_11.tStart = t  # underestimates by a little under one frame
                regionExp_text_11.frameNStart = frameN  # exact frame index
                regionExp_text_11.setAutoDraw(True)
            
            # *regionExp_response_11* updates
            if t >= 0.0 and regionExp_response_11.status == NOT_STARTED:
                # keep track of start time/frame for later
                regionExp_response_11.tStart = t  # underestimates by a little under one frame
                regionExp_response_11.frameNStart = frameN  # exact frame index
                regionExp_response_11.status = STARTED
                # keyboard checking is just starting
                regionExp_response_11.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if regionExp_response_11.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    regionExp_response_11.keys = theseKeys[-1]  # just the last key pressed
                    regionExp_response_11.rt = regionExp_response_11.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in region11_ExpComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "region11_Exp"-------
        for thisComponent in region11_ExpComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if regionExp_response_11.keys in ['', [], None]:  # No response was made
           regionExp_response_11.keys=None
        # store data for trials_exp (TrialHandler)
        trials_exp.addData('regionExp_response_11.keys',regionExp_response_11.keys)
        if regionExp_response_11.keys != None:  # we had a response
            trials_exp.addData('regionExp_response_11.rt', regionExp_response_11.rt)
        # the Routine "region11_Exp" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        #------Prepare to start Routine "region12_Exp"-------
        t = 0
        region12_ExpClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        regionExp_text_12.setText(region12)
        regionExp_response_12 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        regionExp_response_12.status = NOT_STARTED
        # keep track of which components have finished
        region12_ExpComponents = []
        region12_ExpComponents.append(regionExp_text_12)
        region12_ExpComponents.append(regionExp_response_12)
        for thisComponent in region12_ExpComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "region12_Exp"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = region12_ExpClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *regionExp_text_12* updates
            if t >= 0.0 and regionExp_text_12.status == NOT_STARTED:
                # keep track of start time/frame for later
                regionExp_text_12.tStart = t  # underestimates by a little under one frame
                regionExp_text_12.frameNStart = frameN  # exact frame index
                regionExp_text_12.setAutoDraw(True)
            
            # *regionExp_response_12* updates
            if t >= 0.0 and regionExp_response_12.status == NOT_STARTED:
                # keep track of start time/frame for later
                regionExp_response_12.tStart = t  # underestimates by a little under one frame
                regionExp_response_12.frameNStart = frameN  # exact frame index
                regionExp_response_12.status = STARTED
                # keyboard checking is just starting
                regionExp_response_12.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if regionExp_response_12.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    regionExp_response_12.keys = theseKeys[-1]  # just the last key pressed
                    regionExp_response_12.rt = regionExp_response_12.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in region12_ExpComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "region12_Exp"-------
        for thisComponent in region12_ExpComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if regionExp_response_12.keys in ['', [], None]:  # No response was made
           regionExp_response_12.keys=None
        # store data for trials_exp (TrialHandler)
        trials_exp.addData('regionExp_response_12.keys',regionExp_response_12.keys)
        if regionExp_response_12.keys != None:  # we had a response
            trials_exp.addData('regionExp_response_12.rt', regionExp_response_12.rt)
        # the Routine "region12_Exp" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    
    #------Prepare to start Routine "response_Exp"-------
    t = 0
    response_ExpClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    phraseExp_text_1.setText(phrase1)
    phraseExp_text_2.setText(phrase2)
    picExp_text_1.setImage(pic1)
    picExp_text_2.setImage(pic2)
    Q_Exp_text_1.setText(question)
    Q_Exp_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Q_Exp_response.status = NOT_STARTED
    # keep track of which components have finished
    response_ExpComponents = []
    response_ExpComponents.append(phraseExp_text_1)
    response_ExpComponents.append(phraseExp_text_2)
    response_ExpComponents.append(picExp_text_1)
    response_ExpComponents.append(picExp_text_2)
    response_ExpComponents.append(Q_Exp_text_1)
    response_ExpComponents.append(Q_Exp_response)
    for thisComponent in response_ExpComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "response_Exp"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = response_ExpClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *phraseExp_text_1* updates
        if t >= 0.0 and phraseExp_text_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            phraseExp_text_1.tStart = t  # underestimates by a little under one frame
            phraseExp_text_1.frameNStart = frameN  # exact frame index
            phraseExp_text_1.setAutoDraw(True)
        
        # *phraseExp_text_2* updates
        if t >= 0.0 and phraseExp_text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            phraseExp_text_2.tStart = t  # underestimates by a little under one frame
            phraseExp_text_2.frameNStart = frameN  # exact frame index
            phraseExp_text_2.setAutoDraw(True)
        
        # *picExp_text_1* updates
        if t >= 0.0 and picExp_text_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            picExp_text_1.tStart = t  # underestimates by a little under one frame
            picExp_text_1.frameNStart = frameN  # exact frame index
            picExp_text_1.setAutoDraw(True)
        
        # *picExp_text_2* updates
        if t >= 0.0 and picExp_text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            picExp_text_2.tStart = t  # underestimates by a little under one frame
            picExp_text_2.frameNStart = frameN  # exact frame index
            picExp_text_2.setAutoDraw(True)
        
        # *Q_Exp_text_1* updates
        if t >= 0.0 and Q_Exp_text_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Q_Exp_text_1.tStart = t  # underestimates by a little under one frame
            Q_Exp_text_1.frameNStart = frameN  # exact frame index
            Q_Exp_text_1.setAutoDraw(True)
        
        # *Q_Exp_response* updates
        if t >= 0.0 and Q_Exp_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            Q_Exp_response.tStart = t  # underestimates by a little under one frame
            Q_Exp_response.frameNStart = frameN  # exact frame index
            Q_Exp_response.status = STARTED
            # keyboard checking is just starting
            Q_Exp_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Q_Exp_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Q_Exp_response.keys = theseKeys[-1]  # just the last key pressed
                Q_Exp_response.rt = Q_Exp_response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in response_ExpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "response_Exp"-------
    for thisComponent in response_ExpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Q_Exp_response.keys in ['', [], None]:  # No response was made
       Q_Exp_response.keys=None
    # store data for trials_exp (TrialHandler)
    trials_exp.addData('Q_Exp_response.keys',Q_Exp_response.keys)
    if Q_Exp_response.keys != None:  # we had a response
        trials_exp.addData('Q_Exp_response.rt', Q_Exp_response.rt)
    # the Routine "response_Exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_exp'


#------Prepare to start Routine "ExpEnd"-------
t = 0
ExpEndClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
ExpEnd_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
ExpEnd_response.status = NOT_STARTED
# keep track of which components have finished
ExpEndComponents = []
ExpEndComponents.append(ExpEnd_text)
ExpEndComponents.append(ExpEnd_response)
for thisComponent in ExpEndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "ExpEnd"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = ExpEndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ExpEnd_text* updates
    if t >= 0.0 and ExpEnd_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        ExpEnd_text.tStart = t  # underestimates by a little under one frame
        ExpEnd_text.frameNStart = frameN  # exact frame index
        ExpEnd_text.setAutoDraw(True)
    
    # *ExpEnd_response* updates
    if t >= 0.0 and ExpEnd_response.status == NOT_STARTED:
        # keep track of start time/frame for later
        ExpEnd_response.tStart = t  # underestimates by a little under one frame
        ExpEnd_response.frameNStart = frameN  # exact frame index
        ExpEnd_response.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if ExpEnd_response.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExpEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "ExpEnd"-------
for thisComponent in ExpEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "ExpEnd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
win.close()
core.quit()
