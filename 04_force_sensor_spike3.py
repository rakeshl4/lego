"""
Lesson 4: Force Sensor Control (SPIKE 3)
Learn: Control motor speed by pressing the Force Sensor
Time: 5 minutes
Hardware:
  - Force Sensor on port B
  - Motor on port A
"""

import force_sensor
import motor
import runloop
from hub import port

async def main():
    print("Press the Force Sensor to control motor speed!")
    
    while True:
        # Get force value (0 to 100 decinewtons)
        force = force_sensor.force(port.B)
        
        # Multiply by 10 to get good motor speed (0 to 1000 deg/sec)
        speed = force * 10
        
        # Run motor at calculated speed
        motor.run(port.A, speed)
        
        # Print for debugging
        if force > 0:
            print(f"Force: {force} dN, Speed: {speed} deg/sec")
        
        # Small delay
        await runloop.sleep_ms(100)

runloop.run(main())
