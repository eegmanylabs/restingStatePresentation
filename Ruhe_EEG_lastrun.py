#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on May 20, 2022, at 15:59
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, parallel
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'Resting_EEG'  # from the Builder filename that created this script
expInfo = {'participant': '', 'language': 'English', 'parellel port': '03F8'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Stimulus\\Documents\\Psychopy\\restingStatePresentation-main\\Ruhe_EEG_lastrun.py',
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
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
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

# Initialize components for Routine "Instruction_resting_EEG"
Instruction_resting_EEGClock = core.Clock()
import pandas 
import random
# Read in instruction from instruction file
fname = './Languages/' + expInfo['language'] + '/Instruction.xlsx'
instruction = pandas.read_excel(fname).iloc[0, 0]

# Define condition
condition = str(random.randint(1, 2))

sound_instruct = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_instruct')
sound_instruct.setVolume(1)
text_instruct = visual.TextStim(win=win, name='text_instruct',
    text='',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_instruct = keyboard.Keyboard()

# Initialize components for Routine "Start_resting_EEG"
Start_resting_EEGClock = core.Clock()
sound_start_recording = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_start_recording')
sound_start_recording.setVolume(1)

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
sound_trial = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_trial')
sound_trial.setVolume(1)
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "End_resting_EEG"
End_resting_EEGClock = core.Clock()
sound_end_recording = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_end_recording')
sound_end_recording.setVolume(1)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruction_resting_EEG"-------
continueRoutine = True
# update component parameters for each repeat
event.Mouse(visible=False)


sound_instruct.setSound('Languages/' + expInfo['language'] + '/Instruction_experiment.wav', secs=50, hamming=True)
sound_instruct.setVolume(1, log=False)
text_instruct.setText(instruction)
key_resp_instruct.keys = []
key_resp_instruct.rt = []
_key_resp_instruct_allKeys = []
# keep track of which components have finished
Instruction_resting_EEGComponents = [sound_instruct, text_instruct, key_resp_instruct]
for thisComponent in Instruction_resting_EEGComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruction_resting_EEGClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction_resting_EEG"-------
while continueRoutine:
    # get current time
    t = Instruction_resting_EEGClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruction_resting_EEGClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_instruct
    if sound_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sound_instruct.frameNStart = frameN  # exact frame index
        sound_instruct.tStart = t  # local t and not account for scr refresh
        sound_instruct.tStartRefresh = tThisFlipGlobal  # on global time
        sound_instruct.play(when=win)  # sync with win flip
    if sound_instruct.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sound_instruct.tStartRefresh + 50-frameTolerance:
            # keep track of stop time/frame for later
            sound_instruct.tStop = t  # not accounting for scr refresh
            sound_instruct.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sound_instruct, 'tStopRefresh')  # time at next scr refresh
            sound_instruct.stop()
    
    # *text_instruct* updates
    if text_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instruct.frameNStart = frameN  # exact frame index
        text_instruct.tStart = t  # local t and not account for scr refresh
        text_instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instruct, 'tStartRefresh')  # time at next scr refresh
        text_instruct.setAutoDraw(True)
    if text_instruct.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_instruct.tStartRefresh + 47-frameTolerance:
            # keep track of stop time/frame for later
            text_instruct.tStop = t  # not accounting for scr refresh
            text_instruct.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_instruct, 'tStopRefresh')  # time at next scr refresh
            text_instruct.setAutoDraw(False)
    
    # *key_resp_instruct* updates
    waitOnFlip = False
    if key_resp_instruct.status == NOT_STARTED and tThisFlip >= 35-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instruct.frameNStart = frameN  # exact frame index
        key_resp_instruct.tStart = t  # local t and not account for scr refresh
        key_resp_instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instruct, 'tStartRefresh')  # time at next scr refresh
        key_resp_instruct.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instruct.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instruct.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instruct.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instruct.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_instruct_allKeys.extend(theseKeys)
        if len(_key_resp_instruct_allKeys):
            key_resp_instruct.keys = _key_resp_instruct_allKeys[-1].name  # just the last key pressed
            key_resp_instruct.rt = _key_resp_instruct_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction_resting_EEGComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction_resting_EEG"-------
for thisComponent in Instruction_resting_EEGComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_instruct.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_instruct.started', sound_instruct.tStartRefresh)
thisExp.addData('sound_instruct.stopped', sound_instruct.tStopRefresh)
thisExp.addData('text_instruct.started', text_instruct.tStartRefresh)
thisExp.addData('text_instruct.stopped', text_instruct.tStopRefresh)
# check responses
if key_resp_instruct.keys in ['', [], None]:  # No response was made
    key_resp_instruct.keys = None
thisExp.addData('key_resp_instruct.keys',key_resp_instruct.keys)
if key_resp_instruct.keys != None:  # we had a response
    thisExp.addData('key_resp_instruct.rt', key_resp_instruct.rt)
thisExp.addData('key_resp_instruct.started', key_resp_instruct.tStartRefresh)
thisExp.addData('key_resp_instruct.stopped', key_resp_instruct.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instruction_resting_EEG" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start_resting_EEG"-------
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
sound_start_recording.setSound('Languages/' + expInfo['language'] + '/Instruction_start_recording.wav', secs=6, hamming=True)
sound_start_recording.setVolume(1, log=False)
# keep track of which components have finished
Start_resting_EEGComponents = [sound_start_recording]
for thisComponent in Start_resting_EEGComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Start_resting_EEGClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Start_resting_EEG"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Start_resting_EEGClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Start_resting_EEGClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_start_recording
    if sound_start_recording.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sound_start_recording.frameNStart = frameN  # exact frame index
        sound_start_recording.tStart = t  # local t and not account for scr refresh
        sound_start_recording.tStartRefresh = tThisFlipGlobal  # on global time
        sound_start_recording.play(when=win)  # sync with win flip
    if sound_start_recording.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sound_start_recording.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            sound_start_recording.tStop = t  # not accounting for scr refresh
            sound_start_recording.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sound_start_recording, 'tStopRefresh')  # time at next scr refresh
            sound_start_recording.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_resting_EEGComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_resting_EEG"-------
for thisComponent in Start_resting_EEGComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_start_recording.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_start_recording.started', sound_start_recording.tStartRefresh)
thisExp.addData('sound_start_recording.stopped', sound_start_recording.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Resting_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Cond' + condition + '_Resting_EEG_trials.xlsx'),
    seed=None, name='Resting_trials')
thisExp.addLoop(Resting_trials)  # add the loop to the experiment
thisResting_trial = Resting_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisResting_trial.rgb)
if thisResting_trial != None:
    for paramName in thisResting_trial:
        exec('{} = thisResting_trial[paramName]'.format(paramName))

for thisResting_trial in Resting_trials:
    currentLoop = Resting_trials
    # abbreviate parameter names if possible (e.g. rgb = thisResting_trial.rgb)
    if thisResting_trial != None:
        for paramName in thisResting_trial:
            exec('{} = thisResting_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Trial"-------
    continueRoutine = True
    routineTimer.add(63.000000)
    # update component parameters for each repeat
    if int(condition) == 1: 
        Trigger = 253
    elif int(condition) == 2:
        Trigger = 254
    
    sound_trial.setSound('Languages/' + expInfo['language'] + '/' + Instruction_trials, secs=3, hamming=True)
    sound_trial.setVolume(1, log=False)
    # keep track of which components have finished
    TrialComponents = [sound_trial, fixation_cross]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_trial
        if sound_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_trial.frameNStart = frameN  # exact frame index
            sound_trial.tStart = t  # local t and not account for scr refresh
            sound_trial.tStartRefresh = tThisFlipGlobal  # on global time
            sound_trial.play(when=win)  # sync with win flip
        if sound_trial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_trial.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                sound_trial.tStop = t  # not accounting for scr refresh
                sound_trial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_trial, 'tStopRefresh')  # time at next scr refresh
                sound_trial.stop()
        
        # *fixation_cross* updates
        if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.tStart = t  # local t and not account for scr refresh
            fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(True)
        if fixation_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_cross.tStartRefresh + 63.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation_cross.tStop = t  # not accounting for scr refresh
                fixation_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_cross, 'tStopRefresh')  # time at next scr refresh
                fixation_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_trial.stop()  # ensure sound has stopped at end of routine
    Resting_trials.addData('sound_trial.started', sound_trial.tStartRefresh)
    Resting_trials.addData('sound_trial.stopped', sound_trial.tStopRefresh)
    Resting_trials.addData('fixation_cross.started', fixation_cross.tStartRefresh)
    Resting_trials.addData('fixation_cross.stopped', fixation_cross.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Resting_trials'


# ------Prepare to start Routine "End_resting_EEG"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
sound_end_recording.setSound('Languages/' + expInfo['language'] + '/Instruction_end_recording.wav', secs=9, hamming=True)
sound_end_recording.setVolume(1, log=False)
# keep track of which components have finished
End_resting_EEGComponents = [sound_end_recording]
for thisComponent in End_resting_EEGComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
End_resting_EEGClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End_resting_EEG"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = End_resting_EEGClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=End_resting_EEGClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_end_recording
    if sound_end_recording.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
        # keep track of start time/frame for later
        sound_end_recording.frameNStart = frameN  # exact frame index
        sound_end_recording.tStart = t  # local t and not account for scr refresh
        sound_end_recording.tStartRefresh = tThisFlipGlobal  # on global time
        sound_end_recording.play(when=win)  # sync with win flip
    if sound_end_recording.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sound_end_recording.tStartRefresh + 9-frameTolerance:
            # keep track of stop time/frame for later
            sound_end_recording.tStop = t  # not accounting for scr refresh
            sound_end_recording.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sound_end_recording, 'tStopRefresh')  # time at next scr refresh
            sound_end_recording.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in End_resting_EEGComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End_resting_EEG"-------
for thisComponent in End_resting_EEGComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_end_recording.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_end_recording.started', sound_end_recording.tStartRefresh)
thisExp.addData('sound_end_recording.stopped', sound_end_recording.tStopRefresh)

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
