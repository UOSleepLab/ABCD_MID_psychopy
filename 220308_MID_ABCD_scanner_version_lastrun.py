#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on July 25, 2022, at 18:51
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
expName = '220308_MID_ABCD_scanner_version'  # from the Builder filename that created this script
expInfo = {'participant': '', 'handedness(l/r/a)': 'r', 'visit': '001/002', 'run': '001', 'trialorder': '1', 'averageRT': '300'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'], expInfo['visit'], expInfo['run'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\OSLadmin\\Desktop\\22MoTasks\\220707MID_psychopy\\220308_MID_ABCD_scanner_version_lastrun.py',
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
    text='MID',
    font='Open Sans',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_TitlePage = keyboard.Keyboard()
AdjUserRT = 0
TheProbeDuration = 0.3
# default probe duration before any adjustment and when previous RT (practice or visit 1) not available
# the task always maintain a reasonable degree of difficulty
if float(expInfo['averageRT']) > 500:
    TheProbeDuration = 500/1000 
elif float(expInfo['averageRT']) < 150:
    TheProbeDuration = 150/1000 
else:
    TheProbeDuration = float(expInfo['averageRT'])/1000
AdjUserRT = TheProbeDuration
# at this point, RT is in msec, psychopy use sec; may change later if recorded RT is also in sec, so no need to do /1000

final_compensation = 0

index_finger_key = '6'
if expInfo['handedness(l/r/a)'] == 'l':
    index_finger_key = '3'
'''
ABCD used a one-button response pad and they 
had any key as correct key press in their behavioral and practice e-prime files
'''

# Initialize components for Routine "BlockInstructions"
BlockInstructionsClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='Images/MID_Instructions.bmp', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.4, 1.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_instr = keyboard.Keyboard()

# Initialize components for Routine "Waiting4Scanner"
Waiting4ScannerClock = core.Clock()
text_Waiting4Scanner = visual.TextStim(win=win, name='text_Waiting4Scanner',
    text='Waiting for experimenter ...',
    font='Open Sans',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_Waiting4Scanner = keyboard.Keyboard()
wait_buffer_text = visual.TextStim(win=win, name='wait_buffer_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "PrepTime"
PrepTimeClock = core.Clock()
text_PrepTime = visual.TextStim(win=win, name='text_PrepTime',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
run_counter = 0
block_TrialNum = 0
block_nonNeutralTrialNum = 0
block_nonNeutralTrialOmission = 0
block_nonNeutralTrialOmissionPercentage = 0
block_TrialOmission = 0
block_TrialOmissionPercentage = 0

round_counter = 0

block_rt_list = []
block_acc_list = []
block_overall_mean_acc = 0
block_mean_rt = 0

prbacc = 0
prbrt = 0
mean_acc = 0
round_acc = 0

# Initialize components for Routine "Cue_slide"
Cue_slideClock = core.Clock()
image_Cue_slide = visual.ImageStim(
    win=win,
    name='image_Cue_slide', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_Cue_slide = keyboard.Keyboard()

# Initialize components for Routine "Anticipation_slide"
Anticipation_slideClock = core.Clock()
text_Anticipation_slide = visual.TextStim(win=win, name='text_Anticipation_slide',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_Anticipation_slide = keyboard.Keyboard()
anticipation_key_press = 0

# Initialize components for Routine "Probe_slide"
Probe_slideClock = core.Clock()
image_Probe_slide = visual.ImageStim(
    win=win,
    name='image_Probe_slide', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_Probe_slide = keyboard.Keyboard()
probe_key_press = 0
TrialNum = 0
nonNeutralTrialNum = 0
rt_list = []
acc_list = []

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
key_resp_Feedback = keyboard.Keyboard()
feedback = ""
ResponseCheck = ""
Result= ""
updated_trial_type = ''
nonNeutralTrialOmission = 0
nonNeutralTrialOmissionPercentage = 0
TrialOmission = 0
TrialOmissionPercentage = 0
mean_rt = 0
overall_mean_acc = 0
Omission_flag = 0
text_Feedback = visual.TextStim(win=win, name='text_Feedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.095, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "EndFix"
EndFixClock = core.Clock()
text_EndFix = visual.TextStim(win=win, name='text_EndFix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Block_feedback"
Block_feedbackClock = core.Clock()
# default block feedback msg when no block-based red flag was raised 
block_feedback_msg = ''
text_block_feedback = visual.TextStim(win=win, name='text_block_feedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_block_feedback = keyboard.Keyboard()

# Initialize components for Routine "Win_amount"
Win_amountClock = core.Clock()
win_amount = ''
text_win_amount = visual.TextStim(win=win, name='text_win_amount',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_win_amount = keyboard.Keyboard()

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
        theseKeys = key_resp_TitlePage.getKeys(keyList=['space'], waitRelease=False)
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

# set up handler to look after randomisation of conditions etc
trials_RunProc = data.TrialHandler(nReps=(3-int(expInfo['run'])), method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_RunProc')
thisExp.addLoop(trials_RunProc)  # add the loop to the experiment
thisTrials_RunProc = trials_RunProc.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_RunProc.rgb)
if thisTrials_RunProc != None:
    for paramName in thisTrials_RunProc:
        exec('{} = thisTrials_RunProc[paramName]'.format(paramName))

for thisTrials_RunProc in trials_RunProc:
    currentLoop = trials_RunProc
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_RunProc.rgb)
    if thisTrials_RunProc != None:
        for paramName in thisTrials_RunProc:
            exec('{} = thisTrials_RunProc[paramName]'.format(paramName))
    
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
            theseKeys = key_resp_instr.getKeys(keyList=['space', index_finger_key], waitRelease=False)
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
    trials_RunProc.addData('image.started', image.tStartRefresh)
    trials_RunProc.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp_instr.keys in ['', [], None]:  # No response was made
        key_resp_instr.keys = None
    trials_RunProc.addData('key_resp_instr.keys',key_resp_instr.keys)
    if key_resp_instr.keys != None:  # we had a response
        trials_RunProc.addData('key_resp_instr.rt', key_resp_instr.rt)
    trials_RunProc.addData('key_resp_instr.started', key_resp_instr.tStartRefresh)
    trials_RunProc.addData('key_resp_instr.stopped', key_resp_instr.tStopRefresh)
    # the Routine "BlockInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Waiting4Scanner"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_Waiting4Scanner.keys = []
    key_resp_Waiting4Scanner.rt = []
    _key_resp_Waiting4Scanner_allKeys = []
    # keep track of which components have finished
    Waiting4ScannerComponents = [text_Waiting4Scanner, key_resp_Waiting4Scanner, wait_buffer_text]
    for thisComponent in Waiting4ScannerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Waiting4ScannerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Waiting4Scanner"-------
    while continueRoutine:
        # get current time
        t = Waiting4ScannerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Waiting4ScannerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Waiting4Scanner* updates
        if text_Waiting4Scanner.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            text_Waiting4Scanner.frameNStart = frameN  # exact frame index
            text_Waiting4Scanner.tStart = t  # local t and not account for scr refresh
            text_Waiting4Scanner.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Waiting4Scanner, 'tStartRefresh')  # time at next scr refresh
            text_Waiting4Scanner.setAutoDraw(True)
        
        # *key_resp_Waiting4Scanner* updates
        waitOnFlip = False
        if key_resp_Waiting4Scanner.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_Waiting4Scanner.frameNStart = frameN  # exact frame index
            key_resp_Waiting4Scanner.tStart = t  # local t and not account for scr refresh
            key_resp_Waiting4Scanner.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_Waiting4Scanner, 'tStartRefresh')  # time at next scr refresh
            key_resp_Waiting4Scanner.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_Waiting4Scanner.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_Waiting4Scanner.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_Waiting4Scanner.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_Waiting4Scanner.getKeys(keyList=['apostrophe'], waitRelease=False)
            _key_resp_Waiting4Scanner_allKeys.extend(theseKeys)
            if len(_key_resp_Waiting4Scanner_allKeys):
                key_resp_Waiting4Scanner.keys = _key_resp_Waiting4Scanner_allKeys[-1].name  # just the last key pressed
                key_resp_Waiting4Scanner.rt = _key_resp_Waiting4Scanner_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *wait_buffer_text* updates
        if wait_buffer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait_buffer_text.frameNStart = frameN  # exact frame index
            wait_buffer_text.tStart = t  # local t and not account for scr refresh
            wait_buffer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait_buffer_text, 'tStartRefresh')  # time at next scr refresh
            wait_buffer_text.setAutoDraw(True)
        if wait_buffer_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wait_buffer_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                wait_buffer_text.tStop = t  # not accounting for scr refresh
                wait_buffer_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wait_buffer_text, 'tStopRefresh')  # time at next scr refresh
                wait_buffer_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Waiting4ScannerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Waiting4Scanner"-------
    for thisComponent in Waiting4ScannerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_RunProc.addData('text_Waiting4Scanner.started', text_Waiting4Scanner.tStartRefresh)
    trials_RunProc.addData('text_Waiting4Scanner.stopped', text_Waiting4Scanner.tStopRefresh)
    # check responses
    if key_resp_Waiting4Scanner.keys in ['', [], None]:  # No response was made
        key_resp_Waiting4Scanner.keys = None
    trials_RunProc.addData('key_resp_Waiting4Scanner.keys',key_resp_Waiting4Scanner.keys)
    if key_resp_Waiting4Scanner.keys != None:  # we had a response
        trials_RunProc.addData('key_resp_Waiting4Scanner.rt', key_resp_Waiting4Scanner.rt)
    trials_RunProc.addData('key_resp_Waiting4Scanner.started', key_resp_Waiting4Scanner.tStartRefresh)
    trials_RunProc.addData('key_resp_Waiting4Scanner.stopped', key_resp_Waiting4Scanner.tStopRefresh)
    trials_RunProc.addData('wait_buffer_text.started', wait_buffer_text.tStartRefresh)
    trials_RunProc.addData('wait_buffer_text.stopped', wait_buffer_text.tStopRefresh)
    # the Routine "Waiting4Scanner" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "PrepTime"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    round_counter = 0
    # at the beginning and reset trials at 0 after run1
    run_counter += 1
    block_TrialNum = 0
    block_nonNeutralTrialNum = 0
    block_nonNeutralTrialOmission = 0
    block_nonNeutralTrialOmissionPercentage = 0
    block_TrialOmission = 0
    block_TrialOmissionPercentage = 0
    
    block_rt_list = []
    block_acc_list = []
    block_overall_mean_acc = 0
    block_mean_rt = 0
    
    AdjUserRT = 0
    TheProbeDuration = 0.3
    # default probe duration before any adjustment and when previous RT (practice or visit 1) not available
    # the task always maintain a reasonable degree of difficulty
    if float(expInfo['averageRT']) > 500:
        TheProbeDuration = 500/1000 
    elif float(expInfo['averageRT']) < 150:
        TheProbeDuration = 150/1000 
    else:
        TheProbeDuration = float(expInfo['averageRT'])/1000
    AdjUserRT = TheProbeDuration
    
    prbacc = 0
    prbrt = 0
    mean_acc = 0
    round_acc = 0
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
            if tThisFlipGlobal > text_PrepTime.tStartRefresh + 2-frameTolerance:
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
    trials_RunProc.addData('text_PrepTime.started', text_PrepTime.tStartRefresh)
    trials_RunProc.addData('text_PrepTime.stopped', text_PrepTime.tStopRefresh)
    if int(expInfo['run']) == 1 and run_counter == 1:
        if int(expInfo['trialorder']) == 1:
            conditions_file = 'Time_versions/MID_ABCD_time_version5.xlsx'
    else:
        conditions_file = 'Time_versions/MID_ABCD_time_version16.xlsx'
    
    """
    if int(expInfo['run']) == 1 and run_counter == 1:
        if int(expInfo['trialorder']) == 1:
            conditions_file = 'Time_versions/MID_ABCD_time_version5.xlsx'
    else:
        conditions_file = 'Time_versions/MID_ABCD_time_version16.xlsx'
    
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
    """
    
    # set up handler to look after randomisation of conditions etc
    trials_RewardProc = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(conditions_file),
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
        image_Cue_slide.setImage(Cue)
        key_resp_Cue_slide.keys = []
        key_resp_Cue_slide.rt = []
        _key_resp_Cue_slide_allKeys = []
        # keep track of which components have finished
        Cue_slideComponents = [image_Cue_slide, key_resp_Cue_slide]
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
            
            # *key_resp_Cue_slide* updates
            waitOnFlip = False
            if key_resp_Cue_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_Cue_slide.frameNStart = frameN  # exact frame index
                key_resp_Cue_slide.tStart = t  # local t and not account for scr refresh
                key_resp_Cue_slide.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_Cue_slide, 'tStartRefresh')  # time at next scr refresh
                key_resp_Cue_slide.status = STARTED
                # AllowedKeys looks like a variable named `index_finger_key`
                if not type(index_finger_key) in [list, tuple, np.ndarray]:
                    if not isinstance(index_finger_key, str):
                        logging.error('AllowedKeys variable `index_finger_key` is not string- or list-like.')
                        core.quit()
                    elif not ',' in index_finger_key:
                        index_finger_key = (index_finger_key,)
                    else:
                        index_finger_key = eval(index_finger_key)
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_Cue_slide.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_Cue_slide.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_Cue_slide.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_Cue_slide.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_Cue_slide.tStop = t  # not accounting for scr refresh
                    key_resp_Cue_slide.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_Cue_slide, 'tStopRefresh')  # time at next scr refresh
                    key_resp_Cue_slide.status = FINISHED
            if key_resp_Cue_slide.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_Cue_slide.getKeys(keyList=list(index_finger_key), waitRelease=False)
                _key_resp_Cue_slide_allKeys.extend(theseKeys)
                if len(_key_resp_Cue_slide_allKeys):
                    key_resp_Cue_slide.keys = _key_resp_Cue_slide_allKeys[0].name  # just the first key pressed
                    key_resp_Cue_slide.rt = _key_resp_Cue_slide_allKeys[0].rt
            
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
        trials_RewardProc.addData('image_Cue_slide.started', image_Cue_slide.tStartRefresh)
        trials_RewardProc.addData('image_Cue_slide.stopped', image_Cue_slide.tStopRefresh)
        # check responses
        if key_resp_Cue_slide.keys in ['', [], None]:  # No response was made
            key_resp_Cue_slide.keys = None
        trials_RewardProc.addData('key_resp_Cue_slide.keys',key_resp_Cue_slide.keys)
        if key_resp_Cue_slide.keys != None:  # we had a response
            trials_RewardProc.addData('key_resp_Cue_slide.rt', key_resp_Cue_slide.rt)
        trials_RewardProc.addData('key_resp_Cue_slide.started', key_resp_Cue_slide.tStartRefresh)
        trials_RewardProc.addData('key_resp_Cue_slide.stopped', key_resp_Cue_slide.tStopRefresh)
        
        # ------Prepare to start Routine "Anticipation_slide"-------
        continueRoutine = True
        # update component parameters for each repeat
        text_Anticipation_slide.setText('+')
        key_resp_Anticipation_slide.keys = []
        key_resp_Anticipation_slide.rt = []
        _key_resp_Anticipation_slide_allKeys = []
        anticipation_key_press = 0
        # keep track of which components have finished
        Anticipation_slideComponents = [text_Anticipation_slide, key_resp_Anticipation_slide]
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
        while continueRoutine:
            # get current time
            t = Anticipation_slideClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Anticipation_slideClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
                if tThisFlipGlobal > text_Anticipation_slide.tStartRefresh + Anticipation-frameTolerance:
                    # keep track of stop time/frame for later
                    text_Anticipation_slide.tStop = t  # not accounting for scr refresh
                    text_Anticipation_slide.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_Anticipation_slide, 'tStopRefresh')  # time at next scr refresh
                    text_Anticipation_slide.setAutoDraw(False)
            
            # *key_resp_Anticipation_slide* updates
            waitOnFlip = False
            if key_resp_Anticipation_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_Anticipation_slide.frameNStart = frameN  # exact frame index
                key_resp_Anticipation_slide.tStart = t  # local t and not account for scr refresh
                key_resp_Anticipation_slide.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_Anticipation_slide, 'tStartRefresh')  # time at next scr refresh
                key_resp_Anticipation_slide.status = STARTED
                # AllowedKeys looks like a variable named `index_finger_key`
                if not type(index_finger_key) in [list, tuple, np.ndarray]:
                    if not isinstance(index_finger_key, str):
                        logging.error('AllowedKeys variable `index_finger_key` is not string- or list-like.')
                        core.quit()
                    elif not ',' in index_finger_key:
                        index_finger_key = (index_finger_key,)
                    else:
                        index_finger_key = eval(index_finger_key)
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_Anticipation_slide.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_Anticipation_slide.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_Anticipation_slide.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_Anticipation_slide.tStartRefresh + Anticipation-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_Anticipation_slide.tStop = t  # not accounting for scr refresh
                    key_resp_Anticipation_slide.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_Anticipation_slide, 'tStopRefresh')  # time at next scr refresh
                    key_resp_Anticipation_slide.status = FINISHED
            if key_resp_Anticipation_slide.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_Anticipation_slide.getKeys(keyList=list(index_finger_key), waitRelease=False)
                _key_resp_Anticipation_slide_allKeys.extend(theseKeys)
                if len(_key_resp_Anticipation_slide_allKeys):
                    key_resp_Anticipation_slide.keys = _key_resp_Anticipation_slide_allKeys[0].name  # just the first key pressed
                    key_resp_Anticipation_slide.rt = _key_resp_Anticipation_slide_allKeys[0].rt
            
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
        trials_RewardProc.addData('text_Anticipation_slide.started', text_Anticipation_slide.tStartRefresh)
        trials_RewardProc.addData('text_Anticipation_slide.stopped', text_Anticipation_slide.tStopRefresh)
        # check responses
        if key_resp_Anticipation_slide.keys in ['', [], None]:  # No response was made
            key_resp_Anticipation_slide.keys = None
        trials_RewardProc.addData('key_resp_Anticipation_slide.keys',key_resp_Anticipation_slide.keys)
        if key_resp_Anticipation_slide.keys != None:  # we had a response
            trials_RewardProc.addData('key_resp_Anticipation_slide.rt', key_resp_Anticipation_slide.rt)
        trials_RewardProc.addData('key_resp_Anticipation_slide.started', key_resp_Anticipation_slide.tStartRefresh)
        trials_RewardProc.addData('key_resp_Anticipation_slide.stopped', key_resp_Anticipation_slide.tStopRefresh)
        if key_resp_Anticipation_slide.keys != None:
            anticipation_key_press = 1
        # the Routine "Anticipation_slide" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Probe_slide"-------
        continueRoutine = True
        # update component parameters for each repeat
        image_Probe_slide.setImage(Probe)
        key_resp_Probe_slide.keys = []
        key_resp_Probe_slide.rt = []
        _key_resp_Probe_slide_allKeys = []
        TrialNum += 1
        block_TrialNum += 1
        if Condition != "Triangle":
            nonNeutralTrialNum += 1
            block_nonNeutralTrialNum += 1
        # keep track of which components have finished
        Probe_slideComponents = [image_Probe_slide, key_resp_Probe_slide]
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
            
            # *key_resp_Probe_slide* updates
            waitOnFlip = False
            if key_resp_Probe_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_Probe_slide.frameNStart = frameN  # exact frame index
                key_resp_Probe_slide.tStart = t  # local t and not account for scr refresh
                key_resp_Probe_slide.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_Probe_slide, 'tStartRefresh')  # time at next scr refresh
                key_resp_Probe_slide.status = STARTED
                # AllowedKeys looks like a variable named `index_finger_key`
                if not type(index_finger_key) in [list, tuple, np.ndarray]:
                    if not isinstance(index_finger_key, str):
                        logging.error('AllowedKeys variable `index_finger_key` is not string- or list-like.')
                        core.quit()
                    elif not ',' in index_finger_key:
                        index_finger_key = (index_finger_key,)
                    else:
                        index_finger_key = eval(index_finger_key)
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
                theseKeys = key_resp_Probe_slide.getKeys(keyList=list(index_finger_key), waitRelease=False)
                _key_resp_Probe_slide_allKeys.extend(theseKeys)
                if len(_key_resp_Probe_slide_allKeys):
                    key_resp_Probe_slide.keys = _key_resp_Probe_slide_allKeys[0].name  # just the first key pressed
                    key_resp_Probe_slide.rt = _key_resp_Probe_slide_allKeys[0].rt
            
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
        trials_RewardProc.addData('image_Probe_slide.started', image_Probe_slide.tStartRefresh)
        trials_RewardProc.addData('image_Probe_slide.stopped', image_Probe_slide.tStopRefresh)
        # check responses
        if key_resp_Probe_slide.keys in ['', [], None]:  # No response was made
            key_resp_Probe_slide.keys = None
        trials_RewardProc.addData('key_resp_Probe_slide.keys',key_resp_Probe_slide.keys)
        if key_resp_Probe_slide.keys != None:  # we had a response
            trials_RewardProc.addData('key_resp_Probe_slide.rt', key_resp_Probe_slide.rt)
        trials_RewardProc.addData('key_resp_Probe_slide.started', key_resp_Probe_slide.tStartRefresh)
        trials_RewardProc.addData('key_resp_Probe_slide.stopped', key_resp_Probe_slide.tStopRefresh)
        probe_key_press = 0
        if key_resp_Probe_slide.keys != None:
            probe_key_press = 1
        feedback_duration = 2000/1000 - TheProbeDuration
        '''
        It used to be feedback_duration = 1950/1000 - TheProbeDuration
        The same as ABCD's 2016 eprime version. 
        I suspect the 50ms empty text_display1 slide was added back then due to 
        e-prime accurate timing issues.
        So with psychopy, I removed that display slide 50ms as I
        think it was causing omission errors when participants pressed a key near
        the end of the anticipation slide.
        ''' 
        # the Routine "Probe_slide" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Feedback"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_Feedback.keys = []
        key_resp_Feedback.rt = []
        _key_resp_Feedback_allKeys = []
        if anticipation_key_press == 1:
            ResponseCheck = "You pressed too soon!"
            prbacc = 0
            prbrt = 0
            # here cue_slide press doesn't count as too soon to be consistent
            # with ABCD's 20161218 version
        elif anticipation_key_press == 0 and probe_key_press == 1:
            ResponseCheck = "Correct response!"
            prbacc = 1
            prbrt = key_resp_Probe_slide.rt
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
        
        test_omission = "%s"%(block_TrialOmission)
        
        # only gather probe response accuracy for non-neutral trials
        # only compute probe response time average for non-neutral correct trials
        if Condition != "Triangle":
            acc_list.append(prbacc)
            block_acc_list.append(prbacc)
            if prbacc == 1:
                rt_list.append(prbrt)
                block_rt_list.append(prbrt)
        
        rt_array = np.array(rt_list)
        block_rt_array = np.array(block_rt_list)
        
        # mean_rt is the cumulative non-neutral correct trial rt average
        if len(rt_list) > 0:
            mean_rt = rt_array.mean()
        if len(block_rt_list) > 0:
            block_mean_rt = block_rt_array.mean()
        
        if len(acc_list) > 0:
            acc_array = np.array(acc_list)
            # overall_mean_acc is the cumulative non-neutral trial acc/hit average
            overall_mean_acc = acc_array.mean()*100
            # ideally around 60%
        if len(block_acc_list) > 0:
            block_acc_array = np.array(block_acc_list)
            block_overall_mean_acc = block_acc_array.mean()*100
            # ideally around 60%
        
        feedback = ResponseCheck + "\n" + Result
        # debug: test_feedback = ResponseCheck + "\n" + str(prbrt) + "\n" + str(Trials) + str(nonNeutralTrialNum) +"\n" + str(mean_acc) + str(round_acc) + "\n" + str(overall_mean_acc) + "\n" + str(TheProbeDuration)
        
        text_Feedback.setText(feedback)
        # keep track of which components have finished
        FeedbackComponents = [key_resp_Feedback, text_Feedback]
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
        while continueRoutine:
            # get current time
            t = FeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_Feedback* updates
            waitOnFlip = False
            if key_resp_Feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_Feedback.frameNStart = frameN  # exact frame index
                key_resp_Feedback.tStart = t  # local t and not account for scr refresh
                key_resp_Feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_Feedback, 'tStartRefresh')  # time at next scr refresh
                key_resp_Feedback.status = STARTED
                # AllowedKeys looks like a variable named `index_finger_key`
                if not type(index_finger_key) in [list, tuple, np.ndarray]:
                    if not isinstance(index_finger_key, str):
                        logging.error('AllowedKeys variable `index_finger_key` is not string- or list-like.')
                        core.quit()
                    elif not ',' in index_finger_key:
                        index_finger_key = (index_finger_key,)
                    else:
                        index_finger_key = eval(index_finger_key)
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_Feedback.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_Feedback.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_Feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_Feedback.tStartRefresh + feedback_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_Feedback.tStop = t  # not accounting for scr refresh
                    key_resp_Feedback.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_Feedback, 'tStopRefresh')  # time at next scr refresh
                    key_resp_Feedback.status = FINISHED
            if key_resp_Feedback.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_Feedback.getKeys(keyList=list(index_finger_key), waitRelease=False)
                _key_resp_Feedback_allKeys.extend(theseKeys)
                if len(_key_resp_Feedback_allKeys):
                    key_resp_Feedback.keys = _key_resp_Feedback_allKeys[0].name  # just the first key pressed
                    key_resp_Feedback.rt = _key_resp_Feedback_allKeys[0].rt
            
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
                if tThisFlipGlobal > text_Feedback.tStartRefresh + feedback_duration-frameTolerance:
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
        if key_resp_Feedback.keys in ['', [], None]:  # No response was made
            key_resp_Feedback.keys = None
        trials_RewardProc.addData('key_resp_Feedback.keys',key_resp_Feedback.keys)
        if key_resp_Feedback.keys != None:  # we had a response
            trials_RewardProc.addData('key_resp_Feedback.rt', key_resp_Feedback.rt)
        trials_RewardProc.addData('key_resp_Feedback.started', key_resp_Feedback.tStartRefresh)
        trials_RewardProc.addData('key_resp_Feedback.stopped', key_resp_Feedback.tStopRefresh)
        # "The probe duration is adjusted every three trials starting at trial 7"
        # so the first 6 non-neutral trials will be used to calibrate trial 7 probe's duration
        # then every 3 non-neutral trials, RT is adjusted based on the average between the last (3 NNT) and the recent (3 NNT) accs
        if block_nonNeutralTrialNum == (6 + round_counter*3):
            if block_nonNeutralTrialNum == 6:
                mean_acc = block_overall_mean_acc
                round_acc = block_overall_mean_acc
            else:
                round_acc = block_acc_array[(block_nonNeutralTrialNum-3):(block_nonNeutralTrialNum)].mean()*100
                mean_acc = (prev_acc + round_acc)/2
        # adjust probe duration adatively
        if block_nonNeutralTrialNum == (6 + round_counter*3):
            if mean_acc < 5:
                AdjUserRT = AdjUserRT + 70/1000
            elif mean_acc < 15:
                AdjUserRT = AdjUserRT + 60/1000
            elif mean_acc < 25:
                AdjUserRT = AdjUserRT + 50/1000
            elif mean_acc < 35:
                AdjUserRT = AdjUserRT + 40/1000
            elif mean_acc < 45:
                AdjUserRT = AdjUserRT + 30/1000
            elif mean_acc < 55:
                AdjUserRT = AdjUserRT + 20/1000
            elif mean_acc > 95:
                AdjUserRT = AdjUserRT - 50/1000
            elif mean_acc > 85:
                AdjUserRT = AdjUserRT - 40/1000
            elif mean_acc > 75:
                AdjUserRT = AdjUserRT - 30/1000
            elif mean_acc > 65:
                AdjUserRT = AdjUserRT - 20/1000
            TheProbeDuration = AdjUserRT
            round_counter += 1
            prev_acc = round_acc
        
        # note, the following omission count is overly-sensitive 
        # and it appears that key presses right in-between the routines are missed 
        # and treated as omissions. Probably due to the delay between key press and 
        # and it getting registered, and the possible lag between routines. 
        if key_resp_Anticipation_slide.keys in ['', [], None] and key_resp_Probe_slide.keys in ['', [], None] and key_resp_Cue_slide.keys in ['', [], None] and key_resp_Feedback.keys in ['', [], None]:
            Omission_flag = 1 
            TrialOmission += 1
            block_TrialOmission += 1
            TrialOmissionPercentage = nonNeutralTrialOmission/TrialNum*100
            block_TrialOmissionPercentage = block_nonNeutralTrialOmission/block_TrialNum*100
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
        thisExp.addData('Recordedmean_rt', mean_rt)
        
        thisExp.addData('Recordedround_counter', round_counter)
        thisExp.addData('nonNeutralTrialNum', nonNeutralTrialNum)
        thisExp.addData('block_nonNeutralTrialNum', block_nonNeutralTrialNum)
        thisExp.addData('AdjUserRT', AdjUserRT)
        thisExp.addData('overall_mean_acc', overall_mean_acc)
        thisExp.addData('block_overall_mean_acc', block_overall_mean_acc)
        thisExp.addData('round_acc', round_acc)
        thisExp.addData('mean_acc', mean_acc)
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
        # debug variables
        # thisExp.addData('test_key_resp_Anticipation_slide.keys', key_resp_Anticipation_slide.keys)
        # thisExp.addData('test_key_resp_Probe_slide.keys', key_resp_Probe_slide.keys)
        # thisExp.addData('test_key_resp_cue_slide.keys', key_resp_cue_slide.keys)
        # thisExp.addData('test_key_resp_feedback.keys', key_resp_feedback.keys)
        trials_RewardProc.addData('text_Feedback.started', text_Feedback.tStartRefresh)
        trials_RewardProc.addData('text_Feedback.stopped', text_Feedback.tStopRefresh)
        # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
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
    
    # ------Prepare to start Routine "EndFix"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    EndFixComponents = [text_EndFix]
    for thisComponent in EndFixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    EndFixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "EndFix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EndFixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=EndFixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_EndFix* updates
        if text_EndFix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_EndFix.frameNStart = frameN  # exact frame index
            text_EndFix.tStart = t  # local t and not account for scr refresh
            text_EndFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_EndFix, 'tStartRefresh')  # time at next scr refresh
            text_EndFix.setAutoDraw(True)
        if text_EndFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_EndFix.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                text_EndFix.tStop = t  # not accounting for scr refresh
                text_EndFix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_EndFix, 'tStopRefresh')  # time at next scr refresh
                text_EndFix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndFixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "EndFix"-------
    for thisComponent in EndFixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_RunProc.addData('text_EndFix.started', text_EndFix.tStartRefresh)
    trials_RunProc.addData('text_EndFix.stopped', text_EndFix.tStopRefresh)
    
    # ------Prepare to start Routine "Block_feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    block_feedback_msg = 'When you saw a non-triangle sign, \nyou successfully responded %s percent of the time.'%(round(block_overall_mean_acc, 2))
    
    #Informing participants about their omission errors on non-triangle trials.
    #It needs to be < 20%
    text_block_feedback.setText(block_feedback_msg)
    key_resp_block_feedback.keys = []
    key_resp_block_feedback.rt = []
    _key_resp_block_feedback_allKeys = []
    # keep track of which components have finished
    Block_feedbackComponents = [text_block_feedback, key_resp_block_feedback]
    for thisComponent in Block_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block_feedback"-------
    while continueRoutine:
        # get current time
        t = Block_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block_feedbackClock)
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
        for thisComponent in Block_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block_feedback"-------
    for thisComponent in Block_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_RunProc.addData('text_block_feedback.started', text_block_feedback.tStartRefresh)
    trials_RunProc.addData('text_block_feedback.stopped', text_block_feedback.tStopRefresh)
    # check responses
    if key_resp_block_feedback.keys in ['', [], None]:  # No response was made
        key_resp_block_feedback.keys = None
    trials_RunProc.addData('key_resp_block_feedback.keys',key_resp_block_feedback.keys)
    if key_resp_block_feedback.keys != None:  # we had a response
        trials_RunProc.addData('key_resp_block_feedback.rt', key_resp_block_feedback.rt)
    trials_RunProc.addData('key_resp_block_feedback.started', key_resp_block_feedback.tStartRefresh)
    trials_RunProc.addData('key_resp_block_feedback.stopped', key_resp_block_feedback.tStopRefresh)
    # the Routine "Block_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed (3-int(expInfo['run'])) repeats of 'trials_RunProc'


# ------Prepare to start Routine "Win_amount"-------
continueRoutine = True
# update component parameters for each repeat
if int(expInfo['visit']) == 1:
    if final_compensation < 10:
        final_compensation = 10
elif int(expInfo['visit']) == 2:
    if final_compensation < 5:
        final_compensation = 5

win_amount = 'All done!\n You just won $%s.'%(round(final_compensation, 1))

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
