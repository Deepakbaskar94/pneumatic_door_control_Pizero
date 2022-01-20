import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define actuators GPIOs
ledRed = 25
ledYlw = 24

#initialize GPIO status variables
ledRedSts = 0
ledYlwSts = 0

# Define led pins as output
GPIO.setup(ledRed, GPIO.OUT)   
GPIO.setup(ledYlw, GPIO.OUT) 
 
# turn leds OFF 
GPIO.output(ledRed, GPIO.LOW)
GPIO.output(ledYlw, GPIO.LOW)
	
@app.route("/")
def index():
	# Read GPIO Status
	ledRedSts = GPIO.input(ledRed)
	ledYlwSts = GPIO.input(ledYlw)
	
	templateData = {
      'ledRed'  : ledRedSts,
      'ledYlw'  : ledYlwSts,
      }
	return render_template('index.html', **templateData)
	
# The function below is executed when someone requests a URL with the actuator name and action in it:
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	if deviceName == 'dooropen':
		actuator = ledRed
	if deviceName == 'doorclose':
		actuator = ledYlw
	  
	if action == "on":
        	GPIO.output(actuator, GPIO.HIGH)
        	time.sleep(2)
        	GPIO.output(actuator, GPIO.LOW)
		     
	ledRedSts = GPIO.input(ledRed)
	ledYlwSts = GPIO.input(ledYlw)
	   
	templateData = {
	  'ledRed'  : ledRedSts,
          'ledYlw'  : ledYlwSts,
      	}
	return render_template('index.html', **templateData)

if __name__ == "__main__":
   #port = 5000 + random.randint(0, 999)
   #print(port)
   #url = "http://192.168.4.1:{0}".format(port)
   #print(url)
   app.run(use_reloader=False, host='192.168.4.1', port=80, debug=True)
   
