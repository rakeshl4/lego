"""
Lesson 5: Robot Drivebase with Motor Pair (SPIKE 3)
Learn: Control two motors together as a drivebase
Time: 10 minutes
Hardware:
  - Motor on port A (left wheel)
  - Motor on port B (right wheel)
"""

import motor_pair
import runloop
from hub import port, light_matrix

async def main():
    # Pair the motors (left motor = A, right motor = B)
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
    
    print("Moving forward...")
    light_matrix.show_image(light_matrix.IMAGE_ARROW_N)
    # Move straight (steering=0) for 720 degrees at 360 deg/sec
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 720, 0, velocity=360)
    
    print("Turning right...")
    light_matrix.show_image(light_matrix.IMAGE_ARROW_E)
    # Turn right (steering=100) for 360 degrees
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, 100, velocity=360)
    
    print("Moving forward again...")
    light_matrix.show_image(light_matrix.IMAGE_ARROW_N)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 720, 0, velocity=360)
    
    print("Turning left...")
    light_matrix.show_image(light_matrix.IMAGE_ARROW_W)
    # Turn left (steering=-100) for 360 degrees
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, -100, velocity=360)
    
    print("Done!")
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    
    # Clean up
    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(2000)
    light_matrix.clear()

runloop.run(main())
