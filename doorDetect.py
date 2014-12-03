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



while (True) :
	if (GPIO.input(12) == False):
		print("Door opened")
		while (GPIO.input(12) == False):
			x = 1 # Garbage added 
		
		print("Door closed")
		if (currLightState == True):
			currLightState = False
			GPIO.output(11, currLightState)
		else:
			currLightState = True
			GPIO.output(11, currLightState)
		
		
		
GPIO.cleanup()

