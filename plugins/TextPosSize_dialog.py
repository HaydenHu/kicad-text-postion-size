#!/usr/bin/env python

# Teardrop for pcbnew using filled zones
# This is the plugin WX dialog
# (c) Niluje 2019 thewireddoesntexist.org
#
# Based on Teardrops for PCBNEW by svofski, 2014 http://sensi.org/~svo
# Cubic Bezier upgrade by mitxela, 2021 mitxela.com

import json
from re import S
import wx
import pcbnew
import os
import time
from .TextPosSize_gui import TextPosSize_gui
# from .TextPos import __version__


#Add Preset Manager. It creates a json file in the plugin folder and takes values from the Height, Wight, and thickness strings of each type of text when the save preset button is clicked.
class PresetManager:
    def __init__(self):
        plugin_dir = os.path.dirname(os.path.abspath(__file__))
        self.presets_file = os.path.join(plugin_dir, "presets_TPS.json")
        self.presets = self.load_presets()

    def load_presets(self):
        if os.path.exists(self.presets_file):
            with open(self.presets_file, "r") as file:
                return json.load(file)
        else:
            with open(self.presets_file, "w") as file:
                json.dump({}, file, indent=4)
            return {}

    def add_preset(self, name, ref, value, other):
        self.presets[name] = {"Reference": ref, "Value": value, "Other": other}
        self.save_presets()

    def save_presets(self):
        with open(self.presets_file, "w") as file:
            json.dump(self.presets, file, indent=4)

    def get_preset(self, name):
        return self.presets.get(name, None)



class TextPosSizeDialog(TextPosSize_gui):
    """Class that gathers all the Gui control"""

    def __init__(self):
        """Init the brand new instance"""
        super(TextPosSizeDialog, self).__init__(None)
        self.SetTitle("Text Size & Position")
        self.text_type=1

        self.preset_manager = PresetManager()
        self.update_preset_combobox()
        self.preset_combobox.Bind(wx.EVT_COMBOBOX, self.on_preset_selected)

        self.but_manage_presets.Bind(wx.EVT_BUTTON, self.onManagePresets)
        self.text_ref.Bind(wx.EVT_CHECKBOX, self.OnCheckTextRef)
        self.text_ref.SetValue(False)
        self.text_value.Bind(wx.EVT_CHECKBOX, self.OnCheckTextValue)
        self.text_value.SetValue(False)
        self.text_other.Bind(wx.EVT_CHECKBOX, self.OnCheckTextOther)
        self.text_other.SetValue(False)

        self.size_enable.Bind(wx.EVT_CHECKBOX, self.OnCheckSizeEnable)
        self.size_enable.SetValue(False)
        self.size_set=self.size_enable.GetValue()

        self.ref_width.Bind(wx.EVT_TEXT, self.OnTextSizeSet)
        self.ref_width_value=self.ref_width.GetValue()
        self.ref_height.Bind(wx.EVT_TEXT, self.OnTextSizeSet)
        self.ref_height_value=self.ref_height.GetValue()
        self.ref_thickness.Bind(wx.EVT_TEXT, self.OnTextSizeSet)
        self.ref_thickness_value=self.ref_thickness.GetValue()
        self.value_width.Bind(wx.EVT_TEXT, self.OnTextSizeSet)
        self.value_width_value=self.value_width.GetValue()
        self.value_height.Bind(wx.EVT_TEXT, self.OnTextSizeSet)
        self.value_height_value=self.value_height.GetValue()
        self.value_thickness.Bind(wx.EVT_TEXT, self.OnTextSizeSet)
        self.value_thickness_value=self.value_thickness.GetValue()
        self.other_width.Bind(wx.EVT_TEXT, self.OnTextSizeSet)
        self.other_width_value=self.other_width.GetValue()
        self.other_height.Bind(wx.EVT_TEXT, self.OnTextSizeSet)
        self.other_height_value=self.other_height.GetValue()
        self.other_thickness.Bind(wx.EVT_TEXT, self.OnTextSizeSet)
        self.other_thickness_value=self.other_thickness.GetValue()

        self.pos_enable.Bind(wx.EVT_CHECKBOX, self.OnCheckPosEnable)
        self.pos_enable.SetValue(False)
        self.pos_set=self.pos_enable.GetValue()

        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)
        self.Bind(wx.EVT_CLOSE, self.onCloseWindow)
        self.but_cancel.Bind(wx.EVT_BUTTON, self.onCloseWindow)
        self.but_ok.Bind(wx.EVT_BUTTON, self.onProcessAction)
        self.rb1.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)
        self.rb2.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)
        self.rb3.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)
        self.rb4.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)
        self.rb5.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)
        self.rb6.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)
        self.rb7.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)
        self.rb8.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)
        self.rb9.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)
        self.selected_rb=self.rb5
        self.offset.Bind(wx.EVT_TEXT, self.OnTextOffset)
        self.offset.SetValue(pcbnew.ToMM(0.1))
        self.offset_value=self.offset.GetValue()
        self.ref_hide.Bind(wx.EVT_CHECKBOX, self.OnCheckRefHide)
        self.ref_hide.SetValue(False)
        self.ref_hide_check=self.ref_hide.GetValue()

        self.m_onlyProcessSelection.Bind(wx.EVT_CHECKBOX, self.OnCheckOnlyProcessSelection)
        self.only_process_selection=False
        self.m_onlyProcessSelection.SetValue(True)
        self.only_process_selection=self.m_onlyProcessSelection.GetValue()

        self.but_process_sequentially.Bind(wx.EVT_BUTTON, self.onProcessSequentially)
        self.but_next_component.Bind(wx.EVT_BUTTON, self.onNextComponent)

        self.check_text_type_selection()

        self.current_footprint_index = 0

    def OnCheckTextRef(self,event):
        self.check_text_type_selection()
    def OnCheckTextValue(self,event):
        self.check_text_type_selection()
    def OnCheckTextOther(self,event):
        self.check_text_type_selection()
    def OnCheckSizeEnable(self,event):
        self.size_set=event.GetEventObject().GetValue()
    def OnTextSizeSet(self,event):
        self.ref_width_value=self.ref_width.GetValue()
        self.ref_height_value=self.ref_height.GetValue()
        self.ref_thickness_value=self.ref_thickness.GetValue()
        self.value_width_value=self.value_width.GetValue()
        self.value_height_value=self.value_height.GetValue()
        self.value_thickness_value=self.value_thickness.GetValue()
        self.other_width_value=self.other_width.GetValue()
        self.other_height_value=self.other_height.GetValue()
        self.other_thickness_value=self.other_thickness.GetValue()


    def update_preset_combobox(self):
        presets = list(self.preset_manager.presets.keys())
        self.preset_combobox.Clear()
        self.preset_combobox.AppendItems(presets)

    def onManagePresets(self, event):
        dialog = PresetDialog(self, self.preset_manager)
        dialog.ShowModal()
        dialog.Destroy()
        self.update_preset_combobox()

    def on_preset_selected(self, event):
        selected_preset_name = self.preset_combobox.GetValue()
        preset = self.preset_manager.get_preset(selected_preset_name)
        if preset:
            self.ref_width.SetValue(preset["Reference"]["width"])
            self.ref_height.SetValue(preset["Reference"]["height"])
            self.ref_thickness.SetValue(preset["Reference"]["thickness"])
            self.value_width.SetValue(preset["Value"]["width"])
            self.value_height.SetValue(preset["Value"]["height"])
            self.value_thickness.SetValue(preset["Value"]["thickness"])
            self.other_width.SetValue(preset["Other"]["width"])
            self.other_height.SetValue(preset["Other"]["height"])
            self.other_thickness.SetValue(preset["Other"]["thickness"])
            self.OnTextSizeSet(None)


    def OnCheckPosEnable(self,event):
        self.pos_set=event.GetEventObject().GetValue()
    def OnTextOffset(self,event):
        self.offset_value=event.GetEventObject().GetValue()

    def OnCheckOnlyProcessSelection(self,event ):
        self.only_process_selection = event.GetEventObject().GetValue()
    def OnCheckRefHide(self, event):
        self.ref_hide_check=event.GetEventObject().GetValue()
    def OnRadiogroup(self, event):
        """Enables or disables the parameters/options elements"""
        self.selected_rb = event.GetEventObject()
        # wx.MessageBox(str(rb))

    def process_components_sequentially(self):
        board = pcbnew.GetBoard()
        footprints = board.GetFootprints()
        if not footprints:
            wx.MessageBox("No footprints found on the board.", "Error", wx.OK | wx.ICON_ERROR)
            return

        if self.current_footprint_index >= len(footprints):
            wx.MessageBox("All footprints have been processed.", "Info", wx.OK | wx.ICON_INFORMATION)
            self.current_footprint_index = 0  
            return

        footprint = footprints[self.current_footprint_index]
        self.focus_on_component(footprint)  
        self.current_footprint_index += 1

    def onProcessSequentially(self, event):
        self.process_components_sequentially()

    def onNextComponent(self, event):
        self.process_components_sequentially()

    def focus_on_component(self, footprint):
        for fp in pcbnew.GetBoard().GetFootprints():
            fp.ClearSelected()
        pcbnew.FocusOnItem(footprint)  #Focuses on the component. This new feature is a feature that is available in pcbnew. If the correct scale is selected, you can see a clear focus on the component (it may be worthwhile to make an auto scale in the future (but I did not succeed))
        footprint.SetSelected()
        pcbnew.Refresh()  

    def onCloseWindow(self, event):
        self.current_footprint_index = 0  
        return self.EndModal(wx.ID_CANCEL)


    def onProcessAction(self, event):
        self.process_text(self.text_type)
        # self.clear_fields()

    def onCloseWindow(self, event):
        return self.EndModal(wx.ID_CANCEL)
    def check_text_type_selection(self):
        if self.text_ref.GetValue():
            self.text_type|=1
        else:
            self.text_type&=~1
        if self.text_value.GetValue():
            self.text_type|=(1<<1)
        else:
            self.text_type&=~(1<<1)
        if self.text_other.GetValue():
            self.text_type|=(1<<2)
        else:
            self.text_type&=~(1<<2)
    
    def set_text(self,text_type,position):
        board=pcbnew.GetBoard()
        footprints=board.GetFootprints()
        for footprint in footprints:
            reference=footprint.Reference()
            value=footprint.Value()
            footprint_items=footprint.GraphicalItems()
            if self.only_process_selection:
                if not footprint.IsSelected():
                    continue
            if self.ref_hide_check:
                self.clear_fields(footprint)
                if  text_type&1:
                    reference.SetVisible(False)
                else:
                    reference.SetVisible(True)
                if text_type&2:
                    value.SetVisible(False)
                else:
                    value.SetVisible(True)
                if text_type&4:
                    for item in footprint_items:
                        if type(item)==pcbnew.PCB_TEXT and item.GetLayer()==pcbnew.F_Fab:
                            item.SetVisible(False)
                else:
                    pass
            if self.pos_set:
                if text_type&1:
                    self.set_position(footprint,reference,position)
                if text_type&2:                
                    self.set_position(footprint,value,position)
                if text_type&4:
                    for item in footprint_items:
                        if type(item)==pcbnew.PCB_TEXT and item.GetLayer()==pcbnew.F_Fab:
                            self.set_position(footprint,item,position)
                else:
                    pass
            else:
                pass
            if self.size_set:
                if text_type&1:
                    self.set_size(reference,self.ref_width_value,self.ref_height_value,self.ref_thickness_value)
                if text_type&2:
                    self.set_size(value,self.value_width_value,self.value_height_value,self.value_thickness_value)
                if text_type&4:
                    for item in footprint_items:
                        if type(item)==pcbnew.PCB_TEXT and item.GetLayer()==pcbnew.F_Fab:
                            self.set_size(item,self.other_width_value,self.other_height_value,self.other_thickness_value)
                else:
                    pass
        pcbnew.Refresh()



    def process_text(self,text_type):
        if self.selected_rb==self.rb1:
            self.set_text(text_type,position=1)
        elif self.selected_rb==self.rb2:
            self.set_text(text_type,position=2)
        elif self.selected_rb==self.rb3:    
            self.set_text(text_type,position=3)
        elif self.selected_rb==self.rb4:
            self.set_text(text_type,position=4)
        elif self.selected_rb==self.rb5:
            self.set_text(text_type,position=5)
        elif self.selected_rb==self.rb6:
            self.set_text(text_type,position=6)
        elif self.selected_rb==self.rb7:
            self.set_text(text_type,position=7)
        elif self.selected_rb==self.rb8:
            self.set_text(text_type,position=8)
        elif self.selected_rb==self.rb9:
            self.set_text(text_type,position=9)
        else:
            pass
 
    def set_position(self,footprint,item,position):
        offset_value=pcbnew.FromMM(self.offset_value)
        footprint_width,footprint_height=footprint.GetBoundingBox().GetWidth(),footprint.GetBoundingBox().GetHeight()
        pos0=footprint.GetPosition()
        top_pos=pcbnew.VECTOR2I(pos0.x,int(pos0.y-footprint_height/2-offset_value))  
        bottom_pos=pcbnew.VECTOR2I(pos0.x,int(pos0.y+footprint_height/2+offset_value))
        left_pos=pcbnew.VECTOR2I(pos0.x-int(footprint_width/2+offset_value),pos0.y)
        right_pos=pcbnew.VECTOR2I(int(pos0.x+footprint_width/2+offset_value),pos0.y)
        center_pos=pcbnew.VECTOR2I(pos0.x,pos0.y)
        left_top_pos=pcbnew.VECTOR2I(int(pos0.x-footprint_width/2-offset_value),int(pos0.y-footprint_height/2-offset_value))  
        left_bottom_pos=pcbnew.VECTOR2I(int(pos0.x-footprint_width/2-offset_value),int(pos0.y+footprint_height/2+offset_value))   
        right_top_pos=pcbnew.VECTOR2I(int(pos0.x+footprint_width/2+offset_value),int(pos0.y-footprint_height/2-offset_value))
        right_bottom_pos=pcbnew.VECTOR2I(int(pos0.x+footprint_width/2+offset_value),int(pos0.y+footprint_height/2+offset_value))
        if position==1:
            item.SetPosition(left_top_pos)
        elif position==2:
            item.SetPosition(top_pos)
        elif position==3:
            item.SetPosition(right_top_pos)
        elif position==4:
            item.SetPosition(left_pos)
        elif position==5:
            item.SetPosition(center_pos)
        elif position==6:
            item.SetPosition(right_pos)
        elif position==7:
            item.SetPosition(left_bottom_pos)
        elif position==8:
            item.SetPosition(bottom_pos)
        elif position==9:
            item.SetPosition(right_bottom_pos)
        else:
            pass
    def set_size(self,item,width,height,thickness):
        item.SetTextSize(pcbnew.VECTOR2I(pcbnew.FromMM(width),pcbnew.FromMM(height)))
        item.SetTextThickness(pcbnew.FromMM(thickness)) 

    def clear_fields(self,footprint):
        # footprint.GetField("Reference").SetVisible(True)
        # fields=footprint.RemoveField("Field6")
        for footprint in pcbnew.GetBoard().GetFootprints():
            if footprint.IsSelected():
                fields=footprint.GetFields()
                for index, field in enumerate(fields):
                    print(field.GetName())
                    if index>=4:
                        # field.SetVisible(False)
                        footprint.RemoveField(field.GetName())


class PresetDialog(wx.Dialog):
    def __init__(self, parent, preset_manager):
        super(PresetDialog, self).__init__(parent, title="Manage Presets")
        self.preset_manager = preset_manager
        self.init_ui()

    def init_ui(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.preset_list = wx.ListBox(self, choices=list(self.preset_manager.presets.keys()))
        vbox.Add(self.preset_list, 0, wx.EXPAND | wx.ALL, 5)

        btn_apply = wx.Button(self, label="Apply")
        btn_save = wx.Button(self, label="Save New Preset")
        btn_delete = wx.Button(self, label="Delete Preset")

        vbox.Add(btn_apply, 0, wx.ALL, 5)
        vbox.Add(btn_save, 0, wx.ALL, 5)
        vbox.Add(btn_delete, 0, wx.ALL, 5)

        self.SetSizer(vbox)

        btn_apply.Bind(wx.EVT_BUTTON, self.on_apply_preset)
        btn_save.Bind(wx.EVT_BUTTON, self.on_save_preset)
        btn_delete.Bind(wx.EVT_BUTTON, self.on_delete_preset)

    def on_apply_preset(self, event):
        selected = self.preset_list.GetStringSelection()
        preset = self.preset_manager.get_preset(selected)
        if preset:
            self.Parent.ref_width.SetValue(preset["Reference"]["width"])
            self.Parent.ref_height.SetValue(preset["Reference"]["height"])
            self.Parent.ref_thickness.SetValue(preset["Reference"]["thickness"])
            self.Parent.value_width.SetValue(preset["Value"]["width"])
            self.Parent.value_height.SetValue(preset["Value"]["height"])
            self.Parent.value_thickness.SetValue(preset["Value"]["thickness"])
            self.Parent.other_width.SetValue(preset["Other"]["width"])
            self.Parent.other_height.SetValue(preset["Other"]["height"])
            self.Parent.other_thickness.SetValue(preset["Other"]["thickness"])

    def on_save_preset(self, event):
        name = wx.GetTextFromUser("Enter preset name:")
        if name:
            self.preset_manager.add_preset(
                name,
                {
                    "width": self.Parent.ref_width.GetValue(),
                    "height": self.Parent.ref_height.GetValue(),
                    "thickness": self.Parent.ref_thickness.GetValue(),
                },
                {
                    "width": self.Parent.value_width.GetValue(),
                    "height": self.Parent.value_height.GetValue(),
                    "thickness": self.Parent.value_thickness.GetValue(),
                },
                {
                    "width": self.Parent.other_width.GetValue(),
                    "height": self.Parent.other_height.GetValue(),
                    "thickness": self.Parent.other_thickness.GetValue(),
                }
            )
            self.preset_list.Append(name)

    def on_delete_preset(self, event):
        selected = self.preset_list.GetStringSelection()
        if selected:
            del self.preset_manager.presets[selected]
            self.preset_manager.save_presets()
            self.preset_list.Clear()
            self.preset_list.Append(list(self.preset_manager.presets.keys()))





        
  
    
        


 



           