# -*-mode: python; coding: utf-8 -*-
#
# Copyright 2012-2014 Pierre Ossman for Cendio AB.
# For more information, see http://www.cendio.com
if 82 - 82: Iii1i
import math
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
from gi . repository import Gdk
from gi . repository import Gtk
from gi . repository import GdkPixbuf
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
__all__ = [
 "boxed_list" , "check_list" , "radio_list" , "spinner_text" , "scrolled_view" ,
 "switch_list" , "boxed_label_list" , "scale_aware_surface_from_pixbuf" ,
 ]
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
def scrolled_view ( widget , hsb_policy = Gtk . PolicyType . AUTOMATIC ,
 vsb_policy = Gtk . PolicyType . AUTOMATIC ) :
 iI111iiIi11i = Gtk . ScrolledWindow ( )
 iI111iiIi11i . set_policy ( hsb_policy , vsb_policy )
 iI111iiIi11i . set_shadow_type ( Gtk . ShadowType . NONE )
 if 77 - 77: iIiii1i - ooo0O0oO00 . o00o0OO00O
 Ooo = Gtk . Viewport ( )
 Ooo . set_shadow_type ( Gtk . ShadowType . NONE )
 Ooo . add ( widget )
 if 9 - 9: ii . Ii * i1
 iI111iiIi11i . add ( Ooo )
 if 9 - 9: i1iiIII111
 return iI111iiIi11i
 if 10 - 10: ooOOO / IIiIIiIi11I1 * ooo0O0oO00 / o00o0OO00O / o00o0OO00O
def check_list ( choices , title = None , subtitle = None ) :
 oOooo0OOO = [ Gtk . CheckButton ( label = choice , can_focus = False )
 for choice in choices ]
 if 53 - 53: Ii * Oo * ooo000 . i1iiIII111
 def ii1Ii ( list , row ) :
  oOooO0 = oOooo0OOO [ row . get_index ( ) ]
  oOooO0 . emit ( 'activate' )
  if 13 - 13: ooo0O0oO00
 iiIII = boxed_list ( oOooo0OOO , title , subtitle , ii1Ii )
 return ( iiIII , oOooo0OOO )
 if 28 - 28: I1Ii1I1 . Iii1i - ooOOO - iI1iII1I1I1i
def boxed_list ( widgets , title = None , subtitle = None ,
 row_activated_cb = None , activatable = True ) :
 iiIII = Gtk . Box ( orientation = Gtk . Orientation . VERTICAL , spacing = 6 )
 if 37 - 37: ooo0O0oO00 * IIiIIiIi11I1 * I1I / oOo0O00
 if title :
  i11i1Iii1I1 = Gtk . Label ( halign = Gtk . Align . FILL , xalign = 0 )
  i11i1Iii1I1 . set_markup ( "<b>%s</b>" % ( title , ) )
  iiIII . pack_start ( i11i1Iii1I1 , expand = False , fill = False , padding = 0 )
  if 68 - 68: iIiii1i . i1i1i1111I
 if subtitle :
  ii1iIi1i11i = Gtk . Label (
 label = subtitle ,
 halign = Gtk . Align . FILL ,
 xalign = 0 ,
 wrap = True , max_width_chars = 0
 )
  iiIII . pack_start ( ii1iIi1i11i , expand = False , fill = False , padding = 0 )
  if 80 - 80: Ooo0Ooo
 if not widgets :
  iiIII . show_all ( )
  return iiIII
  if 85 - 85: iIiii1i % ooOOO + i1iiIII111 / ooOOO / ooo000
 IIiiI11ii = Gtk . Frame ( )
 iiIII . pack_start ( IIiiI11ii , expand = False , fill = False , padding = 6 )
 if 69 - 69: ooOOO % OooOoo
 oOOoO = Gtk . ListBox ( activate_on_single_click = True ,
 selection_mode = Gtk . SelectionMode . NONE )
 IIiiI11ii . add ( oOOoO )
 if 70 - 70: ii + iIiii1i * ooo0O0oO00 . Oo + ooOOO / Oo
 if row_activated_cb :
  oOOoO . connect ( 'row-activated' , row_activated_cb )
  if 14 - 14: OooOoo % oOo0O00 + I1I % i1iiIII111 * ooOOO / iIiii1i
 for OoOo in widgets :
  oOo0O00O0ooo = Gtk . ListBoxRow (
 selectable = False ,
 activatable = activatable ,
 )
  if 89 - 89: Ii % IiIIii11Ii
  IiII = 12
  I1i1i = 12
  if 46 - 46: ii - OooOoo * I1Ii1I1 / Ooo0Ooo / Iii1i
  I11iIi1i = Gtk . Box ( orientation = Gtk . Orientation . HORIZONTAL )
  I11iIi1i . set_margin_top ( IiII )
  I11iIi1i . set_margin_bottom ( IiII )
  I11iIi1i . pack_start ( OoOo , expand = True , fill = True , padding = I1i1i )
  oOo0O00O0ooo . add ( I11iIi1i )
  if 49 - 49: IIiIIiIi11I1
  oOOoO . add ( oOo0O00O0ooo )
  if 29 - 29: IiIIii11Ii - oOo0O00
 iiIII . show_all ( )
 return iiIII
 if 30 - 30: I1I . ooo000
def boxed_label_list ( labels , title = None , subtitle = None ) :
 oOooo0OOO = [ Gtk . Label ( label = label ) for label in labels ]
 return boxed_list ( oOooo0OOO , title , subtitle , activatable = False )
 if 43 - 43: ooOOO . iIiii1i + ooo000
def radio_list ( choices , title = None , subtitle = None ) :
 if 87 - 87: Iii1i + ooOOO . o00o0OO00O / Ii + Oo
 if 77 - 77: i1iiIII111 + ii - Oo % ooo000
 if 74 - 74: Ii + Ooo0Ooo
 if 1 - 1: I1I % Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo
 if 93 - 93: oOo0O00 % Ooo0Ooo * i1iiIII111
 if 52 - 52: ooo0O0oO00 + I1I / ooo000 - I1Ii1I1 * o00o0OO00O % oOo0O00
 oOooo0OOO = [ Gtk . RadioButton ( label = choice ) for choice in choices ]
 for OoOo in oOooo0OOO [ 1 : ] :
  OoOo . join_group ( oOooo0OOO [ 0 ] )
  if 52 - 52: oOo0O00 . I1I + o00o0OO00O - i1iiIII111 % iI1iII1I1I1i
 def ii1Ii ( list , row ) :
  oOooO0 = oOooo0OOO [ row . get_index ( ) ]
  oOooO0 . emit ( 'activate' )
  if 57 - 57: I1I * IIiIIiIi11I1 % I1Ii1I1 * i1i1i1111I
 iiIII = boxed_list ( oOooo0OOO , title , subtitle , ii1Ii )
 return ( iiIII , oOooo0OOO )
 if 37 - 37: ii * i1i1i1111I + oOo0O00 / I1I / OooOoo
def switch_list ( choices , title = None , subtitle = None ) :
 oOooo0OOO = [ ]
 iI1iI = [ ]
 if 54 - 54: I1I % ooo000 * ooo000 - OooOoo / Iii1i * Oo
 for o00O in choices :
  if 7 - 7: Oo / OooOoo - iIiii1i - ii % i1iiIII111
  OOo0OOOo0O = Gtk . Box ( orientation = Gtk . Orientation . HORIZONTAL )
  if 99 - 99: i1 - iI1iII1I1I1i + oOo0O00 . ooOOO / i1iiIII111
  oooO = Gtk . Label ( label = o00O )
  OOo0OOOo0O . pack_start ( oooO , expand = False , fill = False , padding = 12 )
  if 89 - 89: I1I * i1i1i1111I
  O0OOooO = Gtk . Switch ( )
  O0OOooO . set_can_focus ( False )
  OOo0OOOo0O . pack_end ( O0OOooO , expand = False , fill = False , padding = 0 )
  oOooo0OOO . append ( O0OOooO )
  if 50 - 50: Iii1i * ooo000 % Iii1i - oOo0O00 + ooo000
  iI1iI . append ( OOo0OOOo0O )
  if 54 - 54: ooo0O0oO00 * i1 % i1 - Ooo0Ooo + IIiIIiIi11I1
 def ii1Ii ( list , row ) :
  oOooO0 = oOooo0OOO [ row . get_index ( ) ]
  oOooO0 . emit ( 'activate' )
  if 4 - 4: ooo000 + I1Ii1I1 * OooOoo - ii
 iiIII = boxed_list ( iI1iI , title , subtitle , ii1Ii )
 return iiIII , oOooo0OOO
 if 69 - 69: ooo000
def spinner_text ( text ) :
 iiIII = Gtk . Box ( orientation = Gtk . Orientation . HORIZONTAL ,
 halign = Gtk . Align . CENTER , valign = Gtk . Align . CENTER )
 iiIII . set_spacing ( 6 )
 if 76 - 76: Iii1i * Ooo0Ooo . iI1iII1I1I1i / Ii / ooOOO
 OOOOO = Gtk . Spinner ( active = True )
 iiIII . pack_start ( OOOOO , expand = True , fill = True , padding = 0 )
 if 36 - 36: i1i1i1111I + Iii1i - ooo0O0oO00 * Ii
 oo0ooooo0ooo = Gtk . Label ( label = text )
 iiIII . pack_end ( oo0ooooo0ooo , expand = True , fill = True , padding = 0 )
 if 61 - 61: o00o0OO00O . iI1iII1I1I1i / ooOOO * I1Ii1I1 + ii % Oo
 return iiIII
 if 100 - 100: Oo + o00o0OO00O
def scale_aware_surface_from_pixbuf (
 pixbuf , width , height , preserve_aspect_ratio = False ,
 ) :
 if 4 - 4: ooo000 % I1I - i1i1i1111I
 if 76 - 76: i1 * oOo0O00 . ii * o00o0OO00O . IiIIii11Ii . ooo0O0oO00
 if 55 - 55: i1i1i1111I + i1iiIII111 % Ooo0Ooo . Oo - IiIIii11Ii - iI1iII1I1I1i
 if 91 - 91: I1Ii1I1 - iIiii1i
 if 84 - 84: ooo0O0oO00 % iI1iII1I1I1i - Ooo0Ooo
 if 94 - 94: i1iiIII111 + i1i1i1111I / iI1iII1I1I1i + iI1iII1I1I1i / o00o0OO00O
 if 79 - 79: i1iiIII111 - IIiIIiIi11I1 . I1Ii1I1 + I1I - ooOOO + i1iiIII111
 if 36 - 36: ooOOO * Iii1i % I1I % i1 . Ooo0Ooo
 if 63 - 63: IIiIIiIi11I1 / IIiIIiIi11I1 * Iii1i - oOo0O00 . i1
 if 52 - 52: oOo0O00 / o00o0OO00O * IIiIIiIi11I1 + iIiii1i % Ooo0Ooo + ooo0O0oO00
 if 43 - 43: iI1iII1I1I1i * oOo0O00 + ooOOO
 if 30 - 30: I1I
 if 41 - 41: ooo0O0oO00
 if 98 - 98: I1I / IIiIIiIi11I1 / o00o0OO00O + ii % Oo + I1I
 if 38 - 38: I1Ii1I1 + oOo0O00
 if 2 - 2: OooOoo % Ii + ooo0O0oO00 . OooOoo + IIiIIiIi11I1 * Oo
 if preserve_aspect_ratio :
  if 2 - 2: IIiIIiIi11I1 + iI1iII1I1I1i - I1Ii1I1 + ooOOO . IIiIIiIi11I1
  if 15 - 15: ooo000
  if 63 - 63: o00o0OO00O
  if width == - 1 and height == - 1 :
   width = pixbuf . get_width ( )
   height = pixbuf . get_height ( )
   if 81 - 81: OooOoo . o00o0OO00O / i1i1i1111I + Oo / Ooo0Ooo % ii
  elif width == - 1 and height != - 1 :
   width = ( height / pixbuf . get_height ( ) ) * pixbuf . get_width ( )
   if 77 - 77: iIiii1i / iI1iII1I1I1i - oOo0O00 - Ooo0Ooo % oOo0O00
  elif width != - 1 and height == - 1 :
   height = ( width / pixbuf . get_width ( ) * pixbuf . get_height ( ) )
   if 73 - 73: ii . Oo * I1I / i1i1i1111I + I1Ii1I1
 else :
  if 31 - 31: i1i1i1111I % I1Ii1I1
  I11IIiiI1 = ( pixbuf . get_width ( ) / width , pixbuf . get_height ( ) / height )
  if 37 - 37: i1i1i1111I - i1 * o00o0OO00O + I1I * Oo - ooo0O0oO00
  iiiiiI = (
 max ( 1 , I11IIiiI1 [ 1 ] / I11IIiiI1 [ 0 ] ) , max ( 1 , I11IIiiI1 [ 0 ] / I11IIiiI1 [ 1 ] )
 )
  OO0 = pixbuf . get_width ( ) * iiiiiI [ 0 ]
  O00OOo = pixbuf . get_height ( ) * iiiiiI [ 1 ]
  if 77 - 77: Ooo0Ooo
  pixbuf = pixbuf . scale_simple ( OO0 , O00OOo ,
 GdkPixbuf . InterpType . TILES )
  if 95 - 95: ooOOO % i1i1i1111I . i1
  if 87 - 87: Iii1i % ooOOO * Ii % IIiIIiIi11I1 / iIiii1i
  if 84 - 84: I1Ii1I1 + Ooo0Ooo % IIiIIiIi11I1 * i1i1i1111I
 I11IIiiI1 = ( pixbuf . get_width ( ) / width , pixbuf . get_height ( ) / height )
 if I11IIiiI1 != ( int ( I11IIiiI1 [ 0 ] ) , int ( I11IIiiI1 [ 1 ] ) ) :
  I11IIiiI1 = ( math . ceil ( I11IIiiI1 [ 0 ] ) , math . ceil ( I11IIiiI1 [ 1 ] ) )
  if 61 - 61: i1iiIII111 - Oo + I1Ii1I1
  OOO0O0oOoOOOo = I11IIiiI1 [ 0 ] * width
  o0OOoo0O0O0O = I11IIiiI1 [ 1 ] * height
  pixbuf = pixbuf . scale_simple ( OOO0O0oOoOOOo , o0OOoo0O0O0O ,
 GdkPixbuf . InterpType . TILES )
  if 98 - 98: I1I
 return Gdk . cairo_surface_create_from_pixbuf (
 pixbuf , max ( I11IIiiI1 ) , for_window = None
 )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
