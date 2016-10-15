# Enter script code
import re
winClass = window.get_active_class()
isGoogleChrome1 = re.search("google-chrome\.google-chrome", winClass)
isGoogleChrome2 = re.search("Google-chrome-stable\.Google-chrome-stable", winClass)
isTerminalWin = re.search("x+terminal.*", winClass)
isKonsole = re.search("konsole\\.konsole", winClass)

if isTerminalWin or isGoogleChrome1 or isGoogleChrome2:
	keyboard.send_keys("<ctrl>+<page_down>")
else:
	keyboard.send_keys("<alt>+<super>+<right>")