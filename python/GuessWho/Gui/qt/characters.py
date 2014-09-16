#!/bin/python

mapping = { 'k':('Hair','Black-Haired'),
            'c':('Hair', 'Brown-Haired'), 
            'o':('Hair', 'Orange-Haired'),
            'y':('Hair', 'Yellow-Haired'), 
            'w':('Hair', 'White-Haired'), 
            #
            'B':('Eyes', 'Blue-Eyed'), 
            #
            'h':('Other', 'Hatted'),
            #
            'C':('Facial Hair', 'Bearded'),
            'M':('Facial Hair', 'Moustached'),
            #
            'H':('Other', 'Big-Nosed'),       # H = 'H'onker = Slang for Big Nose
            #
            'F':('Other', 'Bald-On-Top'),     # F = 'F'ly Rink = Victorian Slang for Bald
            #
            'g':('Other', 'Bespectacled'),
            #
            'r':('Other', 'Rosy-Cheeked'),
            #
            'f':('Other', 'Female')
          }

inferred = { frozenset(('Female',)):('Other', 'Male'), 
             frozenset(('Blue-Eyed',)):('Eyes', 'Brown-Eyed'),  
             frozenset(('Hatted',)):('Other', 'Hatless'), 
             frozenset(('Bearded','Moustached')):('Facial Hair', 'Clean-Shaven')
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
