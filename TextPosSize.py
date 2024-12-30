import pcbnew
import os
from pcbnew import wxPoint
from pcbnew import ActionPlugin, GetBoard
from . import TextPosSize_dialog

from . import TextPosSize_gui
import wx
class TextPosSize(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "TextSize&Postion 1.0"
        self.category = "Artistic PCBs"
        self.description = "Change the size and position of text on the PCB"
        self.show_toolbar_button = True # Optional, defaults to False
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'text.png') # Optional, defaults to ""

    def Run(self):


        dialog = TextPosSize_dialog.TextPosSizeDialog()
        dialog.Show()
    
        # dialog.Destroy()

TextPosSize().register() # Instantiate and register to Pcbnew



