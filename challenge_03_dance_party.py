"""
🎯 CHALLENGE 3: Dance Party Function
Concept: Functions (def) and code organization
Difficulty: ⭐⭐ Intermediate
Hardware: Motor on port A, hub buttons

CHALLENGE:
Create dance move functions that combine motor spins and display images!
- Left button triggers "Spin Dance"
- Right button triggers "Wave Dance"
- Each dance should be its own function

BONUS: Create your own third dance move!
"""

import motor
import runloop
from hub import port, button, light_matrix, sound

# Define dance move functions
async def spin_dance():
    """Spin dance: fast rotation with happy face"""
    print("💃 Performing Spin Dance!")
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    await motor.run_for_degrees(port.A, 720, 800)  # 2 fast spins
    sound.beep(800, 200, 100)

async def wave_dance():
    """Wave dance: back and forth motion with arrows"""
    print("🕺 Performing Wave Dance!")
    for i in range(3):
        light_matrix.show_image(light_matrix.IMAGE_ARROW_E)
        await motor.run_for_degrees(port.A, 180, 400)
        
        light_matrix.show_image(light_matrix.IMAGE_ARROW_W)
        await motor.run_for_degrees(port.A, 180, -400)
    sound.beep(600, 300, 100)

async def surprise_dance():
    """BONUS: Your custom dance move!"""
    print("😲 Performing Surprise Dance!")
    light_matrix.show_image(light_matrix.IMAGE_SURPRISED)
    
    # Quick back-and-forth with beeps
    for i in range(5):
        await motor.run_for_degrees(port.A, 90, 1000)
        sound.beep(1000 + i * 100, 50, 100)
        await motor.run_for_degrees(port.A, 90, -1000)
        sound.beep(1000 - i * 100, 50, 100)

async def main():
    print("🎉 Dance Party Challenge Started!")
    print("Press LEFT for Spin Dance, RIGHT for Wave Dance")
    light_matrix.show_image(light_matrix.IMAGE_HEART)
    
    # Run for 30 seconds
    for i in range(300):
        if button.pressed(button.LEFT) > 0:
            await spin_dance()
            light_matrix.show_image(light_matrix.IMAGE_HEART)
            # Wait for button release
            while button.pressed(button.LEFT) > 0:
                await runloop.sleep_ms(10)
                
        elif button.pressed(button.RIGHT) > 0:
            await wave_dance()
            light_matrix.show_image(light_matrix.IMAGE_HEART)
            # Wait for button release
            while button.pressed(button.RIGHT) > 0:
                await runloop.sleep_ms(10)
        
        await runloop.sleep_ms(100)
    
    light_matrix.clear()
    print("✅ Challenge Complete!")

runloop.run(main())
