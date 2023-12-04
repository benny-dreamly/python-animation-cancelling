# python-animation-cancelling
Stardew Valley animation cancelling script written in python that works cross-platform on macOS and Windows.

**Supported Operating Systems**

Works on MacOS and Windows. Unfortunately, it does not yet work on linux, but I am working on getting linux compatibility sorted. 

**Running the script**

On windows, simply run the script and it will check if your stardew valley is open. It works with SMAPI as well. If Stardew is not open, it will just close itself. 

On macOS, the keyboard library I am using to get keyboard presses and actually make the macro work requires administrator permissions to run. In order to get the script to run, use this command: ```sudo python3 macro.py``` If administrator permissions are not granted to the script, it will fail to run. 

**FAQ**

Why should I use this?

I decided to make this script because I couldn't find a way to do animation cancelling on my macbook. I downloaded an autohotkey script on my windows pc and it works flawlessly, but it just doesn't work on macOS. Hopefully you find this useful, and feel free to make any changes you feel are needed, or create an issue, and I can figure out how to get some additional features working.
