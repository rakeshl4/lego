"""
Lesson 10: Advanced - Multiple Tasks at Once (SPIKE 3)
Learn: Run multiple things simultaneously with async
Time: 10 minutes
Hardware:
  - Motor on port A
  - Color Sensor on port B
"""

import motor
import color_sensor
import color
import runloop
from hub import port, light_matrix, sound

# Task 1: Blink the display
async def blink_display():
    print("Display blink task started")
    for i in range(20):
        light_matrix.show_image(light_matrix.IMAGE_HEART)
        await runloop.sleep_ms(500)
        light_matrix.clear()
        await runloop.sleep_ms(500)

# Task 2: Spin motor back and forth
async def spin_motor():
    print("Motor spin task started")
    for i in range(4):
        print("Motor forward...")
        await motor.run_for_degrees(port.A, 360, 500)
        print("Motor backward...")
        await motor.run_for_degrees(port.A, -360, 500)

# Task 3: Monitor color sensor
async def monitor_color():
    print("Color monitor task started")
    while True:
        detected = color_sensor.color(port.B)
        
        if detected == color.RED:
            print("RED detected - BEEP!")
            sound.beep(880, 100, 100)
        elif detected == color.BLUE:
            print("BLUE detected - boop!")
            sound.beep(440, 100, 100)
        
        await runloop.sleep_ms(200)

async def main():
    print("Starting multiple tasks simultaneously!")
    # Run for 10 seconds
    await runloop.sleep_ms(10000)
    print("Main task complete!")

# Run ALL tasks at the same time!
runloop.run(blink_display(), spin_motor(), monitor_color(), main())
