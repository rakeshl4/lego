"""
🎯 CHALLENGE 9: Smart Button Math Game
Concept: Math operations and input handling
Difficulty: ⭐⭐⭐ Advanced
Hardware: Just the hub (uses buttons)

CHALLENGE:
Create a math quiz game using the hub buttons!
- Hub shows a random number (0-9)
- Left button = EVEN, Right button = ODD
- Player must press correct button within 3 seconds
- Score points for correct answers!

Play 5 rounds and try to get a perfect score!
"""

import runloop
from hub import button, light_matrix, sound
import random

async def ask_question(number):
    """Ask if number is even or odd. Returns True if answered correctly."""
    print(f"\n❓ Is {number} EVEN or ODD?")
    print("   LEFT = EVEN | RIGHT = ODD")
    
    # Show the number
    light_matrix.write(str(number))
    sound.beep(600, 100, 100)
    
    # Check if number is actually even
    is_even = (number % 2 == 0)
    
    # Wait for answer (3 seconds max)
    for i in range(30):  # 30 x 100ms = 3 seconds
        if button.pressed(button.LEFT) > 0:
            # Player answered EVEN
            if is_even:
                return True  # Correct!
            else:
                return False  # Wrong!
                
        elif button.pressed(button.RIGHT) > 0:
            # Player answered ODD
            if not is_even:
                return True  # Correct!
            else:
                return False  # Wrong!
        
        await runloop.sleep_ms(100)
    
    # Time ran out
    return False

async def main():
    print("🎮 Smart Button Math Game Started!")
    print("Is the number EVEN or ODD?")
    print("LEFT button = EVEN | RIGHT button = ODD")
    
    # Show instructions
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    await runloop.sleep_ms(2000)
    
    score = 0
    total_questions = 5
    
    # Play 5 rounds
    for round_num in range(1, total_questions + 1):
        print(f"\n--- ROUND {round_num}/{total_questions} ---")
        light_matrix.write(str(round_num))
        await runloop.sleep_ms(1000)
        
        # Generate random number (0-9)
        number = random.randint(0, 9)
        
        # Ask question and get result
        correct = await ask_question(number)
        
        # Show result
        if correct:
            print(f"✅ CORRECT! {number} is {'EVEN' if number % 2 == 0 else 'ODD'}")
            score += 1
            light_matrix.show_image(light_matrix.IMAGE_YES)
            sound.beep(800, 200, 100)
            sound.beep(1000, 200, 100)
        else:
            print(f"❌ WRONG! {number} is {'EVEN' if number % 2 == 0 else 'ODD'}")
            light_matrix.show_image(light_matrix.IMAGE_NO)
            sound.beep(300, 400, 100)
        
        await runloop.sleep_ms(1500)
    
    # Final score
    print(f"\n📊 FINAL SCORE: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    
    # Show score on display
    light_matrix.write(str(score))
    await runloop.sleep_ms(1000)
    
    # Give feedback based on score
    if score == total_questions:
        print("🏆 PERFECT SCORE! You're a math genius!")
        light_matrix.show_image(light_matrix.IMAGE_HAPPY)
        # Perfect score melody
        melody = [523, 659, 784, 1047]
        for note in melody:
            sound.beep(note, 200, 100)
            await runloop.sleep_ms(250)
    elif score >= 3:
        print("🎉 Great job! You got most correct!")
        light_matrix.show_image(light_matrix.IMAGE_YES)
        sound.beep(700, 400, 100)
    else:
        print("💪 Keep practicing! You'll improve!")
        light_matrix.show_image(light_matrix.IMAGE_HEART)
        sound.beep(500, 300, 100)
    
    await runloop.sleep_ms(3000)
    light_matrix.clear()
    print("✅ Challenge Complete!")

runloop.run(main())
