import os
import eel
from engine.command import *
from engine.features import *

eel.init("www")

playAssistantSound()

os.system('start msedge.exe --app="http://localhost:5500/index.html"')  ## Open in app mode like notepad

eel.start('index.html', mode=None, host='localhost', port=5500, block=True)