"""
Lesson 2: Color Detective (SPIKE 3)
Learn: Read colors with the color sensor
Time: 5 minutes
Hardware: Connect a Color Sensor to port A
"""

import color_sensor
import color
import runloop
from hub import port, light_matrix

async def main():
    print("Place colored objects under the sensor!")
    
    for i in range(5):
        # Get the detected color
        detected = color_sensor.color(port.A)
        
        # Show feedback on hub
        if detected == color.RED:
            print("I see RED!")
            light_matrix.show_image(light_matrix.IMAGE_HEART)
        elif detected == color.BLUE:
            print("I see BLUE!")
            light_matrix.show_image(light_matrix.IMAGE_HAPPY)
        elif detected == color.GREEN:
            print("I see GREEN!")
            light_matrix.show_image(light_matrix.IMAGE_YES)
        else:
            print(f"I see color code: {detected}")
            light_matrix.write(str(detected))
        
        # Wait 2 seconds before next reading
        await runloop.sleep_ms(2000)
    
    light_matrix.clear()
    print("Color detection complete!")

runloop.run(main())
