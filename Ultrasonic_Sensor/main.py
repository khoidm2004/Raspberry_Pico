from machine import Pin # type: ignore
import utime # type: ignore

# Define trigger and echo pins
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def main(): 
    # Send a short LOW pulse to ensure the trigger is clean
    trigger.low()
    utime.sleep_us(2)
    
    # Send a HIGH pulse for 10 microseconds
    trigger.high()
    utime.sleep_us(10)
    trigger.low()
    
    # Wait for the echo pin to go HIGH (start of signal)
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    
    # Wait for the echo pin to go LOW (end of signal)
    while echo.value() == 1:
        signalon = utime.ticks_us()
    
    # Calculate time passed
    timepassed = utime.ticks_diff(signalon, signaloff)
    
    # Calculate distance (speed of sound is 0.0343 cm/us, divided by 2 for round trip)
    distance = (timepassed * 0.0343) / 2
    
    # Print the calculated distance
    print("The object is", distance, "cm away.")

# Main loop
while True:
    main()
    utime.sleep(1)
