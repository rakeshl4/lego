"""
Lesson 7: Button Control (SPIKE 3)
Learn: React to button presses on the hub
Time: 5 minutes
Hardware: Just the hub!
"""

import runloop
from hub import button, light_matrix, sound

# Track which button was pressed
async def check_buttons():
    while True:
        # Check left button
        if button.pressed(button.LEFT) > 0:
            print("Left button pressed!")
            light_matrix.show_image(light_matrix.IMAGE_ARROW_W)
            sound.beep(440, 200, 100)  # Play beep at 440 Hz
            
            # Wait until button is released
            while button.pressed(button.LEFT) > 0:
                await runloop.sleep_ms(10)
        
        # Check right button
        elif button.pressed(button.RIGHT) > 0:
            print("Right button pressed!")
            light_matrix.show_image(light_matrix.IMAGE_ARROW_E)
            sound.beep(880, 200, 100)  # Play higher beep
            
            # Wait until button is released
            while button.pressed(button.RIGHT) > 0:
                await runloop.sleep_ms(10)
        
        else:
            # No button pressed - show neutral image
            light_matrix.show_image(light_matrix.IMAGE_HAPPY)
        
        await runloop.sleep_ms(10)

async def main():
    print("Press left or right buttons!")
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    
    # Run for 30 seconds
    await runloop.sleep_ms(30000)
    
    light_matrix.clear()
    print("Time's up!")

# Run both functions at the same time
runloop.run(check_buttons(), main())
