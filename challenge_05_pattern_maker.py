"""
🎯 CHALLENGE 5: Pattern Maker
Concept: Lists and iteration
Difficulty: ⭐⭐ Intermediate
Hardware: Motor on port A

CHALLENGE:
Create a motor that follows different rotation patterns!
- Define patterns as lists of degrees
- Motor executes each pattern in sequence
- Display shows pattern number

Try creating your own custom patterns!
"""

import motor
import runloop
from hub import port, light_matrix, sound

async def execute_pattern(pattern_list, pattern_name):
    """Function to execute a rotation pattern"""
    print(f"🎨 Executing: {pattern_name}")
    
    step = 1
    for degrees in pattern_list:
        print(f"  Step {step}: {degrees}°")
        light_matrix.write(str(step))
        
        # Positive = clockwise, negative = anticlockwise
        speed = 500 if degrees > 0 else -500
        await motor.run_for_degrees(port.A, abs(degrees), speed)
        
        sound.beep(400 + step * 100, 100, 100)
        await runloop.sleep_ms(300)
        step += 1

async def main():
    print("🎨 Pattern Maker Challenge Started!")
    
    # Define different rotation patterns (in degrees)
    pattern_zigzag = [90, -90, 90, -90, 90]
    pattern_crescendo = [45, 90, 180, 360, 720]
    pattern_spiral = [360, 360, -360, -360, 180]
    pattern_custom = [180, -90, 270, -180, 360]  # Create your own!
    
    # List of all patterns
    all_patterns = [
        (pattern_zigzag, "Zigzag"),
        (pattern_crescendo, "Crescendo"),
        (pattern_spiral, "Spiral"),
        (pattern_custom, "Custom")
    ]
    
    # Execute each pattern
    for pattern, name in all_patterns:
        light_matrix.show_image(light_matrix.IMAGE_ARROW_N)
        await runloop.sleep_ms(500)
        
        await execute_pattern(pattern, name)
        
        light_matrix.show_image(light_matrix.IMAGE_YES)
        await runloop.sleep_ms(1000)
    
    # Celebration!
    print("🎉 All patterns complete!")
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    
    # Victory melody
    melody = [523, 587, 659, 784, 880]
    for note in melody:
        sound.beep(note, 200, 100)
        await runloop.sleep_ms(250)
    
    light_matrix.clear()
    print("✅ Challenge Complete!")

runloop.run(main())
