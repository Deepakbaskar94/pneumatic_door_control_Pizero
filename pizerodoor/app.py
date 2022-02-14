import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define actuators GPIOs
ledRed = 14
ledYlw = 15

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
    status = "Unknown"
    return render_template('index2.html', cs = status)

@app.route("/dooropen/on")
def dooropen():
    GPIO.output(ledRed, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(ledRed, GPIO.LOW)

    status = "Door Open"
    return render_template('index2.html', cs = status)


@app.route("/doorclose/on")
def doorclose():
    GPIO.output(ledYlw, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(ledYlw, GPIO.LOW)

    status = "Door Close"
    return render_template('index2.html', cs = status)


@app.route('/repeat', methods = ['POST', 'GET'])
def repeat():
    if request.method == "POST":
        num = request.form['num1']
        num = int(num)
        for x in range(num):
            GPIO.output(ledRed, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(ledRed, GPIO.LOW)
            time.sleep(1)
            GPIO.output(ledYlw, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(ledYlw, GPIO.LOW)
            time.sleep(1)

        status = "completed"
        return render_template('index2.html', cs = status)
    else:
        status = "not completed"
        render_template('index2.html', cs = status)
	
@app.route("/find")
def test():
    result = "door"
    return result

if __name__ == "__main__":
   #port = 5000 + random.randint(0, 999)
   #print(port)
   #url = "http://192.168.4.1:{0}".format(port)
   #print(url)
   app.run(use_reloader=False, host='0.0.0.0', port=3000, debug=True)
   
