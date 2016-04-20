#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Mon Apr  4 17:31:45 2016
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
expName = 'ENG'  # from the Builder filename that created this script
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
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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
    text="Welcome to the experiment. You'll be reading some sentences on the computer screen. You will first see a fixation mark at the center of the screen like this:\n\n\n",    font='Arial',
    pos=[0, 0.2], height=0.085, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='+',    font='Arial',
    pos=[0, 0], height=0.085, wrapWidth=0.1,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='When you press the space bar, the fixation mark disappears and the first word appears. With every press of the space bar, a new word or a group of words will appear and replace the previous word(s).\n\nNow press the space bar to continue.',    font='Arial',
    pos=[0, -0.4], height=0.085, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "instru2"
instru2Clock = core.Clock()
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='When you finish reading the last word of the sentence, press the space bar again. A pair of pictures will appear and you will also see a question about whether the pair of pictures matches the sentence you just read. \n\nTo answer the question, press the "Y" key for YES or the "N" key for NO. Try to answer as quickly and accurately as possible. If you are unsure of the answer, try to pick the better answer.\n\nNow press the space bar to continue.',    font='Arial',
    pos=[0, 0], height=0.085, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instru3"
instru3Clock = core.Clock()
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text='To be able to read and answer quickly, you should keep your fingers resting on the space bar and the "Y" and "N" keys. Try to read as naturally as possible, and make sure that you understand what you read.\n\nYou can take breaks as you need them, but please only do so before you\'ve started reading a new sentence, i.e., only take breaks when the screen shows the fixation mark "+".\n\nWhen the experiment is over, a "thank-you" screen will appear. At that point, you should let the experimenter know you are finished.\n\nNow press the space bar to continue.',    font='Arial',
    pos=[0, 0], height=0.085, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instru4"
instru4Clock = core.Clock()
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text='That\'s all there is to it.  Just to review...\n1. You will read a sentence by pressing the space bar, followed by a pair of pictures from left to right describing the two events in the sentence. \n2. You will encounter one of these situations:\n(a) The events in the sentence match pictures, i.e. the left picture describes the first event; the right picture describes the second event. You should press "Y".\n(b) The event in the left picture doesn\'t match the first event in the sentence. You should press "N". \n(c) The event in the right picture doesn\'t match the second event in the sentence. You should press "N". \nRemember, either the left or the right picture could be a mismatch.\n3. You will be asked whether the pair of pictures matches the sentence. \n\nNow press the space bar to continue.',    font='Arial',
    pos=[0, 0], height=0.075, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "fixation0"
fixation0Clock = core.Clock()
fixation_illustrationS = visual.TextStim(win=win, ori=0, name='fixation_illustrationS',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "illustration"
illustrationClock = core.Clock()
illustrationS_text = visual.TextStim(win=win, ori=0, name='illustrationS_text',
    text='default text',    font=u'Arial',
    pos=[0, 0.65], height=0.085, wrapWidth=None,
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
    pos=[0, -0.6], height=0.085, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0)

# Initialize components for Routine "feedback_2"
feedback_2Clock = core.Clock()
illustrationS_feedback = visual.TextStim(win=win, ori=0, name='illustrationS_feedback',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.085, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
illustrationS_pressToContinue_text = visual.TextStim(win=win, ori=0, name='illustrationS_pressToContinue_text',
    text='default text',    font=u'Arial',
    pos=[-0.085, -0.3], height=0.085, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "instru5"
instru5Clock = core.Clock()
instru_5_text = visual.TextStim(win=win, ori=0, name='instru_5_text',
    text=u'Again, keep in mind that either the left or the right picture can be a mismatch with the sentence. \n\nNow press the space bar to continue.',    font=u'Arial',
    pos=[0, 0], height=0.085, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instru6"
instru6Clock = core.Clock()
instru_6_text = visual.TextStim(win=win, ori=0, name='instru_6_text',
    text=u'But in the actual experiment, you will read the sentences in word/phrase chunks by pressing the space bar.\n\nHere are the examples you just saw as they would appear in the experiment.\n\nNow press the space bar to continue.',    font=u'Arial',
    pos=[0, 0], height=0.085, wrapWidth=None,
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
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region3"
region3Clock = core.Clock()
regionSP_text_3 = visual.TextStim(win=win, ori=0, name='regionSP_text_3',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region4"
region4Clock = core.Clock()
regionSP_text_4 = visual.TextStim(win=win, ori=0, name='regionSP_text_4',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "region5"
region5Clock = core.Clock()
regionSP_text_5 = visual.TextStim(win=win, ori=0, name='regionSP_text_5',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
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
    text='default text',    font='Arial',
    pos=[0, -0.6], height=0.085, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "feedback_SP"
feedback_SPClock = core.Clock()
feedback_SP_text = visual.TextStim(win=win, ori=0, name='feedback_SP_text',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.085, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
textSP_pressToContinue = visual.TextStim(win=win, ori=0, name='textSP_pressToContinue',
    text='default text',    font=u'Arial',
    pos=[-0.085, -0.3], height=0.085, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "instru_prac"
instru_pracClock = core.Clock()
instruction_Prac = visual.TextStim(win=win, ori=0, name='instruction_Prac',
    text='If you understand the task and there is no question, you will do a short practice run.\n\nIt will be just like the main experiment, except that feedback will be provided after each trial.\n\nNow press the space bar to continue.',    font='Arial',
    pos=[0, 0], height=0.085, wrapWidth=None,
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
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
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
    pos=[0, -0.6], height=0.085, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "feedback_prac"
feedback_pracClock = core.Clock()
feedback_prac_text = visual.TextStim(win=win, ori=0, name='feedback_prac_text',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.085, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
feedback_prac_pressToContinue = visual.TextStim(win=win, ori=0, name='feedback_prac_pressToContinue',
    text='default text',    font=u'Arial',
    pos=[-0.085, -0.3], height=0.085, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "pracEnd"
pracEndClock = core.Clock()
text_16 = visual.TextStim(win=win, ori=0, name='text_16',
    text="That's it for the practice.\n\nIf you have any questions, ask the experimenter now. Otherwise, you may begin the experiment.\n\nNow press the space bar to continue.",    font='Arial',
    pos=[0, 0], height=0.085, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "ExpBegin"
ExpBeginClock = core.Clock()
text_17 = visual.TextStim(win=win, ori=0, name='text_17',
    text='Here we go...',    font='Arial',
    pos=[0, 0], height=0.085, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
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
    pos=[0, -0.6], height=0.085, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "ExpEnd"
ExpEndClock = core.Clock()
End_text = visual.TextStim(win=win, ori=0, name='End_text',
    text=u"That's all for the experiment. \n\nThank you for participating!",    font=u'Arial',
    pos=[0, 0], height=0.085, wrapWidth=None,
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
    fixation_illustrationS.setText(u'+')
    fixation_illustrationS_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    fixation_illustrationS_response.status = NOT_STARTED
    # keep track of which components have finished
    fixation0Components = []
    fixation0Components.append(fixation_illustrationS)
    fixation0Components.append(fixation_illustrationS_response)
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
        
        # *fixation_illustrationS* updates
        if t >= 0.0 and fixation_illustrationS.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_illustrationS.tStart = t  # underestimates by a little under one frame
            fixation_illustrationS.frameNStart = frameN  # exact frame index
            fixation_illustrationS.setAutoDraw(True)
        
        # *fixation_illustrationS_response* updates
        if t >= 0.0 and fixation_illustrationS_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_illustrationS_response.tStart = t  # underestimates by a little under one frame
            fixation_illustrationS_response.frameNStart = frameN  # exact frame index
            fixation_illustrationS_response.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if fixation_illustrationS_response.status == STARTED:
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
    illustrationS_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    illustrationS_response.status = NOT_STARTED
    # keep track of which components have finished
    illustrationComponents = []
    illustrationComponents.append(illustrationS_text)
    illustrationComponents.append(illustrationS_phrase_1)
    illustrationComponents.append(illustrationS_phrase_2)
    illustrationComponents.append(illustrationS_pic_1)
    illustrationComponents.append(illustrationS_pic_2)
    illustrationComponents.append(illustrationS_question_text)
    illustrationComponents.append(illustrationS_response)
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
        
        # *illustrationS_response* updates
        if t >= 0.0 and illustrationS_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationS_response.tStart = t  # underestimates by a little under one frame
            illustrationS_response.frameNStart = frameN  # exact frame index
            illustrationS_response.status = STARTED
            # keyboard checking is just starting
            illustrationS_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if illustrationS_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                illustrationS_response.keys = theseKeys[-1]  # just the last key pressed
                illustrationS_response.rt = illustrationS_response.clock.getTime()
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
    if illustrationS_response.keys in ['', [], None]:  # No response was made
       illustrationS_response.keys=None
    # store data for illustrationSentence (TrialHandler)
    illustrationSentence.addData('illustrationS_response.keys',illustrationS_response.keys)
    if illustrationS_response.keys != None:  # we had a response
        illustrationSentence.addData('illustrationS_response.rt', illustrationS_response.rt)
    # the Routine "illustration" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "feedback_2"-------
    t = 0
    feedback_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    illustrationS_feedback.setText(feedback)
    illustrationS_pressToContinue_text.setText(u'Now press the space bar to continue.')
    illustrationS_pressToContinue_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    illustrationS_pressToContinue_response.status = NOT_STARTED
    # keep track of which components have finished
    feedback_2Components = []
    feedback_2Components.append(illustrationS_feedback)
    feedback_2Components.append(illustrationS_pressToContinue_text)
    feedback_2Components.append(illustrationS_pressToContinue_response)
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
        
        # *illustrationS_feedback* updates
        if t >= 0.0 and illustrationS_feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationS_feedback.tStart = t  # underestimates by a little under one frame
            illustrationS_feedback.frameNStart = frameN  # exact frame index
            illustrationS_feedback.setAutoDraw(True)
        
        # *illustrationS_pressToContinue_text* updates
        if t >= 0.0 and illustrationS_pressToContinue_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationS_pressToContinue_text.tStart = t  # underestimates by a little under one frame
            illustrationS_pressToContinue_text.frameNStart = frameN  # exact frame index
            illustrationS_pressToContinue_text.setAutoDraw(True)
        
        # *illustrationS_pressToContinue_response* updates
        if t >= 0.0 and illustrationS_pressToContinue_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationS_pressToContinue_response.tStart = t  # underestimates by a little under one frame
            illustrationS_pressToContinue_response.frameNStart = frameN  # exact frame index
            illustrationS_pressToContinue_response.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if illustrationS_pressToContinue_response.status == STARTED:
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
    illustrationSP_fixation_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    illustrationSP_fixation_response.status = NOT_STARTED
    # keep track of which components have finished
    fixation1Components = []
    fixation1Components.append(illustrationSP_fixation)
    fixation1Components.append(illustrationSP_fixation_response)
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
        
        # *illustrationSP_fixation_response* updates
        if t >= 0.0 and illustrationSP_fixation_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            illustrationSP_fixation_response.tStart = t  # underestimates by a little under one frame
            illustrationSP_fixation_response.frameNStart = frameN  # exact frame index
            illustrationSP_fixation_response.status = STARTED
            # keyboard checking is just starting
            illustrationSP_fixation_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if illustrationSP_fixation_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                illustrationSP_fixation_response.keys = theseKeys[-1]  # just the last key pressed
                illustrationSP_fixation_response.rt = illustrationSP_fixation_response.clock.getTime()
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
    if illustrationSP_fixation_response.keys in ['', [], None]:  # No response was made
       illustrationSP_fixation_response.keys=None
    # store data for illustration_SP (TrialHandler)
    illustration_SP.addData('illustrationSP_fixation_response.keys',illustrationSP_fixation_response.keys)
    if illustrationSP_fixation_response.keys != None:  # we had a response
        illustration_SP.addData('illustrationSP_fixation_response.rt', illustrationSP_fixation_response.rt)
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

    #-------uneven number of cells------

    if region10 == "xyz":

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
        responseSP = event.BuilderKeyResponse()  # create an object of type KeyResponse
        responseSP.status = NOT_STARTED
        # keep track of which components have finished
        response1Components = []
        response1Components.append(phraseSP_text_1)
        response1Components.append(phraseSP_text_2)
        response1Components.append(picSP_1)
        response1Components.append(picSP_2)
        response1Components.append(Q_SP)
        response1Components.append(responseSP)
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
            
            # *responseSP* updates
            if t >= 0.0 and responseSP.status == NOT_STARTED:
                # keep track of start time/frame for later
                responseSP.tStart = t  # underestimates by a little under one frame
                responseSP.frameNStart = frameN  # exact frame index
                responseSP.status = STARTED
                # keyboard checking is just starting
                responseSP.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if responseSP.status == STARTED:
                theseKeys = event.getKeys(keyList=['y', 'n'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    responseSP.keys = theseKeys[-1]  # just the last key pressed
                    responseSP.rt = responseSP.clock.getTime()
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
        if responseSP.keys in ['', [], None]:  # No response was made
           responseSP.keys=None
        # store data for illustration_SP (TrialHandler)
        illustration_SP.addData('responseSP.keys',responseSP.keys)
        if responseSP.keys != None:  # we had a response
            illustration_SP.addData('responseSP.rt', responseSP.rt)
        # the Routine "response1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

    else:
    
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
        # store data for illustration_SP (TrialHandler)
        illustration_SP.addData('regionSP_response_10.keys',regionSP_response_10.keys)
        if regionSP_response_10.keys != None:  # we had a response
            illustration_SP.addData('regionSP_response_10.rt', regionSP_response_10.rt)
        # the Routine "region10" was not non-slip safe, so reset the non-slip timer
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
    responseSP = event.BuilderKeyResponse()  # create an object of type KeyResponse
    responseSP.status = NOT_STARTED
    # keep track of which components have finished
    response1Components = []
    response1Components.append(phraseSP_text_1)
    response1Components.append(phraseSP_text_2)
    response1Components.append(picSP_1)
    response1Components.append(picSP_2)
    response1Components.append(Q_SP)
    response1Components.append(responseSP)
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
        
        # *responseSP* updates
        if t >= 0.0 and responseSP.status == NOT_STARTED:
            # keep track of start time/frame for later
            responseSP.tStart = t  # underestimates by a little under one frame
            responseSP.frameNStart = frameN  # exact frame index
            responseSP.status = STARTED
            # keyboard checking is just starting
            responseSP.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if responseSP.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                responseSP.keys = theseKeys[-1]  # just the last key pressed
                responseSP.rt = responseSP.clock.getTime()
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
    if responseSP.keys in ['', [], None]:  # No response was made
       responseSP.keys=None
    # store data for illustration_SP (TrialHandler)
    illustration_SP.addData('responseSP.keys',responseSP.keys)
    if responseSP.keys != None:  # we had a response
        illustration_SP.addData('responseSP.rt', responseSP.rt)
    # the Routine "response1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "feedback_SP"-------
    t = 0
    feedback_SPClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    feedback_SP_text.setText(feedback)
    textSP_pressToContinue.setText(u'Now press the space bar to continue.')
    feedback_SP_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    feedback_SP_response.status = NOT_STARTED
    # keep track of which components have finished
    feedback_SPComponents = []
    feedback_SPComponents.append(feedback_SP_text)
    feedback_SPComponents.append(textSP_pressToContinue)
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
        
        # *textSP_pressToContinue* updates
        if t >= 0.0 and textSP_pressToContinue.status == NOT_STARTED:
            # keep track of start time/frame for later
            textSP_pressToContinue.tStart = t  # underestimates by a little under one frame
            textSP_pressToContinue.frameNStart = frameN  # exact frame index
            textSP_pressToContinue.setAutoDraw(True)
        
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
instruction_Prac_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
instruction_Prac_response.status = NOT_STARTED
# keep track of which components have finished
instru_pracComponents = []
instru_pracComponents.append(instruction_Prac)
instru_pracComponents.append(instruction_Prac_response)
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
    
    # *instruction_Prac_response* updates
    if t >= 0.0 and instruction_Prac_response.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruction_Prac_response.tStart = t  # underestimates by a little under one frame
        instruction_Prac_response.frameNStart = frameN  # exact frame index
        instruction_Prac_response.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if instruction_Prac_response.status == STARTED:
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
    trialList=data.importConditions('prac1_ENG.xlsx'),
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
    region_prac_1_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_prac_1_response.status = NOT_STARTED
    # keep track of which components have finished
    region1_2Components = []
    region1_2Components.append(region_prac_1)
    region1_2Components.append(region_prac_1_response)
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
        
        # *region_prac_1_response* updates
        if t >= 0.0 and region_prac_1_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_1_response.tStart = t  # underestimates by a little under one frame
            region_prac_1_response.frameNStart = frameN  # exact frame index
            region_prac_1_response.status = STARTED
            # keyboard checking is just starting
            region_prac_1_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_prac_1_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_prac_1_response.keys = theseKeys[-1]  # just the last key pressed
                region_prac_1_response.rt = region_prac_1_response.clock.getTime()
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
    if region_prac_1_response.keys in ['', [], None]:  # No response was made
       region_prac_1_response.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_prac_1_response.keys',region_prac_1_response.keys)
    if region_prac_1_response.keys != None:  # we had a response
        trials_prac.addData('region_prac_1_response.rt', region_prac_1_response.rt)
    # the Routine "region1_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region2_2"-------
    t = 0
    region2_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_2.setText(region2)
    region_prac_2_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_prac_2_response.status = NOT_STARTED
    # keep track of which components have finished
    region2_2Components = []
    region2_2Components.append(region_prac_2)
    region2_2Components.append(region_prac_2_response)
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
        
        # *region_prac_2_response* updates
        if t >= 0.0 and region_prac_2_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_2_response.tStart = t  # underestimates by a little under one frame
            region_prac_2_response.frameNStart = frameN  # exact frame index
            region_prac_2_response.status = STARTED
            # keyboard checking is just starting
            region_prac_2_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_prac_2_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_prac_2_response.keys = theseKeys[-1]  # just the last key pressed
                region_prac_2_response.rt = region_prac_2_response.clock.getTime()
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
    if region_prac_2_response.keys in ['', [], None]:  # No response was made
       region_prac_2_response.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_prac_2_response.keys',region_prac_2_response.keys)
    if region_prac_2_response.keys != None:  # we had a response
        trials_prac.addData('region_prac_2_response.rt', region_prac_2_response.rt)
    # the Routine "region2_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region3_2"-------
    t = 0
    region3_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_3.setText(region3)
    region_prac_3_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_prac_3_response.status = NOT_STARTED
    # keep track of which components have finished
    region3_2Components = []
    region3_2Components.append(region_prac_3)
    region3_2Components.append(region_prac_3_response)
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
        
        # *region_prac_3_response* updates
        if t >= 0.0 and region_prac_3_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_3_response.tStart = t  # underestimates by a little under one frame
            region_prac_3_response.frameNStart = frameN  # exact frame index
            region_prac_3_response.status = STARTED
            # keyboard checking is just starting
            region_prac_3_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_prac_3_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_prac_3_response.keys = theseKeys[-1]  # just the last key pressed
                region_prac_3_response.rt = region_prac_3_response.clock.getTime()
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
    if region_prac_3_response.keys in ['', [], None]:  # No response was made
       region_prac_3_response.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_prac_3_response.keys',region_prac_3_response.keys)
    if region_prac_3_response.keys != None:  # we had a response
        trials_prac.addData('region_prac_3_response.rt', region_prac_3_response.rt)
    # the Routine "region3_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region4_2"-------
    t = 0
    region4_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_4.setText(region4)
    region_prac_4_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_prac_4_response.status = NOT_STARTED
    # keep track of which components have finished
    region4_2Components = []
    region4_2Components.append(region_prac_4)
    region4_2Components.append(region_prac_4_response)
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
        
        # *region_prac_4_response* updates
        if t >= 0.0 and region_prac_4_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_4_response.tStart = t  # underestimates by a little under one frame
            region_prac_4_response.frameNStart = frameN  # exact frame index
            region_prac_4_response.status = STARTED
            # keyboard checking is just starting
            region_prac_4_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_prac_4_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_prac_4_response.keys = theseKeys[-1]  # just the last key pressed
                region_prac_4_response.rt = region_prac_4_response.clock.getTime()
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
    if region_prac_4_response.keys in ['', [], None]:  # No response was made
       region_prac_4_response.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_prac_4_response.keys',region_prac_4_response.keys)
    if region_prac_4_response.keys != None:  # we had a response
        trials_prac.addData('region_prac_4_response.rt', region_prac_4_response.rt)
    # the Routine "region4_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region5_2"-------
    t = 0
    region5_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_5.setText(region5)
    region_prac_5_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_prac_5_response.status = NOT_STARTED
    # keep track of which components have finished
    region5_2Components = []
    region5_2Components.append(region_prac_5)
    region5_2Components.append(region_prac_5_response)
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
        
        # *region_prac_5_response* updates
        if t >= 0.0 and region_prac_5_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_5_response.tStart = t  # underestimates by a little under one frame
            region_prac_5_response.frameNStart = frameN  # exact frame index
            region_prac_5_response.status = STARTED
            # keyboard checking is just starting
            region_prac_5_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_prac_5_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_prac_5_response.keys = theseKeys[-1]  # just the last key pressed
                region_prac_5_response.rt = region_prac_5_response.clock.getTime()
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
    if region_prac_5_response.keys in ['', [], None]:  # No response was made
       region_prac_5_response.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_prac_5_response.keys',region_prac_5_response.keys)
    if region_prac_5_response.keys != None:  # we had a response
        trials_prac.addData('region_prac_5_response.rt', region_prac_5_response.rt)
    # the Routine "region5_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region6_2"-------
    t = 0
    region6_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_6.setText(region6)
    region_prac_6_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_prac_6_response.status = NOT_STARTED
    # keep track of which components have finished
    region6_2Components = []
    region6_2Components.append(region_prac_6)
    region6_2Components.append(region_prac_6_response)
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
        
        # *region_prac_6_response* updates
        if t >= 0.0 and region_prac_6_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_6_response.tStart = t  # underestimates by a little under one frame
            region_prac_6_response.frameNStart = frameN  # exact frame index
            region_prac_6_response.status = STARTED
            # keyboard checking is just starting
            region_prac_6_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_prac_6_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_prac_6_response.keys = theseKeys[-1]  # just the last key pressed
                region_prac_6_response.rt = region_prac_6_response.clock.getTime()
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
    if region_prac_6_response.keys in ['', [], None]:  # No response was made
       region_prac_6_response.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_prac_6_response.keys',region_prac_6_response.keys)
    if region_prac_6_response.keys != None:  # we had a response
        trials_prac.addData('region_prac_6_response.rt', region_prac_6_response.rt)
    # the Routine "region6_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region7_2"-------
    t = 0
    region7_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_7.setText(region7)
    region_prac_7_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_prac_7_response.status = NOT_STARTED
    # keep track of which components have finished
    region7_2Components = []
    region7_2Components.append(region_prac_7)
    region7_2Components.append(region_prac_7_response)
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
        
        # *region_prac_7_response* updates
        if t >= 0.0 and region_prac_7_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_7_response.tStart = t  # underestimates by a little under one frame
            region_prac_7_response.frameNStart = frameN  # exact frame index
            region_prac_7_response.status = STARTED
            # keyboard checking is just starting
            region_prac_7_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_prac_7_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_prac_7_response.keys = theseKeys[-1]  # just the last key pressed
                region_prac_7_response.rt = region_prac_7_response.clock.getTime()
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
    if region_prac_7_response.keys in ['', [], None]:  # No response was made
       region_prac_7_response.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_prac_7_response.keys',region_prac_7_response.keys)
    if region_prac_7_response.keys != None:  # we had a response
        trials_prac.addData('region_prac_7_response.rt', region_prac_7_response.rt)
    # the Routine "region7_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region8_2"-------
    t = 0
    region8_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_8.setText(region8)
    region_prac_8_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_prac_8_response.status = NOT_STARTED
    # keep track of which components have finished
    region8_2Components = []
    region8_2Components.append(region_prac_8)
    region8_2Components.append(region_prac_8_response)
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
        
        # *region_prac_8_response* updates
        if t >= 0.0 and region_prac_8_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_8_response.tStart = t  # underestimates by a little under one frame
            region_prac_8_response.frameNStart = frameN  # exact frame index
            region_prac_8_response.status = STARTED
            # keyboard checking is just starting
            region_prac_8_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_prac_8_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_prac_8_response.keys = theseKeys[-1]  # just the last key pressed
                region_prac_8_response.rt = region_prac_8_response.clock.getTime()
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
    if region_prac_8_response.keys in ['', [], None]:  # No response was made
       region_prac_8_response.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_prac_8_response.keys',region_prac_8_response.keys)
    if region_prac_8_response.keys != None:  # we had a response
        trials_prac.addData('region_prac_8_response.rt', region_prac_8_response.rt)
    # the Routine "region8_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region9_2"-------
    t = 0
    region9_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_9.setText(region9)
    region_prac_9_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_prac_9_response.status = NOT_STARTED
    # keep track of which components have finished
    region9_2Components = []
    region9_2Components.append(region_prac_9)
    region9_2Components.append(region_prac_9_response)
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
        
        # *region_prac_9_response* updates
        if t >= 0.0 and region_prac_9_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            region_prac_9_response.tStart = t  # underestimates by a little under one frame
            region_prac_9_response.frameNStart = frameN  # exact frame index
            region_prac_9_response.status = STARTED
            # keyboard checking is just starting
            region_prac_9_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if region_prac_9_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                region_prac_9_response.keys = theseKeys[-1]  # just the last key pressed
                region_prac_9_response.rt = region_prac_9_response.clock.getTime()
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
    if region_prac_9_response.keys in ['', [], None]:  # No response was made
       region_prac_9_response.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('region_prac_9_response.keys',region_prac_9_response.keys)
    if region_prac_9_response.keys != None:  # we had a response
        trials_prac.addData('region_prac_9_response.rt', region_prac_9_response.rt)
    # the Routine "region9_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "region10_2"-------
    t = 0
    region10_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    region_prac_10.setText(region10)
    region_prac_10_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    region_prac_10_response.status = NOT_STARTED
    # keep track of which components have finished
    region10_2Components = []
    region10_2Components.append(region_prac_10)
    region10_2Components.append(region_prac_10_response)
    for thisComponent in region10_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------uneven number of cells------

    if region10 == "xyz":

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
        Q_prac_text_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
        Q_prac_text_response.status = NOT_STARTED
        # keep track of which components have finished
        response_PracComponents = []
        response_PracComponents.append(phrase_prac_1)
        response_PracComponents.append(phrase_prac_2)
        response_PracComponents.append(image_prac_1)
        response_PracComponents.append(image_prac_2)
        response_PracComponents.append(Q_prac_text)
        response_PracComponents.append(Q_prac_text_response)
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
            
            # *Q_prac_text_response* updates
            if t >= 0.0 and Q_prac_text_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                Q_prac_text_response.tStart = t  # underestimates by a little under one frame
                Q_prac_text_response.frameNStart = frameN  # exact frame index
                Q_prac_text_response.status = STARTED
                # keyboard checking is just starting
                Q_prac_text_response.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if Q_prac_text_response.status == STARTED:
                theseKeys = event.getKeys(keyList=['y', 'n'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Q_prac_text_response.keys = theseKeys[-1]  # just the last key pressed
                    Q_prac_text_response.rt = Q_prac_text_response.clock.getTime()
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
        if Q_prac_text_response.keys in ['', [], None]:  # No response was made
           Q_prac_text_response.keys=None
        # store data for trials_prac (TrialHandler)
        trials_prac.addData('Q_prac_text_response.keys',Q_prac_text_response.keys)
        if Q_prac_text_response.keys != None:  # we had a response
            trials_prac.addData('Q_prac_text_response.rt', Q_prac_text_response.rt)
        # the Routine "response_Prac" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

    else:
   
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
            
            # *region_prac_10_response* updates
            if t >= 0.0 and region_prac_10_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                region_prac_10_response.tStart = t  # underestimates by a little under one frame
                region_prac_10_response.frameNStart = frameN  # exact frame index
                region_prac_10_response.status = STARTED
                # keyboard checking is just starting
                region_prac_10_response.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if region_prac_10_response.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    region_prac_10_response.keys = theseKeys[-1]  # just the last key pressed
                    region_prac_10_response.rt = region_prac_10_response.clock.getTime()
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
        if region_prac_10_response.keys in ['', [], None]:  # No response was made
           region_prac_10_response.keys=None
        # store data for trials_prac (TrialHandler)
        trials_prac.addData('region_prac_10_response.keys',region_prac_10_response.keys)
        if region_prac_10_response.keys != None:  # we had a response
            trials_prac.addData('region_prac_10_response.rt', region_prac_10_response.rt)
        # the Routine "region10_2" was not non-slip safe, so reset the non-slip timer
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
    Q_prac_text_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Q_prac_text_response.status = NOT_STARTED
    # keep track of which components have finished
    response_PracComponents = []
    response_PracComponents.append(phrase_prac_1)
    response_PracComponents.append(phrase_prac_2)
    response_PracComponents.append(image_prac_1)
    response_PracComponents.append(image_prac_2)
    response_PracComponents.append(Q_prac_text)
    response_PracComponents.append(Q_prac_text_response)
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
        
        # *Q_prac_text_response* updates
        if t >= 0.0 and Q_prac_text_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            Q_prac_text_response.tStart = t  # underestimates by a little under one frame
            Q_prac_text_response.frameNStart = frameN  # exact frame index
            Q_prac_text_response.status = STARTED
            # keyboard checking is just starting
            Q_prac_text_response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Q_prac_text_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Q_prac_text_response.keys = theseKeys[-1]  # just the last key pressed
                Q_prac_text_response.rt = Q_prac_text_response.clock.getTime()
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
    if Q_prac_text_response.keys in ['', [], None]:  # No response was made
       Q_prac_text_response.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('Q_prac_text_response.keys',Q_prac_text_response.keys)
    if Q_prac_text_response.keys != None:  # we had a response
        trials_prac.addData('Q_prac_text_response.rt', Q_prac_text_response.rt)
    # the Routine "response_Prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "feedback_prac"-------
    t = 0
    feedback_pracClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    feedback_prac_text.setText(feedback)
    feedback_prac_pressToContinue.setText(u'Now press the space bar to continue.')
    key_resp_40 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_40.status = NOT_STARTED
    # keep track of which components have finished
    feedback_pracComponents = []
    feedback_pracComponents.append(feedback_prac_text)
    feedback_pracComponents.append(feedback_prac_pressToContinue)
    feedback_pracComponents.append(key_resp_40)
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
        
        # *key_resp_40* updates
        if t >= 0.0 and key_resp_40.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_40.tStart = t  # underestimates by a little under one frame
            key_resp_40.frameNStart = frameN  # exact frame index
            key_resp_40.status = STARTED
            # keyboard checking is just starting
            key_resp_40.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_40.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_40.keys = theseKeys[-1]  # just the last key pressed
                key_resp_40.rt = key_resp_40.clock.getTime()
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
    if key_resp_40.keys in ['', [], None]:  # No response was made
       key_resp_40.keys=None
    # store data for trials_prac (TrialHandler)
    trials_prac.addData('key_resp_40.keys',key_resp_40.keys)
    if key_resp_40.keys != None:  # we had a response
        trials_prac.addData('key_resp_40.rt', key_resp_40.rt)
    # the Routine "feedback_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_prac'


#------Prepare to start Routine "pracEnd"-------
t = 0
pracEndClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_42 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_42.status = NOT_STARTED
# keep track of which components have finished
pracEndComponents = []
pracEndComponents.append(text_16)
pracEndComponents.append(key_resp_42)
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
    
    # *text_16* updates
    if t >= 0.0 and text_16.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_16.tStart = t  # underestimates by a little under one frame
        text_16.frameNStart = frameN  # exact frame index
        text_16.setAutoDraw(True)
    
    # *key_resp_42* updates
    if t >= 0.0 and key_resp_42.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_42.tStart = t  # underestimates by a little under one frame
        key_resp_42.frameNStart = frameN  # exact frame index
        key_resp_42.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_42.status == STARTED:
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
key_resp_43 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_43.status = NOT_STARTED
# keep track of which components have finished
ExpBeginComponents = []
ExpBeginComponents.append(text_17)
ExpBeginComponents.append(key_resp_43)
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
    
    # *text_17* updates
    if t >= 0.0 and text_17.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_17.tStart = t  # underestimates by a little under one frame
        text_17.frameNStart = frameN  # exact frame index
        text_17.setAutoDraw(True)
    
    # *key_resp_43* updates
    if t >= 0.0 and key_resp_43.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_43.tStart = t  # underestimates by a little under one frame
        key_resp_43.frameNStart = frameN  # exact frame index
        key_resp_43.status = STARTED
        # keyboard checking is just starting
        key_resp_43.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_43.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_43.keys = theseKeys[-1]  # just the last key pressed
            key_resp_43.rt = key_resp_43.clock.getTime()
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
# check responses
if key_resp_43.keys in ['', [], None]:  # No response was made
   key_resp_43.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_43.keys',key_resp_43.keys)
if key_resp_43.keys != None:  # we had a response
    thisExp.addData('key_resp_43.rt', key_resp_43.rt)
thisExp.nextEntry()
# the Routine "ExpBegin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_exp = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('List1ENG.xlsx'),
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

    
    #-------uneven number of cells------

    if region10 == "xyz":

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
        Q_Exp_reponse_1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        Q_Exp_reponse_1.status = NOT_STARTED
        # keep track of which components have finished
        response_ExpComponents = []
        response_ExpComponents.append(phraseExp_text_1)
        response_ExpComponents.append(phraseExp_text_2)
        response_ExpComponents.append(picExp_text_1)
        response_ExpComponents.append(picExp_text_2)
        response_ExpComponents.append(Q_Exp_text_1)
        response_ExpComponents.append(Q_Exp_reponse_1)
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
            
            # *Q_Exp_reponse_1* updates
            if t >= 0.0 and Q_Exp_reponse_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                Q_Exp_reponse_1.tStart = t  # underestimates by a little under one frame
                Q_Exp_reponse_1.frameNStart = frameN  # exact frame index
                Q_Exp_reponse_1.status = STARTED
                # keyboard checking is just starting
                Q_Exp_reponse_1.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if Q_Exp_reponse_1.status == STARTED:
                theseKeys = event.getKeys(keyList=['y', 'n'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Q_Exp_reponse_1.keys = theseKeys[-1]  # just the last key pressed
                    Q_Exp_reponse_1.rt = Q_Exp_reponse_1.clock.getTime()
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
        if Q_Exp_reponse_1.keys in ['', [], None]:  # No response was made
           Q_Exp_reponse_1.keys=None
        # store data for trials_exp (TrialHandler)
        trials_exp.addData('Q_Exp_reponse_1.keys',Q_Exp_reponse_1.keys)
        if Q_Exp_reponse_1.keys != None:  # we had a response
            trials_exp.addData('Q_Exp_reponse_1.rt', Q_Exp_reponse_1.rt)
        # the Routine "response_Exp" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

    else:
    
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
    Q_Exp_reponse_1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Q_Exp_reponse_1.status = NOT_STARTED
    # keep track of which components have finished
    response_ExpComponents = []
    response_ExpComponents.append(phraseExp_text_1)
    response_ExpComponents.append(phraseExp_text_2)
    response_ExpComponents.append(picExp_text_1)
    response_ExpComponents.append(picExp_text_2)
    response_ExpComponents.append(Q_Exp_text_1)
    response_ExpComponents.append(Q_Exp_reponse_1)
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
        
        # *Q_Exp_reponse_1* updates
        if t >= 0.0 and Q_Exp_reponse_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Q_Exp_reponse_1.tStart = t  # underestimates by a little under one frame
            Q_Exp_reponse_1.frameNStart = frameN  # exact frame index
            Q_Exp_reponse_1.status = STARTED
            # keyboard checking is just starting
            Q_Exp_reponse_1.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Q_Exp_reponse_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Q_Exp_reponse_1.keys = theseKeys[-1]  # just the last key pressed
                Q_Exp_reponse_1.rt = Q_Exp_reponse_1.clock.getTime()
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
    if Q_Exp_reponse_1.keys in ['', [], None]:  # No response was made
       Q_Exp_reponse_1.keys=None
    # store data for trials_exp (TrialHandler)
    trials_exp.addData('Q_Exp_reponse_1.keys',Q_Exp_reponse_1.keys)
    if Q_Exp_reponse_1.keys != None:  # we had a response
        trials_exp.addData('Q_Exp_reponse_1.rt', Q_Exp_reponse_1.rt)
    # the Routine "response_Exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_exp'


#------Prepare to start Routine "ExpEnd"-------
t = 0
ExpEndClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
End_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
End_response.status = NOT_STARTED
# keep track of which components have finished
ExpEndComponents = []
ExpEndComponents.append(End_text)
ExpEndComponents.append(End_response)
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
    
    # *End_text* updates
    if t >= 0.0 and End_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        End_text.tStart = t  # underestimates by a little under one frame
        End_text.frameNStart = frameN  # exact frame index
        End_text.setAutoDraw(True)
    
    # *End_response* updates
    if t >= 0.0 and End_response.status == NOT_STARTED:
        # keep track of start time/frame for later
        End_response.tStart = t  # underestimates by a little under one frame
        End_response.frameNStart = frameN  # exact frame index
        End_response.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if End_response.status == STARTED:
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
