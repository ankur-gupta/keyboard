# Settings for autokey 

These `autokey` settings make keyboard shortcuts in Kubuntu behave like in a Mac. Best used with a Mac keyboard. These settings require some modifications to Kubuntu Global shortcuts and Konsole shortcuts.

## Installation

0. Install `autokey`. Add it to autostart. Switch keyboard to 
1. Quit `autokey` if it's already running.
2. Backup existing settings in `~/.config/autokey`.
3. Git clone this repository.
4. Put this folder, named `autokey`, inside `~/.config` replacing existing 
`~/.config/autokey`. Even better solution is to clone this repository in a location where you keep your settings files and then symlink.
5. Start `autokey` (preferably using the GUI menu instead of command line).

### Suggested commands
```bash
# Clone keyboard to a location where you keep settings
mkdir -p ~/toolbox
git clone git@github.com:ankur-gupta/keyboard.git ~/toolbox/keyboard

# Backup existing autokey (this overwrites your old backup)
mv ~/.config/autokey ~/.config/autokey.bk

# Create a symlink
ln -s ~/toolbox/keyboard/autokey ~/.config/autokey

```