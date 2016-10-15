# Enter script code
import re
winClass = window.get_active_class()
isGoogleChrome1 = re.search("google-chrome\.", winClass)
# isGoogleChrome1 = re.search("google-chrome\.google-chrome", winClass)
isGoogleChrome2 = re.search("Google-chrome-stable\.Google-chrome-stable", winClass)
isTerminal = re.search("x+terminal.*", winClass)

# For this to work, you need to setup <ctrl+1> as the shortcut
# manually within Konsole. There should be a konsole.shortcuts
# file in the autokey repository that can be imported within
# Konsole instead of manual setup.
isKonsole = re.search("konsole\\.konsole", winClass)

if isGoogleChrome1 or isGoogleChrome2 or isKonsole:
    keyboard.send_keys("<ctrl>+9")
else:
    keyboard.send_keys("<super>+9")

