# Enter script code
import re
winClass = window.get_active_class()
isTerminalWin1 = re.search("konsole\\.konsole", winClass)
isTerminalWin2 = re.search("x+terminal.*", winClass)
if isTerminalWin1 or isTerminalWin2:
        keyboard.send_keys("<ctrl>+<shift>+t")
else:
        keyboard.send_keys("<ctrl>+t")
