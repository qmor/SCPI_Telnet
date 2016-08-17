import telnetlib
import time
class SCPI_Telnet():
	def __init__(self,host,port):
		self.tn = telnetlib.Telnet(host,port)
		#self.tn.set_debuglevel("info")
		time.sleep(0.1)
		self.tn.read_some()
	def __send_set_command(self,command):
		self.tn.read_eager()
		p=1
		dt=""
		while(p>0):
			self.tn.write(command)
			dt +=self.tn.read_some()
			p-=1
	def set_output_off(self):
		self.__send_set_command(":OUTPut OFF\n")
	def set_pulse_width(self,width):
		self.__send_set_command(":FUNCtion:PULSe:WIDTh %f\n" %width)
	def set_high_voltage(self,value):
		self.__send_set_command(":VOLTage:HIGH %d\n" %value)
	def set_low_voltage(self,value):
		self.__send_set_command(":VOLTage:LOW %d\n" %value)
	def set_frequency(self,freq):
		self.__send_set_command(":FREQ %d\n" %freq)
	def set_burst_source(self,source): #source is IMM EXT BUS
		self.__send_set_command(":BURSt:SOURce %s\n" %source)
	def set_trigger_source(self,source): #source is IMM EXT BUS
		self.__send_set_command(":TRIG:SOURce %s\n" %source)
	def set_burst_ncycles(self,ncycles):
		self.__send_set_command(":BURSt:NCYCLES %d\n" %ncycles)
	def set_burst_stat(self,onoroff): #onoroff is ON OFF
		self.__send_set_command(":BURSt:STAT %s\n" %onoroff)
	def set_burst_triggered(self):
		self.__send_set_command("*TRG\n")
	def set_mode(self,mode): #MODE is SIN SQU RAMP PULS NOISE DC USER
		self.__send_set_command(":FUNCtion %s \n" %mode)
	def set_output(self,channel,status):
		self.__send_set_command(":OUTP %s, (@" %(["off","on"][status==1]) + str(channel) + ")\n")


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

	def get_output(self,channel):
		self.tn.read_eager()
		p=1
		dt=""
		while(p>0):
			self.tn.write(":STAT:OPER:COND? (@" + str(channel) + ")\n")
			dt +=self.tn.read_some()
			p-=1
		dt = dt.split('\n')[0].strip().replace('+','')
		dt = int(dt)
		if ((dt>>2)&1 == 1):#bit 3 means "1 - output off, 0 - output on"
			return 0
		else:
			return 1