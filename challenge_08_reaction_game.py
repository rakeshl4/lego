"""
🎯 CHALLENGE 8: Motion Reaction Game
Concept: Boolean flags and event detection
Difficulty: ⭐⭐ Intermediate
Hardware: Just the hub!

CHALLENGE:
Create a reaction game using the motion sensor!
- Wait for player to shake the hub
- When shaken, start a countdown from 3
- Player must flip hub upside-down before countdown ends
- If successful, celebrate! If not, show sad face

Test your reaction speed!
"""

import runloop
from hub import motion_sensor, light_matrix, sound

async def wait_for_shake():
    """Wait until hub is shaken"""
    print("🎮 Shake the hub to start!")
    light_matrix.write("?")
    
    while True:
        if motion_sensor.gesture() == motion_sensor.SHAKEN:
            print("✅ Shaken detected! Get ready...")
            sound.beep(600, 200, 100)
            return
        await runloop.sleep_ms(50)

async def countdown_challenge():
    """3 second countdown - player must flip hub upside-down!"""
    print("⏱️ Quick! Flip the hub upside-down!")
    
    # Countdown from 3 to 1
    for num in range(3, 0, -1):
        light_matrix.write(str(num))
        sound.beep(500 + num * 100, 200, 100)
        print(f"Countdown: {num}")
        
        # Check each 0.1 second if hub is upside-down
        for i in range(10):
            if motion_sensor.up_face() == motion_sensor.FRONT:
                # Success! Front (display) facing down means upside-down!
                return True
            await runloop.sleep_ms(100)
    
    return False  # Time ran out

async def main():
    print("🎯 Motion Reaction Game Started!")
    
    games_won = 0
    games_played = 0
    
    # Play 3 rounds
    for round_num in range(1, 4):
        print(f"\n--- ROUND {round_num}/3 ---")
        light_matrix.write(str(round_num))
        await runloop.sleep_ms(1000)
        
        # Wait for shake to start
        await wait_for_shake()
        await runloop.sleep_ms(500)
        
        # Run countdown challenge
        success = await countdown_challenge()
        games_played += 1
        
        if success:
            # Player won this round!
            print("🎉 SUCCESS! You flipped it in time!")
            games_won += 1
            light_matrix.show_image(light_matrix.IMAGE_YES)
            # Victory sound
            for i in range(3):
                sound.beep(800 + i * 200, 150, 100)
                await runloop.sleep_ms(200)
        else:
            # Player failed this round
            print("😢 Too slow! Better luck next round.")
            light_matrix.show_image(light_matrix.IMAGE_NO)
            sound.beep(300, 400, 100)
        
        await runloop.sleep_ms(2000)
    
    # Final results
    print(f"\n📊 FINAL SCORE: {games_won}/{games_played}")
    
    if games_won == 3:
        print("🏆 PERFECT! You won all rounds!")
        light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    elif games_won >= 2:
        print("🎉 Great job! You won most rounds!")
        light_matrix.show_image(light_matrix.IMAGE_YES)
    else:
        print("💪 Keep practicing!")
        light_matrix.show_image(light_matrix.IMAGE_HEART)
    
    await runloop.sleep_ms(3000)
    light_matrix.clear()
    print("✅ Challenge Complete!")

runloop.run(main())
