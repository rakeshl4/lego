"""
Lesson 9: Motion Sensor Fun (SPIKE 3)
Learn: Detect tilt, shake, and orientation of the hub
Time: 5 minutes
Hardware: Just the hub!
"""

import runloop
from hub import motion_sensor, light_matrix, sound

async def main():
    print("Tilt and shake the hub!")
    
    for i in range(100):  # Run for 10 seconds
        # Check which face is up
        face = motion_sensor.up_face()
        
        if face == motion_sensor.FRONT:
            # Front face (with light matrix) is up
            light_matrix.show_image(light_matrix.IMAGE_HAPPY)
        elif face == motion_sensor.BACK:
            # Back face is up
            light_matrix.show_image(light_matrix.IMAGE_SAD)
        elif face == motion_sensor.TOP:
            # Top face (USB port) is up
            light_matrix.show_image(light_matrix.IMAGE_ARROW_N)
        elif face == motion_sensor.BOTTOM:
            # Bottom face is up
            light_matrix.show_image(light_matrix.IMAGE_ARROW_S)
        else:
            # Side faces
            light_matrix.show_image(light_matrix.IMAGE_CONFUSED)
        
        # Check for gestures
        gesture = motion_sensor.gesture()
        
        if gesture == motion_sensor.SHAKEN:
            print("Hub was shaken!")
            sound.beep(1000, 100, 100)
            light_matrix.show_image(light_matrix.IMAGE_SURPRISED)
            await runloop.sleep_ms(500)
        elif gesture == motion_sensor.TAPPED:
            print("Hub was tapped!")
            sound.beep(500, 100, 100)
        
        await runloop.sleep_ms(100)
    
    light_matrix.clear()
    print("Done!")

runloop.run(main())
