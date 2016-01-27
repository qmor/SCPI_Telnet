import scpi_telnet
import time
scpi = scpi_telnet.SCPI_Telnet("192.168.3.99",5024)


print "power on main power"
scpi.set_output(2,1)
time.sleep(0.5)
print "main voltage ",scpi.read_measure_volage(2)
print "main current ",scpi.read_measure_current(2)

print "power on pulse"
scpi.set_output(3,1)
time.sleep(0.5)
print "pulse voltage ",scpi.read_measure_volage(3)
print "pulse current ",scpi.read_measure_current(3)

print "power off pulse"
scpi.set_output(3,0)
time.sleep(0.5)
print "pulse voltage ",scpi.read_measure_volage(3)
print "pulse current ",scpi.read_measure_current(3)
print "main voltage ",scpi.read_measure_volage(2)
print "main current ",scpi.read_measure_current(2)