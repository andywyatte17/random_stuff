import SimpleHTTPServer
import SocketServer
import logging
import cgi
import datetime
import random
from pprint import pprint
import os
import platform

PORT = 8000

def RandomCodeGen():
	return random.randint(0x1000,0xffff)

CODE = "{0:x}".format(RandomCodeGen())
open("code.txt", "w").write(CODE)

class SendKeyOS:
	(Dunno, WinXX, OSX) = range(0, 3)

sendKeyOS = SendKeyOS.Dunno

platSys = platform.system()
if platSys=="Darwin":
	sendKeyOS = SendKeyOS.OSX
if platSys=="Windows":
	sendKeyOS = SendKeyOS.WinXX

if sendKeyOS==SendKeyOS.WinXX:
	try:
		import win32com.client
	except:
		print "You must install pyWin32"
		exit(1)

def SendKey(keys):
	if sendKeyOS==SendKeyOS.WinXX:
		shell = win32com.client.Dispatch("WScript.Shell")
		shell.SendKeys(keys, 0)
	if sendKeyOS==SendKeyOS.OSX:
		# Keycode list... http://apple.stackexchange.com/questions/36943/how-do-i-automate-a-key-press-in-applescript
		kc = 0
		if keys=="{RIGHT}": kc = 124
		if keys=="{LEFT}": kc = 123
		if kc:
			cmd = """ osascript -e 'tell application "System Events" to key code {0}' """.format( kc )
			os.system(cmd)
	return

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_POST_op(self, path):
		if path=='/right':
			SendKey("{RIGHT}")
			print "Sending {RIGHT}"
		if path=='/left':
			SendKey("{LEFT}")
			print "Sending {LEFT}"

	def do_GET(self):
		logging.error(self.headers)
		SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

	def do_POST(self):
		length = int( self.headers['Content-Length'] )
		post_data = self.rfile.read(length).decode('utf-8')
		print "post_data=", post_data
		if post_data==CODE:
			self.do_POST_op( self.path )
		self.send_response(200)
		self.send_header('Content-type','text')
		self.end_headers()
		self.wfile.write( self.path )

Handler = ServerHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()