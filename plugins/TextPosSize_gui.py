# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Apr 12 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
###########################################################################
## Class teardrop_gui
###########################################################################

class TextPosSize_gui ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"SetTextPositionSize", pos = wx.DefaultPosition, size = wx.Size( 400,640 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

        #self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        import sys
        if sys.version_info[0] == 2:
            self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        else:
            self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        amain = wx.BoxSizer( wx.VERTICAL )
        txt_type_box = wx.BoxSizer( wx.HORIZONTAL )

        box01 = wx.BoxSizer( wx.HORIZONTAL )
        self.txt1 = wx.StaticText( self, wx.ID_ANY, u"Refrence:", wx.DefaultPosition, wx.DefaultSize, 0 )
        box01.Add( self.txt1, 0, wx.ALL, 5 )
        self.text_ref = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        box01.Add( self.text_ref, 0, wx.ALL, 5 )
        self.m_staticline01 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        box01.Add( self.m_staticline01, 0, wx.EXPAND |wx.ALL, 5 )
        txt_type_box.Add( box01, 5, wx.EXPAND, 5 )
       

        box02 = wx.BoxSizer( wx.HORIZONTAL )
        self.txt2 = wx.StaticText( self, wx.ID_ANY, u"Value:", wx.DefaultPosition, wx.DefaultSize, 0 )
        box02.Add( self.txt2, 0, wx.ALL, 5)
        self.text_value = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        box02.Add( self.text_value, 0, wx.ALL, 5 )
        self.m_staticline02 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        box02.Add( self.m_staticline02, 0, wx.EXPAND |wx.ALL, 5 )
        txt_type_box.Add( box02, 5, wx.EXPAND, 5 )
       
        
        box03 = wx.BoxSizer( wx.HORIZONTAL )
        self.txt3 = wx.StaticText( self, wx.ID_ANY, u"Other:", wx.DefaultPosition, wx.DefaultSize, 0 )
        box03.Add( self.txt3, 0, wx.ALL, 5 )
        self.text_other = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        box03.Add( self.text_other, 0, wx.EXPAND |wx.ALL, 5 )
        txt_type_box.Add( box03, 5, wx.EXPAND, 5 )
        
        size_box = wx.BoxSizer( wx.HORIZONTAL )
        self.size_enable = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.size_enable.SetToolTip( u"Enable/Disable the size of the text" )
        size_box.Add( self.size_enable, 0, wx.ALL, 5 )
        self.m_staticline03 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        size_box.Add( self.m_staticline03, 1, wx.ALIGN_CENTER |wx.ALL, 5 )
        


        wht_x3_box=wx.BoxSizer(wx.HORIZONTAL)

        wht_box=wx.BoxSizer(wx.VERTICAL)
        self.txt5 = wx.StaticText( self, wx.ID_ANY, u"Width:", wx.DefaultPosition, wx.DefaultSize, 0 )
        wht_box.Add( self.txt5, 5, wx.ALL, 5 )
        self.txt6 = wx.StaticText( self, wx.ID_ANY, u"Height:", wx.DefaultPosition, wx.DefaultSize, 0 )
        wht_box.Add( self.txt6, 5, wx.ALL, 5 )
        self.txt7 = wx.StaticText( self, wx.ID_ANY, u"Thickness:", wx.DefaultPosition, wx.DefaultSize, 0 )
        wht_box.Add( self.txt7, 5, wx.ALL, 5 )

        wht_x3_box.Add( wht_box, 1, wx.EXPAND, 5 )

        ref_value_box=wx.BoxSizer(wx.VERTICAL)
        self.ref_width = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0.8, 0.1 )
        ref_value_box.Add( self.ref_width, 0, wx.EXPAND, 5 )
        self.ref_height = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0.8, 0.1 )
        ref_value_box.Add( self.ref_height, 0, wx.EXPAND, 5 )
        self.ref_thickness = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0.15, 0.01 )
        ref_value_box.Add( self.ref_thickness, 0, wx.EXPAND, 5 )

        wht_x3_box.Add( ref_value_box, 1, wx.ALL, 5 )

        value_value_box=wx.BoxSizer(wx.VERTICAL)
        self.value_width = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0.8, 0.1 )
        value_value_box.Add( self.value_width, 0, wx.EXPAND, 5 )
        self.value_height = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0.8, 0.1 )
        value_value_box.Add( self.value_height, 0, wx.EXPAND, 5 )
        self.value_thickness = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0.15, 0.01 )
        value_value_box.Add( self.value_thickness, 0, wx.EXPAND, 5 )

        wht_x3_box.Add( value_value_box, 1, wx.ALL, 5 )

        other_value_box=wx.BoxSizer(wx.VERTICAL)
        self.other_width = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0.8, 0.1 )
        other_value_box.Add( self.other_width, 0, wx.EXPAND, 5 )
        self.other_height = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0.8, 0.1 )
        other_value_box.Add( self.other_height, 0, wx.EXPAND, 5 )
        self.other_thickness = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0.15, 0.01 )
        other_value_box.Add( self.other_thickness, 0,wx.EXPAND, 5 )

        wht_x3_box.Add( other_value_box, 1, wx.ALL, 5 )


        amain.Add( txt_type_box, 0, wx.ALIGN_RIGHT, 5 ) 
        amain.Add( size_box, 0, wx.EXPAND, 5 )
        amain.Add( wht_x3_box, 0, wx.ALIGN_RIGHT, 5 )

        pos_en_box = wx.BoxSizer( wx.HORIZONTAL )
        self.pos_enable = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.pos_enable.SetToolTip( u"Enable/Disable the position of the text" )
        pos_en_box.Add( self.pos_enable, 0, wx.ALL, 5 )
        self.m_staticline04 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        pos_en_box.Add( self.m_staticline04, 1, wx.ALIGN_CENTER |wx.ALL, 5 )
        amain.Add( pos_en_box, 0, wx.EXPAND, 5 )
        

        pos_set_box = wx.BoxSizer( wx.HORIZONTAL )


        panel = wx.Panel(self)
        panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
        
        self.rb1 = wx.RadioButton(panel,11, label = '', style = wx.RB_GROUP) 
        self.rb2 = wx.RadioButton(panel,22, label = '') 
        self.rb3 = wx.RadioButton(panel,33, label = '')
        self.rb4 = wx.RadioButton(panel,44, label = '') 
        self.rb5 = wx.RadioButton(panel,55, label = '') 
        self.rb6 = wx.RadioButton(panel,66, label = '')
        self.rb7 = wx.RadioButton(panel,77, label = '') 
        self.rb8 = wx.RadioButton(panel,88, label = '') 
        self.rb9 = wx.RadioButton(panel,99, label = '')
        
        self.rb5.SetValue(True)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)
        
        gs=wx.GridSizer(cols=3, rows=3, vgap=100,hgap=100)
        gs.AddMany([
            (self.rb1, 0, wx.EXPAND),
            (self.rb2, 0, wx.EXPAND),
            (self.rb3, 0, wx.EXPAND),
            (self.rb4, 0, wx.EXPAND),
            (self.rb5, 0, wx.EXPAND),
            (self.rb6, 0, wx.EXPAND),
            (self.rb7, 0, wx.EXPAND),
            (self.rb8, 0, wx.EXPAND),
            (self.rb9, 0, wx.EXPAND)
        ])
        panel.SetSizer(gs)
       
        amain.Add( pos_set_box, 0, wx.EXPAND, 5 )
    
        amain.Add( panel, 0, wx.ALL|wx.ALIGN_CENTER, 10 )
        offset_box = wx.BoxSizer( wx.HORIZONTAL )
        self.txt4 = wx.StaticText( self, wx.ID_ANY, u"Offset:", wx.DefaultPosition, wx.DefaultSize, 0 )
        offset_box.Add( self.txt4, 0, wx.ALL, 5 )
        self.offset = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -100, 1000, 0.0, 0.1 )
        offset_box.Add( self.offset, 0, wx.ALL, 5 )
        amain.Add( offset_box, 0, wx.EXPAND, 5 )

        self.m_staticline05 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        amain.Add( self.m_staticline05, 0, wx.EXPAND |wx.ALL, 5 )
        
        box1 = wx.BoxSizer( wx.HORIZONTAL )
        box2 = wx.BoxSizer( wx.HORIZONTAL )
        self.ref_hide = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ref_hide.SetValue(False)
        self.ref_hide.SetToolTip( u"Hide all references." )
        box1.Add( self.ref_hide, 0, wx.ALL, 5 )
        self.m_staticText0 = wx.StaticText( self, wx.ID_ANY, u"Hide", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText0.Wrap( -1 )
        box1.Add( self.m_staticText0, 0, wx.ALL, 5 )
 

        self.m_onlyProcessSelection = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_onlyProcessSelection.SetToolTip( u"Check to only move the silkscreen of the selected footprints." )
        box2.Add( self.m_onlyProcessSelection, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Only process selection", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        box2.Add( self.m_staticText1, 0, wx.ALL, 5 )
       
        amain.Add( box1, 0, wx.ALIGN_LEFT, 5 )
        amain.Add( box2, 0, wx.ALIGN_LEFT, 5 )
        
        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        amain.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        box3 = wx.BoxSizer( wx.HORIZONTAL )

        
        self.but_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        box3.Add( self.but_cancel, 0, wx.ALL, 5 )

        self.but_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
        box3.Add( self.but_ok, 0, wx.ALL, 5 )


        amain.Add( box3, 0, wx.ALIGN_RIGHT, 5 )
        

        self.SetSizer( amain )
        self.Layout()

        self.Centre( wx.BOTH )
    def scale_bitmap(bitmap, width, height):
        image = wx.ImageFromBitmap(bitmap)
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.BitmapFromImage(image)
        return result
    def OnRadiogroup(self, e):
        rb = e.GetEventObject()
        self.id=rb.GetId()
        print(rb.GetLabel(),' is clicked from Radio Group')
        # wx.MessageBox("{} is selected".format(self.id))
        
    def OnEraseBack(self,event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".", "fpx.png"))
        dc.DrawBitmap(bmp, 32, 25)
    def __del__( self ):
        pass


