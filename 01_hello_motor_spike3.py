"""
Lesson 1: Hello Motor! (SPIKE 3)
Learn: How to make a motor spin
Time: 5 minutes
Hardware: Connect a motor to port A
"""

import motor
import runloop
from hub import port

async def main():
    print("Motor starting...")
    
    # Run motor for 360 degrees (1 rotation) at 360 deg/sec
    await motor.run_for_degrees(port.A, 360, 360)
    
    print("Done! Try changing the numbers!")

# Always end SPIKE 3 programs with this line
runloop.run(main())
