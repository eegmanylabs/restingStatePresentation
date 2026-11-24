# Resting state EEG: PsychoPy

Authors:
Dr. rer. nat. Johannes Rodrigues, Dipl. Psych. Julius-Maximilians University of Würzburg. johannes.rodrigues@uni-wuerzburg.de;
Yuri Pavlov, University of Tuebingen, pavlovug@gmail.com;
Nick Menger, University of Tuebingen, nickmenger@hotmail.com

There are 8 trials of one minute each: four minutes of eyes-open and four minutes of eyes-closed in total. The trial order is in the files Cond1_Resting_EEG_trials.xlsx and Cond2_Resting_EEG_trials.xlsx (one of them is chosen at random for each participant).

The commands to open and close the eyes are presented via loudspeakers in the language of your choice. Check the available languages in the Languages folder. If your language is not available, please write to Yuri Pavlov for instructions.

## What you need

* Windows and PsychoPy 2022.1.3 or newer. It was tested with PsychoPy 2022.1.3, 2022.2.5, 2023.1.2, 2023.2.3, 2024.1.5, 2024.2.4, 2025.2.4, 2026.2.4 and 2026.2.5.
* Open `Ruhe_EEG.psyexp` in the PsychoPy Builder and run it from there. Do not run a `.py` file made on another computer: Builder writes the script for the PsychoPy version you have.

## The dialog box at the start

| Field | What to enter |
|---|---|
| participant | the participant code |
| language | choose from the menu (the names are the folder names in `Languages`) |
| trigger device | choose from the menu how the triggers reach your EEG system (see below) |
| port address | where the trigger device is connected (see below) |

| trigger device | port address | What is sent for trigger code 7 |
|---|---|---|
| parallel port | for example `0x3FF8`, `0x378`, `0xD010` | the 8 data pins of the parallel (LPT) port are set to 7 |
| serial port (byte) | for example `COM3` | one byte with the value 7 (most USB trigger boxes) |
| serial port (text) | for example `COM3` | the text `7` |
| Cedrus | not used | Cedrus StimTracker, c-pod or m-pod |
| LSL | not used | a marker in a Lab Streaming Layer stream called `PsychoPyMarkers` |
| no EEG (test) | not used | nothing is sent; the codes are printed. For trying out the experiment on any computer |

With the parallel port and the serial ports, the port is set to 0 when the experiment starts; each trigger then stays on for at least 15 ms and the port is set back to 0. Cedrus devices end the trigger themselves after 15 ms.

The serial port is opened at 115200 baud for `serial port (byte)` and at 9600 baud for `serial port (text)`. If your device needs another speed, change it at the top of the trigger code (see "Changing the trigger code").

With LSL nothing is set back to 0, a marker is a single event. With some PsychoPy versions (2024 and 2025 in our tests) the recording nevertheless contains one extra marker 0 at the very end: the LSL library of these versions adds it when the experiment closes the stream. It can be ignored.

LSL needs the Python package `pylsl` and Cedrus needs `pyxid2` and the Cedrus driver. The standard PsychoPy installer contains both packages; in PsychoPy Studio they have to be installed first.

If you used the Luck (1996) #EEGManyLabs script: `parallel` there is `parallel port` here, `ghent` is `serial port (byte)`, `serial` is `serial port (text)`, `cedrus` is `Cedrus` and `noEEGtest` is `no EEG (test)`.

## Set the defaults for your lab (once)

So that nobody has to choose the right entries for every participant:

1. In Builder, click the cog-wheel icon ("Edit experiment settings").
2. On the first tab, find "Experiment info". It is a small table with the columns Field and Default.
3. In the row `trigger device`, replace the whole content by the name of your device, for example `parallel port` (just these words: no brackets, no quotation marks).
4. In the row `port address`, type your address, for example `0x378` or `COM3`.
5. In the row `language`, replace the whole content by your language, for example `German`.
6. Press OK and save the experiment.

A field whose default is a list like `['English', 'German']` is shown as a menu, and the first entry is the one that is preselected. A list must have at least two entries; for a single fixed value type plain text as described above.

## Trigger codes

| Code | Meaning |
|---|---|
| 7 | start of the recording, order 1: the first minute is eyes open (o-c-c-o-c-o-o-c) |
| 8 | start of the recording, order 2: the first minute is eyes closed (c-o-o-c-o-c-c-o) |
| 1 | a minute with eyes open starts |
| 2 | a minute with eyes closed starts |

Each trigger is sent at the moment its voice command starts.

**Check that the triggers arrive in your EEG recording before you collect data of your first participant.** Start a recording, run the experiment and look for a 7 or 8 right after the space bar is pressed, a 1 or 2 six seconds later, and then a 1 or 2 every 63 seconds.

After a session you can also check what the computer sent: the `.log` file in the folder `data` has a line "TRIGGER ... sent" for every trigger, and the `.csv` file has the columns `Condition_Trigger` and `Triggers`.

## Parallel port

* **Port address.** Windows Device Manager > Ports (COM & LPT) > your LPT port > Properties > Resources. The address is the first number of the "I/O Range", written with `0x` in front, for example `0x3FF8`.
* **Driver.** PsychoPy talks to the parallel port through the file `inpoutx64.dll`. PsychoPy up to 2024.1 contains this file, the newer installers (checked: 2024.2.4, 2025.2.4, 2026.2.4) do not. That is why a copy is in this folder: leave it next to `Ruhe_EEG.psyexp`.
* **First use on a computer.** The driver installs itself the first time it is used, and Windows only allows that for an administrator. If the experiment says "the parallel port driver is not running": close PsychoPy, start it once with a right-click > "Run as administrator", run the experiment once, then use PsychoPy normally again.

`inpoutx64.dll` is the InpOutx64 driver by Phillip Gibbons (https://www.highrez.co.uk/downloads/inpout32/); the copy in this folder is the one that is distributed with PsychoPy 2022.1.3.

## If something is wrong

The experiment checks the language files and the trigger device before it starts, and shows a message on the screen instead of failing in the middle of a recording.

| Message | What to do |
|---|---|
| SETTINGS PROBLEM ... field is missing | A row was deleted from "Experiment info". The rows `language`, `trigger device` and `port address` are needed. |
| LANGUAGE PROBLEM ... files are missing | The folder of that language is incomplete or a file name is misspelled. |
| TRIGGER PROBLEM ... driver file inpoutx64.dll was not found | Put `inpoutx64.dll` next to `Ruhe_EEG.psyexp` (see "Parallel port"). |
| TRIGGER PROBLEM ... driver is not running | Start PsychoPy once as administrator (see "Parallel port"). |
| TRIGGER PROBLEM ... could not open port 'COM3' | Wrong port name, or another program is using the port. |
| TEST MODE: NO TRIGGERS ARE SENT TO THE EEG (red, on the instruction screen) | The trigger device "no EEG (test)" was chosen. Do not record a participant like this. |

No message does not prove that triggers arrive: a wrong parallel port address or an unplugged cable cannot be detected by the computer. Always look at the EEG recording.

## Changing the trigger code

All trigger code is in one place: routine `Instruction_resting_EEG` > code component `code_triggers` > tab "Begin Experiment". At its top are the settings (how long a trigger stays on, the speed of the serial port). Each trigger device is one short block that defines `write_port(code)`; to add another device, copy a block and change it.

The routines `Start_resting_EEG` and `Trial` each have a small code component directly below their sound component. In its tab "Each Frame" it calls `send_trigger(code)` when the voice command starts, so the trigger and the sound start at the same screen refresh, and `update_trigger()`, which sets the port back to 0. Keep these code components below the sound components.

## Adding a language

Make a new folder in `Languages` with the same seven files as the other languages (`Instruction.xlsx` and six `.wav` files with exactly the same names). Then add the folder name to the list in the row `language` of "Experiment info" (see "Set the defaults for your lab").

## What changed compared with the first version

* The trigger device is chosen in the dialog box at the start; before, only the parallel port could be used. The field `LPTport` is now called `port address`.
* The trigger codes are the same. As before, a trigger is sent when the voice command starts and the port is set back to 0 after 15 ms.
* The language is chosen from a menu.
* The experiment checks the language files and the trigger device at the start and explains on the screen what is wrong.
* It runs in PsychoPy 2022.1.3 and newer. Three things that stopped the first version in some PsychoPy versions are taken care of:
  * PsychoPy 2023.1.2 and 2023.1.3 stopped with the error `'SoundPTB' object has no attribute 'isFinished'` when a voice command had finished (an error in those two PsychoPy versions).
  * With the standard settings of PsychoPy 2022.1, the Italian and Polish voice commands (recorded at 48 kHz) stopped the experiment. The experiment now always uses PsychoPy's "ptb" sound engine.
  * The PsychoPy installers from 2024.2 on no longer contain the parallel port driver file; it is now in this folder.
* The misspelled file name in the Chinese folder is corrected.
* The compiled script `Ruhe_EEG.py` is no longer part of the package, because a compiled script only fits the PsychoPy version that wrote it.

IMPORTANT NOTE: THERE IS NO WARRANTY INCLUDED ! -> GNU
