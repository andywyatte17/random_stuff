#!/usr/bin/env python3

import base64
from clipboard_win_lib import *

'''
The data copied from various software indicates the following information about the way CF_DIBV5
data is used in various software:

+-------------------------------+--------------+-----------------------------------------------+----------------+-----------------------+-----------+
| ..CF_DIBV5..                  | BI_type      | bitcount                                      | Alpha premult? | RGBA mask             | bV5CSType |
+-------------------------------+--------------+-----------------------------------------------+----------------+-----------------------+-----------+
| Chrome_78                     | BI_BITFIELDS | 32 - alpha                                    | Yes            | (f00, f0, f, 0)       | BGRs      |
+-------------------------------+--------------+-----------------------------------------------+----------------+-----------------------+-----------+
| Gimp_282_DIBV5                | BI_RGB       | 24 - no alpha                                 | N/A            | (0,0,0,0)             | BGRs      |
+-------------------------------+--------------+-----------------------------------------------+----------------+-----------------------+-----------+
| Paint.NET_425                 | BI_RGB       | 32 - alpha                                    | No             | (f00, f0, 000f, f000) | BGRs      |
+-------------------------------+--------------+-----------------------------------------------+----------------+-----------------------+-----------+
| P+2 PhotoStitch 12.4.2        | BI_BITFIELDS | 32 - alpha - program allows only 0/255 alpha. | No?            | (f00, f0, 000f, f000) | ' niW'    |
+-------------------------------+--------------+-----------------------------------------------+----------------+-----------------------+-----------+
| P+2 PhotoStitch 12.4.2 Hacked | BI_BITFIELDS | 32 - alpha                                    | No             | (f00, f0, 000f, f000) | ' niW'    |
+-------------------------------+--------------+-----------------------------------------------+----------------+-----------------------+-----------+

Generated from tsv data with help of https://www.tablesgenerator.com/text_tables

..CF_DIBV5..	BI_type	bitcount	Alpha premult?	RGBA mask	bV5CSType
Chrome_78	BI_BITFIELDS	32 - alpha	Yes	(f00, f0, f, 0)	BGRs
Gimp_282_DIBV5	BI_RGB	24 - no alpha	N/A	(0,0,0,0)	BGRs
Paint.NET_425	BI_RGB	32 - alpha	No	(f00, f0, 000f, f000)	BGRs
P+2 PhotoStitch 12.4.2	BI_BITFIELDS	32 - alpha - program allows only 0/255 alpha.	No?	(f00, f0, 000f, f000)	' niW'
P+2 PhotoStitch 12.4.2 Hacked	BI_BITFIELDS	32 - alpha	No	(f00, f0, 000f, f000)	' niW'

'''

def Install_Gimp_ClipExample16x16_PNG():
    '''
    This is clip-example-16x16.tga loading into Gimp 2.8.2 and copied.
    The data is the "PNG" clipboard type.
    '''
    d = r"""iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAfJJREFU
OE+FUstu00AUPQluRaQuiqIqUiV2sGDDrhLfUPEv/EJ/oKt+QldddMEGwQ4JiQokqJASx4nzdh7O
w4mTOKmT2AlzbnFVtwRGuhp77POYc2/C3N/3AYxU/VB18dJ1zzdqqefYCsMQw+EQhvEVvn+Go6PP
SKVCaOqvmSpb1S9VtQe4u1cSzOdzOM4G3e5THB7uIJO5JWj8ARtK/cs2guVyidFohH6/j6urJK6v
D5BOW+LggyqCz7eBqe55nlJ30Ol0MBisoesaej0Iwcd/KZOU6uPxWFnvKvBAspjNZup8B8n/ganu
ui5arRYsy5KdJL7vY71eQ/tb4tFV+MN0OhXb9XodtVoN7XZbzhaLBdis5LZ7E0ybBFQqFZRKJdl7
6uLMIwiC7QQEs2W2bQuoWCyiUCiIE16HmUSjwhBjK1ImmKq6riOXy4l9qpM4UidJjIAfaJtBUZng
bDYL0zRFfTKZYLVaiXrMAV+iQWGrqGwYhiiXy2XJIbJOh/cnXbu5CZUljqiDZrMpABLk83lJPgIz
dYLjaxfa6ff3eBVmsLfyUK1WBUj7jUZDBocto7uHysA7xXWMhNZLb56br/H20xt4li2qHJho2pgL
h+m+7VvwiSJIQQueOai/+IlvlwES+vKuVZw0Ah8r74kywcAT/AZZybA9ZaaVDAAAAABJRU5ErkJg
gg=="""
    d = base64.decodebytes(d.encode('ascii'))
    InstallClipData(PNG, d)


def Install_Gimp_ClipExample16x16_DIBV5():
    '''
    This is clip-example-16x16.tga loading into Gimp 2.8.2 and copied.
    The data is the CF_DIBV5 clipboard type.
    '''
    d = r"""fAAAABAAAAAQAAAAAQAYAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABC
R1JzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAA
AAAAAAAAAAAAAAD7AA/pAj1yNjc3Nx4eHg4ODgYGBgMDAwEBAQAAAAAAAAAAAAwAALkAAPgAAPsA
ABPqBEHFIXl+bWFhYUJCQiUlJRMTEwgICAQEBAEBAQAAAAAAAAAAAG8AAO8AAPgAAK3Ag8S9rLi4
uJeXl25ubkxMTC4uLhcXFwoKCgQEBAEBAQAAAAAAAAAAAG8AALkAAPz29vLy8t/f38PDw6CgoHx8
fFNTUzQ0NBoaGgoKCgMDAwEBAQEBAQAAAAAAAAYAAP////7+/vj4+Ofn59DQ0KysrISEhFlZWTY2
NhsbGwoKCgMDAwEBAQAAAAAAAAAAAP////////////v7+/Dw8NXV1bOzs4mJiV1dXTU1NRoaGgkJ
CQMDAwEBAQAAAAAAAP////////////////39/fLy8tra2ra2tomJiVpaWjMzMxcXFwgICAICAgEB
AQAAAP////////////////////39/fPz89ra2rOzs4WFhVNTUy0tLRISEgYGBgICAgEBAf//////
//////////////////39/fLy8tXV1aurq3p6ekZGRiIiIgwMDAMDAwEBAf//////////////////
//////////39/e/v783NzZ6enmhoaDg4OBgYGAcHBwICAgAAAAAAAAAAAAAAAAAAAP//////////
//z8/Obm5r29vYiIiFJSUiUlJQ4ODgMDAxAQ2wAAAAAAAAAAAAAAAP////////////////b29tjY
2KWlpW1tbTk5ORYWFgUFBRAQ2xAQ2wAAAAAAAAAAAP////////////////z8/Ofn57y8vIGBgUtL
SyEhIQALCxAQ2xAQ2xAQ2wAAAAAAAP////////////////////Pz88/Pz5qamk1fXx1nZwB6ehAQ
2xAQ2xAQ2xAQ2wAAAP////////////////////n5+eDg4K+vr0uYmAjU1ADr6xAQ2xAQ2xAQ2xAQ
2wAAAP////////////////////z8/Orq6rDCwkO6ugPv7wD4+A==
"""
    d = base64.decodebytes(d.encode('ascii'))
    InstallClipData(CF_DIBV5, d)


def Install_PaintNET_ClipExample16x16_DIBV5():
    '''
    This is clip-example-16x16.tga loading into Paint.NET 4.2.5 and copied.
    The data is the CF_DIBV5 clipboard type.
    '''
    d = r"""fAAAABAAAAAQAAAAAQAgAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAA/wAA/wAA/wAAAAAAAP9C
R1JzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAA
AAAAAAAAAAAAAAD7AP8P6QL/PXI2/zc3N/8eHh7/Dg4O/wYGBv8DAwP/AQEB/wAAAP8AAAD/AAAA
/wwAAP+5AAD/+AAA//sAAP8T6gT/QcUh/3l+bf9hYWH/QkJC/yUlJf8TExP/CAgI/wQEBP8BAQH/
AAAA/wAAAP8AAAD/bwAA/+8AAP/4AAD/rcCD/8S9rP+4uLj/l5eX/25ubv9MTEz/Li4u/xcXF/8K
Cgr/BAQE/wEBAf8AAAD/AAAA/wAAAP9vAAD/uQAA//z29v/y8vL/39/f/8PDw/+goKD/fHx8/1NT
U/80NDT/Ghoa/woKCv8DAwP/AQEB/wEBAf8AAAD/AAAA/wYAAP///////v7+//j4+P/n5+f/0NDQ
/6ysrP+EhIT/WVlZ/zY2Nv8bGxv/CgoK/wMDA/8BAQH/AAAA/wAAAP8AAAD/////////////////
+/v7//Dw8P/V1dX/s7Oz/4mJif9dXV3/NTU1/xoaGv8JCQn/AwMD/wEBAf8AAAD/AAAA////////
///////////////9/f3/8vLy/9ra2v+2trb/iYmJ/1paWv8zMzP/FxcX/wgICP8CAgL/AQEB/wAA
AP////////////////////////////39/f/z8/P/2tra/7Ozs/+FhYX/U1NT/y0tLf8SEhL/BgYG
/wICAv8BAQH//////////////////////////////////f39//Ly8v/V1dX/q6ur/3p6ev9GRkb/
IiIi/wwMDP8DAwP/AQEB///////////////////////////////////////9/f3/7+/v/83Nzf+e
np7/aGho/zg4OP8YGBj/BwcH/wICAv////8A////AP///wD///8A////AP////////////////z8
/P/m5ub/vb29/4iIiP9SUlL/JSUl/w4ODv8DAwP/EBDbPf///wD///8A////AP///wD/////////
////////////9vb2/9jY2P+lpaX/bW1t/zk5Of8WFhb/BQUF/xAQ24UQENtd////AP///wD///8A
//////////////////////z8/P/n5+f/vLy8/4GBgf9LS0v/ISEh/wALC/8QENvPEBDboBAQ213/
//8A////AP//////////////////////////8/Pz/8/Pz/+ampr/TV9f/x1nZ/8Aenr/EBDb7RAQ
288QENuFEBDbPf///wD///////////////////////////n5+f/g4OD/r6+v/0uYmP8I1NT/AOvr
/xAQ2/gQENvnEBDbtBAQ213///8A///////////////////////////8/Pz/6urq/7DCwv9Durr/
A+/v/wD4+P8="""
    d = base64.decodebytes(d.encode('ascii'))
    InstallClipData(CF_DIBV5, d)


def Install_Chrome_ClipExample16x16_Png_DIBV5():
    '''
    This is clip-example-16x16.png loading into Chrome 78.0.3904.97 and copied.
    The data is the CF_DIBV5 clipboard type.
    '''
    d = r"""fAAAABAAAAAQAAAAAQAgAAMAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAA/wAA/wAA/wAAAAAAAABC
R1JzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAA
AAAAAAAAAAAAAAAA/wAA/wAA/wAAAAD7AP8P6QL/PXI2/zc3N/8eHh7/Dg4O/wYGBv8DAwP/AQEB
/wAAAP8AAAD/AAAA/wwAAP+5AAD/+AAA//sAAP8T6gT/QcUh/3l+bf9hYWH/QkJC/yUlJf8TExP/
CAgI/wQEBP8BAQH/AAAA/wAAAP8AAAD/bwAA/+8AAP/4AAD/rcCD/8S9rP+4uLj/l5eX/25ubv9M
TEz/Li4u/xcXF/8KCgr/BAQE/wEBAf8AAAD/AAAA/wAAAP9vAAD/uQAA//z29v/y8vL/39/f/8PD
w/+goKD/fHx8/1NTU/80NDT/Ghoa/woKCv8DAwP/AQEB/wEBAf8AAAD/AAAA/wYAAP///////v7+
//j4+P/n5+f/0NDQ/6ysrP+EhIT/WVlZ/zY2Nv8bGxv/CgoK/wMDA/8BAQH/AAAA/wAAAP8AAAD/
////////////////+/v7//Dw8P/V1dX/s7Oz/4mJif9dXV3/NTU1/xoaGv8JCQn/AwMD/wEBAf8A
AAD/AAAA///////////////////////9/f3/8vLy/9ra2v+2trb/iYmJ/1paWv8zMzP/FxcX/wgI
CP8CAgL/AQEB/wAAAP////////////////////////////39/f/z8/P/2tra/7Ozs/+FhYX/U1NT
/y0tLf8SEhL/BgYG/wICAv8BAQH//////////////////////////////////f39//Ly8v/V1dX/
q6ur/3p6ev9GRkb/IiIi/wwMDP8DAwP/AQEB///////////////////////////////////////9
/f3/7+/v/83Nzf+enp7/aGho/zg4OP8YGBj/BwcH/wICAv8AAAAAAAAAAAAAAAAAAAAAAAAAAP//
//////////////z8/P/m5ub/vb29/4iIiP9SUlL/JSUl/w4ODv8DAwP/BAQ0PQAAAAAAAAAAAAAA
AAAAAAD/////////////////////9vb2/9jY2P+lpaX/bW1t/zk5Of8WFhb/BQUF/wgIcoUGBlBd
AAAAAAAAAAAAAAAA//////////////////////z8/P/n5+f/vLy8/4GBgf9LS0v/ISEh/wALC/8N
DbLPCgqJoAYGUF0AAAAAAAAAAP//////////////////////////8/Pz/8/Pz/+ampr/TV9f/x1n
Z/8Aenr/Dw/M7Q0Nss8ICHKFBAQ0PQAAAAD///////////////////////////n5+f/g4OD/r6+v
/0uYmP8I1NT/AOvr/xAQ1fgODsbnCwubtAYGUF0AAAAA///////////////////////////8/Pz/
6urq/7DCwv9Durr/A+/v/wD4+P8="""
    d = base64.decodebytes(d.encode('ascii'))
    InstallClipData(CF_DIBV5, d)


def Install_Pp2PhotoStitch_1242_ClipExample16x16_Png_DIBV5():
    '''
    This is clip-example-16x16.png loaded into Premier+ 2 PhotoStitch 12.4.2 and copied.
    The data is the CF_DIBV5 clipboard type.
    '''
    d = r"""fAAAABAAAAAQAAAAAQAgAAMAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAA/wAA/wAA/wAAAAAAAP8g
bmlXAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAA
AAAAAAAAAAAAAP8AAAAA/wAAAAD/AAD7AP8P6QL/PXI2/zc3N/8eHh7/Dg4O/wYGBv8DAwP/AQEB
/wAAAP8AAAD/AAAA/wwAAP+5AAD/+AAA//sAAP8T6gT/QcUh/3l+bf9hYWH/QkJC/yUlJf8TExP/
CAgI/wQEBP8BAQH/AAAA/wAAAP8AAAD/bwAA/+8AAP/4AAD/rcCD/8S9rP+4uLj/l5eX/25ubv9M
TEz/Li4u/xcXF/8KCgr/BAQE/wEBAf8AAAD/AAAA/wAAAP9vAAD/uQAA//z29v/y8vL/39/f/8PD
w/+goKD/fHx8/1NTU/80NDT/Ghoa/woKCv8DAwP/AQEB/wEBAf8AAAD/AAAA/wYAAP///////v7+
//j4+P/n5+f/0NDQ/6ysrP+EhIT/WVlZ/zY2Nv8bGxv/CgoK/wMDA/8BAQH/AAAA/wAAAP8AAAD/
////////////////+/v7//Dw8P/V1dX/s7Oz/4mJif9dXV3/NTU1/xoaGv8JCQn/AwMD/wEBAf8A
AAD/AAAA///////////////////////9/f3/8vLy/9ra2v+2trb/iYmJ/1paWv8zMzP/FxcX/wgI
CP8CAgL/AQEB/wAAAP////////////////////////////39/f/z8/P/2tra/7Ozs/+FhYX/U1NT
/y0tLf8SEhL/BgYG/wICAv8BAQH//////////////////////////////////f39//Ly8v/V1dX/
q6ur/3p6ev9GRkb/IiIi/wwMDP8DAwP/AQEB///////////////////////////////////////9
/f3/7+/v/83Nzf+enp7/aGho/zg4OP8YGBj/BwcH/wICAv////8A////AP///wD///8A////AP//
//////////////z8/P/m5ub/vb29/4iIiP9SUlL/JSUl/w4ODv8DAwP/EBDbAP///wD///8A////
AP///wD/////////////////////9vb2/9jY2P+lpaX/bW1t/zk5Of8WFhb/BQUF/xAQ2/8QENv/
////AP///wD///8A//////////////////////z8/P/n5+f/vLy8/4GBgf9LS0v/ISEh/wALC/8Q
ENv/EBDb/xAQ2/////8A////AP//////////////////////////8/Pz/8/Pz/+ampr/TV9f/x1n
Z/8Aenr/EBDb/xAQ2/8QENv/EBDbAP///wD///////////////////////////n5+f/g4OD/r6+v
/0uYmP8I1NT/AOvr/xAQ2/8QENv/EBDb/xAQ2/////8A///////////////////////////8/Pz/
6urq/7DCwv9Durr/A+/v/wD4+P8="""
    d = base64.decodebytes(d.encode('ascii'))
    InstallClipData(CF_DIBV5, d)


def Install_Pp2PhotoStitch_1242_Hacked_ClipExample16x16_Png_DIBV5():
    '''
    Premier+ 2 PhotoStitch was hacked to use the standard Premier+ 2 copy-bitmap
    code using clip-example-16x16.png as the source data.
    The data is the CF_DIBV5 clipboard type.
    '''
    d = r"""fAAAABAAAAAQAAAAAQAgAAMAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAA/wAA/wAA/wAAAAAAAP8g
bmlXAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAA
AAAAAAAAAAAAAP8AAAAA/wAAAAD/AAD7AP8P6QL/PXI2/zc3N/8eHh7/Dg4O/wYGBv8DAwP/AQEB
/wAAAP8AAAD/AAAA/wwAAP+5AAD/+AAA//sAAP8T6gT/QcUh/3l+bf9hYWH/QkJC/yUlJf8TExP/
CAgI/wQEBP8BAQH/AAAA/wAAAP8AAAD/bwAA/+8AAP/4AAD/rcCD/8S9rP+4uLj/l5eX/25ubv9M
TEz/Li4u/xcXF/8KCgr/BAQE/wEBAf8AAAD/AAAA/wAAAP9vAAD/uQAA//z29v/y8vL/39/f/8PD
w/+goKD/fHx8/1NTU/80NDT/Ghoa/woKCv8DAwP/AQEB/wEBAf8AAAD/AAAA/wYAAP///////v7+
//j4+P/n5+f/0NDQ/6ysrP+EhIT/WVlZ/zY2Nv8bGxv/CgoK/wMDA/8BAQH/AAAA/wAAAP8AAAD/
////////////////+/v7//Dw8P/V1dX/s7Oz/4mJif9dXV3/NTU1/xoaGv8JCQn/AwMD/wEBAf8A
AAD/AAAA///////////////////////9/f3/8vLy/9ra2v+2trb/iYmJ/1paWv8zMzP/FxcX/wgI
CP8CAgL/AQEB/wAAAP////////////////////////////39/f/z8/P/2tra/7Ozs/+FhYX/U1NT
/y0tLf8SEhL/BgYG/wICAv8BAQH//////////////////////////////////f39//Ly8v/V1dX/
q6ur/3p6ev9GRkb/IiIi/wwMDP8DAwP/AQEB///////////////////////////////////////9
/f3/7+/v/83Nzf+enp7/aGho/zg4OP8YGBj/BwcH/wICAv////8A////AP///wD///8A////AP//
//////////////z8/P/m5ub/vb29/4iIiP9SUlL/JSUl/w4ODv8DAwP/EBDbPf///wD///8A////
AP///wD/////////////////////9vb2/9jY2P+lpaX/bW1t/zk5Of8WFhb/BQUF/xAQ24UQENtd
////AP///wD///8A//////////////////////z8/P/n5+f/vLy8/4GBgf9LS0v/ISEh/wALC/8Q
ENvPEBDboBAQ213///8A////AP//////////////////////////8/Pz/8/Pz/+ampr/TV9f/x1n
Z/8Aenr/EBDb7RAQ288QENuFEBDbPf///wD///////////////////////////n5+f/g4OD/r6+v
/0uYmP8I1NT/AOvr/xAQ2/gQENvnEBDbtBAQ213///8A///////////////////////////8/Pz/
6urq/7DCwv9Durr/A+/v/wD4+P8="""
    d = base64.decodebytes(d.encode('ascii'))
    InstallClipData(CF_DIBV5, d)
