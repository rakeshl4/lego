"""
Lesson 8: Line Follower Robot (SPIKE 3)
Learn: Follow a black line using the Color Sensor
Time: 15 minutes
Hardware:
  - Color Sensor on port C (pointing down at the line)
  - Motors on ports A & B (left and right wheels)
Challenge: Follow a black line on white surface
"""

import color_sensor
import motor_pair
import color
import runloop
from hub import port, light_matrix

async def main():
    # Setup motor pair
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
    
    print("Line follower starting!")
    light_matrix.show_image(light_matrix.IMAGE_ARROW_N)
    
    base_speed = 300  # Base speed for motors
    
    # Run for 20 seconds
    for i in range(400):  # 400 * 50ms = 20 seconds
        # Get reflected light intensity (0-100)
        reflection = color_sensor.reflection(port.C)
        
        # Simple line following logic:
        # - High reflection (white) = turn one way
        # - Low reflection (black) = turn other way
        
        if reflection > 50:
            # On white surface - turn left to find line
            steering = -30
        else:
            # On black line - turn right to stay on it
            steering = 30
        
        # Move with calculated steering
        motor_pair.move(motor_pair.PAIR_1, steering, velocity=base_speed)
        
        await runloop.sleep_ms(50)
    
    # Stop motors
    motor_pair.stop(motor_pair.PAIR_1)
    light_matrix.show_image(light_matrix.IMAGE_YES)
    print("Line following complete!")

runloop.run(main())
