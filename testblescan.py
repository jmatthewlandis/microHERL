# test BLE Scanning software
# jcs 6/8/2014

# Setup GPIO on RPi
import RPi.GPIO as GPIO
# Use board pin numbering
GPIO.setmode(GPIO.BOARD)


# Setup GPIO pins
GPIO.setup(11, GPIO.OUT) # Output for PowerTail
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Input for door detection

# Initialize light state to off
currLightState = False
# Initialize PowerTail to off
GPIO.output(11, currLightState)




import blescan
import sys

import bluetooth._bluetooth as bluez

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)



while True:
	returnedList = blescan.parse_events(sock, 10)
	#print "----------"
	for beacon in returnedList:
		if ((pkt[report_pkt_offset -22: report_pkt_offset - 6]) == "2f 23 44 54 cf 6d 4a 0f ad f2 f4 91 1b a9 ff a6 None")
		print("Found correct beacon!!!")
		#print beacon



GPIO.cleanup()