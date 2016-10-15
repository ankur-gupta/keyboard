# Enter script code
import re
winClass = window.get_active_class()
isGoogleChrome1 = re.search("google-chrome\.google-chrome", winClass)
isGoogleChrome2 = re.search("Google-chrome-stable\.Google-chrome-stable", winClass)
if isGoogleChrome1 or isGoogleChrome2:
	keyboard.send_keys("<ctrl>+0")
else:
	keyboard.send_keys("<super>+0")