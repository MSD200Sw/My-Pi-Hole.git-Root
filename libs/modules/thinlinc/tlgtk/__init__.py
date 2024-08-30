# -*-mode: python; coding: utf-8 -*-
#
# Copyright 2012-2014 Pierre Ossman for Cendio AB.
# For more information, see http://www.cendio.com
if 82 - 82: Iii1i
import os
import sys
import _thread
import re
import warnings
import shutil
import textwrap
import subprocess
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
import thinlinc . prefix
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
__all__ = [ "init" ,
 "has_gtk" ,
 "Gtk" , "Gdk" , "GdkPixbuf" , "GLib" , "GObject" , "Pango" ,
 "factory" , "wizard" , "SimpleMessageDialog" , "EntryDialog" ,
 "linkify_text" , "sanitise_wrap" , "message" , "avoid_center_on_seam" ]
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
if 98 - 98: I11iiIi11i1I % oOO
if 31 - 31: i1I
has_gtk = False
if 9 - 9: IiI11Ii111 / oOo0O00 / IiIIii11Ii - I11iiIi11i1I - iI1iII1I1I1i
if 16 - 16: i1i1i1111I / i1iiIII111
if 3 - 3: i1 % i1 % i1i1i1111I . Ii * i1
ii1iI1I = _thread . get_ident ( )
if 28 - 28: i1I / IIiIIiIi11I1 % IIiIIiIi11I1 / I1I - Oo
def IIII1i1 ( exc_type , exc_value , exc_traceback , old_hook ) :
 old_hook ( exc_type , exc_value , exc_traceback )
 if 84 - 84: Ii . i1iiIII111 - i1 . I1I / iI1iII1I1I1i % OooOoo
 if 55 - 55: iI1iII1I1I1i + i1
 if 10 - 10: Oo % oOO . i1i1i1111I . i1
 if 22 - 22: IIiIIiIi11I1 - ooo000 / I1Ii1I1 . ooo000
 if _thread . get_ident ( ) != ii1iI1I :
  return
  if 1 - 1: iI1iII1I1I1i + Ooo0Ooo + oOO * IIiIIiIi11I1
  if 20 - 20: I1I + Ii
 if Gtk . main_level ( ) == 0 :
  return
  if 75 - 75: Ii % i1iiIII111 * Ii . IIiIIiIi11I1 % I11iiIi11i1I % I1Ii1I1
 sys . exit ( 1 )
 if 8 - 8: I1Ii1I1 . IiI11Ii111 . i1 . Oo - i1I
def init ( wmclass = None ) :
 global Gtk , Gdk , GdkPixbuf , GLib , GObject , Pango
 global has_gtk
 if 32 - 32: Ii % i1i1i1111I % i1I - I11iiIi11i1I % i1iiIII111
 if 34 - 34: i1iiIII111 * i1
 if 34 - 34: oOo0O00 / i1iiIII111 - Iii1i . iI1iII1I1I1i
 if not os . environ . get ( "DISPLAY" , "" ) :
  return False
  if 80 - 80: i1i1i1111I . I1I % ooOOO % IiIIii11Ii / i1i1i1111I
 try :
  import gi
  if 32 - 32: I1Ii1I1 + oOO - oOo0O00
  if 79 - 79: Iii1i % oOO * Oo + ooOOO / Oo . oOO
  if 20 - 20: IiI11Ii111 + i1iiIII111 / I1I
  if 88 - 88: I11iiIi11i1I + ooOOO - i1i1i1111I . Ooo0Ooo * Ii + Iii1i
  if not hasattr ( gi , 'require_version' ) :
   raise ImportError
   if 43 - 43: ooOOO * I1Ii1I1
   if 95 - 95: Ooo0Ooo % Iii1i % i1i1i1111I . OooOoo
   if 70 - 70: IiIIii11Ii
   if 75 - 75: Ooo0Ooo / Ii / IiIIii11Ii + IiIIii11Ii . I1I
  gi . require_version ( "Gtk" , "3.0" )
  gi . require_version ( "Gdk" , "3.0" )
  gi . require_version ( "GdkPixbuf" , "2.0" )
  gi . require_version ( "GLib" , "2.0" )
  gi . require_version ( "GObject" , "2.0" )
  gi . require_version ( "Pango" , "1.0" )
  if 88 - 88: Oo * IiIIii11Ii
  if 100 - 100: IiI11Ii111 - OooOoo * I1Ii1I1 / Ooo0Ooo / Iii1i
  if 23 - 23: Ooo0Ooo + i1 * I1Ii1I1 + Oo * Ii - IIiIIiIi11I1
  if 29 - 29: IiIIii11Ii - oOo0O00
  if 30 - 30: I1I . ooo000
  if 43 - 43: ooOOO . I11iiIi11i1I + ooo000
  gi . require_foreign ( 'cairo' )
  if 87 - 87: Iii1i + ooOOO . i1I / Ii + Oo
  if 77 - 77: i1iiIII111 + IiI11Ii111 - Oo % ooo000
  if 74 - 74: Ii + Ooo0Ooo
  with warnings . catch_warnings ( ) :
   warnings . filterwarnings ( "ignore" , ".*falling back to load_module.*" , ImportWarning )
   if 1 - 1: I1I % Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo
   from gi . repository import Gtk
   from gi . repository import Gdk
   from gi . repository import GdkPixbuf
   from gi . repository import GLib
   from gi . repository import GObject
   from gi . repository import Pango
   if 93 - 93: oOo0O00 % Ooo0Ooo * i1iiIII111
   if 52 - 52: oOO + I1I / ooo000 - I1Ii1I1 * i1I % oOo0O00
  if Gtk . check_version ( 3 , 20 , 0 ) is not None :
   raise RuntimeError
   if 52 - 52: oOo0O00 . I1I + i1I - i1iiIII111 % iI1iII1I1I1i
   if 57 - 57: I1I * IIiIIiIi11I1 % I1Ii1I1 * i1i1i1111I
  if not hasattr ( Gtk , 'PyGTKDeprecationWarning' ) :
   raise ImportError
   if 37 - 37: IiI11Ii111 * i1i1i1111I + oOo0O00 / I1I / OooOoo
  try :
   iI1iI = GdkPixbuf . PixbufLoader . new_with_mime_type ( 'image/svg+xml' )
   if 54 - 54: I1I % ooo000 * ooo000 - OooOoo / Iii1i * Oo
   try :
    iI1iI . close ( )
   except GLib . GError :
    if 100 - 100: I1Ii1I1 / I11iiIi11i1I * Ii - oOO
    pass
  except GLib . GError :
   raise RuntimeError
   if 32 - 32: iI1iII1I1I1i
  I111II111I1I = Gtk . init_check ( [ ] ) [ 0 ]
  if not I111II111I1I :
   raise RuntimeError
   if 21 - 21: iI1iII1I1I1i - i1 + ooOOO * IIiIIiIi11I1 % i1 * ooOOO
  if wmclass is not None :
   Gdk . set_program_class ( wmclass )
   if 57 - 57: oOo0O00
  has_gtk = True
  if 31 - 31: i1iiIII111 + i1i1i1111I % OooOoo
  if 20 - 20: OooOoo - I1I
  if 9 - 9: i1iiIII111 - iI1iII1I1I1i % Ii - I1I
  if 54 - 54: Iii1i % ooo000 % Iii1i - IiIIii11Ii
  if 39 - 39: oOO - oOO * i1 % IIiIIiIi11I1
  IIiII11I = sys . excepthook
  sys . excepthook = lambda I11i , o0O , IiII : IIII1i1 ( I11i , o0O , IiII , IIiII11I )
 except ImportError :
  if 42 - 42: i1iiIII111 - i1iiIII111
  return False
 except RuntimeError :
  if 98 - 98: Ooo0Ooo + i1i1i1111I + Iii1i - oOO
  return False
 except ValueError :
  if 7 - 7: i1i1i1111I / Ii * Iii1i
  return False
  if 32 - 32: IiI11Ii111 . OooOoo
  if 31 - 31: Oo - i1I
  if 28 - 28: ooOOO * I1Ii1I1 + IiI11Ii111 % Oo
 I1i = Gtk . CssProvider ( )
 I1i . load_from_data ( b"""
    .title-1 {
       font-weight: 800;
       font-size: 20pt;
    }
    """ )
 if 40 - 40: ooo000 * I1I - i1I . i1 * Oo
 if 90 - 90: IiI11Ii111 * i1I . Ii
 if 45 - 45: IiIIii11Ii - I11iiIi11i1I . i1iiIII111 * Ooo0Ooo . IIiIIiIi11I1
 if 14 - 14: iI1iII1I1I1i + OooOoo * I1Ii1I1 - I11iiIi11i1I
 if 84 - 84: oOO % iI1iII1I1I1i - Ooo0Ooo
 if 94 - 94: i1iiIII111 + i1i1i1111I / iI1iII1I1I1i + iI1iII1I1I1i / i1I
 if Gtk . MAJOR_VERSION == 3 and Gtk . MINOR_VERSION < 22 :
  I1i . load_from_data ( b"""
        .title-1 {
           font-weight: 800;
           font-size: 20px;
        }
        """ )
  if 79 - 79: i1iiIII111 - IIiIIiIi11I1 . I1Ii1I1 + I1I - ooOOO + i1iiIII111
 Gtk . StyleContext . add_provider_for_screen (
 Gdk . Screen . get_default ( ) ,
 I1i ,
 Gtk . STYLE_PROVIDER_PRIORITY_FALLBACK )
 if 36 - 36: ooOOO * Iii1i % I1I % i1 . Ooo0Ooo
 oO00OOooOoO0o = thinlinc . prefix . get_tl_prefix ( ) + "/share/icons"
 if 40 - 40: IiIIii11Ii % oOO - IiIIii11Ii % oOO - IiIIii11Ii + iI1iII1I1I1i
 Ooo0oO = [ ]
 for ii1II in [ 16 , 22 , 24 , 32 , 48 , 64 , 128 ] :
  try :
   oOoOo = "%s/thinlinc_%d.png" % ( oO00OOooOoO0o , ii1II )
   o0oOoo0O0o0Oo = GdkPixbuf . Pixbuf . new_from_file ( oOoOo )
  except :
   o0oOoo0O0o0Oo = None
   if 2 - 2: IIiIIiIi11I1 + iI1iII1I1I1i - I1Ii1I1 + ooOOO . IIiIIiIi11I1
  if o0oOoo0O0o0Oo is None :
   try :
    oOoOo = "%s/thinlinc.svg" % oO00OOooOoO0o
    o0oOoo0O0o0Oo = GdkPixbuf . Pixbuf . new_from_file_at_size ( oOoOo , ii1II , ii1II )
   except :
    o0oOoo0O0o0Oo = None
    if 15 - 15: ooo000
  if o0oOoo0O0o0Oo is not None :
   Ooo0oO . append ( o0oOoo0O0o0Oo )
   if 63 - 63: i1I
 if Ooo0oO :
  Gtk . Window . set_default_icon_list ( Ooo0oO )
  if 81 - 81: OooOoo . i1I / i1i1i1111I + Oo / Ooo0Ooo % IiI11Ii111
  if 77 - 77: I11iiIi11i1I / iI1iII1I1I1i - oOo0O00 - Ooo0Ooo % oOo0O00
  if 73 - 73: IiI11Ii111 . Oo * I1I / i1i1i1111I + I1Ii1I1
 global factory
 from . import factory
 if 31 - 31: i1i1i1111I % I1Ii1I1
 global wizard
 from . import wizard
 if 1 - 1: IiI11Ii111 - oOo0O00 - i1 . oOo0O00
 global EntryDialog
 from . dialog import EntryDialog
 if 91 - 91: iI1iII1I1I1i * i1 . ooOOO
 global SimpleMessageDialog
 from . dialog import SimpleMessageDialog
 if 81 - 81: I1I * Oo - i1 % OooOoo * ooOOO
 if 19 - 19: Ii
 if 22 - 22: i1I % iI1iII1I1I1i + Oo
 return True
 if 60 - 60: ooo000 + I11iiIi11i1I + IIiIIiIi11I1 % i1i1i1111I - Ii % Ooo0Ooo
 if 95 - 95: ooOOO % i1i1i1111I . i1
 if 87 - 87: Iii1i % ooOOO * Ii % IIiIIiIi11I1 / I11iiIi11i1I
def linkify_text ( text ) :
 if not has_gtk :
  return text
  if 84 - 84: I1Ii1I1 + Ooo0Ooo % IIiIIiIi11I1 * i1i1i1111I
  if 61 - 61: i1iiIII111 - Oo + I1Ii1I1
  if 43 - 43: IIiIIiIi11I1 * ooo000 + Ii % iI1iII1I1I1i
 IIiI1i = "(https?|ftp)://[0-9a-zA-Z;/?:@&=+$\\.\\-_!~*'()%]+(#[0-9a-zA-Z;/?:@&=+$\\.\\-_!~*'()%]+)?"
 return re . sub ( "(%s)" % IIiI1i , "<a href=\"\\1\">\\1</a>" , text )
 if 85 - 85: Ooo0Ooo - I1I . IiIIii11Ii % IIiIIiIi11I1 % iI1iII1I1I1i
def sanitise_wrap ( text ) :
 if not has_gtk :
  return text
  if 98 - 98: I1I
  if 35 - 35: oOo0O00 / IIiIIiIi11I1 - Iii1i . IiI11Ii111 * i1
  if 91 - 91: oOO + Iii1i
  if 71 - 71: i1 . iI1iII1I1I1i . OooOoo . IIiIIiIi11I1
  if 92 - 92: ooOOO % IIiIIiIi11I1 - IIiIIiIi11I1
  if 32 - 32: OooOoo % I1I - I11iiIi11i1I % OooOoo
  if 9 - 9: i1iiIII111 - ooOOO % Iii1i
  if 37 - 37: i1I + IIiIIiIi11I1 % iI1iII1I1I1i / IIiIIiIi11I1 % i1iiIII111 + oOO
  if 98 - 98: iI1iII1I1I1i - I1I + i1 * ooo000 % i1
  if 100 - 100: i1iiIII111 . IIiIIiIi11I1 * ooo000 * ooo000
 Iioo0Oo0oO0 = ""
 iII11I1iI = False
 for O0O0o0oo00Oo in text :
  if O0O0o0oo00Oo == "<" :
   iII11I1iI = True
   if 96 - 96: Ooo0Ooo
  if iII11I1iI or O0O0o0oo00Oo . isalnum ( ) or O0O0o0oo00Oo . isspace ( ) :
   Iioo0Oo0oO0 += O0O0o0oo00Oo
  else :
   Iioo0Oo0oO0 += "\u200d%s\u200d" % O0O0o0oo00Oo
   if 13 - 13: Oo * I1Ii1I1 - oOo0O00 * Ii . Ii + oOo0O00
  if O0O0o0oo00Oo == ">" :
   iII11I1iI = False
   if 46 - 46: OooOoo - I11iiIi11i1I / Ooo0Ooo
 return Iioo0Oo0oO0
 if 73 - 73: I1Ii1I1 / i1i1i1111I / ooo000 % i1 % i1I - OooOoo
def IIII1iII11ii ( mainwin ) :
 OO0O0OOOoOO = Gtk . check_version ( 3 , 22 , 0 ) is None
 if 14 - 14: i1I - IiIIii11Ii
 if OO0O0OOOoOO :
  return mainwin . get_display ( ) . get_n_monitors ( )
 else :
  return mainwin . get_screen ( ) . get_n_monitors ( )
  if 74 - 74: oOo0O00 * ooo000 . ooOOO
  if 2 - 2: Ii * IIiIIiIi11I1 % i1 + IiIIii11Ii % i1
  if 82 - 82: ooOOO % OooOoo
  if 81 - 81: Ii
  if 40 - 40: i1I . OooOoo + oOo0O00 . i1iiIII111
  if 96 - 96: I1I / oOO / I11iiIi11i1I + I11iiIi11i1I
  if 35 - 35: IIiIIiIi11I1 + oOo0O00
  if 96 - 96: iI1iII1I1I1i . OooOoo . i1
def avoid_center_on_seam ( mainwin ) :
 if IIII1iII11ii ( mainwin ) == 1 :
  OO0O0OOOoOO = Gtk . check_version ( 3 , 22 , 0 ) is None
  if OO0O0OOOoOO :
   OOo = mainwin . get_display ( ) . get_monitor ( 0 )
   oO000O0O0 = OOo . get_geometry ( )
   ooOo00O0o0o0 , OOooooOOooo0 = oO000O0O0 . width , oO000O0O0 . height
  else :
   II1111I11 = mainwin . get_screen ( )
   ooOo00O0o0o0 , OOooooOOooo0 = II1111I11 . get_width ( ) , II1111I11 . get_height ( )
   if 94 - 94: Oo - IIiIIiIi11I1
  O0 , oOoOo0O00 = ooOo00O0o0o0 , OOooooOOooo0
  if 46 - 46: ooo000
  if 36 - 36: iI1iII1I1I1i . i1i1i1111I
  if 85 - 85: IiI11Ii111 * Iii1i
  if 7 - 7: OooOoo / I1I % i1i1i1111I
  if 98 - 98: i1I / i1 / OooOoo + Iii1i % ooOOO
  for iIii1iiiIi in range ( 1 , ooOo00O0o0o0 ) :
   O0 = ooOo00O0o0o0 / iIii1iiiIi
   if float ( O0 ) / OOooooOOooo0 < 2.4 :
    break
  for iIii1iiiIi in range ( 1 , OOooooOOooo0 ) :
   oOoOo0O00 = OOooooOOooo0 / iIii1iiiIi
   if float ( O0 ) / oOoOo0O00 > 1.2 :
    break
  oOoo , ooOOO00oO0o0o = mainwin . get_size ( )
  OooOOO0oO0Oo = ( O0 - oOoo ) / 2
  IiiiI11111I = ( oOoOo0O00 - ooOOO00oO0o0o ) / 2
  if OooOOO0oO0Oo > 0 and IiiiI11111I > 0 :
   mainwin . move ( OooOOO0oO0Oo , IiiiI11111I )
   if 49 - 49: oOo0O00 % I11iiIi11i1I - Ooo0Ooo % Oo . oOO
def IiIIIII1i ( title , msg ) :
 O0OOo0O = shutil . which ( "zenity" )
 if O0OOo0O is None :
  return False
  if 9 - 9: i1i1i1111I
 try :
  I11 = subprocess . call ( [ O0OOo0O , "--error" , "--title" , title , "--text" , msg ] )
  if I11 < 0 or I11 == 255 :
   return False
 except OSError :
  return False
  if 48 - 48: Ii % i1I
 return True
 if 72 - 72: Oo + IiIIii11Ii - Ooo0Ooo * Ii * oOo0O00
def O00 ( title , msg ) :
 O0OOo0O = shutil . which ( "Xdialog" )
 if O0OOo0O is None :
  return False
  if 28 - 28: IIiIIiIi11I1 * i1
 try :
  I11 = subprocess . call ( [ O0OOo0O , "--title" , title ,
 "--msgbox" , msg , "0" , "0" ] )
  if I11 < 0 :
   return False
 except OSError :
  return False
  if 14 - 14: IiIIii11Ii % ooOOO . i1I
 return True
 if 29 - 29: IiI11Ii111 % oOO % IiI11Ii111 . ooOOO
def i1IIIi ( title , msg ) :
 O0OOo0O = shutil . which ( "kdialog" )
 if O0OOo0O is None :
  return False
  if 24 - 24: ooo000 % i1i1i1111I
 try :
  I11 = subprocess . call ( [ O0OOo0O , "--title" , title , "--error" , msg ] )
  if I11 != 0 :
   return False
 except OSError :
  return False
  if 19 - 19: Iii1i * I11iiIi11i1I . ooo000 / iI1iII1I1I1i - I1Ii1I1 + IiIIii11Ii
 return True
 if 40 - 40: i1I + i1i1i1111I % OooOoo . IiI11Ii111 / i1i1i1111I . ooOOO
def message ( title , msg ) :
 if 57 - 57: IIiIIiIi11I1 - iI1iII1I1I1i % ooOOO - I11iiIi11i1I / IiIIii11Ii . Ooo0Ooo
 if 15 - 15: i1I * I11iiIi11i1I - oOo0O00
 if 6 - 6: IiI11Ii111 - Ii
 if not os . environ . get ( "DISPLAY" , "" ) :
  return False
  if 1 - 1: I1I + OooOoo
  if 98 - 98: i1iiIII111 + Iii1i . IIiIIiIi11I1
 msg = "\n" . join ( textwrap . wrap ( msg ) )
 if 96 - 96: OooOoo / oOO - i1 * I11iiIi11i1I
 if IiIIIII1i ( title , msg ) :
  return True
  if 72 - 72: i1i1i1111I + Ii - Iii1i - i1i1i1111I - i1I + Ooo0Ooo
 if O00 ( title , msg ) :
  return True
  if 74 - 74: Ooo0Ooo * Oo + Iii1i - i1iiIII111
 if i1IIIi ( title , msg ) :
  return True
  if 22 - 22: IiIIii11Ii - Ooo0Ooo . i1 . i1I - ooo000
 return False
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
