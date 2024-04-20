import smtplib
import time
import busio
import board
import adafruit_adxl34x

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com (http://smtp.gmail.com/)', 587)
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)
accelerometer.enable_tap_detection()
# start TLS for security
s.starttls()
# Authentication
s.login("SenderEmail@gmail.com (mailto:SenderEmail@gmail.com)", "CHANGED FOR PRIVACY")
# message to be sent
message = "The player has been hit hard enough to warrant a concussion. Please Remove them from the game and run concussion protocol"

while True:

print("%f %f %f" % accelerometer.acceleration)

print("Tapped: %s" % accelerometer.events["tap"])
if accelerometer.events["tap"]==True:
print("worked")
# sending the mail
s.sendmail("SenderEmail@gmail.com (mailto:SenderEmail@gmail.com)
", "
Recipient@gmail.com (mailto:Recipient@gmail.com)
", message)
time.sleep(0.5)
