"""
🎯 CHALLENGE 2: Countdown Timer
Concept: FOR loops and range()
Difficulty: ⭐ Beginner
Hardware: Just the hub!

CHALLENGE:
Create a countdown timer from 5 to 1, then show "GO!"
- Display each number on the light matrix
- Play a beep for each number
- After "GO!", show a happy face and celebrate!

BONUS: Try changing the countdown to start from 10!
"""

import runloop
from hub import light_matrix, sound

async def main():
    print("⏱️ Countdown Timer Challenge Started!")
    
    # Countdown from 5 to 1
    for number in range(5, 0, -1):  # Start at 5, stop before 0, go down by 1
        print(f"Counting: {number}")
        
        # Show the number on the display
        light_matrix.write(str(number))
        
        # Play a beep (frequency increases with each count)
        sound.beep(400 + number * 100, 200, 100)
        
        # Wait 1 second
        await runloop.sleep_ms(1000)
    
    # Blast off!
    print("🚀 GO!")
    await light_matrix.write("GO!")
    sound.beep(1000, 500, 100)  # Victory sound!
    await runloop.sleep_ms(1000)
    
    # Show celebration
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    
    # Play victory melody
    notes = [523, 587, 659, 784]  # C, D, E, G
    for note in notes:
        sound.beep(note, 200, 100)
        await runloop.sleep_ms(250)
    
    await runloop.sleep_ms(1000)
    light_matrix.clear()
    print("✅ Challenge Complete!")

runloop.run(main())
