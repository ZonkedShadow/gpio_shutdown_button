import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pin 26 als Eingang, mit Pull-Up-Widerstand

def shutdown_when_low():
    while True:
        if GPIO.input(26) == GPIO.LOW:  # Wenn der Pin auf LOW ist
            time.sleep(3)  # Warte 3 Sekunden
            if GPIO.input(26) == GPIO.LOW:  # Überprüfe erneut, ob der Pin immer noch auf LOW ist
                time.sleep(2)
                if GPIO.input(26) == GPIO.LOW:
                    os.system("sudo shutdown -h now")  # Raspberry Pi herunterfahren

                os.system("sudo reboot")
        time.sleep(0.1)  # Kurze Pause, um die CPU-Auslastung zu reduzieren

try:
    shutdown_when_low()
except KeyboardInterrupt:
    GPIO.cleanup()  # GPIO-Pins zurücksetzen, wenn das Skript mit Strg+C beendet wird
