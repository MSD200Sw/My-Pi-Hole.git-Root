# -*-mode: python; coding: utf-8 -*-
#
# Copyright 2012-2014 Pierre Ossman for Cendio AB.
# For more information, see http://www.cendio.com
import textwrap
if 82 - 82: Iii1i
from . import tlgtk
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
__all__ = [ "Wizard" ,
 "text_print_wrapped" , "text_print_title" , "text_wait_prompt" , "text_prompt" ,
 "interactive" ]
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
if 98 - 98: I11iiIi11i1I % oOO
if 31 - 31: i1I
if 9 - 9: IiI11Ii111 / oOo0O00 / IiIIii11Ii - I11iiIi11i1I - iI1iII1I1I1i
if 16 - 16: i1i1i1111I / i1iiIII111
interactive = True
if 3 - 3: i1 % i1 % i1i1i1111I . Ii * i1
def text_print_wrapped ( text , width = 72 ) :
 for ii1iI1I in text . splitlines ( ) :
  print ( textwrap . fill ( ii1iI1I , width ) )
  if 28 - 28: i1I / IIiIIiIi11I1 % IIiIIiIi11I1 / I1I - Oo
  if 13 - 13: IiIIii11Ii - Ooo0Ooo - Ii - Oo * ooo000 . i1iiIII111
def text_print_title ( title ) :
 print ( title )
 print ( len ( title ) * "=" )
 if 14 - 14: I1I / oOO
 if 58 - 58: I1Ii1I1 - ooOOO
def text_wait_prompt ( ) :
 if interactive :
  input ( "Press Enter to continue..." )
  if 60 - 60: iI1iII1I1I1i . oOO
  if 13 - 13: oOO
def text_prompt ( text , accepts ) :
 iiIII = None
 if 28 - 28: I1Ii1I1 . Iii1i - ooOOO - iI1iII1I1I1i
 if 37 - 37: oOO * IIiIIiIi11I1 * I1I / oOo0O00
 if 28 - 28: i1I
 if 95 - 95: i1iiIII111 . Ii . IIiIIiIi11I1 % I11iiIi11i1I % I1Ii1I1
 if 8 - 8: I1Ii1I1 . IiI11Ii111 . i1 . Oo - i1I
 for iiI1111IIi1 in accepts :
  if not iiI1111IIi1 . islower ( ) and iiIII is None :
   iiIII = iiI1111IIi1 . lower ( )
   if 92 - 92: ooOOO / OooOoo - oOo0O00
   if 59 - 59: Iii1i . IiI11Ii111 - i1I
 ii1IiIiiII = [ iiI1111IIi1 . lower ( ) for iiI1111IIi1 in accepts ]
 if 21 - 21: oOo0O00 % I11iiIi11i1I % oOO . oOo0O00
 while ( True ) :
  iii11i = input ( text + " [" + "/" . join ( accepts ) + "]?" )
  if len ( iii11i ) == 0 and iiIII is not None :
   return iiIII
   if 35 - 35: I1I % i1iiIII111 * I1I
  iii11i = iii11i . lower ( )
  if 88 - 88: I11iiIi11i1I + ooOOO - i1i1i1111I . Ooo0Ooo * Ii + Iii1i
  if iii11i is None :
   continue
   if 43 - 43: ooOOO * I1Ii1I1
   if 95 - 95: Ooo0Ooo % Iii1i % i1i1i1111I . OooOoo
  I1iIiiIIiIi = 0
  i1I11ii = ""
  for iiI1111IIi1 in ii1IiIiiII :
   if iiI1111IIi1 . startswith ( iii11i ) :
    I1iIiiIIiIi = I1iIiiIIiIi + 1
    if I1iIiiIIiIi == 1 :
     i1I11ii = iiI1111IIi1
     if 21 - 21: Iii1i - I1Ii1I1
  if I1iIiiIIiIi == 1 :
   return i1I11ii
   if 95 - 95: i1 - I1Ii1I1 + Oo
   if 49 - 49: IIiIIiIi11I1
class Wizard :
 def __init__ ( self ) :
  self . _title = None
  if 29 - 29: IiIIii11Ii - oOo0O00
  self . _intro = None
  self . _intro_title = None
  self . _intro_text = None
  self . _intro_button_text = None
  if 30 - 30: I1I . ooo000
  self . _banner_path = None
  self . _width = - 1
  self . _height = - 1
  if 43 - 43: ooOOO . I11iiIi11i1I + ooo000
  self . _text_handlers = [ ]
  self . _gui_handlers = [ ]
  if 87 - 87: Iii1i + ooOOO . i1I / Ii + Oo
 def set_title ( self , title ) :
  self . _title = title
  if 77 - 77: i1iiIII111 + IiI11Ii111 - Oo % ooo000
 def set_intro ( self , title , text , button_text ,
 banner_path = None , width = - 1 , height = - 1 ) :
  self . _intro_title = title
  self . _intro_text = text
  self . _intro_button_text = button_text
  if 74 - 74: Ii + Ooo0Ooo
  self . _banner_path = banner_path
  self . _width = width
  self . _height = height
  if 1 - 1: I1I % Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo
 def add_text_handler ( self , handler ) :
  self . _text_handlers . append ( handler )
  if 93 - 93: oOo0O00 % Ooo0Ooo * i1iiIII111
 def add_gui_handler ( self , handler ) :
  self . _gui_handlers . append ( handler )
  if 52 - 52: oOO + I1I / ooo000 - I1Ii1I1 * i1I % oOo0O00
 def run ( self ) :
  try :
   if not tlgtk . has_gtk :
    return self . _run_text ( )
   else :
    return self . _run_gui ( )
  except KeyboardInterrupt :
   return False
   if 52 - 52: oOo0O00 . I1I + i1I - i1iiIII111 % iI1iII1I1I1i
 def _run_text ( self ) :
  if self . _intro_title is not None :
   text_print_title ( self . _intro_title )
   print ( )
   if 57 - 57: I1I * IIiIIiIi11I1 % I1Ii1I1 * i1i1i1111I
  if self . _intro_text is not None :
   text_print_wrapped ( self . _intro_text )
   print ( )
   text_wait_prompt ( )
   print ( )
   if 37 - 37: IiI11Ii111 * i1i1i1111I + oOo0O00 / I1I / OooOoo
  for iI1iI in self . _text_handlers :
   iI1iI ( )
   if 54 - 54: I1I % ooo000 * ooo000 - OooOoo / Iii1i * Oo
  return True
  if 100 - 100: I1Ii1I1 / I11iiIi11i1I * Ii - oOO
 def _run_gui ( self ) :
  iiI1111II = tlgtk . wizard . Wizard ( )
  iiI1111II . set_default_size ( 880 , 530 )
  if 79 - 79: Ooo0Ooo % iI1iII1I1I1i % IIiIIiIi11I1 / ooOOO - ooOOO / I11iiIi11i1I
  if self . _title is not None :
   iiI1111II . set_title ( self . _title )
   if 63 - 63: ooOOO / i1i1i1111I - oOo0O00 * ooOOO / i1iiIII111 + oOO
  if self . _intro_title is not None :
   iiI1 = self . _intro_text
   iiI1111II . add_intro ( self . _intro_title , iiI1 ,
 self . _intro_button_text ,
 self . _banner_path , self . _width , self . _height )
   if 20 - 20: i1i1i1111I / Ooo0Ooo - oOO + Ooo0Ooo - I1I . Ooo0Ooo
  for iI1iI in self . _gui_handlers :
   iI1iI ( iiI1111II )
   if 50 - 50: Iii1i * ooo000 % Iii1i - oOo0O00 + ooo000
  return iiI1111II . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
