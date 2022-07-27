#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on July 26, 2022, at 11:42
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

"This psychopy2 builder file of MID is fully based on the MID eprime file from ABCD and created by Xi Yang."
"Five possible trial types: Win $.2, Win $5, Lose $.2, Lose $5, $0-no money at stake."
"The combination of the trial order (1-12) to be collected at the beginning and run number (1-2) determine the time version (1-16) to be used."
"As Casey et al., 2018 described, such combinations ensure optimized trial orders of the task (2 runs each)."
"Each run has 50 contiguous trials (10 per trial type) and lasts 5:42."
"Please refer to ABCD website or Casey et at.'s paper for complete descriptions and original eprime files."

"""
SetTrials code from eprime
TrialOrdersR1(1) = "TimeVersion5"
TrialOrdersR1(2) = "TimeVersion13"
TrialOrdersR1(3) = "TimeVersion9"
TrialOrdersR1(4) = "TimeVersion15"
TrialOrdersR1(5) = "TimeVersion6"
TrialOrdersR1(6) = "TimeVersion8"
TrialOrdersR1(7) = "TimeVersion2"
TrialOrdersR1(8) = "TimeVersion3"
TrialOrdersR1(9) = "TimeVersion10"
TrialOrdersR1(10) = "TimeVersion7"
TrialOrdersR1(11) = "TimeVersion11"
TrialOrdersR1(12) = "TimeVersion4"

TrialOrdersR2(1) = "TimeVersion16"
TrialOrdersR2(2) = "TimeVersion1"
TrialOrdersR2(3) = "TimeVersion14"
TrialOrdersR2(4) = "TimeVersion12"
TrialOrdersR2(5) = "TimeVersion5"
TrialOrdersR2(6) = "TimeVersion11"
TrialOrdersR2(7) = "TimeVersion9"
TrialOrdersR2(8) = "TimeVersion8"
TrialOrdersR2(9) = "TimeVersion2"
TrialOrdersR2(10) = "TimeVersion13"
TrialOrdersR2(11) = "TimeVersion7"
TrialOrdersR2(12) = "TimeVersion3"

toRunOne = TrialOrdersR1(numTrialOrder)
toRunTwo = TrialOrdersR2(numTrialOrder)
"""

'handedness, a means ambidextrous'
'in the ABCD version, "session" appears equivalent to "run" in a scan, such that session = 001, means run 1 and run 2 in the same scan'
'session = 002, means start from run 2. This may be used 1). when the scan needs to be cut short, so only run the second run; 2). 2nd run needs to be rerun due to some issues'
'to reduce ambiguity, ABCD "session" is changed to "run" and "visit" is added to record isolated scan visits'
from psychopy.hardware import keyboard
from psychopy import core


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = '220308_MID_ABCD_prac_version'  # from the Builder filename that created this script
expInfo = {'participant': '', 'handedness(l/r/a)': 'r', 'visit': '001/002'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'], expInfo['visit'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\OSLadmin\\Desktop\\22MoTasks\\220707MID_psychopy\\220308_MID_ABCD_prac_version_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[3440, 1440], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "TitlePage"
TitlePageClock = core.Clock()
text_TitlePage = visual.TextStim(win=win, name='text_TitlePage',
    text='MID - Practice',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_TitlePage = keyboard.Keyboard()
TheProbeDuration = 0.35

final_compensation = 0

"""
ABCD used a one-button response pad and they 
had any key as correct key press in their behavioral and practice e-prime files
in case, you want to restrict one key, 6 or 7, also based on handedness, use the script below
index_finger_key = '6'
if expInfo['handedness(l/r/a)'] == 'l':
    index_finger_key = '7'
scripts for calculating correct hit may be updated too!
"""

# Initialize components for Routine "IntroShapes"
IntroShapesClock = core.Clock()
text_IntroShapes = visual.TextStim(win=win, name='text_IntroShapes',
    text='In this game you will have the chance to win money! The game is played with three shapes.\n\nFirst, you will see all the shapes and learn what each shape means! ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_IntroShapes = keyboard.Keyboard()

# Initialize components for Routine "WinSml"
WinSmlClock = core.Clock()
image_WinSml = visual.ImageStim(
    win=win,
    name='image_WinSml', 
    image='Images/WinSmall.BMP', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_WinSml = keyboard.Keyboard()

# Initialize components for Routine "WinLrg"
WinLrgClock = core.Clock()
image_WinLrg = visual.ImageStim(
    win=win,
    name='image_WinLrg', 
    image='Images/WinBig.BMP', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_WinLrg = keyboard.Keyboard()

# Initialize components for Routine "LoseSml"
LoseSmlClock = core.Clock()
image_LoseSml = visual.ImageStim(
    win=win,
    name='image_LoseSml', 
    image='Images/LoseSmall.BMP', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_LoseSml = keyboard.Keyboard()

# Initialize components for Routine "LoseLrg"
LoseLrgClock = core.Clock()
image_LoseLrg = visual.ImageStim(
    win=win,
    name='image_LoseLrg', 
    image='Images/LoseBig.BMP', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_LoseLrg = keyboard.Keyboard()

# Initialize components for Routine "Neut"
NeutClock = core.Clock()
image_Neut = visual.ImageStim(
    win=win,
    name='image_Neut', 
    image='Images/Neutral.BMP', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_Neut = keyboard.Keyboard()

# Initialize components for Routine "ShapeFixInstruct"
ShapeFixInstructClock = core.Clock()
text_ShapeFixInstruct = visual.TextStim(win=win, name='text_ShapeFixInstruct',
    text='The first thing that will happen in the game is one of the shapes you just saw will come up. All you have to do is read the shape to see if you will win, lose, or if no money is at stake.\n\nAfter the shape you will see a plus sign. When you see the plus sign you should just wait. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_ShapeFixInstruct = keyboard.Keyboard()

# Initialize components for Routine "IntroProbes"
IntroProbesClock = core.Clock()
text_IntroProbes = visual.TextStim(win=win, name='text_IntroProbes',
    text='After the plus sign there will always be a black shape that is the same shape as the one you just saw. \nYour job is to press a button under your pointer finger when you see the black shape. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_IntroProbes = keyboard.Keyboard()

# Initialize components for Routine "Winprb"
WinprbClock = core.Clock()
image_Winprb = visual.ImageStim(
    win=win,
    name='image_Winprb', 
    image='Images/WinProbe.BMP', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_Winprb = keyboard.Keyboard()

# Initialize components for Routine "Loseprb"
LoseprbClock = core.Clock()
image_Loseprb = visual.ImageStim(
    win=win,
    name='image_Loseprb', 
    image='Images/LoseProbe.BMP', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_Loseprb = keyboard.Keyboard()

# Initialize components for Routine "Neuprob"
NeuprobClock = core.Clock()
image_Neuprb = visual.ImageStim(
    win=win,
    name='image_Neuprb', 
    image='Images/NeutralProbe.BMP', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_Neuprb = keyboard.Keyboard()

# Initialize components for Routine "Probes2"
Probes2Clock = core.Clock()
text_Probes2 = visual.TextStim(win=win, name='text_Probes2',
    text='If you press too soon or do not press when the black shape is up, you will not receive the outcome for that shape. \n\nYou are now going to practice pressing your pointer finger when you see the black shape! ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_Probes2 = keyboard.Keyboard()

# Initialize components for Routine "BlockInstruction"
BlockInstructionClock = core.Clock()
text_BlockInstruction1 = visual.TextStim(win=win, name='text_BlockInstruction1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_BlockInstruction2 = visual.TextStim(win=win, name='text_BlockInstruction2',
    text='',
    font='Open Sans',
    pos=(0, 3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_BlockInstruction = keyboard.Keyboard()

# Initialize components for Routine "prac_cue_slide"
prac_cue_slideClock = core.Clock()
key_resp_cue_slide_2 = keyboard.Keyboard()
prac_cue_image = 'Images/WinSmall.bmp'
cue_key_press = 0
image_Cue_slide_2 = visual.ImageStim(
    win=win,
    name='image_Cue_slide_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "Anticipation_slide"
Anticipation_slideClock = core.Clock()
key_resp_Anticipation_slide = keyboard.Keyboard()
text_Anticipation_slide = visual.TextStim(win=win, name='text_Anticipation_slide',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.14, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
anticipation_key_press = 0

# Initialize components for Routine "prac_probe_slide"
prac_probe_slideClock = core.Clock()
key_resp_Probe_slide_2 = keyboard.Keyboard()
probe_key_press = 0
probe_key_press_rt = 0
TrialNum = 0
nonNeutralTrialNum = 0
rt_list = []
acc_list = []
prac_probe_image = 'Images/WinProbe.bmp'
image_Probe_slide_2 = visual.ImageStim(
    win=win,
    name='image_Probe_slide_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
key_resp_feedback = keyboard.Keyboard()
feedback = ""
ResponseCheck = ""
Result= ""
updated_trial_type = ''
nonNeutralTrialOmission = 0
nonNeutralTrialOmissionPercentage = 0
TrialOmission = 0
TrialOmissionPercentage = 0
mean_rt = 0
Omission_flag = 0
text_Feedback = visual.TextStim(win=win, name='text_Feedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "PartOneEndText"
PartOneEndTextClock = core.Clock()
text_PartOneEndText = visual.TextStim(win=win, name='text_PartOneEndText',
    text='Great job!\n\nWe have one more practice round for the MID game.\n\nRemember to press your POINTER FINGER when you see the black shape appear on the screen.\n\nPress your POINTER FINGER to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_PartOneEndText = keyboard.Keyboard()

# Initialize components for Routine "BlockInstructions"
BlockInstructionsClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='Images/MID_Instructions.bmp', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.7, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_instr = keyboard.Keyboard()

# Initialize components for Routine "PrepTime"
PrepTimeClock = core.Clock()
text_PrepTime = visual.TextStim(win=win, name='text_PrepTime',
    text='Ready...',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
block_TrialNum = 0
block_nonNeutralTrialNum = 0
block_nonNeutralTrialOmission = 0
block_nonNeutralTrialOmissionPercentage = 0
block_TrialOmission = 0
block_TrialOmissionPercentage = 0

block_rt_list = []
block_mean_rt = 0

prbacc = 0
prbrt = 0

# Initialize components for Routine "Cue_slide"
Cue_slideClock = core.Clock()
key_resp_cue_slide = keyboard.Keyboard()
image_Cue_slide = visual.ImageStim(
    win=win,
    name='image_Cue_slide', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "Anticipation_slide"
Anticipation_slideClock = core.Clock()
key_resp_Anticipation_slide = keyboard.Keyboard()
text_Anticipation_slide = visual.TextStim(win=win, name='text_Anticipation_slide',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.14, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
anticipation_key_press = 0

# Initialize components for Routine "Probe_slide"
Probe_slideClock = core.Clock()
key_resp_Probe_slide = keyboard.Keyboard()
probe_key_press = 0
TrialNum = 0
nonNeutralTrialNum = 0
rt_list = []
acc_list = []
image_Probe_slide = visual.ImageStim(
    win=win,
    name='image_Probe_slide', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
key_resp_feedback = keyboard.Keyboard()
feedback = ""
ResponseCheck = ""
Result= ""
updated_trial_type = ''
nonNeutralTrialOmission = 0
nonNeutralTrialOmissionPercentage = 0
TrialOmission = 0
TrialOmissionPercentage = 0
mean_rt = 0
Omission_flag = 0
text_Feedback = visual.TextStim(win=win, name='text_Feedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "CheckRT"
CheckRTClock = core.Clock()

# Initialize components for Routine "Goodbye"
GoodbyeClock = core.Clock()
text_Goodbye = visual.TextStim(win=win, name='text_Goodbye',
    text='All done!\n\n\nPlease tell the experimenter you are finished.',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_Goodbye = keyboard.Keyboard()

# Initialize components for Routine "Win_amount"
Win_amountClock = core.Clock()
win_amount = ''
text_win_amount = visual.TextStim(win=win, name='text_win_amount',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_win_amount = keyboard.Keyboard()

# Initialize components for Routine "DisplayPracticeRT"
DisplayPracticeRTClock = core.Clock()
# default block feedback msg when no block-based red flag was raised 
block_feedback_msg = ''
text_block_feedback = visual.TextStim(win=win, name='text_block_feedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_block_feedback = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "TitlePage"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_TitlePage.keys = []
key_resp_TitlePage.rt = []
_key_resp_TitlePage_allKeys = []
# keep track of which components have finished
TitlePageComponents = [text_TitlePage, key_resp_TitlePage]
for thisComponent in TitlePageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TitlePageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "TitlePage"-------
while continueRoutine:
    # get current time
    t = TitlePageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TitlePageClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_TitlePage* updates
    if text_TitlePage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_TitlePage.frameNStart = frameN  # exact frame index
        text_TitlePage.tStart = t  # local t and not account for scr refresh
        text_TitlePage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_TitlePage, 'tStartRefresh')  # time at next scr refresh
        text_TitlePage.setAutoDraw(True)
    
    # *key_resp_TitlePage* updates
    waitOnFlip = False
    if key_resp_TitlePage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_TitlePage.frameNStart = frameN  # exact frame index
        key_resp_TitlePage.tStart = t  # local t and not account for scr refresh
        key_resp_TitlePage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_TitlePage, 'tStartRefresh')  # time at next scr refresh
        key_resp_TitlePage.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_TitlePage.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_TitlePage.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_TitlePage.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_TitlePage.getKeys(keyList=None, waitRelease=False)
        _key_resp_TitlePage_allKeys.extend(theseKeys)
        if len(_key_resp_TitlePage_allKeys):
            key_resp_TitlePage.keys = _key_resp_TitlePage_allKeys[-1].name  # just the last key pressed
            key_resp_TitlePage.rt = _key_resp_TitlePage_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TitlePageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TitlePage"-------
for thisComponent in TitlePageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_TitlePage.started', text_TitlePage.tStartRefresh)
thisExp.addData('text_TitlePage.stopped', text_TitlePage.tStopRefresh)
# check responses
if key_resp_TitlePage.keys in ['', [], None]:  # No response was made
    key_resp_TitlePage.keys = None
thisExp.addData('key_resp_TitlePage.keys',key_resp_TitlePage.keys)
if key_resp_TitlePage.keys != None:  # we had a response
    thisExp.addData('key_resp_TitlePage.rt', key_resp_TitlePage.rt)
thisExp.addData('key_resp_TitlePage.started', key_resp_TitlePage.tStartRefresh)
thisExp.addData('key_resp_TitlePage.stopped', key_resp_TitlePage.tStopRefresh)
thisExp.nextEntry()
# the Routine "TitlePage" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "IntroShapes"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_IntroShapes.keys = []
key_resp_IntroShapes.rt = []
_key_resp_IntroShapes_allKeys = []
# keep track of which components have finished
IntroShapesComponents = [text_IntroShapes, key_resp_IntroShapes]
for thisComponent in IntroShapesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroShapesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "IntroShapes"-------
while continueRoutine:
    # get current time
    t = IntroShapesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroShapesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_IntroShapes* updates
    if text_IntroShapes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_IntroShapes.frameNStart = frameN  # exact frame index
        text_IntroShapes.tStart = t  # local t and not account for scr refresh
        text_IntroShapes.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_IntroShapes, 'tStartRefresh')  # time at next scr refresh
        text_IntroShapes.setAutoDraw(True)
    
    # *key_resp_IntroShapes* updates
    waitOnFlip = False
    if key_resp_IntroShapes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_IntroShapes.frameNStart = frameN  # exact frame index
        key_resp_IntroShapes.tStart = t  # local t and not account for scr refresh
        key_resp_IntroShapes.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_IntroShapes, 'tStartRefresh')  # time at next scr refresh
        key_resp_IntroShapes.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_IntroShapes.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_IntroShapes.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_IntroShapes.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_IntroShapes.getKeys(keyList=None, waitRelease=False)
        _key_resp_IntroShapes_allKeys.extend(theseKeys)
        if len(_key_resp_IntroShapes_allKeys):
            key_resp_IntroShapes.keys = _key_resp_IntroShapes_allKeys[-1].name  # just the last key pressed
            key_resp_IntroShapes.rt = _key_resp_IntroShapes_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroShapesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "IntroShapes"-------
for thisComponent in IntroShapesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_IntroShapes.started', text_IntroShapes.tStartRefresh)
thisExp.addData('text_IntroShapes.stopped', text_IntroShapes.tStopRefresh)
# check responses
if key_resp_IntroShapes.keys in ['', [], None]:  # No response was made
    key_resp_IntroShapes.keys = None
thisExp.addData('key_resp_IntroShapes.keys',key_resp_IntroShapes.keys)
if key_resp_IntroShapes.keys != None:  # we had a response
    thisExp.addData('key_resp_IntroShapes.rt', key_resp_IntroShapes.rt)
thisExp.addData('key_resp_IntroShapes.started', key_resp_IntroShapes.tStartRefresh)
thisExp.addData('key_resp_IntroShapes.stopped', key_resp_IntroShapes.tStopRefresh)
thisExp.nextEntry()
# the Routine "IntroShapes" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WinSml"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_WinSml.keys = []
key_resp_WinSml.rt = []
_key_resp_WinSml_allKeys = []
# keep track of which components have finished
WinSmlComponents = [image_WinSml, key_resp_WinSml]
for thisComponent in WinSmlComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WinSmlClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WinSml"-------
while continueRoutine:
    # get current time
    t = WinSmlClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WinSmlClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_WinSml* updates
    if image_WinSml.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_WinSml.frameNStart = frameN  # exact frame index
        image_WinSml.tStart = t  # local t and not account for scr refresh
        image_WinSml.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_WinSml, 'tStartRefresh')  # time at next scr refresh
        image_WinSml.setAutoDraw(True)
    
    # *key_resp_WinSml* updates
    waitOnFlip = False
    if key_resp_WinSml.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_WinSml.frameNStart = frameN  # exact frame index
        key_resp_WinSml.tStart = t  # local t and not account for scr refresh
        key_resp_WinSml.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_WinSml, 'tStartRefresh')  # time at next scr refresh
        key_resp_WinSml.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_WinSml.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_WinSml.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_WinSml.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_WinSml.getKeys(keyList=None, waitRelease=False)
        _key_resp_WinSml_allKeys.extend(theseKeys)
        if len(_key_resp_WinSml_allKeys):
            key_resp_WinSml.keys = _key_resp_WinSml_allKeys[-1].name  # just the last key pressed
            key_resp_WinSml.rt = _key_resp_WinSml_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WinSmlComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WinSml"-------
for thisComponent in WinSmlComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_WinSml.started', image_WinSml.tStartRefresh)
thisExp.addData('image_WinSml.stopped', image_WinSml.tStopRefresh)
# check responses
if key_resp_WinSml.keys in ['', [], None]:  # No response was made
    key_resp_WinSml.keys = None
thisExp.addData('key_resp_WinSml.keys',key_resp_WinSml.keys)
if key_resp_WinSml.keys != None:  # we had a response
    thisExp.addData('key_resp_WinSml.rt', key_resp_WinSml.rt)
thisExp.addData('key_resp_WinSml.started', key_resp_WinSml.tStartRefresh)
thisExp.addData('key_resp_WinSml.stopped', key_resp_WinSml.tStopRefresh)
thisExp.nextEntry()
# the Routine "WinSml" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WinLrg"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_WinLrg.keys = []
key_resp_WinLrg.rt = []
_key_resp_WinLrg_allKeys = []
# keep track of which components have finished
WinLrgComponents = [image_WinLrg, key_resp_WinLrg]
for thisComponent in WinLrgComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WinLrgClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WinLrg"-------
while continueRoutine:
    # get current time
    t = WinLrgClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WinLrgClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_WinLrg* updates
    if image_WinLrg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_WinLrg.frameNStart = frameN  # exact frame index
        image_WinLrg.tStart = t  # local t and not account for scr refresh
        image_WinLrg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_WinLrg, 'tStartRefresh')  # time at next scr refresh
        image_WinLrg.setAutoDraw(True)
    
    # *key_resp_WinLrg* updates
    waitOnFlip = False
    if key_resp_WinLrg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_WinLrg.frameNStart = frameN  # exact frame index
        key_resp_WinLrg.tStart = t  # local t and not account for scr refresh
        key_resp_WinLrg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_WinLrg, 'tStartRefresh')  # time at next scr refresh
        key_resp_WinLrg.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_WinLrg.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_WinLrg.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_WinLrg.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_WinLrg.getKeys(keyList=None, waitRelease=False)
        _key_resp_WinLrg_allKeys.extend(theseKeys)
        if len(_key_resp_WinLrg_allKeys):
            key_resp_WinLrg.keys = _key_resp_WinLrg_allKeys[-1].name  # just the last key pressed
            key_resp_WinLrg.rt = _key_resp_WinLrg_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WinLrgComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WinLrg"-------
for thisComponent in WinLrgComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_WinLrg.started', image_WinLrg.tStartRefresh)
thisExp.addData('image_WinLrg.stopped', image_WinLrg.tStopRefresh)
# check responses
if key_resp_WinLrg.keys in ['', [], None]:  # No response was made
    key_resp_WinLrg.keys = None
thisExp.addData('key_resp_WinLrg.keys',key_resp_WinLrg.keys)
if key_resp_WinLrg.keys != None:  # we had a response
    thisExp.addData('key_resp_WinLrg.rt', key_resp_WinLrg.rt)
thisExp.addData('key_resp_WinLrg.started', key_resp_WinLrg.tStartRefresh)
thisExp.addData('key_resp_WinLrg.stopped', key_resp_WinLrg.tStopRefresh)
thisExp.nextEntry()
# the Routine "WinLrg" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "LoseSml"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_LoseSml.keys = []
key_resp_LoseSml.rt = []
_key_resp_LoseSml_allKeys = []
# keep track of which components have finished
LoseSmlComponents = [image_LoseSml, key_resp_LoseSml]
for thisComponent in LoseSmlComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
LoseSmlClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "LoseSml"-------
while continueRoutine:
    # get current time
    t = LoseSmlClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=LoseSmlClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_LoseSml* updates
    if image_LoseSml.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_LoseSml.frameNStart = frameN  # exact frame index
        image_LoseSml.tStart = t  # local t and not account for scr refresh
        image_LoseSml.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_LoseSml, 'tStartRefresh')  # time at next scr refresh
        image_LoseSml.setAutoDraw(True)
    
    # *key_resp_LoseSml* updates
    waitOnFlip = False
    if key_resp_LoseSml.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_LoseSml.frameNStart = frameN  # exact frame index
        key_resp_LoseSml.tStart = t  # local t and not account for scr refresh
        key_resp_LoseSml.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_LoseSml, 'tStartRefresh')  # time at next scr refresh
        key_resp_LoseSml.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_LoseSml.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_LoseSml.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_LoseSml.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_LoseSml.getKeys(keyList=None, waitRelease=False)
        _key_resp_LoseSml_allKeys.extend(theseKeys)
        if len(_key_resp_LoseSml_allKeys):
            key_resp_LoseSml.keys = _key_resp_LoseSml_allKeys[-1].name  # just the last key pressed
            key_resp_LoseSml.rt = _key_resp_LoseSml_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LoseSmlComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "LoseSml"-------
for thisComponent in LoseSmlComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_LoseSml.started', image_LoseSml.tStartRefresh)
thisExp.addData('image_LoseSml.stopped', image_LoseSml.tStopRefresh)
# check responses
if key_resp_LoseSml.keys in ['', [], None]:  # No response was made
    key_resp_LoseSml.keys = None
thisExp.addData('key_resp_LoseSml.keys',key_resp_LoseSml.keys)
if key_resp_LoseSml.keys != None:  # we had a response
    thisExp.addData('key_resp_LoseSml.rt', key_resp_LoseSml.rt)
thisExp.addData('key_resp_LoseSml.started', key_resp_LoseSml.tStartRefresh)
thisExp.addData('key_resp_LoseSml.stopped', key_resp_LoseSml.tStopRefresh)
thisExp.nextEntry()
# the Routine "LoseSml" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "LoseLrg"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_LoseLrg.keys = []
key_resp_LoseLrg.rt = []
_key_resp_LoseLrg_allKeys = []
# keep track of which components have finished
LoseLrgComponents = [image_LoseLrg, key_resp_LoseLrg]
for thisComponent in LoseLrgComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
LoseLrgClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "LoseLrg"-------
while continueRoutine:
    # get current time
    t = LoseLrgClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=LoseLrgClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_LoseLrg* updates
    if image_LoseLrg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_LoseLrg.frameNStart = frameN  # exact frame index
        image_LoseLrg.tStart = t  # local t and not account for scr refresh
        image_LoseLrg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_LoseLrg, 'tStartRefresh')  # time at next scr refresh
        image_LoseLrg.setAutoDraw(True)
    
    # *key_resp_LoseLrg* updates
    waitOnFlip = False
    if key_resp_LoseLrg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_LoseLrg.frameNStart = frameN  # exact frame index
        key_resp_LoseLrg.tStart = t  # local t and not account for scr refresh
        key_resp_LoseLrg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_LoseLrg, 'tStartRefresh')  # time at next scr refresh
        key_resp_LoseLrg.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_LoseLrg.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_LoseLrg.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_LoseLrg.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_LoseLrg.getKeys(keyList=None, waitRelease=False)
        _key_resp_LoseLrg_allKeys.extend(theseKeys)
        if len(_key_resp_LoseLrg_allKeys):
            key_resp_LoseLrg.keys = _key_resp_LoseLrg_allKeys[-1].name  # just the last key pressed
            key_resp_LoseLrg.rt = _key_resp_LoseLrg_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LoseLrgComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "LoseLrg"-------
for thisComponent in LoseLrgComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_LoseLrg.started', image_LoseLrg.tStartRefresh)
thisExp.addData('image_LoseLrg.stopped', image_LoseLrg.tStopRefresh)
# check responses
if key_resp_LoseLrg.keys in ['', [], None]:  # No response was made
    key_resp_LoseLrg.keys = None
thisExp.addData('key_resp_LoseLrg.keys',key_resp_LoseLrg.keys)
if key_resp_LoseLrg.keys != None:  # we had a response
    thisExp.addData('key_resp_LoseLrg.rt', key_resp_LoseLrg.rt)
thisExp.addData('key_resp_LoseLrg.started', key_resp_LoseLrg.tStartRefresh)
thisExp.addData('key_resp_LoseLrg.stopped', key_resp_LoseLrg.tStopRefresh)
thisExp.nextEntry()
# the Routine "LoseLrg" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Neut"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_Neut.keys = []
key_resp_Neut.rt = []
_key_resp_Neut_allKeys = []
# keep track of which components have finished
NeutComponents = [image_Neut, key_resp_Neut]
for thisComponent in NeutComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
NeutClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Neut"-------
while continueRoutine:
    # get current time
    t = NeutClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=NeutClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_Neut* updates
    if image_Neut.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_Neut.frameNStart = frameN  # exact frame index
        image_Neut.tStart = t  # local t and not account for scr refresh
        image_Neut.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_Neut, 'tStartRefresh')  # time at next scr refresh
        image_Neut.setAutoDraw(True)
    
    # *key_resp_Neut* updates
    waitOnFlip = False
    if key_resp_Neut.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_Neut.frameNStart = frameN  # exact frame index
        key_resp_Neut.tStart = t  # local t and not account for scr refresh
        key_resp_Neut.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_Neut, 'tStartRefresh')  # time at next scr refresh
        key_resp_Neut.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_Neut.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_Neut.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_Neut.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_Neut.getKeys(keyList=None, waitRelease=False)
        _key_resp_Neut_allKeys.extend(theseKeys)
        if len(_key_resp_Neut_allKeys):
            key_resp_Neut.keys = _key_resp_Neut_allKeys[-1].name  # just the last key pressed
            key_resp_Neut.rt = _key_resp_Neut_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in NeutComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Neut"-------
for thisComponent in NeutComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_Neut.started', image_Neut.tStartRefresh)
thisExp.addData('image_Neut.stopped', image_Neut.tStopRefresh)
# check responses
if key_resp_Neut.keys in ['', [], None]:  # No response was made
    key_resp_Neut.keys = None
thisExp.addData('key_resp_Neut.keys',key_resp_Neut.keys)
if key_resp_Neut.keys != None:  # we had a response
    thisExp.addData('key_resp_Neut.rt', key_resp_Neut.rt)
thisExp.addData('key_resp_Neut.started', key_resp_Neut.tStartRefresh)
thisExp.addData('key_resp_Neut.stopped', key_resp_Neut.tStopRefresh)
thisExp.nextEntry()
# the Routine "Neut" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ShapeFixInstruct"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_ShapeFixInstruct.keys = []
key_resp_ShapeFixInstruct.rt = []
_key_resp_ShapeFixInstruct_allKeys = []
# keep track of which components have finished
ShapeFixInstructComponents = [text_ShapeFixInstruct, key_resp_ShapeFixInstruct]
for thisComponent in ShapeFixInstructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ShapeFixInstructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ShapeFixInstruct"-------
while continueRoutine:
    # get current time
    t = ShapeFixInstructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ShapeFixInstructClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_ShapeFixInstruct* updates
    if text_ShapeFixInstruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_ShapeFixInstruct.frameNStart = frameN  # exact frame index
        text_ShapeFixInstruct.tStart = t  # local t and not account for scr refresh
        text_ShapeFixInstruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_ShapeFixInstruct, 'tStartRefresh')  # time at next scr refresh
        text_ShapeFixInstruct.setAutoDraw(True)
    
    # *key_resp_ShapeFixInstruct* updates
    waitOnFlip = False
    if key_resp_ShapeFixInstruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_ShapeFixInstruct.frameNStart = frameN  # exact frame index
        key_resp_ShapeFixInstruct.tStart = t  # local t and not account for scr refresh
        key_resp_ShapeFixInstruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_ShapeFixInstruct, 'tStartRefresh')  # time at next scr refresh
        key_resp_ShapeFixInstruct.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_ShapeFixInstruct.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_ShapeFixInstruct.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_ShapeFixInstruct.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_ShapeFixInstruct.getKeys(keyList=None, waitRelease=False)
        _key_resp_ShapeFixInstruct_allKeys.extend(theseKeys)
        if len(_key_resp_ShapeFixInstruct_allKeys):
            key_resp_ShapeFixInstruct.keys = _key_resp_ShapeFixInstruct_allKeys[-1].name  # just the last key pressed
            key_resp_ShapeFixInstruct.rt = _key_resp_ShapeFixInstruct_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ShapeFixInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ShapeFixInstruct"-------
for thisComponent in ShapeFixInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_ShapeFixInstruct.started', text_ShapeFixInstruct.tStartRefresh)
thisExp.addData('text_ShapeFixInstruct.stopped', text_ShapeFixInstruct.tStopRefresh)
# check responses
if key_resp_ShapeFixInstruct.keys in ['', [], None]:  # No response was made
    key_resp_ShapeFixInstruct.keys = None
thisExp.addData('key_resp_ShapeFixInstruct.keys',key_resp_ShapeFixInstruct.keys)
if key_resp_ShapeFixInstruct.keys != None:  # we had a response
    thisExp.addData('key_resp_ShapeFixInstruct.rt', key_resp_ShapeFixInstruct.rt)
thisExp.addData('key_resp_ShapeFixInstruct.started', key_resp_ShapeFixInstruct.tStartRefresh)
thisExp.addData('key_resp_ShapeFixInstruct.stopped', key_resp_ShapeFixInstruct.tStopRefresh)
thisExp.nextEntry()
# the Routine "ShapeFixInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "IntroProbes"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_IntroProbes.keys = []
key_resp_IntroProbes.rt = []
_key_resp_IntroProbes_allKeys = []
# keep track of which components have finished
IntroProbesComponents = [text_IntroProbes, key_resp_IntroProbes]
for thisComponent in IntroProbesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroProbesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "IntroProbes"-------
while continueRoutine:
    # get current time
    t = IntroProbesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroProbesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_IntroProbes* updates
    if text_IntroProbes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_IntroProbes.frameNStart = frameN  # exact frame index
        text_IntroProbes.tStart = t  # local t and not account for scr refresh
        text_IntroProbes.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_IntroProbes, 'tStartRefresh')  # time at next scr refresh
        text_IntroProbes.setAutoDraw(True)
    
    # *key_resp_IntroProbes* updates
    waitOnFlip = False
    if key_resp_IntroProbes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_IntroProbes.frameNStart = frameN  # exact frame index
        key_resp_IntroProbes.tStart = t  # local t and not account for scr refresh
        key_resp_IntroProbes.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_IntroProbes, 'tStartRefresh')  # time at next scr refresh
        key_resp_IntroProbes.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_IntroProbes.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_IntroProbes.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_IntroProbes.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_IntroProbes.getKeys(keyList=None, waitRelease=False)
        _key_resp_IntroProbes_allKeys.extend(theseKeys)
        if len(_key_resp_IntroProbes_allKeys):
            key_resp_IntroProbes.keys = _key_resp_IntroProbes_allKeys[-1].name  # just the last key pressed
            key_resp_IntroProbes.rt = _key_resp_IntroProbes_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroProbesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "IntroProbes"-------
for thisComponent in IntroProbesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_IntroProbes.started', text_IntroProbes.tStartRefresh)
thisExp.addData('text_IntroProbes.stopped', text_IntroProbes.tStopRefresh)
# check responses
if key_resp_IntroProbes.keys in ['', [], None]:  # No response was made
    key_resp_IntroProbes.keys = None
thisExp.addData('key_resp_IntroProbes.keys',key_resp_IntroProbes.keys)
if key_resp_IntroProbes.keys != None:  # we had a response
    thisExp.addData('key_resp_IntroProbes.rt', key_resp_IntroProbes.rt)
thisExp.addData('key_resp_IntroProbes.started', key_resp_IntroProbes.tStartRefresh)
thisExp.addData('key_resp_IntroProbes.stopped', key_resp_IntroProbes.tStopRefresh)
thisExp.nextEntry()
# the Routine "IntroProbes" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Winprb"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_Winprb.keys = []
key_resp_Winprb.rt = []
_key_resp_Winprb_allKeys = []
# keep track of which components have finished
WinprbComponents = [image_Winprb, key_resp_Winprb]
for thisComponent in WinprbComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WinprbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Winprb"-------
while continueRoutine:
    # get current time
    t = WinprbClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WinprbClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_Winprb* updates
    if image_Winprb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_Winprb.frameNStart = frameN  # exact frame index
        image_Winprb.tStart = t  # local t and not account for scr refresh
        image_Winprb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_Winprb, 'tStartRefresh')  # time at next scr refresh
        image_Winprb.setAutoDraw(True)
    
    # *key_resp_Winprb* updates
    waitOnFlip = False
    if key_resp_Winprb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_Winprb.frameNStart = frameN  # exact frame index
        key_resp_Winprb.tStart = t  # local t and not account for scr refresh
        key_resp_Winprb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_Winprb, 'tStartRefresh')  # time at next scr refresh
        key_resp_Winprb.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_Winprb.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_Winprb.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_Winprb.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_Winprb.getKeys(keyList=None, waitRelease=False)
        _key_resp_Winprb_allKeys.extend(theseKeys)
        if len(_key_resp_Winprb_allKeys):
            key_resp_Winprb.keys = _key_resp_Winprb_allKeys[-1].name  # just the last key pressed
            key_resp_Winprb.rt = _key_resp_Winprb_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WinprbComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Winprb"-------
for thisComponent in WinprbComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_Winprb.started', image_Winprb.tStartRefresh)
thisExp.addData('image_Winprb.stopped', image_Winprb.tStopRefresh)
# check responses
if key_resp_Winprb.keys in ['', [], None]:  # No response was made
    key_resp_Winprb.keys = None
thisExp.addData('key_resp_Winprb.keys',key_resp_Winprb.keys)
if key_resp_Winprb.keys != None:  # we had a response
    thisExp.addData('key_resp_Winprb.rt', key_resp_Winprb.rt)
thisExp.addData('key_resp_Winprb.started', key_resp_Winprb.tStartRefresh)
thisExp.addData('key_resp_Winprb.stopped', key_resp_Winprb.tStopRefresh)
thisExp.nextEntry()
# the Routine "Winprb" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Loseprb"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_Loseprb.keys = []
key_resp_Loseprb.rt = []
_key_resp_Loseprb_allKeys = []
# keep track of which components have finished
LoseprbComponents = [image_Loseprb, key_resp_Loseprb]
for thisComponent in LoseprbComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
LoseprbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Loseprb"-------
while continueRoutine:
    # get current time
    t = LoseprbClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=LoseprbClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_Loseprb* updates
    if image_Loseprb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_Loseprb.frameNStart = frameN  # exact frame index
        image_Loseprb.tStart = t  # local t and not account for scr refresh
        image_Loseprb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_Loseprb, 'tStartRefresh')  # time at next scr refresh
        image_Loseprb.setAutoDraw(True)
    
    # *key_resp_Loseprb* updates
    waitOnFlip = False
    if key_resp_Loseprb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_Loseprb.frameNStart = frameN  # exact frame index
        key_resp_Loseprb.tStart = t  # local t and not account for scr refresh
        key_resp_Loseprb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_Loseprb, 'tStartRefresh')  # time at next scr refresh
        key_resp_Loseprb.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_Loseprb.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_Loseprb.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_Loseprb.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_Loseprb.getKeys(keyList=None, waitRelease=False)
        _key_resp_Loseprb_allKeys.extend(theseKeys)
        if len(_key_resp_Loseprb_allKeys):
            key_resp_Loseprb.keys = _key_resp_Loseprb_allKeys[-1].name  # just the last key pressed
            key_resp_Loseprb.rt = _key_resp_Loseprb_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LoseprbComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Loseprb"-------
for thisComponent in LoseprbComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_Loseprb.started', image_Loseprb.tStartRefresh)
thisExp.addData('image_Loseprb.stopped', image_Loseprb.tStopRefresh)
# check responses
if key_resp_Loseprb.keys in ['', [], None]:  # No response was made
    key_resp_Loseprb.keys = None
thisExp.addData('key_resp_Loseprb.keys',key_resp_Loseprb.keys)
if key_resp_Loseprb.keys != None:  # we had a response
    thisExp.addData('key_resp_Loseprb.rt', key_resp_Loseprb.rt)
thisExp.addData('key_resp_Loseprb.started', key_resp_Loseprb.tStartRefresh)
thisExp.addData('key_resp_Loseprb.stopped', key_resp_Loseprb.tStopRefresh)
thisExp.nextEntry()
# the Routine "Loseprb" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Neuprob"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_Neuprb.keys = []
key_resp_Neuprb.rt = []
_key_resp_Neuprb_allKeys = []
# keep track of which components have finished
NeuprobComponents = [image_Neuprb, key_resp_Neuprb]
for thisComponent in NeuprobComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
NeuprobClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Neuprob"-------
while continueRoutine:
    # get current time
    t = NeuprobClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=NeuprobClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_Neuprb* updates
    if image_Neuprb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_Neuprb.frameNStart = frameN  # exact frame index
        image_Neuprb.tStart = t  # local t and not account for scr refresh
        image_Neuprb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_Neuprb, 'tStartRefresh')  # time at next scr refresh
        image_Neuprb.setAutoDraw(True)
    
    # *key_resp_Neuprb* updates
    waitOnFlip = False
    if key_resp_Neuprb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_Neuprb.frameNStart = frameN  # exact frame index
        key_resp_Neuprb.tStart = t  # local t and not account for scr refresh
        key_resp_Neuprb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_Neuprb, 'tStartRefresh')  # time at next scr refresh
        key_resp_Neuprb.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_Neuprb.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_Neuprb.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_Neuprb.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_Neuprb.getKeys(keyList=None, waitRelease=False)
        _key_resp_Neuprb_allKeys.extend(theseKeys)
        if len(_key_resp_Neuprb_allKeys):
            key_resp_Neuprb.keys = _key_resp_Neuprb_allKeys[-1].name  # just the last key pressed
            key_resp_Neuprb.rt = _key_resp_Neuprb_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in NeuprobComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Neuprob"-------
for thisComponent in NeuprobComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_Neuprb.started', image_Neuprb.tStartRefresh)
thisExp.addData('image_Neuprb.stopped', image_Neuprb.tStopRefresh)
# check responses
if key_resp_Neuprb.keys in ['', [], None]:  # No response was made
    key_resp_Neuprb.keys = None
thisExp.addData('key_resp_Neuprb.keys',key_resp_Neuprb.keys)
if key_resp_Neuprb.keys != None:  # we had a response
    thisExp.addData('key_resp_Neuprb.rt', key_resp_Neuprb.rt)
thisExp.addData('key_resp_Neuprb.started', key_resp_Neuprb.tStartRefresh)
thisExp.addData('key_resp_Neuprb.stopped', key_resp_Neuprb.tStopRefresh)
thisExp.nextEntry()
# the Routine "Neuprob" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Probes2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_Probes2.keys = []
key_resp_Probes2.rt = []
_key_resp_Probes2_allKeys = []
# keep track of which components have finished
Probes2Components = [text_Probes2, key_resp_Probes2]
for thisComponent in Probes2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Probes2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Probes2"-------
while continueRoutine:
    # get current time
    t = Probes2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Probes2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Probes2* updates
    if text_Probes2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Probes2.frameNStart = frameN  # exact frame index
        text_Probes2.tStart = t  # local t and not account for scr refresh
        text_Probes2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Probes2, 'tStartRefresh')  # time at next scr refresh
        text_Probes2.setAutoDraw(True)
    
    # *key_resp_Probes2* updates
    waitOnFlip = False
    if key_resp_Probes2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_Probes2.frameNStart = frameN  # exact frame index
        key_resp_Probes2.tStart = t  # local t and not account for scr refresh
        key_resp_Probes2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_Probes2, 'tStartRefresh')  # time at next scr refresh
        key_resp_Probes2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_Probes2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_Probes2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_Probes2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_Probes2.getKeys(keyList=None, waitRelease=False)
        _key_resp_Probes2_allKeys.extend(theseKeys)
        if len(_key_resp_Probes2_allKeys):
            key_resp_Probes2.keys = _key_resp_Probes2_allKeys[-1].name  # just the last key pressed
            key_resp_Probes2.rt = _key_resp_Probes2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Probes2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Probes2"-------
for thisComponent in Probes2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Probes2.started', text_Probes2.tStartRefresh)
thisExp.addData('text_Probes2.stopped', text_Probes2.tStopRefresh)
# check responses
if key_resp_Probes2.keys in ['', [], None]:  # No response was made
    key_resp_Probes2.keys = None
thisExp.addData('key_resp_Probes2.keys',key_resp_Probes2.keys)
if key_resp_Probes2.keys != None:  # we had a response
    thisExp.addData('key_resp_Probes2.rt', key_resp_Probes2.rt)
thisExp.addData('key_resp_Probes2.started', key_resp_Probes2.tStartRefresh)
thisExp.addData('key_resp_Probes2.stopped', key_resp_Probes2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Probes2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_IFISBlockList = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Time_versions/MID_ABCD_prac1.xlsx'),
    seed=None, name='trials_IFISBlockList')
thisExp.addLoop(trials_IFISBlockList)  # add the loop to the experiment
thisTrials_IFISBlockList = trials_IFISBlockList.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_IFISBlockList.rgb)
if thisTrials_IFISBlockList != None:
    for paramName in thisTrials_IFISBlockList:
        exec('{} = thisTrials_IFISBlockList[paramName]'.format(paramName))

for thisTrials_IFISBlockList in trials_IFISBlockList:
    currentLoop = trials_IFISBlockList
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_IFISBlockList.rgb)
    if thisTrials_IFISBlockList != None:
        for paramName in thisTrials_IFISBlockList:
            exec('{} = thisTrials_IFISBlockList[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "BlockInstruction"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_BlockInstruction1.setText(Instruction1)
    text_BlockInstruction2.setText(Instruction2)
    key_resp_BlockInstruction.keys = []
    key_resp_BlockInstruction.rt = []
    _key_resp_BlockInstruction_allKeys = []
    # keep track of which components have finished
    BlockInstructionComponents = [text_BlockInstruction1, text_BlockInstruction2, key_resp_BlockInstruction]
    for thisComponent in BlockInstructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BlockInstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BlockInstruction"-------
    while continueRoutine:
        # get current time
        t = BlockInstructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BlockInstructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_BlockInstruction1* updates
        if text_BlockInstruction1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_BlockInstruction1.frameNStart = frameN  # exact frame index
            text_BlockInstruction1.tStart = t  # local t and not account for scr refresh
            text_BlockInstruction1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_BlockInstruction1, 'tStartRefresh')  # time at next scr refresh
            text_BlockInstruction1.setAutoDraw(True)
        
        # *text_BlockInstruction2* updates
        if text_BlockInstruction2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_BlockInstruction2.frameNStart = frameN  # exact frame index
            text_BlockInstruction2.tStart = t  # local t and not account for scr refresh
            text_BlockInstruction2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_BlockInstruction2, 'tStartRefresh')  # time at next scr refresh
            text_BlockInstruction2.setAutoDraw(True)
        
        # *key_resp_BlockInstruction* updates
        waitOnFlip = False
        if key_resp_BlockInstruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_BlockInstruction.frameNStart = frameN  # exact frame index
            key_resp_BlockInstruction.tStart = t  # local t and not account for scr refresh
            key_resp_BlockInstruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_BlockInstruction, 'tStartRefresh')  # time at next scr refresh
            key_resp_BlockInstruction.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_BlockInstruction.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_BlockInstruction.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_BlockInstruction.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_BlockInstruction.getKeys(keyList=None, waitRelease=False)
            _key_resp_BlockInstruction_allKeys.extend(theseKeys)
            if len(_key_resp_BlockInstruction_allKeys):
                key_resp_BlockInstruction.keys = _key_resp_BlockInstruction_allKeys[-1].name  # just the last key pressed
                key_resp_BlockInstruction.rt = _key_resp_BlockInstruction_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlockInstructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BlockInstruction"-------
    for thisComponent in BlockInstructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_IFISBlockList.addData('text_BlockInstruction1.started', text_BlockInstruction1.tStartRefresh)
    trials_IFISBlockList.addData('text_BlockInstruction1.stopped', text_BlockInstruction1.tStopRefresh)
    trials_IFISBlockList.addData('text_BlockInstruction2.started', text_BlockInstruction2.tStartRefresh)
    trials_IFISBlockList.addData('text_BlockInstruction2.stopped', text_BlockInstruction2.tStopRefresh)
    # check responses
    if key_resp_BlockInstruction.keys in ['', [], None]:  # No response was made
        key_resp_BlockInstruction.keys = None
    trials_IFISBlockList.addData('key_resp_BlockInstruction.keys',key_resp_BlockInstruction.keys)
    if key_resp_BlockInstruction.keys != None:  # we had a response
        trials_IFISBlockList.addData('key_resp_BlockInstruction.rt', key_resp_BlockInstruction.rt)
    trials_IFISBlockList.addData('key_resp_BlockInstruction.started', key_resp_BlockInstruction.tStartRefresh)
    trials_IFISBlockList.addData('key_resp_BlockInstruction.stopped', key_resp_BlockInstruction.tStopRefresh)
    # the Routine "BlockInstruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=2.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "prac_cue_slide"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        key_resp_cue_slide_2.keys = []
        key_resp_cue_slide_2.rt = []
        _key_resp_cue_slide_2_allKeys = []
        prac_cue_image = 'Images/'+Task+'.bmp'
        cue_key_press = 0
        image_Cue_slide_2.setImage(prac_cue_image)
        # keep track of which components have finished
        prac_cue_slideComponents = [key_resp_cue_slide_2, image_Cue_slide_2]
        for thisComponent in prac_cue_slideComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        prac_cue_slideClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "prac_cue_slide"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = prac_cue_slideClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=prac_cue_slideClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_cue_slide_2* updates
            waitOnFlip = False
            if key_resp_cue_slide_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_cue_slide_2.frameNStart = frameN  # exact frame index
                key_resp_cue_slide_2.tStart = t  # local t and not account for scr refresh
                key_resp_cue_slide_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_cue_slide_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_cue_slide_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_cue_slide_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_cue_slide_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_cue_slide_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_cue_slide_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_cue_slide_2.tStop = t  # not accounting for scr refresh
                    key_resp_cue_slide_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_cue_slide_2, 'tStopRefresh')  # time at next scr refresh
                    key_resp_cue_slide_2.status = FINISHED
            if key_resp_cue_slide_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_cue_slide_2.getKeys(keyList=None, waitRelease=False)
                _key_resp_cue_slide_2_allKeys.extend(theseKeys)
                if len(_key_resp_cue_slide_2_allKeys):
                    key_resp_cue_slide_2.keys = _key_resp_cue_slide_2_allKeys[0].name  # just the first key pressed
                    key_resp_cue_slide_2.rt = _key_resp_cue_slide_2_allKeys[0].rt
            
            # *image_Cue_slide_2* updates
            if image_Cue_slide_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_Cue_slide_2.frameNStart = frameN  # exact frame index
                image_Cue_slide_2.tStart = t  # local t and not account for scr refresh
                image_Cue_slide_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_Cue_slide_2, 'tStartRefresh')  # time at next scr refresh
                image_Cue_slide_2.setAutoDraw(True)
            if image_Cue_slide_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_Cue_slide_2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_Cue_slide_2.tStop = t  # not accounting for scr refresh
                    image_Cue_slide_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_Cue_slide_2, 'tStopRefresh')  # time at next scr refresh
                    image_Cue_slide_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_cue_slideComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "prac_cue_slide"-------
        for thisComponent in prac_cue_slideComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_cue_slide_2.keys in ['', [], None]:  # No response was made
            key_resp_cue_slide_2.keys = None
        trials.addData('key_resp_cue_slide_2.keys',key_resp_cue_slide_2.keys)
        if key_resp_cue_slide_2.keys != None:  # we had a response
            trials.addData('key_resp_cue_slide_2.rt', key_resp_cue_slide_2.rt)
        trials.addData('key_resp_cue_slide_2.started', key_resp_cue_slide_2.tStartRefresh)
        trials.addData('key_resp_cue_slide_2.stopped', key_resp_cue_slide_2.tStopRefresh)
        if key_resp_cue_slide_2.keys != None:
            cue_key_press = 1
        trials.addData('image_Cue_slide_2.started', image_Cue_slide_2.tStartRefresh)
        trials.addData('image_Cue_slide_2.stopped', image_Cue_slide_2.tStopRefresh)
        
        # ------Prepare to start Routine "Anticipation_slide"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        key_resp_Anticipation_slide.keys = []
        key_resp_Anticipation_slide.rt = []
        _key_resp_Anticipation_slide_allKeys = []
        text_Anticipation_slide.setText('+')
        anticipation_key_press = 0
        # keep track of which components have finished
        Anticipation_slideComponents = [key_resp_Anticipation_slide, text_Anticipation_slide]
        for thisComponent in Anticipation_slideComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Anticipation_slideClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Anticipation_slide"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Anticipation_slideClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Anticipation_slideClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_Anticipation_slide* updates
            waitOnFlip = False
            if key_resp_Anticipation_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_Anticipation_slide.frameNStart = frameN  # exact frame index
                key_resp_Anticipation_slide.tStart = t  # local t and not account for scr refresh
                key_resp_Anticipation_slide.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_Anticipation_slide, 'tStartRefresh')  # time at next scr refresh
                key_resp_Anticipation_slide.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_Anticipation_slide.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_Anticipation_slide.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_Anticipation_slide.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_Anticipation_slide.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_Anticipation_slide.tStop = t  # not accounting for scr refresh
                    key_resp_Anticipation_slide.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_Anticipation_slide, 'tStopRefresh')  # time at next scr refresh
                    key_resp_Anticipation_slide.status = FINISHED
            if key_resp_Anticipation_slide.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_Anticipation_slide.getKeys(keyList=None, waitRelease=False)
                _key_resp_Anticipation_slide_allKeys.extend(theseKeys)
                if len(_key_resp_Anticipation_slide_allKeys):
                    key_resp_Anticipation_slide.keys = _key_resp_Anticipation_slide_allKeys[0].name  # just the first key pressed
                    key_resp_Anticipation_slide.rt = _key_resp_Anticipation_slide_allKeys[0].rt
            
            # *text_Anticipation_slide* updates
            if text_Anticipation_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Anticipation_slide.frameNStart = frameN  # exact frame index
                text_Anticipation_slide.tStart = t  # local t and not account for scr refresh
                text_Anticipation_slide.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Anticipation_slide, 'tStartRefresh')  # time at next scr refresh
                text_Anticipation_slide.setAutoDraw(True)
            if text_Anticipation_slide.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_Anticipation_slide.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_Anticipation_slide.tStop = t  # not accounting for scr refresh
                    text_Anticipation_slide.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_Anticipation_slide, 'tStopRefresh')  # time at next scr refresh
                    text_Anticipation_slide.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Anticipation_slideComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Anticipation_slide"-------
        for thisComponent in Anticipation_slideComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_Anticipation_slide.keys in ['', [], None]:  # No response was made
            key_resp_Anticipation_slide.keys = None
        trials.addData('key_resp_Anticipation_slide.keys',key_resp_Anticipation_slide.keys)
        if key_resp_Anticipation_slide.keys != None:  # we had a response
            trials.addData('key_resp_Anticipation_slide.rt', key_resp_Anticipation_slide.rt)
        trials.addData('key_resp_Anticipation_slide.started', key_resp_Anticipation_slide.tStartRefresh)
        trials.addData('key_resp_Anticipation_slide.stopped', key_resp_Anticipation_slide.tStopRefresh)
        trials.addData('text_Anticipation_slide.started', text_Anticipation_slide.tStartRefresh)
        trials.addData('text_Anticipation_slide.stopped', text_Anticipation_slide.tStopRefresh)
        if key_resp_Anticipation_slide.keys != None:
            anticipation_key_press = 1
        
        # ------Prepare to start Routine "prac_probe_slide"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_Probe_slide_2.keys = []
        key_resp_Probe_slide_2.rt = []
        _key_resp_Probe_slide_2_allKeys = []
        prac_probe_image = 'Images/' + ProbeType + 'Probe.bmp'
        probe_key_press = 0
        
        TrialNum += 1
        block_TrialNum += 1
        if Condition != "Triangle":
            nonNeutralTrialNum += 1
            block_nonNeutralTrialNum += 1
        image_Probe_slide_2.setImage(prac_probe_image)
        # keep track of which components have finished
        prac_probe_slideComponents = [key_resp_Probe_slide_2, image_Probe_slide_2]
        for thisComponent in prac_probe_slideComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        prac_probe_slideClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "prac_probe_slide"-------
        while continueRoutine:
            # get current time
            t = prac_probe_slideClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=prac_probe_slideClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_Probe_slide_2* updates
            waitOnFlip = False
            if key_resp_Probe_slide_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_Probe_slide_2.frameNStart = frameN  # exact frame index
                key_resp_Probe_slide_2.tStart = t  # local t and not account for scr refresh
                key_resp_Probe_slide_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_Probe_slide_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_Probe_slide_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_Probe_slide_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_Probe_slide_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_Probe_slide_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_Probe_slide_2.tStartRefresh + TheProbeDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_Probe_slide_2.tStop = t  # not accounting for scr refresh
                    key_resp_Probe_slide_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_Probe_slide_2, 'tStopRefresh')  # time at next scr refresh
                    key_resp_Probe_slide_2.status = FINISHED
            if key_resp_Probe_slide_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_Probe_slide_2.getKeys(keyList=None, waitRelease=False)
                _key_resp_Probe_slide_2_allKeys.extend(theseKeys)
                if len(_key_resp_Probe_slide_2_allKeys):
                    key_resp_Probe_slide_2.keys = _key_resp_Probe_slide_2_allKeys[0].name  # just the first key pressed
                    key_resp_Probe_slide_2.rt = _key_resp_Probe_slide_2_allKeys[0].rt
            
            # *image_Probe_slide_2* updates
            if image_Probe_slide_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_Probe_slide_2.frameNStart = frameN  # exact frame index
                image_Probe_slide_2.tStart = t  # local t and not account for scr refresh
                image_Probe_slide_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_Probe_slide_2, 'tStartRefresh')  # time at next scr refresh
                image_Probe_slide_2.setAutoDraw(True)
            if image_Probe_slide_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_Probe_slide_2.tStartRefresh + TheProbeDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    image_Probe_slide_2.tStop = t  # not accounting for scr refresh
                    image_Probe_slide_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_Probe_slide_2, 'tStopRefresh')  # time at next scr refresh
                    image_Probe_slide_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_probe_slideComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "prac_probe_slide"-------
        for thisComponent in prac_probe_slideComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_Probe_slide_2.keys in ['', [], None]:  # No response was made
            key_resp_Probe_slide_2.keys = None
        trials.addData('key_resp_Probe_slide_2.keys',key_resp_Probe_slide_2.keys)
        if key_resp_Probe_slide_2.keys != None:  # we had a response
            trials.addData('key_resp_Probe_slide_2.rt', key_resp_Probe_slide_2.rt)
        trials.addData('key_resp_Probe_slide_2.started', key_resp_Probe_slide_2.tStartRefresh)
        trials.addData('key_resp_Probe_slide_2.stopped', key_resp_Probe_slide_2.tStopRefresh)
        if key_resp_Probe_slide_2.keys != None:
            probe_key_press = 1
        probe_key_press_rt = key_resp_Probe_slide_2.rt
        trials.addData('image_Probe_slide_2.started', image_Probe_slide_2.tStartRefresh)
        trials.addData('image_Probe_slide_2.stopped', image_Probe_slide_2.tStopRefresh)
        # the Routine "prac_probe_slide" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Feedback"-------
        continueRoutine = True
        routineTimer.add(1.650000)
        # update component parameters for each repeat
        key_resp_feedback.keys = []
        key_resp_feedback.rt = []
        _key_resp_feedback_allKeys = []
        if cue_key_press == 1 or anticipation_key_press == 1:
            ResponseCheck = "You pressed too soon!"
            prbacc = 0
            prbrt = 0
            # even if ABCD's prac and scanner version didn't check for key press
            # during cue slide
            # OSL prac file check for that and try to correct participant's error
        elif anticipation_key_press == 0 and probe_key_press == 1:
            ResponseCheck = "Correct response!"
            prbacc = 1
            if Condition != "Triangle":
                prbrt = probe_key_press_rt
                rt_list.append(prbrt)
                block_rt_list.append(prbrt)      
        elif anticipation_key_press == 0 and probe_key_press == 0:
            ResponseCheck = "You pressed too slow!"
            prbacc = 0
            prbrt = 0
        
        if Condition == "SmallReward":
            if prbacc == 1:
                Result = "You earn $0.20!"
            else:
                Result = "You did not earn $0.20!"
        elif Condition == "LgReward":
            if prbacc == 1:
                Result = "You earn $5!"
            else:
                Result = "You did not earn $5!"
        elif Condition == "SmallPun":
            if prbacc == 1:
                Result = "You keep $0.20!"
            else:
                Result = "You lose $0.20!"
        elif Condition == "LgPun":
            if prbacc == 1:
                Result = "You keep $5!"
            else:
                Result = "You lose $5!"
        elif Condition == "Triangle":
             Result = "No money at stake!"
        
        
        feedback = ResponseCheck + "\n" + Result
        # debug: test_feedback = ResponseCheck + "\n" + str(prbrt) + "\n" + str(Trials) + str(nonNeutralTrialNum) +"\n" + str(mean_acc) + str(round_acc) + "\n" + str(overall_mean_acc) + "\n" + str(TheProbeDuration)
        text_Feedback.setText(feedback)
        # keep track of which components have finished
        FeedbackComponents = [key_resp_feedback, text_Feedback]
        for thisComponent in FeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_feedback* updates
            waitOnFlip = False
            if key_resp_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_feedback.frameNStart = frameN  # exact frame index
                key_resp_feedback.tStart = t  # local t and not account for scr refresh
                key_resp_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_feedback, 'tStartRefresh')  # time at next scr refresh
                key_resp_feedback.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_feedback.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_feedback.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_feedback.tStartRefresh + 1.65-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_feedback.tStop = t  # not accounting for scr refresh
                    key_resp_feedback.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_feedback, 'tStopRefresh')  # time at next scr refresh
                    key_resp_feedback.status = FINISHED
            if key_resp_feedback.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_feedback.getKeys(keyList=None, waitRelease=False)
                _key_resp_feedback_allKeys.extend(theseKeys)
                if len(_key_resp_feedback_allKeys):
                    key_resp_feedback.keys = _key_resp_feedback_allKeys[0].name  # just the first key pressed
                    key_resp_feedback.rt = _key_resp_feedback_allKeys[0].rt
            
            # *text_Feedback* updates
            if text_Feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Feedback.frameNStart = frameN  # exact frame index
                text_Feedback.tStart = t  # local t and not account for scr refresh
                text_Feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Feedback, 'tStartRefresh')  # time at next scr refresh
                text_Feedback.setAutoDraw(True)
            if text_Feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_Feedback.tStartRefresh + 1.65-frameTolerance:
                    # keep track of stop time/frame for later
                    text_Feedback.tStop = t  # not accounting for scr refresh
                    text_Feedback.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_Feedback, 'tStopRefresh')  # time at next scr refresh
                    text_Feedback.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_feedback.keys in ['', [], None]:  # No response was made
            key_resp_feedback.keys = None
        trials.addData('key_resp_feedback.keys',key_resp_feedback.keys)
        if key_resp_feedback.keys != None:  # we had a response
            trials.addData('key_resp_feedback.rt', key_resp_feedback.rt)
        trials.addData('key_resp_feedback.started', key_resp_feedback.tStartRefresh)
        trials.addData('key_resp_feedback.stopped', key_resp_feedback.tStopRefresh)
        if key_resp_Anticipation_slide.keys in ['', [], None] and probe_key_press == 0 and cue_key_press == 0 and key_resp_feedback.keys in ['', [], None]:
            Omission_flag = 1
            TrialOmission += 1
            block_TrialOmission += 1
            TrialOmissionPercentage = TrialOmission/TrialNum*100
            block_TrialOmissionPercentage = block_TrialOmission/block_TrialNum*100
            if Condition != "Triangle":
                nonNeutralTrialOmission += 1
                block_nonNeutralTrialOmission += 1
            nonNeutralTrialOmissionPercentage = nonNeutralTrialOmission/nonNeutralTrialNum*100
            block_nonNeutralTrialOmissionPercentage = block_nonNeutralTrialOmission/block_nonNeutralTrialNum*100
        
        if Condition == "SmallReward":
            if prbacc == 1:
                updated_trial_type = 'WinSmallHit'
                final_compensation += .2 
            else:
                if Omission_flag == 0:
                    updated_trial_type = 'WinSmallMiss'
                elif Omission_flag == 1:
                    updated_trial_type = 'WinSmallOmission'
        elif Condition == "LgReward":
            if prbacc == 1:
                updated_trial_type = 'WinBigHit'
                final_compensation += 5
            else:
                if Omission_flag == 0:
                    updated_trial_type = 'WinBigMiss'
                elif Omission_flag == 1:
                    updated_trial_type = 'WinBigOmission'
        elif Condition == "SmallPun":
            if prbacc == 1:
                updated_trial_type = 'PunSmallHit'
            else:
                final_compensation -= .2 
                if Omission_flag == 0:
                    updated_trial_type = 'PunSmallMiss'
                elif Omission_flag == 1:
                    updated_trial_type = 'PunSmallOmission'
        elif Condition == "LgPun":
            if prbacc == 1:
                updated_trial_type = 'PunBigHit'
            else:
                final_compensation -= 5 
                if Omission_flag == 0:
                    updated_trial_type = 'PunBigMiss'
                elif Omission_flag == 1:
                    updated_trial_type = 'PunBigOmission'
        elif Condition == "Triangle":
             if prbacc == 1:
                updated_trial_type = 'NeuHit'
             else:
                if Omission_flag == 0:
                    updated_trial_type = 'NeuMiss'
                elif Omission_flag == 1:
                    updated_trial_type = 'NeuOmission'
        
        Omission_flag = 0
        
        thisExp.addData('updated_trial_type', updated_trial_type)
        
        thisExp.addData('Recordedprbacc', prbacc)
        thisExp.addData('Recordedprbrt', prbrt)
        
        thisExp.addData('TrialNum', TrialNum)
        thisExp.addData('block_TrialNum', block_TrialNum)
        thisExp.addData('nonNeutralTrialNum', nonNeutralTrialNum)
        thisExp.addData('block_nonNeutralTrialNum', block_nonNeutralTrialNum)
        thisExp.addData('RecordedProbeDuration', TheProbeDuration)
        
        thisExp.addData('nonNeutralTrialOmission', nonNeutralTrialOmission)
        thisExp.addData('nonNeutralTrialOmissionPercentage', nonNeutralTrialOmissionPercentage)
        thisExp.addData('TrialOmission', TrialOmission)
        thisExp.addData('TrialOmissionPercentage', TrialOmissionPercentage)
        thisExp.addData('block_nonNeutralTrialOmission', block_nonNeutralTrialOmission)
        thisExp.addData('block_nonNeutralTrialOmissionPercentage', block_nonNeutralTrialOmissionPercentage)
        thisExp.addData('block_TrialOmission', block_TrialOmission)
        thisExp.addData('block_TrialOmissionPercentage', block_TrialOmissionPercentage)
        thisExp.addData('final_compensation', final_compensation)
        trials.addData('text_Feedback.started', text_Feedback.tStartRefresh)
        trials.addData('text_Feedback.stopped', text_Feedback.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'trials'
    
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials.saveAsText(filename + 'trials.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
# completed 1.0 repeats of 'trials_IFISBlockList'


# ------Prepare to start Routine "PartOneEndText"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_PartOneEndText.keys = []
key_resp_PartOneEndText.rt = []
_key_resp_PartOneEndText_allKeys = []
# keep track of which components have finished
PartOneEndTextComponents = [text_PartOneEndText, key_resp_PartOneEndText]
for thisComponent in PartOneEndTextComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PartOneEndTextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PartOneEndText"-------
while continueRoutine:
    # get current time
    t = PartOneEndTextClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PartOneEndTextClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_PartOneEndText* updates
    if text_PartOneEndText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_PartOneEndText.frameNStart = frameN  # exact frame index
        text_PartOneEndText.tStart = t  # local t and not account for scr refresh
        text_PartOneEndText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_PartOneEndText, 'tStartRefresh')  # time at next scr refresh
        text_PartOneEndText.setAutoDraw(True)
    
    # *key_resp_PartOneEndText* updates
    waitOnFlip = False
    if key_resp_PartOneEndText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_PartOneEndText.frameNStart = frameN  # exact frame index
        key_resp_PartOneEndText.tStart = t  # local t and not account for scr refresh
        key_resp_PartOneEndText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_PartOneEndText, 'tStartRefresh')  # time at next scr refresh
        key_resp_PartOneEndText.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_PartOneEndText.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_PartOneEndText.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_PartOneEndText.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_PartOneEndText.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_PartOneEndText_allKeys.extend(theseKeys)
        if len(_key_resp_PartOneEndText_allKeys):
            key_resp_PartOneEndText.keys = _key_resp_PartOneEndText_allKeys[-1].name  # just the last key pressed
            key_resp_PartOneEndText.rt = _key_resp_PartOneEndText_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PartOneEndTextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PartOneEndText"-------
for thisComponent in PartOneEndTextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_PartOneEndText.started', text_PartOneEndText.tStartRefresh)
thisExp.addData('text_PartOneEndText.stopped', text_PartOneEndText.tStopRefresh)
# check responses
if key_resp_PartOneEndText.keys in ['', [], None]:  # No response was made
    key_resp_PartOneEndText.keys = None
thisExp.addData('key_resp_PartOneEndText.keys',key_resp_PartOneEndText.keys)
if key_resp_PartOneEndText.keys != None:  # we had a response
    thisExp.addData('key_resp_PartOneEndText.rt', key_resp_PartOneEndText.rt)
thisExp.addData('key_resp_PartOneEndText.started', key_resp_PartOneEndText.tStartRefresh)
thisExp.addData('key_resp_PartOneEndText.stopped', key_resp_PartOneEndText.tStopRefresh)
thisExp.nextEntry()
TrialNum = 0
nonNeutralTrialNum = 0
nonNeutralTrialOmission = 0
nonNeutralTrialOmissionPercentage = 0
TrialOmission = 0
TrialOmissionPercentage = 0
mean_rt = 0
rt_list = []
final_compensation = 0
# the Routine "PartOneEndText" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
TimingBlockList = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='TimingBlockList')
thisExp.addLoop(TimingBlockList)  # add the loop to the experiment
thisTimingBlockList = TimingBlockList.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTimingBlockList.rgb)
if thisTimingBlockList != None:
    for paramName in thisTimingBlockList:
        exec('{} = thisTimingBlockList[paramName]'.format(paramName))

for thisTimingBlockList in TimingBlockList:
    currentLoop = TimingBlockList
    # abbreviate parameter names if possible (e.g. rgb = thisTimingBlockList.rgb)
    if thisTimingBlockList != None:
        for paramName in thisTimingBlockList:
            exec('{} = thisTimingBlockList[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "BlockInstructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_instr.keys = []
    key_resp_instr.rt = []
    _key_resp_instr_allKeys = []
    # keep track of which components have finished
    BlockInstructionsComponents = [image, key_resp_instr]
    for thisComponent in BlockInstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BlockInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BlockInstructions"-------
    while continueRoutine:
        # get current time
        t = BlockInstructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BlockInstructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # *key_resp_instr* updates
        waitOnFlip = False
        if key_resp_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_instr.frameNStart = frameN  # exact frame index
            key_resp_instr.tStart = t  # local t and not account for scr refresh
            key_resp_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_instr, 'tStartRefresh')  # time at next scr refresh
            key_resp_instr.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_instr.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_instr.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_instr.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_instr.getKeys(keyList=None, waitRelease=False)
            _key_resp_instr_allKeys.extend(theseKeys)
            if len(_key_resp_instr_allKeys):
                key_resp_instr.keys = _key_resp_instr_allKeys[-1].name  # just the last key pressed
                key_resp_instr.rt = _key_resp_instr_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlockInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BlockInstructions"-------
    for thisComponent in BlockInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    TimingBlockList.addData('image.started', image.tStartRefresh)
    TimingBlockList.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp_instr.keys in ['', [], None]:  # No response was made
        key_resp_instr.keys = None
    TimingBlockList.addData('key_resp_instr.keys',key_resp_instr.keys)
    if key_resp_instr.keys != None:  # we had a response
        TimingBlockList.addData('key_resp_instr.rt', key_resp_instr.rt)
    TimingBlockList.addData('key_resp_instr.started', key_resp_instr.tStartRefresh)
    TimingBlockList.addData('key_resp_instr.stopped', key_resp_instr.tStopRefresh)
    # the Routine "BlockInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "PrepTime"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    # at the beginning and reset trials at 0 after run1
    block_TrialNum = 0
    block_nonNeutralTrialNum = 0
    block_nonNeutralTrialOmission = 0
    block_nonNeutralTrialOmissionPercentage = 0
    block_TrialOmission = 0
    block_TrialOmissionPercentage = 0
    
    block_rt_list = []
    block_acc_list = []
    block_mean_rt = 0
    
    prbacc = 0
    prbrt = 0
    # keep track of which components have finished
    PrepTimeComponents = [text_PrepTime]
    for thisComponent in PrepTimeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PrepTimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "PrepTime"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PrepTimeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PrepTimeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_PrepTime* updates
        if text_PrepTime.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_PrepTime.frameNStart = frameN  # exact frame index
            text_PrepTime.tStart = t  # local t and not account for scr refresh
            text_PrepTime.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_PrepTime, 'tStartRefresh')  # time at next scr refresh
            text_PrepTime.setAutoDraw(True)
        if text_PrepTime.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_PrepTime.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_PrepTime.tStop = t  # not accounting for scr refresh
                text_PrepTime.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_PrepTime, 'tStopRefresh')  # time at next scr refresh
                text_PrepTime.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PrepTimeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PrepTime"-------
    for thisComponent in PrepTimeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    TimingBlockList.addData('text_PrepTime.started', text_PrepTime.tStartRefresh)
    TimingBlockList.addData('text_PrepTime.stopped', text_PrepTime.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials_RewardProc = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Time_versions/MID_ABCD_prac2.xlsx'),
        seed=None, name='trials_RewardProc')
    thisExp.addLoop(trials_RewardProc)  # add the loop to the experiment
    thisTrials_RewardProc = trials_RewardProc.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_RewardProc.rgb)
    if thisTrials_RewardProc != None:
        for paramName in thisTrials_RewardProc:
            exec('{} = thisTrials_RewardProc[paramName]'.format(paramName))
    
    for thisTrials_RewardProc in trials_RewardProc:
        currentLoop = trials_RewardProc
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_RewardProc.rgb)
        if thisTrials_RewardProc != None:
            for paramName in thisTrials_RewardProc:
                exec('{} = thisTrials_RewardProc[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Cue_slide"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        key_resp_cue_slide.keys = []
        key_resp_cue_slide.rt = []
        _key_resp_cue_slide_allKeys = []
        cue_key_press = 0
        image_Cue_slide.setImage(Cue)
        # keep track of which components have finished
        Cue_slideComponents = [key_resp_cue_slide, image_Cue_slide]
        for thisComponent in Cue_slideComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Cue_slideClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Cue_slide"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Cue_slideClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Cue_slideClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_cue_slide* updates
            waitOnFlip = False
            if key_resp_cue_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_cue_slide.frameNStart = frameN  # exact frame index
                key_resp_cue_slide.tStart = t  # local t and not account for scr refresh
                key_resp_cue_slide.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_cue_slide, 'tStartRefresh')  # time at next scr refresh
                key_resp_cue_slide.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_cue_slide.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_cue_slide.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_cue_slide.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_cue_slide.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_cue_slide.tStop = t  # not accounting for scr refresh
                    key_resp_cue_slide.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_cue_slide, 'tStopRefresh')  # time at next scr refresh
                    key_resp_cue_slide.status = FINISHED
            if key_resp_cue_slide.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_cue_slide.getKeys(keyList=None, waitRelease=False)
                _key_resp_cue_slide_allKeys.extend(theseKeys)
                if len(_key_resp_cue_slide_allKeys):
                    key_resp_cue_slide.keys = _key_resp_cue_slide_allKeys[0].name  # just the first key pressed
                    key_resp_cue_slide.rt = _key_resp_cue_slide_allKeys[0].rt
            
            # *image_Cue_slide* updates
            if image_Cue_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_Cue_slide.frameNStart = frameN  # exact frame index
                image_Cue_slide.tStart = t  # local t and not account for scr refresh
                image_Cue_slide.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_Cue_slide, 'tStartRefresh')  # time at next scr refresh
                image_Cue_slide.setAutoDraw(True)
            if image_Cue_slide.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_Cue_slide.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_Cue_slide.tStop = t  # not accounting for scr refresh
                    image_Cue_slide.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_Cue_slide, 'tStopRefresh')  # time at next scr refresh
                    image_Cue_slide.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Cue_slideComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Cue_slide"-------
        for thisComponent in Cue_slideComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_cue_slide.keys in ['', [], None]:  # No response was made
            key_resp_cue_slide.keys = None
        trials_RewardProc.addData('key_resp_cue_slide.keys',key_resp_cue_slide.keys)
        if key_resp_cue_slide.keys != None:  # we had a response
            trials_RewardProc.addData('key_resp_cue_slide.rt', key_resp_cue_slide.rt)
        trials_RewardProc.addData('key_resp_cue_slide.started', key_resp_cue_slide.tStartRefresh)
        trials_RewardProc.addData('key_resp_cue_slide.stopped', key_resp_cue_slide.tStopRefresh)
        if key_resp_cue_slide.keys != None:
            cue_key_press = 1
        trials_RewardProc.addData('image_Cue_slide.started', image_Cue_slide.tStartRefresh)
        trials_RewardProc.addData('image_Cue_slide.stopped', image_Cue_slide.tStopRefresh)
        
        # ------Prepare to start Routine "Anticipation_slide"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        key_resp_Anticipation_slide.keys = []
        key_resp_Anticipation_slide.rt = []
        _key_resp_Anticipation_slide_allKeys = []
        text_Anticipation_slide.setText('+')
        anticipation_key_press = 0
        # keep track of which components have finished
        Anticipation_slideComponents = [key_resp_Anticipation_slide, text_Anticipation_slide]
        for thisComponent in Anticipation_slideComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Anticipation_slideClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Anticipation_slide"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Anticipation_slideClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Anticipation_slideClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_Anticipation_slide* updates
            waitOnFlip = False
            if key_resp_Anticipation_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_Anticipation_slide.frameNStart = frameN  # exact frame index
                key_resp_Anticipation_slide.tStart = t  # local t and not account for scr refresh
                key_resp_Anticipation_slide.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_Anticipation_slide, 'tStartRefresh')  # time at next scr refresh
                key_resp_Anticipation_slide.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_Anticipation_slide.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_Anticipation_slide.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_Anticipation_slide.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_Anticipation_slide.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_Anticipation_slide.tStop = t  # not accounting for scr refresh
                    key_resp_Anticipation_slide.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_Anticipation_slide, 'tStopRefresh')  # time at next scr refresh
                    key_resp_Anticipation_slide.status = FINISHED
            if key_resp_Anticipation_slide.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_Anticipation_slide.getKeys(keyList=None, waitRelease=False)
                _key_resp_Anticipation_slide_allKeys.extend(theseKeys)
                if len(_key_resp_Anticipation_slide_allKeys):
                    key_resp_Anticipation_slide.keys = _key_resp_Anticipation_slide_allKeys[0].name  # just the first key pressed
                    key_resp_Anticipation_slide.rt = _key_resp_Anticipation_slide_allKeys[0].rt
            
            # *text_Anticipation_slide* updates
            if text_Anticipation_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Anticipation_slide.frameNStart = frameN  # exact frame index
                text_Anticipation_slide.tStart = t  # local t and not account for scr refresh
                text_Anticipation_slide.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Anticipation_slide, 'tStartRefresh')  # time at next scr refresh
                text_Anticipation_slide.setAutoDraw(True)
            if text_Anticipation_slide.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_Anticipation_slide.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_Anticipation_slide.tStop = t  # not accounting for scr refresh
                    text_Anticipation_slide.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_Anticipation_slide, 'tStopRefresh')  # time at next scr refresh
                    text_Anticipation_slide.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Anticipation_slideComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Anticipation_slide"-------
        for thisComponent in Anticipation_slideComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_Anticipation_slide.keys in ['', [], None]:  # No response was made
            key_resp_Anticipation_slide.keys = None
        trials_RewardProc.addData('key_resp_Anticipation_slide.keys',key_resp_Anticipation_slide.keys)
        if key_resp_Anticipation_slide.keys != None:  # we had a response
            trials_RewardProc.addData('key_resp_Anticipation_slide.rt', key_resp_Anticipation_slide.rt)
        trials_RewardProc.addData('key_resp_Anticipation_slide.started', key_resp_Anticipation_slide.tStartRefresh)
        trials_RewardProc.addData('key_resp_Anticipation_slide.stopped', key_resp_Anticipation_slide.tStopRefresh)
        trials_RewardProc.addData('text_Anticipation_slide.started', text_Anticipation_slide.tStartRefresh)
        trials_RewardProc.addData('text_Anticipation_slide.stopped', text_Anticipation_slide.tStopRefresh)
        if key_resp_Anticipation_slide.keys != None:
            anticipation_key_press = 1
        
        # ------Prepare to start Routine "Probe_slide"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_Probe_slide.keys = []
        key_resp_Probe_slide.rt = []
        _key_resp_Probe_slide_allKeys = []
        probe_key_press = 0
        
        TrialNum += 1
        block_TrialNum += 1
        if Condition != "Triangle":
            nonNeutralTrialNum += 1
            block_nonNeutralTrialNum += 1
        image_Probe_slide.setImage(Probe)
        # keep track of which components have finished
        Probe_slideComponents = [key_resp_Probe_slide, image_Probe_slide]
        for thisComponent in Probe_slideComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Probe_slideClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Probe_slide"-------
        while continueRoutine:
            # get current time
            t = Probe_slideClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Probe_slideClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_Probe_slide* updates
            waitOnFlip = False
            if key_resp_Probe_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_Probe_slide.frameNStart = frameN  # exact frame index
                key_resp_Probe_slide.tStart = t  # local t and not account for scr refresh
                key_resp_Probe_slide.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_Probe_slide, 'tStartRefresh')  # time at next scr refresh
                key_resp_Probe_slide.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_Probe_slide.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_Probe_slide.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_Probe_slide.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_Probe_slide.tStartRefresh + TheProbeDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_Probe_slide.tStop = t  # not accounting for scr refresh
                    key_resp_Probe_slide.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_Probe_slide, 'tStopRefresh')  # time at next scr refresh
                    key_resp_Probe_slide.status = FINISHED
            if key_resp_Probe_slide.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_Probe_slide.getKeys(keyList=None, waitRelease=False)
                _key_resp_Probe_slide_allKeys.extend(theseKeys)
                if len(_key_resp_Probe_slide_allKeys):
                    key_resp_Probe_slide.keys = _key_resp_Probe_slide_allKeys[0].name  # just the first key pressed
                    key_resp_Probe_slide.rt = _key_resp_Probe_slide_allKeys[0].rt
            
            # *image_Probe_slide* updates
            if image_Probe_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_Probe_slide.frameNStart = frameN  # exact frame index
                image_Probe_slide.tStart = t  # local t and not account for scr refresh
                image_Probe_slide.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_Probe_slide, 'tStartRefresh')  # time at next scr refresh
                image_Probe_slide.setAutoDraw(True)
            if image_Probe_slide.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_Probe_slide.tStartRefresh + TheProbeDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    image_Probe_slide.tStop = t  # not accounting for scr refresh
                    image_Probe_slide.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_Probe_slide, 'tStopRefresh')  # time at next scr refresh
                    image_Probe_slide.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Probe_slideComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Probe_slide"-------
        for thisComponent in Probe_slideComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_Probe_slide.keys in ['', [], None]:  # No response was made
            key_resp_Probe_slide.keys = None
        trials_RewardProc.addData('key_resp_Probe_slide.keys',key_resp_Probe_slide.keys)
        if key_resp_Probe_slide.keys != None:  # we had a response
            trials_RewardProc.addData('key_resp_Probe_slide.rt', key_resp_Probe_slide.rt)
        trials_RewardProc.addData('key_resp_Probe_slide.started', key_resp_Probe_slide.tStartRefresh)
        trials_RewardProc.addData('key_resp_Probe_slide.stopped', key_resp_Probe_slide.tStopRefresh)
        if key_resp_Probe_slide.keys != None:
            probe_key_press = 1
        
        probe_key_press_rt = key_resp_Probe_slide.rt
        trials_RewardProc.addData('image_Probe_slide.started', image_Probe_slide.tStartRefresh)
        trials_RewardProc.addData('image_Probe_slide.stopped', image_Probe_slide.tStopRefresh)
        # the Routine "Probe_slide" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Feedback"-------
        continueRoutine = True
        routineTimer.add(1.650000)
        # update component parameters for each repeat
        key_resp_feedback.keys = []
        key_resp_feedback.rt = []
        _key_resp_feedback_allKeys = []
        if cue_key_press == 1 or anticipation_key_press == 1:
            ResponseCheck = "You pressed too soon!"
            prbacc = 0
            prbrt = 0
            # even if ABCD's prac and scanner version didn't check for key press
            # during cue slide
            # OSL prac file check for that and try to correct participant's error
        elif anticipation_key_press == 0 and probe_key_press == 1:
            ResponseCheck = "Correct response!"
            prbacc = 1
            if Condition != "Triangle":
                prbrt = probe_key_press_rt
                rt_list.append(prbrt)
                block_rt_list.append(prbrt)      
        elif anticipation_key_press == 0 and probe_key_press == 0:
            ResponseCheck = "You pressed too slow!"
            prbacc = 0
            prbrt = 0
        
        if Condition == "SmallReward":
            if prbacc == 1:
                Result = "You earn $0.20!"
            else:
                Result = "You did not earn $0.20!"
        elif Condition == "LgReward":
            if prbacc == 1:
                Result = "You earn $5!"
            else:
                Result = "You did not earn $5!"
        elif Condition == "SmallPun":
            if prbacc == 1:
                Result = "You keep $0.20!"
            else:
                Result = "You lose $0.20!"
        elif Condition == "LgPun":
            if prbacc == 1:
                Result = "You keep $5!"
            else:
                Result = "You lose $5!"
        elif Condition == "Triangle":
             Result = "No money at stake!"
        
        
        feedback = ResponseCheck + "\n" + Result
        # debug: test_feedback = ResponseCheck + "\n" + str(prbrt) + "\n" + str(Trials) + str(nonNeutralTrialNum) +"\n" + str(mean_acc) + str(round_acc) + "\n" + str(overall_mean_acc) + "\n" + str(TheProbeDuration)
        text_Feedback.setText(feedback)
        # keep track of which components have finished
        FeedbackComponents = [key_resp_feedback, text_Feedback]
        for thisComponent in FeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_feedback* updates
            waitOnFlip = False
            if key_resp_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_feedback.frameNStart = frameN  # exact frame index
                key_resp_feedback.tStart = t  # local t and not account for scr refresh
                key_resp_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_feedback, 'tStartRefresh')  # time at next scr refresh
                key_resp_feedback.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_feedback.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_feedback.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_feedback.tStartRefresh + 1.65-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_feedback.tStop = t  # not accounting for scr refresh
                    key_resp_feedback.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_feedback, 'tStopRefresh')  # time at next scr refresh
                    key_resp_feedback.status = FINISHED
            if key_resp_feedback.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_feedback.getKeys(keyList=None, waitRelease=False)
                _key_resp_feedback_allKeys.extend(theseKeys)
                if len(_key_resp_feedback_allKeys):
                    key_resp_feedback.keys = _key_resp_feedback_allKeys[0].name  # just the first key pressed
                    key_resp_feedback.rt = _key_resp_feedback_allKeys[0].rt
            
            # *text_Feedback* updates
            if text_Feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Feedback.frameNStart = frameN  # exact frame index
                text_Feedback.tStart = t  # local t and not account for scr refresh
                text_Feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Feedback, 'tStartRefresh')  # time at next scr refresh
                text_Feedback.setAutoDraw(True)
            if text_Feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_Feedback.tStartRefresh + 1.65-frameTolerance:
                    # keep track of stop time/frame for later
                    text_Feedback.tStop = t  # not accounting for scr refresh
                    text_Feedback.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_Feedback, 'tStopRefresh')  # time at next scr refresh
                    text_Feedback.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_feedback.keys in ['', [], None]:  # No response was made
            key_resp_feedback.keys = None
        trials_RewardProc.addData('key_resp_feedback.keys',key_resp_feedback.keys)
        if key_resp_feedback.keys != None:  # we had a response
            trials_RewardProc.addData('key_resp_feedback.rt', key_resp_feedback.rt)
        trials_RewardProc.addData('key_resp_feedback.started', key_resp_feedback.tStartRefresh)
        trials_RewardProc.addData('key_resp_feedback.stopped', key_resp_feedback.tStopRefresh)
        if key_resp_Anticipation_slide.keys in ['', [], None] and probe_key_press == 0 and cue_key_press == 0 and key_resp_feedback.keys in ['', [], None]:
            Omission_flag = 1
            TrialOmission += 1
            block_TrialOmission += 1
            TrialOmissionPercentage = TrialOmission/TrialNum*100
            block_TrialOmissionPercentage = block_TrialOmission/block_TrialNum*100
            if Condition != "Triangle":
                nonNeutralTrialOmission += 1
                block_nonNeutralTrialOmission += 1
            nonNeutralTrialOmissionPercentage = nonNeutralTrialOmission/nonNeutralTrialNum*100
            block_nonNeutralTrialOmissionPercentage = block_nonNeutralTrialOmission/block_nonNeutralTrialNum*100
        
        if Condition == "SmallReward":
            if prbacc == 1:
                updated_trial_type = 'WinSmallHit'
                final_compensation += .2 
            else:
                if Omission_flag == 0:
                    updated_trial_type = 'WinSmallMiss'
                elif Omission_flag == 1:
                    updated_trial_type = 'WinSmallOmission'
        elif Condition == "LgReward":
            if prbacc == 1:
                updated_trial_type = 'WinBigHit'
                final_compensation += 5
            else:
                if Omission_flag == 0:
                    updated_trial_type = 'WinBigMiss'
                elif Omission_flag == 1:
                    updated_trial_type = 'WinBigOmission'
        elif Condition == "SmallPun":
            if prbacc == 1:
                updated_trial_type = 'PunSmallHit'
            else:
                final_compensation -= .2 
                if Omission_flag == 0:
                    updated_trial_type = 'PunSmallMiss'
                elif Omission_flag == 1:
                    updated_trial_type = 'PunSmallOmission'
        elif Condition == "LgPun":
            if prbacc == 1:
                updated_trial_type = 'PunBigHit'
            else:
                final_compensation -= 5 
                if Omission_flag == 0:
                    updated_trial_type = 'PunBigMiss'
                elif Omission_flag == 1:
                    updated_trial_type = 'PunBigOmission'
        elif Condition == "Triangle":
             if prbacc == 1:
                updated_trial_type = 'NeuHit'
             else:
                if Omission_flag == 0:
                    updated_trial_type = 'NeuMiss'
                elif Omission_flag == 1:
                    updated_trial_type = 'NeuOmission'
        
        Omission_flag = 0
        
        thisExp.addData('updated_trial_type', updated_trial_type)
        
        thisExp.addData('Recordedprbacc', prbacc)
        thisExp.addData('Recordedprbrt', prbrt)
        
        thisExp.addData('TrialNum', TrialNum)
        thisExp.addData('block_TrialNum', block_TrialNum)
        thisExp.addData('nonNeutralTrialNum', nonNeutralTrialNum)
        thisExp.addData('block_nonNeutralTrialNum', block_nonNeutralTrialNum)
        thisExp.addData('RecordedProbeDuration', TheProbeDuration)
        
        thisExp.addData('nonNeutralTrialOmission', nonNeutralTrialOmission)
        thisExp.addData('nonNeutralTrialOmissionPercentage', nonNeutralTrialOmissionPercentage)
        thisExp.addData('TrialOmission', TrialOmission)
        thisExp.addData('TrialOmissionPercentage', TrialOmissionPercentage)
        thisExp.addData('block_nonNeutralTrialOmission', block_nonNeutralTrialOmission)
        thisExp.addData('block_nonNeutralTrialOmissionPercentage', block_nonNeutralTrialOmissionPercentage)
        thisExp.addData('block_TrialOmission', block_TrialOmission)
        thisExp.addData('block_TrialOmissionPercentage', block_TrialOmissionPercentage)
        thisExp.addData('final_compensation', final_compensation)
        trials_RewardProc.addData('text_Feedback.started', text_Feedback.tStartRefresh)
        trials_RewardProc.addData('text_Feedback.stopped', text_Feedback.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_RewardProc'
    
    # get names of stimulus parameters
    if trials_RewardProc.trialList in ([], [None], None):
        params = []
    else:
        params = trials_RewardProc.trialList[0].keys()
    # save data for this loop
    trials_RewardProc.saveAsExcel(filename + '.xlsx', sheetName='trials_RewardProc',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_RewardProc.saveAsText(filename + 'trials_RewardProc.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "CheckRT"-------
    continueRoutine = True
    # update component parameters for each repeat
    rt_array = np.array(rt_list)
    block_rt_array = np.array(block_rt_list)
    
    # mean_rt is the cumulative non-neutral correct trial rt average
    if len(rt_list) > 0:
        mean_rt = rt_array.mean()
    if len(block_rt_list) > 0:
        block_mean_rt = block_rt_array.mean()
    
    if block_mean_rt > .1:
        TimingBlockList.finished = True
    else:
        TheProbeDuration = .4
    
    thisExp.addData('mean_rt', mean_rt)
    thisExp.addData('block_mean_rt', block_mean_rt)
    # keep track of which components have finished
    CheckRTComponents = []
    for thisComponent in CheckRTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CheckRTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "CheckRT"-------
    while continueRoutine:
        # get current time
        t = CheckRTClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CheckRTClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CheckRTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "CheckRT"-------
    for thisComponent in CheckRTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "CheckRT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 2.0 repeats of 'TimingBlockList'


# ------Prepare to start Routine "Goodbye"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_Goodbye.keys = []
key_resp_Goodbye.rt = []
_key_resp_Goodbye_allKeys = []
# keep track of which components have finished
GoodbyeComponents = [text_Goodbye, key_resp_Goodbye]
for thisComponent in GoodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GoodbyeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Goodbye"-------
while continueRoutine:
    # get current time
    t = GoodbyeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GoodbyeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Goodbye* updates
    if text_Goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Goodbye.frameNStart = frameN  # exact frame index
        text_Goodbye.tStart = t  # local t and not account for scr refresh
        text_Goodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Goodbye, 'tStartRefresh')  # time at next scr refresh
        text_Goodbye.setAutoDraw(True)
    
    # *key_resp_Goodbye* updates
    waitOnFlip = False
    if key_resp_Goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_Goodbye.frameNStart = frameN  # exact frame index
        key_resp_Goodbye.tStart = t  # local t and not account for scr refresh
        key_resp_Goodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_Goodbye, 'tStartRefresh')  # time at next scr refresh
        key_resp_Goodbye.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_Goodbye.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_Goodbye.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_Goodbye.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_Goodbye.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_Goodbye_allKeys.extend(theseKeys)
        if len(_key_resp_Goodbye_allKeys):
            key_resp_Goodbye.keys = _key_resp_Goodbye_allKeys[-1].name  # just the last key pressed
            key_resp_Goodbye.rt = _key_resp_Goodbye_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Goodbye"-------
for thisComponent in GoodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Goodbye.started', text_Goodbye.tStartRefresh)
thisExp.addData('text_Goodbye.stopped', text_Goodbye.tStopRefresh)
# check responses
if key_resp_Goodbye.keys in ['', [], None]:  # No response was made
    key_resp_Goodbye.keys = None
thisExp.addData('key_resp_Goodbye.keys',key_resp_Goodbye.keys)
if key_resp_Goodbye.keys != None:  # we had a response
    thisExp.addData('key_resp_Goodbye.rt', key_resp_Goodbye.rt)
thisExp.addData('key_resp_Goodbye.started', key_resp_Goodbye.tStartRefresh)
thisExp.addData('key_resp_Goodbye.stopped', key_resp_Goodbye.tStopRefresh)
thisExp.nextEntry()
# the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Win_amount"-------
continueRoutine = True
# update component parameters for each repeat
if final_compensation < 5:
    if expInfo['visit'] == '001':
        final_compensation = 4.8
    else:
        final_compensation = 5.2

win_amount = 'You just finished MID practice!\n You won $%s in the practice!\nYou can cash the reward for real when you complete the MID in the scanner!'%(round(final_compensation, 1))

"""
Based on ABCD's description of MID, 
Participants gain an average of $21 and 
all subjects are given at least $1 regardless of performance to maintain motivation during the scan protocol. 
So OSL version, at least $10 on visit 1 (for more motivation during the 2nd visit)
& at least $5 on visit 2
"""
text_win_amount.setText(win_amount)
key_resp_win_amount.keys = []
key_resp_win_amount.rt = []
_key_resp_win_amount_allKeys = []
# keep track of which components have finished
Win_amountComponents = [text_win_amount, key_resp_win_amount]
for thisComponent in Win_amountComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Win_amountClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Win_amount"-------
while continueRoutine:
    # get current time
    t = Win_amountClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Win_amountClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_win_amount* updates
    if text_win_amount.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_win_amount.frameNStart = frameN  # exact frame index
        text_win_amount.tStart = t  # local t and not account for scr refresh
        text_win_amount.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_win_amount, 'tStartRefresh')  # time at next scr refresh
        text_win_amount.setAutoDraw(True)
    
    # *key_resp_win_amount* updates
    waitOnFlip = False
    if key_resp_win_amount.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_win_amount.frameNStart = frameN  # exact frame index
        key_resp_win_amount.tStart = t  # local t and not account for scr refresh
        key_resp_win_amount.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_win_amount, 'tStartRefresh')  # time at next scr refresh
        key_resp_win_amount.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_win_amount.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_win_amount.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_win_amount.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_win_amount.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_win_amount_allKeys.extend(theseKeys)
        if len(_key_resp_win_amount_allKeys):
            key_resp_win_amount.keys = _key_resp_win_amount_allKeys[-1].name  # just the last key pressed
            key_resp_win_amount.rt = _key_resp_win_amount_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Win_amountComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Win_amount"-------
for thisComponent in Win_amountComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_win_amount.started', text_win_amount.tStartRefresh)
thisExp.addData('text_win_amount.stopped', text_win_amount.tStopRefresh)
# check responses
if key_resp_win_amount.keys in ['', [], None]:  # No response was made
    key_resp_win_amount.keys = None
thisExp.addData('key_resp_win_amount.keys',key_resp_win_amount.keys)
if key_resp_win_amount.keys != None:  # we had a response
    thisExp.addData('key_resp_win_amount.rt', key_resp_win_amount.rt)
thisExp.addData('key_resp_win_amount.started', key_resp_win_amount.tStartRefresh)
thisExp.addData('key_resp_win_amount.stopped', key_resp_win_amount.tStopRefresh)
thisExp.nextEntry()
# the Routine "Win_amount" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "DisplayPracticeRT"-------
continueRoutine = True
# update component parameters for each repeat
mean_rt_ms = mean_rt *1000
block_feedback_msg = 'When you saw a non-triangle sign, \nyour reaction time was %smsec;\nyou did not respond for %s time(s).\nIncluding the triangle rounds, you did not respond %s percent of the time.'%(round(mean_rt_ms, 1), nonNeutralTrialOmission, round(TrialOmissionPercentage, 2))

#Informing participants about their omission errors on non-triangle and all trials. 
#omission means no key press at all, not including slow responses
#both non-triangle and all trial omission need to be < 20%; if the latter is higher than the former value, remind the participant to try to respond as much as they can, even if it's a triangle trial
# the mean_rt needs to be recorded to put in the scanner version later
text_block_feedback.setText(block_feedback_msg)
key_resp_block_feedback.keys = []
key_resp_block_feedback.rt = []
_key_resp_block_feedback_allKeys = []
# keep track of which components have finished
DisplayPracticeRTComponents = [text_block_feedback, key_resp_block_feedback]
for thisComponent in DisplayPracticeRTComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
DisplayPracticeRTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "DisplayPracticeRT"-------
while continueRoutine:
    # get current time
    t = DisplayPracticeRTClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=DisplayPracticeRTClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_block_feedback* updates
    if text_block_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_block_feedback.frameNStart = frameN  # exact frame index
        text_block_feedback.tStart = t  # local t and not account for scr refresh
        text_block_feedback.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_block_feedback, 'tStartRefresh')  # time at next scr refresh
        text_block_feedback.setAutoDraw(True)
    
    # *key_resp_block_feedback* updates
    waitOnFlip = False
    if key_resp_block_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_block_feedback.frameNStart = frameN  # exact frame index
        key_resp_block_feedback.tStart = t  # local t and not account for scr refresh
        key_resp_block_feedback.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_block_feedback, 'tStartRefresh')  # time at next scr refresh
        key_resp_block_feedback.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_block_feedback.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_block_feedback.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_block_feedback.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_block_feedback.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_block_feedback_allKeys.extend(theseKeys)
        if len(_key_resp_block_feedback_allKeys):
            key_resp_block_feedback.keys = _key_resp_block_feedback_allKeys[-1].name  # just the last key pressed
            key_resp_block_feedback.rt = _key_resp_block_feedback_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DisplayPracticeRTComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "DisplayPracticeRT"-------
for thisComponent in DisplayPracticeRTComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_block_feedback.started', text_block_feedback.tStartRefresh)
thisExp.addData('text_block_feedback.stopped', text_block_feedback.tStopRefresh)
# check responses
if key_resp_block_feedback.keys in ['', [], None]:  # No response was made
    key_resp_block_feedback.keys = None
thisExp.addData('key_resp_block_feedback.keys',key_resp_block_feedback.keys)
if key_resp_block_feedback.keys != None:  # we had a response
    thisExp.addData('key_resp_block_feedback.rt', key_resp_block_feedback.rt)
thisExp.addData('key_resp_block_feedback.started', key_resp_block_feedback.tStartRefresh)
thisExp.addData('key_resp_block_feedback.stopped', key_resp_block_feedback.tStopRefresh)
thisExp.nextEntry()
# the Routine "DisplayPracticeRT" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
