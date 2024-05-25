# Py-AudioSwitcher 
Python wrapper for AudioDeviceCmdlet

## Requirements
- Powershell AudioDeviceCmdlets module (`Install-Module -Name AudioDeviceCmdlets`)
- Python if not using the provided exe

## Usage
Specify audio output using `-o "Audio output name"`<br/>
This script rely on keywords for detection.<br/>
If your Device is called "Headset Earphone (CORSAIR Wireless)" you can specify `-o "Corsair Headset"` and it will work.
