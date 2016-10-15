#Enter script code
import commands, os

# File where last window id is stored
last_window_id_file = "~/.last_window_id"
last_window_id_file = os.path.expanduser(last_window_id_file)

# Get the current window id
current_window_id = commands.getstatusoutput("""xdpyinfo | grep -Eo 'window 0x[^,]+' | cut -d" " -f2""")

# Raise Konsole (this command raises the still-living, first-spawned console window)
raising_console_output = commands.getstatusoutput("wmctrl -x -a konsole.konsole")

# Get the new window id
new_window_id = commands.getstatusoutput("""xdpyinfo | grep -Eo 'window 0x[^,]+' | cut -d" " -f2""")

if current_window_id[1] == new_window_id[1]:
    # If the new window id and the current window id are the same, then we were already on the 
    # Konsole window and we need to switch to some other window.
    if os.path.isfile(last_window_id_file):
        # If the last_window_id_file exists, then switch to the last window
        # If not, switch to the Desktop (basically just take the focus away from the Konsole)
        with open(last_window_id_file, "r") as f:
            last_window_id = f.readline().rstrip('\n')

        raising_lastwindow_output = commands.getstatusoutput("wmctrl -i -a " + last_window_id)
    else:
        raising_lastwindow_output = commands.getstatusoutput("wmctrl -a Plasma")
else:
    # If the new window id and the old window id are not the same then our job is done.
    # All we need to to do is save the old window id into the file
    with open(last_window_id_file, "w") as f:
        f.write(current_window_id[1] + '\n')