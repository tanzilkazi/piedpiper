# Reads temperature from sensor and prints to stdout
# id is the id of the sensor
# def readSensor(id):
# 	tfile = open("/sys/bus/w1/devices/"+id+"/w1_slave")
# 	text = tfile.read()
# 	tfile.close()
# 	secondline = text.split("\n")[1]
# 	temperaturedata = secondline.split(" ")[9]
# 	temperature = float(temperaturedata[2:])
# 	temperature = temperature / 1000
# 	print "Sensor: " + id  + " - Current temperature : %0.3f C" % temperature


# Reads temperature from all sensors found in /sys/bus/w1/devices/
# starting with "28-...

import os, time

def readTemp():
	count = 0
	while True:
		sensor = ""
		for file in os.listdir("/sys/bus/w1/devices/"):
			if (file.startswith("28-")):
				# Reads temperature from sensor and prints to stdout
				# id is the id of the sensor
				tfile = open("/sys/bus/w1/devices/"+file+"/w1_slave")
				text = tfile.read()
				tfile.close()
				secondline = text.split("\n")[1]
				temperaturedata = secondline.split(" ")[9]
				temperature = float(temperaturedata[2:])/1000
				print "Sensor: " + file  + " - Current temperature : %0.3f C" % temperature
			count+=1
		if (count == 0):
			print "No sensor found! Check connection"
		time.sleep(1)

def destroy():
	print "Stopping sensor reading..."

if __name__ == "__main__":
	try:
		readTemp()
	except KeyboardInterrupt:
		destroy()