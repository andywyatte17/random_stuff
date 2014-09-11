#!/bin/python

mapping = { 'k':'Black-Haired', 'c':'Brown-Haired',
            'o':'Orange-Haired', 'y':'Yellow-Haired',
            'w':'White-Haired',
            #
            'B':'Blue-Eyed',
            #
            'h':'Hatted',
            #
            'C':'Bearded', 'M':'Moustached',
            #
            'H':'Big-Nosed',       # H = 'H'onker = Slang for Big Nose
            #
            'F':'Bald-On-Top',     # F = 'F'ly Rink = Victorian Slang for Bald
            #
            'g':'Bespectacled',
            #
            'r':'Rosy-Cheeked',
            #
            'f':'Female'
          }

inferred = { frozenset(('Female',)):'Male',
             frozenset(('Blue-Eyed',)):'Brown-Eyed',
             frozenset(('Hatted',)):'Un-hatted',
             frozenset(('Bearded','Moustached')):'Clean-Shaven'
           }

people = \
'''
  Alex - k,M,
  Alfred - M,o,B,
  Anita - f,y,r,B,
  Anne - f,k,H,
  Bernard - c,H,h
  Bill - C,o,F,r,
  Charles - M,y,
  Claire - f,g,o,h
  David - C,y,
  Eric - y,h,
  Frans - o,
  George - w,h,
  Herman - o,H,F,
  Joe - g,y,
  Maria - f,c,h,
  Max - M,c,H,
  Paul - g,w,
  Peter - w,H,B,
  Philip - C,k,r,
  Richard - M,C,c,F,
  Robert - c,H,r,B,
  Sam - g,w,F,
  Susan - f,w,r,
  Tom - g,k,F,B,
'''