"""
🎯 CHALLENGE 1: Traffic Light System
Concept: IF-ELIF-ELSE statements
Difficulty: ⭐ Beginner
Hardware: Color Sensor on port A, Motor on port B

CHALLENGE:
Create a traffic light system! When the color sensor sees:
- RED: Motor stops, show sad face
- YELLOW: Motor runs slowly (speed 200), show caution
- GREEN: Motor runs fast (speed 600), show happy face
- Other colors: Motor stops, show confused face

Try placing red, yellow, and green LEGO bricks under the sensor!
"""

import color_sensor
import color
import motor
import runloop
from hub import port, light_matrix

async def main():
    print("🚦 Traffic Light Challenge Started!")
    print("Place RED, YELLOW, or GREEN under the sensor")
    
    # Run for 20 seconds
    for i in range(200):
        # Read the color from sensor
        detected_color = color_sensor.color(port.A)
        
        # Traffic light logic
        if detected_color == color.RED:
            # RED = STOP
            motor.stop(port.B)
            light_matrix.show_image(light_matrix.IMAGE_SAD)
            print("🔴 RED - STOP!")
            
        elif detected_color == color.YELLOW:
            # YELLOW = SLOW DOWN
            motor.run(port.B, 200)
            light_matrix.write("?")
            print("🟡 YELLOW - Slow down!")
            
        elif detected_color == color.GREEN:
            # GREEN = GO!
            motor.run(port.B, 600)
            light_matrix.show_image(light_matrix.IMAGE_HAPPY)
            print("🟢 GREEN - GO!")
            
        else:
            # Unknown color - stop for safety
            motor.stop(port.B)
            light_matrix.show_image(light_matrix.IMAGE_CONFUSED)
        
        await runloop.sleep_ms(100)
    
    # Stop motor and clear display
    motor.stop(port.B)
    light_matrix.clear()
    print("✅ Challenge Complete!")

runloop.run(main())
