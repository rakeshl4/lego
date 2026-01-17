"""
Lesson 3: Distance Bot (SPIKE 3)
Learn: Stop before hitting walls using distance sensor
Time: 10 minutes
Hardware: 
  - Distance Sensor on port C
  - Motors on ports A & B (left and right wheels)
Challenge: Make robot stop 100mm from obstacles
"""

import distance_sensor
import motor
import runloop
from hub import port, light_matrix

async def main():
    print("Robot starting... will stop near walls!")
    light_matrix.show_image(light_matrix.IMAGE_ARROW_N)
    
    while True:
        # Get distance in millimeters
        dist = distance_sensor.distance(port.C)
        
        # Check if something is close (within 100mm)
        if dist != -1 and dist < 100:
            print(f"Too close! Distance: {dist}mm. Stopping.")
            light_matrix.show_image(light_matrix.IMAGE_NO)
            motor.stop(port.A)
            motor.stop(port.B)
            break
        
        # Keep moving forward
        motor.run(port.A, 300)  # Left wheel
        motor.run(port.B, 300)  # Right wheel
        
        # Small delay to check distance regularly
        await runloop.sleep_ms(50)
    
    print("Mission complete!")
    await runloop.sleep_ms(2000)
    light_matrix.clear()

runloop.run(main())
