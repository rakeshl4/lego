"""
Lesson 11: Happy & Sad Motor (SPIKE 3)
Learn: Show emotions on display while rotating motor
Time: 5 minutes
Hardware: Connect a motor to port A
"""

import motor
import runloop
from hub import port, light_matrix

async def main():
    print("Starting Happy & Sad Motor program...")
    
    # Show happy face and rotate clockwise 10 times
    print("Happy! Rotating clockwise 10 times...")
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    await motor.run_for_degrees(port.A, 3600, 360)  # 3600 degrees = 10 rotations
    
    await runloop.sleep_ms(1000)
    
    # Show sad face and rotate anticlockwise 10 times
    print("Sad! Rotating anticlockwise 10 times...")
    light_matrix.show_image(light_matrix.IMAGE_SAD)
    await motor.run_for_degrees(port.A, 3600, -360)  # Negative speed = anticlockwise
    
    await runloop.sleep_ms(1000)
    
    # Clear display
    light_matrix.clear()
    print("Program complete!")

# Always end SPIKE 3 programs with this line
runloop.run(main())
