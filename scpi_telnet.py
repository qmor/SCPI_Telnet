import telnetlib
import time
class SCPI_Telnet():
	def __init__(self,host,port):
		self.tn = telnetlib.Telnet(host,port)
		#self.tn.set_debuglevel("info")
		time.sleep(0.1)
		self.tn.read_some()
	def read_measure_volage(self,channel):
		p=1
		dt=""
		self.tn.read_eager()
		while(p>0):
			self.tn.write(":MEAS:VOLT? (@" + str(channel) + ")\n")
			#self.tn.write("FETC:VOLT? (@" + str(channel) + ")\n")
			dt +=self.tn.read_some()
			p-=1
		return float(dt.split("\n")[0].strip())
	def read_measure_current(self,channel):
		self.tn.read_eager()
		p=1
		dt=""
		while(p>0):
			self.tn.write(":MEAS:CURR? (@" + str(channel) + ")\n")
			dt +=self.tn.read_some()
			p-=1
		return float(dt.split("\n")[0].strip())

	def set_output(self,channel,status):
		self.tn.read_eager()
		p=1
		dt=""
		while(p>0):
			self.tn.write(":OUTP %s, (@" %(["off","on"][status==1]) + str(channel) + ")\n")
			dt +=self.tn.read_some()
			p-=1