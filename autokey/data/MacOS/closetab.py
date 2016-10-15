# Enter script code
import re
winClass = window.get_active_class()
isKonsole = re.search("konsole\\.konsole", winClass)
isTerminal = re.search("x+terminal.*", winClass)
# isGoogleChrome = re.search("Google-chrome-stable\.Google-chrome-stable", winClass)
if isKonsole or isTerminal:
	keyboard.send_keys("<ctrl>+<shift>+w")
else:
    # Includes Google Chrome
	keyboard.send_keys("<ctrl>+w")