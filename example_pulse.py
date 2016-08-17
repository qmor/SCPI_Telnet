import time
import scpi_telnet
scpi = scpi_telnet.SCPI_Telnet("192.168.3.9",5024)
scpi.set_mode("PULS")
scpi.set_frequency(100)
scpi.set_high_voltage(5)
scpi.set_low_voltage(0)
scpi.set_pulse_width(0.000001)

scpi.set_burst_stat("ON")
scpi.set_trigger_source("BUS")
scpi.set_burst_ncycles(1)


while(1):
	scpi.set_burst_triggered()
	time.sleep(1)
