# -*-mode: python; coding: utf-8 -*-
#
# Copyright 2012-2014 Pierre Ossman for Cendio AB.
# For more information, see http://www.cendio.com
import os
import gettext
if 82 - 82: Iii1i
from gi . repository import Gtk
from gi . repository import Gdk
from gi . repository import GObject
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
from thinlinc import prefix
from thinlinc import tlgtk
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
__all__ = [ "Wizard" , "centered_view" , "centered_label" ]
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
iI111iiIi11i = None
if 77 - 77: iIiii1i - ooo0O0oO00 . o00o0OO00O
Ooo = 30
I1 = 150
if 71 - 71: i11 % Ii
def iI ( ) :
 global iI111iiIi11i
 if iI111iiIi11i is None :
  i1Ii1i = os . path . join ( prefix . get_tl_prefix ( ) , "share" , "locale" )
  oOooo0OOO = gettext . translation ( "tl-misc" , i1Ii1i , fallback = True )
  iI111iiIi11i = oOooo0OOO . gettext
  if 53 - 53: Ii * Oo * ooo000 . i1iiIII111
def centered_view ( scrollable = False , orientation = Gtk . Orientation . VERTICAL ,
 spacing = 30 , ** kwargs ) :
 ii1Ii = Gtk . Box ( orientation = Gtk . Orientation . VERTICAL ,
 halign = Gtk . Align . FILL , valign = Gtk . Align . START )
 ii1Ii . set_margin_top ( Ooo )
 ii1Ii . set_margin_bottom ( Ooo )
 ii1Ii . set_margin_start ( I1 )
 ii1Ii . set_margin_end ( I1 )
 if 55 - 55: iI1iII1I1I1i + i1
 Iii11iiiiI = Gtk . Box ( orientation = orientation , spacing = spacing , ** kwargs )
 ii1Ii . pack_start ( Iii11iiiiI , expand = True , fill = True , padding = 0 )
 if 63 - 63: ooo000 / I1Ii1I1 . Iii1i - ooo000
 if scrollable :
  ii1Ii = tlgtk . factory . scrolled_view ( ii1Ii )
  if 34 - 34: Ooo0Ooo + ooo0O0oO00 * IIiIIiIi11I1 * OooOoo
 return ii1Ii , Iii11iiiiI
 if 25 - 25: Ii / ooo0O0oO00 % Ii
 if 96 - 96: Ii . IIiIIiIi11I1 % iIiii1i
 if 68 - 68: iIiii1i . i1i1i1111I
 if 24 - 24: i11
 if 9 - 9: ooo000 / o00o0OO00O . o00o0OO00O / Ii % i1i1i1111I % Ooo0Ooo
 if 85 - 85: iIiii1i % ooOOO + i1iiIII111 / ooOOO / ooo000
def centered_label ( label , use_markup = True ,
 max_width_chars = 0 , wrap = True ,
 xalign = 0.5 ,
 valign = Gtk . Align . CENTER ,
 ** label_kwargs ) :
 IIiiI11ii = Gtk . Label (
 label = label , use_markup = use_markup ,
 max_width_chars = max_width_chars , wrap = wrap ,
 xalign = xalign , valign = valign ,
 margin_start = I1 , margin_end = I1 ,
 ** label_kwargs
 )
 if 69 - 69: ooOOO % OooOoo
 def oOOoO ( widget , * args ) :
  if 70 - 70: i11 + iIiii1i * ooo0O0oO00 . Oo + ooOOO / Oo
  iI1i1I = widget . get_layout ( ) . get_line_count ( )
  if 27 - 27: ooOOO * IIiIIiIi11I1 % Ii + Ooo0Ooo . Ii + Iii1i
  if 43 - 43: ooOOO * I1Ii1I1
  if 95 - 95: Ooo0Ooo % Iii1i % i1i1i1111I . OooOoo
  if 70 - 70: IiIIii11Ii
  if iI1i1I > 2 :
   widget . set_justify ( Gtk . Justification . LEFT )
  else :
   widget . set_justify ( Gtk . Justification . CENTER )
   if 75 - 75: Ooo0Ooo / Ii / IiIIii11Ii + IiIIii11Ii . I1I
 IIiiI11ii . connect ( 'map' , oOOoO )
 IIiiI11ii . connect ( 'notify::label' , oOOoO )
 if 88 - 88: Oo * IiIIii11Ii
 return IIiiI11ii
 if 100 - 100: i11 - OooOoo * I1Ii1I1 / Ooo0Ooo / Iii1i
class Wizard ( Gtk . Window ) :
 __gsignals__ = {
 'close' : ( GObject . SignalFlags . RUN_LAST | GObject . SignalFlags . ACTION ,
 GObject . TYPE_NONE ,
 ( ) )
 }
 if 23 - 23: Ooo0Ooo + i1 * I1Ii1I1 + Oo * Ii - IIiIIiIi11I1
 def __init__ ( self ) :
  Gtk . Window . __init__ ( self )
  if 29 - 29: IiIIii11Ii - oOo0O00
  iI ( )
  if 30 - 30: I1I . ooo000
  self . connect ( "delete-event" , self . _on_delete )
  self . connect ( "key-press-event" , self . _on_key_press )
  self . set_resizable ( False )
  if 43 - 43: ooOOO . iIiii1i + ooo000
  self . _history = [ ]
  if 87 - 87: Iii1i + ooOOO . o00o0OO00O / Ii + Oo
  self . _build_ui ( )
  if 77 - 77: i1iiIII111 + i11 - Oo % ooo000
 def run ( self ) :
  self . _finished = False
  if 74 - 74: Ii + Ooo0Ooo
  self . connect ( "destroy" , Gtk . main_quit )
  if 1 - 1: I1I % Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo
  if self . forward_button . get_property ( "visible" ) :
   self . forward_button . grab_focus ( )
  elif self . close_button . get_property ( "visible" ) :
   self . close_button . grab_focus ( )
   if 93 - 93: oOo0O00 % Ooo0Ooo * i1iiIII111
  self . show ( )
  Gtk . main ( )
  if 52 - 52: ooo0O0oO00 + I1I / ooo000 - I1Ii1I1 * o00o0OO00O % oOo0O00
  return self . _finished
  if 52 - 52: oOo0O00 . I1I + o00o0OO00O - i1iiIII111 % iI1iII1I1I1i
 def _add_intro_or_finish ( self , title , text , intro_forward_button = None ,
 banner_path = None , width = - 1 , height = - 1 ) :
  Oo0O0o0oO000 = Gtk . EventBox ( valign = Gtk . Align . CENTER )
  ii1Ii , o0Ooo = centered_view ( spacing = 0 )
  Oo0O0o0oO000 . add ( ii1Ii )
  if 19 - 19: Ii
  if banner_path is not None :
   if 32 - 32: i1i1i1111I % Ooo0Ooo - o00o0OO00O * I1I
   Ooo00ooO = 480
   i1Ii1iiIiI111 = 144
   if 77 - 77: i11 - iIiii1i * Ooo0Ooo
   if ( width , height ) == ( - 1 , - 1 ) :
    width = Ooo00ooO
    height = i1Ii1iiIiI111
    if 71 - 71: IIiIIiIi11I1 / ooOOO - ooOOO / iIiii1i
    if 63 - 63: ooOOO / i1i1i1111I - oOo0O00 * ooOOO / i1iiIII111 + ooo0O0oO00
   iiI1 = 1
   iII = 1
   if width > Ooo00ooO :
    iiI1 = Ooo00ooO / width
   if height > i1Ii1iiIiI111 :
    iII = i1Ii1iiIiI111 / height
   width = width * min ( iiI1 , iII )
   height = height * min ( iiI1 , iII )
   if 43 - 43: Ooo0Ooo - I1I . ooo000 - Iii1i % o00o0OO00O
   if 49 - 49: IiIIii11Ii . ooo000 + ooo0O0oO00 - ooo0O0oO00
   if 78 - 78: i1 - ooOOO
   if 56 - 56: ooo000 . ooo000 + I1Ii1I1 * iI1iII1I1I1i
   if 17 - 17: Iii1i % o00o0OO00O - Iii1i % Ooo0Ooo . OooOoo
   if os . path . splitext ( banner_path ) [ 1 ] == '.svg' :
    if 60 - 60: ooOOO . ooo000
    oOOOOOOoO = ( 1 , 1 )
    if width != - 1 and height != - 1 :
     oOOOOOOoO = ( width * 4 , height * 4 )
    elif width == - 1 and height != - 1 :
     oOOOOOOoO = ( - 1 , height * 4 )
    elif width != - 1 and height == - 1 :
     oOOOOOOoO = ( width * 4 , - 1 )
     if 3 - 3: Ii % i1 + i1i1i1111I * Ii * i1 . I1I
    iiI1i = tlgtk . GdkPixbuf . Pixbuf . new_from_file_at_scale (
 banner_path ,
 width = oOOOOOOoO [ 0 ] ,
 height = oOOOOOOoO [ 1 ] ,
 preserve_aspect_ratio = True ,
 )
    if 73 - 73: ooOOO - IiIIii11Ii
   else :
    iiI1i = tlgtk . GdkPixbuf . Pixbuf . new_from_file ( banner_path )
    if 22 - 22: Oo % oOo0O00 / o00o0OO00O . oOo0O00 . o00o0OO00O
    if 87 - 87: I1I - o00o0OO00O . i1 * Oo
    if 90 - 90: i11 * o00o0OO00O . Ii
    if 45 - 45: IiIIii11Ii - iIiii1i . i1iiIII111 * Ooo0Ooo . IIiIIiIi11I1
    if 14 - 14: iI1iII1I1I1i + OooOoo * I1Ii1I1 - iIiii1i
    if 84 - 84: ooo0O0oO00 % iI1iII1I1I1i - Ooo0Ooo
    if 94 - 94: i1iiIII111 + i1i1i1111I / iI1iII1I1I1i + iI1iII1I1I1i / o00o0OO00O
   if width != - 1 and height != - 1 :
    iiI1 = iiI1i . get_width ( ) / width
    iII = iiI1i . get_height ( ) / height
    if 79 - 79: i1iiIII111 - IIiIIiIi11I1 . I1Ii1I1 + I1I - ooOOO + i1iiIII111
    if iiI1 < iII :
     width = width * ( iiI1 / iII )
    elif iiI1 > iII :
     height = height * ( iII / iiI1 )
     if 36 - 36: ooOOO * Iii1i % I1I % i1 . Ooo0Ooo
   oO00OOooOoO0o = tlgtk . factory . scale_aware_surface_from_pixbuf (
 iiI1i ,
 width = width ,
 height = height ,
 preserve_aspect_ratio = True ,
 )
   if 40 - 40: IiIIii11Ii % ooo0O0oO00 - IiIIii11Ii % ooo0O0oO00 - IiIIii11Ii + iI1iII1I1I1i
   Ooo0oO = tlgtk . Gtk . Image . new_from_surface ( oO00OOooOoO0o )
   Ooo0oO . set_margin_bottom ( 60 )
   o0Ooo . pack_start ( Ooo0oO , expand = False , fill = False , padding = 0 )
   if 16 - 16: I1Ii1I1 % I1I / IIiIIiIi11I1 * o00o0OO00O + i11 % oOo0O00
  iiIiIi = Gtk . Box ( orientation = Gtk . Orientation . VERTICAL , vexpand = True ,
 halign = Gtk . Align . FILL , valign = Gtk . Align . CENTER ,
 spacing = 18 )
  o0Ooo . pack_start ( iiIiIi , expand = False , fill = False , padding = 0 )
  if 91 - 91: ooOOO / Ii . oOo0O00 % OooOoo * IIiIIiIi11I1
  iIIIIIiiIIi = Gtk . Label (
 label = title , max_width_chars = 35 , wrap = True ,
 xalign = 0.5 , justify = Gtk . Justification . CENTER ,
 )
  iIIIIIiiIIi . get_style_context ( ) . add_class ( 'title-1' )
  iiIiIi . pack_start ( iIIIIIiiIIi , expand = False , fill = True , padding = 0 )
  if 9 - 9: i1i1i1111I - Ii % OooOoo / o00o0OO00O
  if text is not None :
   oo0O0 = Gtk . Label (
 label = text , halign = Gtk . Align . FILL , valign = Gtk . Align . START ,
 max_width_chars = 35 ,
 xalign = 0.5 , justify = Gtk . Justification . CENTER ,
 )
   oo0O0 . set_use_markup ( True )
   oo0O0 . set_line_wrap ( True )
   iiIiIi . pack_start ( oo0O0 , expand = True , fill = True , padding = 0 )
   if 77 - 77: iIiii1i / iI1iII1I1I1i - oOo0O00 - Ooo0Ooo % oOo0O00
  i1iI1 = intro_forward_button is not None
  if 11 - 11: I1Ii1I1 / ooo0O0oO00
  iIOooO0O = ooO000oOo0o0 ( self , '' , halign = Gtk . Align . FILL , valign = Gtk . Align . FILL )
  iIOooO0O . connect ( "notify::page-backable" , self . _on_page_notify )
  iIOooO0O . connect ( "notify::page-forwardable" , self . _on_page_notify )
  iIOooO0O . connect ( "notify::page-intro" , self . _on_page_notify )
  iIOooO0O . connect ( "notify::page-busy" , self . _on_page_notify )
  if 20 - 20: i1i1i1111I / I1Ii1I1 . oOo0O00
  iIOooO0O . set_page_intro ( i1iI1 )
  iiIiIi . pack_end ( iIOooO0O , expand = True , fill = True , padding = 0 )
  if 77 - 77: oOo0O00 % Oo - oOo0O00 - ooo000 * iIiii1i + ooo0O0oO00
  if i1iI1 :
   intro_forward_button . connect ( "clicked" , self . _on_forward )
   iiIiIi . pack_start ( intro_forward_button ,
 expand = False , fill = False , padding = 0 )
   iiIiIi . set_focus_child ( intro_forward_button )
   if 64 - 64: i11 . Ooo0Ooo . i1iiIII111 * i11
  Oo0O0o0oO000 . show_all ( )
  if 33 - 33: i1i1i1111I
  Oo0O0o0oO000 . page = iIOooO0O
  self . notebook . append_page ( Oo0O0o0oO000 )
  if 30 - 30: o00o0OO00O % ooOOO . Ii % IIiIIiIi11I1 / iI1iII1I1I1i % ooOOO
  return iIOooO0O
  if 24 - 24: IIiIIiIi11I1 - IIiIIiIi11I1 . Ooo0Ooo + i1iiIII111 + Oo
 def add_intro ( self , title , text , button_label ,
 banner_path = None , width = - 1 , height = - 1 ) :
  I1II1I1i = Gtk . Button . new_with_mnemonic ( button_label )
  I1II1I1i . set_halign ( Gtk . Align . CENTER )
  I1II1I1i . get_style_context ( ) . add_class ( 'suggested-action' )
  return self . _add_intro_or_finish ( title , text , I1II1I1i ,
 banner_path , width , height )
  if 59 - 59: i1iiIII111
 def add_finish ( self , title , text ,
 banner_path = None , width = - 1 , height = - 1 ) :
  if 33 - 33: ooo000 . Iii1i % ooo0O0oO00
  return self . _add_intro_or_finish ( title , text ,
 banner_path = banner_path ,
 width = width , height = height )
  if 60 - 60: I1I . IiIIii11Ii % IIiIIiIi11I1 % iI1iII1I1I1i
 def add_page ( self , title ) :
  i1iII1 = Gtk . Box ( orientation = Gtk . Orientation . VERTICAL )
  if 63 - 63: Iii1i
  iIOooO0O = ooO000oOo0o0 ( self , title , margin = 0 )
  iIOooO0O . connect ( "notify::page-backable" , self . _on_page_notify )
  iIOooO0O . connect ( "notify::page-forwardable" , self . _on_page_notify )
  iIOooO0O . connect ( "notify::page-intro" , self . _on_page_notify )
  iIOooO0O . connect ( "notify::page-busy" , self . _on_page_notify )
  i1iII1 . pack_end ( iIOooO0O , expand = True , fill = True , padding = 0 )
  if 81 - 81: I1Ii1I1 / ooo0O0oO00 + ooo0O0oO00 . i1i1i1111I - i1
  i1iII1 . show_all ( )
  if 15 - 15: OooOoo . oOo0O00 - ooOOO % Ooo0Ooo
  i1iII1 . page = iIOooO0O
  self . notebook . append_page ( i1iII1 )
  if 62 - 62: iI1iII1I1I1i / OooOoo % I1I - i11
  return iIOooO0O
  if 66 - 66: i1i1i1111I / Ooo0Ooo + iIiii1i + Iii1i + oOo0O00 + o00o0OO00O
 def _build_ui ( self ) :
  o0OOO00OO = Gtk . Box ( orientation = Gtk . Orientation . VERTICAL )
  self . add ( o0OOO00OO )
  if 42 - 42: i1 * o00o0OO00O
  self . notebook = Gtk . Notebook ( )
  self . notebook . set_show_tabs ( False )
  self . notebook . set_show_border ( False )
  self . notebook . connect ( "page-added" , self . _page_change )
  self . notebook . connect ( "page-removed" , self . _page_change )
  self . notebook . connect ( "switch-page" , self . _switch_page )
  o0OOO00OO . pack_start ( self . notebook , expand = True , fill = True , padding = 0 )
  if 50 - 50: Ii - i1iiIII111
  O00oOoo0 = Gtk . HeaderBar ( )
  O00oOoo0 . show ( )
  if 76 - 76: iI1iII1I1I1i . iIiii1i . iI1iII1I1I1i
  self . window_title = Gtk . Label ( label = "" )
  self . window_title . get_style_context ( ) . add_class ( "title" )
  self . window_title . show ( )
  O00oOoo0 . set_custom_title ( self . window_title )
  if 2 - 2: Ooo0Ooo / OooOoo * IIiIIiIi11I1 . i1iiIII111 + ooo000 % i1i1i1111I
  self . cancel_button = Gtk . Button . new_with_mnemonic ( iI111iiIi11i ( "_Cancel" ) )
  self . cancel_button . connect ( "clicked" , self . _on_cancel )
  O00oOoo0 . pack_start ( self . cancel_button )
  if 43 - 43: ooo000 % IIiIIiIi11I1 + Ii % i1i1i1111I % oOo0O00 / i1
  self . back_button = Gtk . Button . new_with_mnemonic ( iI111iiIi11i ( "_Back" ) )
  self . back_button . connect ( "clicked" , self . _on_back )
  O00oOoo0 . pack_start ( self . back_button )
  if 96 - 96: Ooo0Ooo
  self . forward_button = Gtk . Button . new_with_mnemonic ( iI111iiIi11i ( "_Forward" ) )
  self . forward_button . connect ( "clicked" , self . _on_forward )
  self . forward_button . get_style_context ( ) . add_class ( 'suggested-action' )
  self . forward_button . set_property ( "can-default" , True )
  O00oOoo0 . pack_end ( self . forward_button )
  if 13 - 13: Oo * I1Ii1I1 - oOo0O00 * Ii . Ii + oOo0O00
  self . close_button = Gtk . Button . new_with_mnemonic ( iI111iiIi11i ( "_Close" ) )
  self . close_button . connect ( "clicked" , self . _on_close )
  self . close_button . get_style_context ( ) . add_class ( 'suggested-action' )
  self . close_button . set_property ( "can-default" , True )
  O00oOoo0 . pack_end ( self . close_button )
  if 46 - 46: OooOoo - iIiii1i / Ooo0Ooo
  self . set_titlebar ( O00oOoo0 )
  if 73 - 73: I1Ii1I1 / i1i1i1111I / ooo000 % i1 % o00o0OO00O - OooOoo
  o0OOO00OO . show_all ( )
  if 30 - 30: ooOOO * ooOOO - Iii1i * iI1iII1I1I1i
 def _get_next_willing ( self , index = None ) :
  if index is None :
   index = self . notebook . get_current_page ( )
   if 37 - 37: I1Ii1I1 % iI1iII1I1I1i . o00o0OO00O + Ooo0Ooo + ooOOO * iI1iII1I1I1i
  while True :
   index += 1
   if 39 - 39: IIiIIiIi11I1 - Oo
   IIiiI11ii = self . notebook . get_nth_page ( index )
   if IIiiI11ii is None :
    return None
    if 31 - 31: IiIIii11Ii % oOo0O00 % oOo0O00 * Iii1i
   iIOooO0O = IIiiI11ii . page
   if iIOooO0O is None :
    return index
    if 85 - 85: Iii1i + Ii % IIiIIiIi11I1 % oOo0O00
   I1i1I = iIOooO0O . emit ( "page-unwilling" , self )
   if not I1i1I :
    return index
    if 87 - 87: OooOoo * Oo * Ii * iI1iII1I1I1i + o00o0OO00O . IiIIii11Ii
 def do_close ( self ) :
  self . _on_delete ( self , None )
  if 94 - 94: oOo0O00 . i1iiIII111
 def _on_delete ( self , window , event ) :
  oo0O0oOO0Oo = self . notebook . get_current_page ( )
  iIOooO0O = self . _get_page_widget ( oo0O0oOO0Oo )
  if 60 - 60: OooOoo
  if iIOooO0O is None or not iIOooO0O . get_page_busy ( ) :
   if 97 - 97: ooo000 * ooo0O0oO00
   if 47 - 47: ooo000
   self . _on_cancel ( None )
   if 2 - 2: Oo % IiIIii11Ii - ooOOO
   if 75 - 75: IiIIii11Ii * i1 . Iii1i - i11
  return True
  if 72 - 72: i1 % i1i1i1111I * iI1iII1I1I1i
 def _on_key_press ( self , window , event ) :
  if event . keyval == Gdk . KEY_Escape :
   self . emit ( "close" )
   if 90 - 90: Ooo0Ooo * OooOoo . Ii
 def _on_cancel ( self , button ) :
  Iiii1iIII = "Abort and Exit"
  o0oO0OOo = "Are you sure you wish to abort " + "%s and exit?" % self . get_title ( )
  if 89 - 89: iI1iII1I1I1i / i1 - IiIIii11Ii
  I1IiIIiiIi = tlgtk . SimpleMessageDialog (
 title = self . get_title ( ) ,
 text = Iiii1iIII ,
 secondary_text = o0oO0OOo ,
 cancel_button = True ,
 cancel_button_label = iI111iiIi11i ( "_Return" ) ,
 ok_button_label = iI111iiIi11i ( "_Abort" ) ,
 default_response = Gtk . ResponseType . CANCEL ,
 transient_for = self ,
 modal = True ,
 message_type = Gtk . MessageType . QUESTION )
  iIiii1i1iiIi1 = I1IiIIiiIi . run ( )
  I1IiIIiiIi . destroy ( )
  if 1 - 1: OooOoo / ooOOO % I1Ii1I1
  if iIiii1i1iiIi1 != Gtk . ResponseType . OK :
   return
   if 15 - 15: OooOoo . IiIIii11Ii . o00o0OO00O / Iii1i + ooOOO / Ii
  oo0O0oOO0Oo = self . notebook . get_current_page ( )
  iIOooO0O = self . _get_page_widget ( oo0O0oOO0Oo )
  if iIOooO0O is not None :
   iIOooO0O . emit ( "page-abort" , self )
   if 17 - 17: iIiii1i - i1i1i1111I . iI1iII1I1I1i - iIiii1i + Oo % iI1iII1I1I1i
  self . destroy ( )
  if 65 - 65: Ii % iIiii1i
 def _on_back ( self , button ) :
  assert len ( self . _history ) > 0
  oo0O0oOO0Oo = self . notebook . get_current_page ( )
  iIOooO0O = self . _get_page_widget ( oo0O0oOO0Oo )
  if iIOooO0O is not None :
   iIOooO0O . emit ( "page-abort" , self )
   if 39 - 39: Iii1i * IIiIIiIi11I1 . Ooo0Ooo - Oo
  self . notebook . set_current_page ( self . _history [ - 1 ] )
  if 63 - 63: i1i1i1111I - i1iiIII111 . OooOoo % OooOoo . i11 + o00o0OO00O
 def _on_forward ( self , button ) :
  oo0O0oOO0Oo = self . notebook . get_current_page ( )
  iIOooO0O = self . _get_page_widget ( oo0O0oOO0Oo )
  if iIOooO0O is not None :
   iIOooO0O . emit ( "page-done" , self )
   if 71 - 71: ooo000 + iIiii1i % iI1iII1I1I1i + i11 % Oo - Oo
  oo0O0oOO0Oo = self . _get_next_willing ( )
  assert oo0O0oOO0Oo is not None
  if 84 - 84: I1I % iI1iII1I1I1i - Ooo0Ooo / iI1iII1I1I1i + Ooo0Ooo - Oo
  self . notebook . set_current_page ( oo0O0oOO0Oo )
  if 41 - 41: ooOOO + OooOoo + IIiIIiIi11I1 * i1i1i1111I
 def _on_close ( self , button ) :
  oo0O0oOO0Oo = self . notebook . get_current_page ( )
  iIOooO0O = self . _get_page_widget ( oo0O0oOO0Oo )
  if iIOooO0O is not None :
   iIOooO0O . emit ( "page-done" , self )
   if 12 - 12: i1i1i1111I
  self . _finished = True
  if 56 - 56: IiIIii11Ii
  self . destroy ( )
  if 17 - 17: o00o0OO00O . ooo0O0oO00 % Oo + IiIIii11Ii - Ooo0Ooo
 def _page_change ( self , notebook , child , page_num ) :
  self . _update_buttons ( self . notebook . get_current_page ( ) )
  if 93 - 93: oOo0O00
 def _switch_page ( self , notebook , page , page_num ) :
  O00 = self . _get_page_widget ( page_num )
  if 28 - 28: IIiIIiIi11I1 * i1
  if O00 . title :
   self . window_title . set_label ( O00 . title )
  else :
   self . window_title . set_label ( self . get_title ( ) )
   if 14 - 14: IiIIii11Ii % ooOOO . o00o0OO00O
  if page_num in self . _history :
   oo0O0oOO0Oo = self . _history . index ( page_num )
   self . _history = self . _history [ : oo0O0oOO0Oo ]
  else :
   oo0O0oOO0Oo = self . notebook . get_current_page ( )
   if oo0O0oOO0Oo != - 1 :
    self . _history . append ( oo0O0oOO0Oo )
    if 29 - 29: i11 % ooo0O0oO00 % i11 . ooOOO
  self . _update_buttons ( page_num )
  if 4 - 4: oOo0O00 + i1iiIII111
 def _on_page_notify ( self , page , property ) :
  self . _update_buttons ( self . notebook . get_current_page ( ) )
  if 45 - 45: I1Ii1I1
 def _update_buttons ( self , page_num ) :
  iIOooO0O = self . _get_page_widget ( page_num )
  if iIOooO0O is not None :
   Ii1 = iIOooO0O . get_page_backable ( )
   i1iIIIIiII1I1 = iIOooO0O . get_page_forwardable ( )
   ii1i = iIOooO0O . get_page_intro ( )
   I1II1IIIi = iIOooO0O . get_page_busy ( )
  else :
   Ii1 = True
   i1iIIIIiII1I1 = True
   ii1i = False
   I1II1IIIi = False
   if 97 - 97: IiIIii11Ii . Oo - o00o0OO00O + iIiii1i - oOo0O00
  if len ( self . _history ) > 0 :
   self . back_button . show ( )
   self . back_button . set_sensitive ( Ii1 and not I1II1IIIi )
  else :
   self . back_button . hide ( )
   if 6 - 6: i11 - Ii
  if ii1i :
   self . forward_button . hide ( )
   self . forward_button . set_sensitive ( False )
   self . cancel_button . show ( )
   self . cancel_button . set_sensitive ( True )
   self . close_button . hide ( )
  elif self . _get_next_willing ( page_num ) is not None :
   self . forward_button . show ( )
   self . forward_button . set_sensitive ( i1iIIIIiII1I1 and not I1II1IIIi )
   self . set_default ( self . forward_button )
   self . cancel_button . show ( )
   self . cancel_button . set_sensitive ( not I1II1IIIi )
   self . close_button . hide ( )
  else :
   self . forward_button . hide ( )
   self . cancel_button . hide ( )
   self . close_button . show ( )
   self . close_button . set_sensitive ( not I1II1IIIi )
   self . set_default ( self . close_button )
   if 1 - 1: I1I + OooOoo
   if 98 - 98: i1iiIII111 + Iii1i . IIiIIiIi11I1
  oO00 = self . get_window ( )
  if oO00 is not None :
   if I1II1IIIi :
    II1 = Gdk . Cursor . new_for_display (
 oO00 . get_display ( ) ,
 cursor_type = Gdk . CursorType . WATCH
 )
    oO00 . set_cursor ( II1 )
   else :
    oO00 . set_cursor ( None )
    if 6 - 6: iI1iII1I1I1i . i1iiIII111 . Ooo0Ooo % o00o0OO00O
 def _get_page_widget ( self , page_num ) :
  IIiiI11ii = self . notebook . get_nth_page ( page_num )
  if IIiiI11ii is None :
   return None
   if 52 - 52: Ooo0Ooo * Oo + Iii1i - I1Ii1I1 + iI1iII1I1I1i % IiIIii11Ii
  return IIiiI11ii . page
  if 12 - 12: i1 . o00o0OO00O - iIiii1i - i1i1i1111I
class ooO000oOo0o0 ( Gtk . Bin ) :
 __gproperties__ = {

 # i1iiIII111 + i1iiIII111 / i1i1i1111I / iIiii1i
 'page-backable' : ( GObject . TYPE_BOOLEAN ,
 '' , '' ,
 True ,
 GObject . ParamFlags . READWRITE ) ,

 # iIiii1i . I1I % IiIIii11Ii + OooOoo * Oo / OooOoo
 'page-forwardable' : ( GObject . TYPE_BOOLEAN ,
 '' , '' ,
 True ,
 GObject . ParamFlags . READWRITE ) ,

 # I1Ii1I1 / OooOoo % i1i1i1111I
 'page-intro' : ( GObject . TYPE_BOOLEAN ,
 '' , '' ,
 False ,
 GObject . ParamFlags . READWRITE ) ,

 # IIiIIiIi11I1 * iI1iII1I1I1i
 # iI1iII1I1I1i % o00o0OO00O * i11 * i1iiIII111 + OooOoo
 'page-busy' : ( GObject . TYPE_BOOLEAN ,
 '' , '' ,
 False ,
 GObject . ParamFlags . READWRITE )
 }
 if 57 - 57: IIiIIiIi11I1
 __gsignals__ = {

 # oOo0O00 * o00o0OO00O + IiIIii11Ii . iIiii1i
 'page-unwilling' : ( GObject . SignalFlags . RUN_LAST ,
 GObject . TYPE_BOOLEAN ,
 ( Wizard , ) ) ,

 # oOo0O00
 'page-show' : ( GObject . SignalFlags . RUN_LAST ,
 GObject . TYPE_NONE ,
 ( Wizard , GObject . TYPE_BOOLEAN ) ) ,

 # Ii - IiIIii11Ii . i1i1i1111I + i1i1i1111I
 'page-done' : ( GObject . SignalFlags . RUN_LAST ,
 GObject . TYPE_NONE ,
 ( Wizard , ) ) ,

 # iIiii1i % iI1iII1I1I1i - ooo0O0oO00 % Ii * iI1iII1I1I1i
 'page-abort' : ( GObject . SignalFlags . RUN_LAST ,
 GObject . TYPE_NONE ,
 ( Wizard , ) ) ,
 }
 if 74 - 74: i1iiIII111 / IIiIIiIi11I1 % OooOoo % iI1iII1I1I1i . i1iiIII111 . i1i1i1111I
 def __init__ ( self , wizard , title = None , ** kwargs ) :
  GObject . GObject . __init__ ( self , ** kwargs )
  if 65 - 65: Ii / iI1iII1I1I1i / iIiii1i - i11 % IiIIii11Ii / IiIIii11Ii
  self . title = title
  if 37 - 37: i1iiIII111 - i11 * i1iiIII111 . i1i1i1111I
  self . page_backable = True
  self . page_forwardable = True
  self . page_intro = False
  self . page_busy = False
  if 43 - 43: ooo0O0oO00
  self . _first_map = True
  self . _wizard = wizard
  if 87 - 87: ooOOO + i11 * i1iiIII111 / i1i1i1111I
  self . connect ( "map" , ooO000oOo0o0 . on_map )
  if 75 - 75: IiIIii11Ii / ooo000 + i11 / i1i1i1111I * ooo0O0oO00 + ooo000
 def get_page_backable ( self ) :
  return self . get_property ( 'page-backable' )
  if 83 - 83: iIiii1i / Ooo0Ooo . iIiii1i
 def set_page_backable ( self , value ) :
  return self . set_property ( 'page-backable' , value )
  if 47 - 47: IiIIii11Ii
 def get_page_forwardable ( self ) :
  return self . get_property ( 'page-forwardable' )
  if 40 - 40: i1iiIII111 / IIiIIiIi11I1
 def set_page_forwardable ( self , value ) :
  return self . set_property ( 'page-forwardable' , value )
  if 25 - 25: OooOoo / i1i1i1111I
 def get_page_intro ( self ) :
  return self . get_property ( 'page-intro' )
  if 38 - 38: iIiii1i
 def set_page_intro ( self , value ) :
  return self . set_property ( 'page-intro' , value )
  if 99 - 99: iIiii1i * i1iiIII111 . OooOoo % ooo000 % OooOoo
 def get_page_busy ( self ) :
  return self . get_property ( 'page-busy' )
  if 21 - 21: i11 * I1Ii1I1
 def set_page_busy ( self , value ) :
  return self . set_property ( 'page-busy' , value )
  if 93 - 93: Ooo0Ooo . i1 + i11 - oOo0O00
 def on_map ( self ) :
  if 97 - 97: i1 - i1 % IIiIIiIi11I1 + IiIIii11Ii / o00o0OO00O * iI1iII1I1I1i
  if 60 - 60: iIiii1i - Ooo0Ooo % I1Ii1I1
  self . emit ( "page-show" , self . _wizard , self . _first_map )
  self . _first_map = False
  if 26 - 26: ooOOO / IIiIIiIi11I1 . ooo0O0oO00 + iIiii1i . Oo
 def do_size_request ( self , req ) :
  req . width = 0
  req . height = 0
  oOO0 = self . get_child ( )
  if oOO0 and oOO0 . get_property ( "visible" ) :
   ( req . width , req . height ) = oOO0 . size_request ( )
   if 19 - 19: i1 . IiIIii11Ii - Ooo0Ooo . Ii
 def do_size_allocate ( self , alloc ) :
  self . set_allocation ( alloc )
  oOO0 = self . get_child ( )
  if oOO0 and oOO0 . get_property ( "visible" ) :
   oOO0 . size_allocate ( alloc )
   if 51 - 51: i1 + i1i1i1111I - i1 + i1iiIII111 . Oo
 def do_get_property ( self , property ) :
  if property . name == "page-backable" :
   return self . page_backable
  if property . name == "page-forwardable" :
   return self . page_forwardable
  if property . name == "page-intro" :
   return self . page_intro
  if property . name == "page-busy" :
   return self . page_busy
   if 92 - 92: OooOoo + Ii / IIiIIiIi11I1 + OooOoo * IIiIIiIi11I1 * iI1iII1I1I1i
  raise AttributeError
  if 79 - 79: i1i1i1111I
 def do_set_property ( self , property , value ) :
  if property . name == "page-backable" :
   self . page_backable = value
  elif property . name == "page-forwardable" :
   self . page_forwardable = value
  elif property . name == "page-intro" :
   self . page_intro = value
  elif property . name == "page-busy" :
   self . page_busy = value
  else :
   raise AttributeError
   if 3 - 3: OooOoo / i11 % iIiii1i
GObject . type_register ( Wizard )
GObject . type_register ( ooO000oOo0o0 )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
