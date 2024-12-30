#!/usr/bin/env python

# Teardrop for pcbnew using filled zones
# This is the plugin WX dialog
# (c) Niluje 2019 thewireddoesntexist.org
#
# Based on Teardrops for PCBNEW by svofski, 2014 http://sensi.org/~svo
# Cubic Bezier upgrade by mitxela, 2021 mitxela.com

import wx
import pcbnew
import os
import time
from .TextPosSize_gui import TextPosSize_gui
# from .TextPos import __version__

class TextPosSizeDialog(TextPosSize_gui):
    """Class that gathers all the Gui control"""

    def __init__(self):
        """Init the brand new instance"""
        super(TextPosSizeDialog, self).__init__(None)
        self.SetTitle("Text Size & Position")
        self.text_type=1
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

        self.check_text_type_selection()

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

    def onProcessAction(self, event):
        self.process_text(self.text_type)
        # return self.EndModal(wx.ID_OK)

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
        fields=footprint.Fields()
        for index, field in fields:
            if index>=5:
                field.SetVisible(False)


        
  
    
        


 



           


