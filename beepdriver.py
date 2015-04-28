from smap import driver
from smap.archiver.client import RepublishClient
import time
import socket

class beepdriver(driver.SmapDriver):
	def setup(self, opts):
		self.add_timeseries('/beep', 'unit', data_type='double')
		self.archiverurl = opts.get('archiverurl','http://shell.storm.pm:8079')
		self.subscription = opts.get('subscription','Metadata/Sourcename = "BeepCommand"')
		self.r = RepublishClient(self.archiverurl, self.cb, restrict=self.subscription)
		self.sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
		self.target = opts.get("target", "2001:470:832b:2:212:6d02:0:3103")
        
	def cb(self, points, data):
	    ivkid = int(time.time())
		msg = chr(ivkid&0xFF) + chr((ivkid>>8)&0xFF) + chr((ivkid>>16)&0xFF) + chr((ivkid>>24)&0xFF)
		self.sock.sendto(msg, (self.target, 4000)
		self.sock.sendto(msg, (self.target, 4000)
	
	def start(self):
		self.r.connect()
	
	def stop(self):
        pass
