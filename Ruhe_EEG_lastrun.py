#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Mai 03, 2022, at 16:32
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'Ruhe_EEG'  # from the Builder filename that created this script
expInfo = {'participant': '', 'condition': '1', 'language': '1'}
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
    originPath='G:\\NACHSTUDIUM\\STUDIEN\\EEG_ManyLabs\\Ruhe_EEG_film_VR\\Ruhe_EEG_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

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

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruktion_ruhe_eeg"
Instruktion_ruhe_eegClock = core.Clock()
sound_2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1)
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Start_Ruhe_EEG"
Start_Ruhe_EEGClock = core.Clock()
sound_4 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_4')
sound_4.setVolume(1)
text_4 = visual.TextStim(win=win, name='text_4',
    text=None,
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
sound_1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1)
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Ende_Ruhe_EEG"
Ende_Ruhe_EEGClock = core.Clock()
sound_3 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1)
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
total = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Gesamt.xlsx'),
    seed=None, name='total')
thisExp.addLoop(total)  # add the loop to the experiment
thisTotal = total.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTotal.rgb)
if thisTotal != None:
    for paramName in thisTotal:
        exec('{} = thisTotal[paramName]'.format(paramName))

for thisTotal in total:
    currentLoop = total
    # abbreviate parameter names if possible (e.g. rgb = thisTotal.rgb)
    if thisTotal != None:
        for paramName in thisTotal:
            exec('{} = thisTotal[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instruktion_ruhe_eeg"-------
    # update component parameters for each repeat
    event.Mouse(visible=False)
    
    if int(expInfo['language']) == 1: 
        Instruction2 = Instruktion_D
        Texter1 = 'Starten mit der Leertaste'
    
    if int(expInfo['language']) == 2: 
        Instruction2 = Instruktion_E
        Texter1 = 'Press space to start'
    
    
    if int(expInfo['language']) == 3: 
        Instruction2 = Instruktion_F
        Texter1 = 'Appuyez sur l´ espace pour commencer'
    
    
    if int(expInfo['language']) == 4: 
        Instruction2 = Instruktion_S
        Texter1 = 'Pulse el espacio para empezar'
    
    
    if int(expInfo['language']) == 5: 
        Instruction2 = Instruktion_R
        Texter1 = 'Нажмите пробел, чтобы начать'
    
    
    
    sound_2.setSound(Instruction2, secs=50, hamming=True)
    sound_2.setVolume(1, log=False)
    text_5.setText(Texter1)
    key_resp_2.keys = []
    key_resp_2.rt = []
    # keep track of which components have finished
    Instruktion_ruhe_eegComponents = [sound_2, text_2, text_5, key_resp_2]
    for thisComponent in Instruktion_ruhe_eegComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Instruktion_ruhe_eegClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Instruktion_ruhe_eeg"-------
    while continueRoutine:
        # get current time
        t = Instruktion_ruhe_eegClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Instruktion_ruhe_eegClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play(when=win)  # sync with win flip
        if sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2.tStartRefresh + 50-frameTolerance:
                # keep track of stop time/frame for later
                sound_2.tStop = t  # not accounting for scr refresh
                sound_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
                sound_2.stop()
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 47-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 47-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 47-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_2.keys = theseKeys.name  # just the last key pressed
                key_resp_2.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruktion_ruhe_eegComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instruktion_ruhe_eeg"-------
    for thisComponent in Instruktion_ruhe_eegComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_2.stop()  # ensure sound has stopped at end of routine
    total.addData('sound_2.started', sound_2.tStartRefresh)
    total.addData('sound_2.stopped', sound_2.tStopRefresh)
    total.addData('text_2.started', text_2.tStartRefresh)
    total.addData('text_2.stopped', text_2.tStopRefresh)
    total.addData('text_5.started', text_5.tStartRefresh)
    total.addData('text_5.stopped', text_5.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    total.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        total.addData('key_resp_2.rt', key_resp_2.rt)
    total.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    total.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "Instruktion_ruhe_eeg" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Start_Ruhe_EEG.xlsx'),
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
        
        # ------Prepare to start Routine "Start_Ruhe_EEG"-------
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        
        if int(expInfo['language']) == 1: 
            Anfang2 = Anfang_D
        
        if int(expInfo['language']) == 2: 
            Anfang2 = Anfang_E
        
        
        if int(expInfo['language']) == 3: 
            Anfang2 = Anfang_F
        
        if int(expInfo['language']) == 4: 
            Anfang2 = Anfang_S
        
        if int(expInfo['language']) == 5: 
            Anfang2 = Anfang_R
        
        
        
        sound_4.setSound(Anfang2, secs=3, hamming=True)
        sound_4.setVolume(1, log=False)
        # keep track of which components have finished
        Start_Ruhe_EEGComponents = [sound_4, text_4]
        for thisComponent in Start_Ruhe_EEGComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Start_Ruhe_EEGClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Start_Ruhe_EEG"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Start_Ruhe_EEGClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Start_Ruhe_EEGClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop sound_4
            if sound_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_4.frameNStart = frameN  # exact frame index
                sound_4.tStart = t  # local t and not account for scr refresh
                sound_4.tStartRefresh = tThisFlipGlobal  # on global time
                sound_4.play(when=win)  # sync with win flip
            if sound_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_4.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_4.tStop = t  # not accounting for scr refresh
                    sound_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_4, 'tStopRefresh')  # time at next scr refresh
                    sound_4.stop()
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            if text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Start_Ruhe_EEGComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Start_Ruhe_EEG"-------
        for thisComponent in Start_Ruhe_EEGComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_4.stop()  # ensure sound has stopped at end of routine
        trials.addData('sound_4.started', sound_4.tStartRefresh)
        trials.addData('sound_4.stopped', sound_4.tStopRefresh)
        trials.addData('text_4.started', text_4.tStartRefresh)
        trials.addData('text_4.stopped', text_4.tStopRefresh)
    # completed 1 repeats of 'trials'
    
    
    # set up handler to look after randomisation of conditions etc
    resting_trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Ruhe_eeg_trials.xlsx'),
        seed=None, name='resting_trials')
    thisExp.addLoop(resting_trials)  # add the loop to the experiment
    thisResting_trial = resting_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisResting_trial.rgb)
    if thisResting_trial != None:
        for paramName in thisResting_trial:
            exec('{} = thisResting_trial[paramName]'.format(paramName))
    
    for thisResting_trial in resting_trials:
        currentLoop = resting_trials
        # abbreviate parameter names if possible (e.g. rgb = thisResting_trial.rgb)
        if thisResting_trial != None:
            for paramName in thisResting_trial:
                exec('{} = thisResting_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        routineTimer.add(60.000000)
        # update component parameters for each repeat
        
        if int(expInfo['language']) == 1: 
            Anweisungen = Anweisung_D
            Anweisungen2 = Anweisung2_D
        
        if int(expInfo['language']) == 2: 
            Anweisungen = Anweisung_E
            Anweisungen2 = Anweisung2_E
        
        if int(expInfo['language']) == 3: 
            Anweisungen = Anweisung_F
            Anweisungen2 = Anweisung2_F
        
        if int(expInfo['language']) == 4: 
            Anweisungen = Anweisung_S
            Anweisungen2 = Anweisung2_S
        
        
        if int(expInfo['language']) == 5: 
            Anweisungen = Anweisung_R
            Anweisungen2 = Anweisung2_R
        
        
        if int(expInfo['condition']) == 1: 
            Trigger = Trigger2
            sound_1.setSound(Anweisungen)
        
        if int(expInfo['condition']) == 2:
            Trigger = Trigger3
            sound_1.setSound(Anweisungen2)
        sound_1.setSound(Anweisung, secs=3, hamming=True)
        sound_1.setVolume(1, log=False)
        # keep track of which components have finished
        trialComponents = [sound_1, text]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop sound_1
            if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.tStart = t  # local t and not account for scr refresh
                sound_1.tStartRefresh = tThisFlipGlobal  # on global time
                sound_1.play(when=win)  # sync with win flip
            if sound_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_1.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_1.tStop = t  # not accounting for scr refresh
                    sound_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                    sound_1.stop()
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 60-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_1.stop()  # ensure sound has stopped at end of routine
        resting_trials.addData('sound_1.started', sound_1.tStartRefresh)
        resting_trials.addData('sound_1.stopped', sound_1.tStopRefresh)
        resting_trials.addData('text.started', text.tStartRefresh)
        resting_trials.addData('text.stopped', text.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'resting_trials'
    
    
    # ------Prepare to start Routine "Ende_Ruhe_EEG"-------
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    
    if int(expInfo['language']) == 1: 
        Ende2 = Ende_D
    
    if int(expInfo['language']) == 2: 
        Ende2 = Ende_E
    
    if int(expInfo['language']) == 3: 
        Ende2 = Ende_F
    
    if int(expInfo['language']) == 4: 
        Ende2 = Ende_S
    
    if int(expInfo['language']) == 5: 
        Ende2 = Ende_R
    
    
    sound_3.setSound(Ende2, secs=3, hamming=True)
    sound_3.setVolume(1, log=False)
    # keep track of which components have finished
    Ende_Ruhe_EEGComponents = [sound_3, text_3]
    for thisComponent in Ende_Ruhe_EEGComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Ende_Ruhe_EEGClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Ende_Ruhe_EEG"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Ende_Ruhe_EEGClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Ende_Ruhe_EEGClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_3
        if sound_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_3.frameNStart = frameN  # exact frame index
            sound_3.tStart = t  # local t and not account for scr refresh
            sound_3.tStartRefresh = tThisFlipGlobal  # on global time
            sound_3.play(when=win)  # sync with win flip
        if sound_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_3.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                sound_3.tStop = t  # not accounting for scr refresh
                sound_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_3, 'tStopRefresh')  # time at next scr refresh
                sound_3.stop()
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Ende_Ruhe_EEGComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Ende_Ruhe_EEG"-------
    for thisComponent in Ende_Ruhe_EEGComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_3.stop()  # ensure sound has stopped at end of routine
    total.addData('sound_3.started', sound_3.tStartRefresh)
    total.addData('sound_3.stopped', sound_3.tStopRefresh)
    total.addData('text_3.started', text_3.tStartRefresh)
    total.addData('text_3.stopped', text_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'total'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
