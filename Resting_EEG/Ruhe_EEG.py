#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.02), Februar 06, 2015, at 14:19
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui, parallel
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Ruhe_EEG'  # from the Builder filename that created this script
expInfo = {u'participant': u'', u'condition': u'1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

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
win = visual.Window(size=(1920, 1200), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Instruktion_ruhe_eeg"
Instruktion_ruhe_eegClock = core.Clock()
sound_2 = sound.Sound('A', secs=50)
sound_2.setVolume(1)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=None,    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text=u'Starten mit der Leertaste',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Start_Ruhe_EEG"
Start_Ruhe_EEGClock = core.Clock()
sound_4 = sound.Sound('A', secs=3)
sound_4.setVolume(1)
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text=None,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
sound_1 = sound.Sound('A', secs=3)
sound_1.setVolume(1)
text = visual.TextStim(win=win, ori=0, name='text',
    text=None,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
p_port = parallel.ParallelPort(address='0x0C10')


# Initialize components for Routine "Ende_Ruhe_EEG"
Ende_Ruhe_EEGClock = core.Clock()
sound_3 = sound.Sound('A', secs=3)
sound_3.setVolume(1)
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text=None,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
total = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('Gesamt.xlsx'),
    seed=None, name='total')
thisExp.addLoop(total)  # add the loop to the experiment
thisTotal = total.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTotal.rgb)
if thisTotal != None:
    for paramName in thisTotal.keys():
        exec(paramName + '= thisTotal.' + paramName)

for thisTotal in total:
    currentLoop = total
    # abbreviate parameter names if possible (e.g. rgb = thisTotal.rgb)
    if thisTotal != None:
        for paramName in thisTotal.keys():
            exec(paramName + '= thisTotal.' + paramName)
    
    #------Prepare to start Routine "Instruktion_ruhe_eeg"-------
    t = 0
    Instruktion_ruhe_eegClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    sound_2.setSound(Instruktion)
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    # keep track of which components have finished
    Instruktion_ruhe_eegComponents = []
    Instruktion_ruhe_eegComponents.append(sound_2)
    Instruktion_ruhe_eegComponents.append(text_2)
    Instruktion_ruhe_eegComponents.append(text_5)
    Instruktion_ruhe_eegComponents.append(key_resp_2)
    for thisComponent in Instruktion_ruhe_eegComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Instruktion_ruhe_eeg"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Instruktion_ruhe_eegClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_2
        if t >= 0.0 and sound_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_2.tStart = t  # underestimates by a little under one frame
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.play()  # start the sound (it finishes automatically)
        elif sound_2.status == STARTED and t >= (0.0 + (50-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_2.stop()  # stop the sound (if longer than duration)
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        elif text_2.status == STARTED and t >= (0.0 + (47-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_2.setAutoDraw(False)
        
        # *text_5* updates
        if t >= 47 and text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_5.tStart = t  # underestimates by a little under one frame
            text_5.frameNStart = frameN  # exact frame index
            text_5.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 47 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruktion_ruhe_eegComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "Instruktion_ruhe_eeg"-------
    for thisComponent in Instruktion_ruhe_eegComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
       key_resp_2.keys=None
    # store data for total (TrialHandler)
    total.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        total.addData('key_resp_2.rt', key_resp_2.rt)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('Start_Ruhe_EEG.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        #------Prepare to start Routine "Start_Ruhe_EEG"-------
        t = 0
        Start_Ruhe_EEGClock.reset()  # clock 
        frameN = -1
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        sound_4.setSound(Anfang)
        # keep track of which components have finished
        Start_Ruhe_EEGComponents = []
        Start_Ruhe_EEGComponents.append(sound_4)
        Start_Ruhe_EEGComponents.append(text_4)
        for thisComponent in Start_Ruhe_EEGComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Start_Ruhe_EEG"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Start_Ruhe_EEGClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop sound_4
            if t >= 0.0 and sound_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                sound_4.tStart = t  # underestimates by a little under one frame
                sound_4.frameNStart = frameN  # exact frame index
                sound_4.play()  # start the sound (it finishes automatically)
            elif sound_4.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
                sound_4.stop()  # stop the sound (if longer than duration)
            
            # *text_4* updates
            if t >= 0.0 and text_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_4.tStart = t  # underestimates by a little under one frame
                text_4.frameNStart = frameN  # exact frame index
                text_4.setAutoDraw(True)
            elif text_4.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_4.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Start_Ruhe_EEGComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Start_Ruhe_EEG"-------
        for thisComponent in Start_Ruhe_EEGComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
    # completed 1 repeats of 'trials'
    
    
    # set up handler to look after randomisation of conditions etc
    resting_trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('Ruhe_eeg_trials.xlsx'),
        seed=None, name='resting_trials')
    thisExp.addLoop(resting_trials)  # add the loop to the experiment
    thisResting_trial = resting_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisResting_trial.rgb)
    if thisResting_trial != None:
        for paramName in thisResting_trial.keys():
            exec(paramName + '= thisResting_trial.' + paramName)
    
    for thisResting_trial in resting_trials:
        currentLoop = resting_trials
        # abbreviate parameter names if possible (e.g. rgb = thisResting_trial.rgb)
        if thisResting_trial != None:
            for paramName in thisResting_trial.keys():
                exec(paramName + '= thisResting_trial.' + paramName)
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        routineTimer.add(60.000000)
        # update component parameters for each repeat
        sound_1.setSound(Anweisung)
        
        if int(expInfo['condition']) == 1: 
            Trigger = Trigger2
            sound_1.setSound(Anweisung)
        
        if int(expInfo['condition']) == 2:
            Trigger = Trigger3
            sound_1.setSound(Anweisung2)
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(sound_1)
        trialComponents.append(text)
        trialComponents.append(p_port)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop sound_1
            if t >= 0.0 and sound_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                sound_1.tStart = t  # underestimates by a little under one frame
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.play()  # start the sound (it finishes automatically)
            elif sound_1.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
                sound_1.stop()  # stop the sound (if longer than duration)
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t  # underestimates by a little under one frame
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            elif text.status == STARTED and t >= (0.0 + (60-win.monitorFramePeriod*0.75)): #most of one frame period left
                text.setAutoDraw(False)
            # *p_port* updates
            if t >= 0.0 and p_port.status == NOT_STARTED:
                # keep track of start time/frame for later
                p_port.tStart = t  # underestimates by a little under one frame
                p_port.frameNStart = frameN  # exact frame index
                p_port.status = STARTED
                win.callOnFlip(p_port.setData, int(Trigger))
            elif p_port.status == STARTED and t >= (0.0 + (0.015-win.monitorFramePeriod*0.75)): #most of one frame period left
                p_port.status = STOPPED
                win.callOnFlip(p_port.setData, int(0))
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if p_port.status == STARTED:
            win.callOnFlip(p_port.setData, int(0))
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'resting_trials'
    
    
    #------Prepare to start Routine "Ende_Ruhe_EEG"-------
    t = 0
    Ende_Ruhe_EEGClock.reset()  # clock 
    frameN = -1
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    sound_3.setSound(Ende)
    # keep track of which components have finished
    Ende_Ruhe_EEGComponents = []
    Ende_Ruhe_EEGComponents.append(sound_3)
    Ende_Ruhe_EEGComponents.append(text_3)
    for thisComponent in Ende_Ruhe_EEGComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Ende_Ruhe_EEG"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Ende_Ruhe_EEGClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_3
        if t >= 0.0 and sound_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_3.tStart = t  # underestimates by a little under one frame
            sound_3.frameNStart = frameN  # exact frame index
            sound_3.play()  # start the sound (it finishes automatically)
        elif sound_3.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_3.stop()  # stop the sound (if longer than duration)
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        elif text_3.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Ende_Ruhe_EEGComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Ende_Ruhe_EEG"-------
    for thisComponent in Ende_Ruhe_EEGComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'total'


win.close()
core.quit()
