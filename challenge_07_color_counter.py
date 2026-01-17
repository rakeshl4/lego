"""
🎯 CHALLENGE 7: Color Counter Game
Concept: Variables, counters, and state tracking
Difficulty: ⭐⭐ Intermediate
Hardware: Color Sensor on port A

CHALLENGE:
Create a color counting game!
- Count how many times each color (RED, BLUE, GREEN) is detected
- Display the count on the hub when that color is seen
- At the end, announce the winner (most detected color)

Try showing different colored LEGO bricks rapidly!
"""

import color_sensor
import color
import runloop
from hub import port, light_matrix, sound

async def main():
    print("🎮 Color Counter Game Started!")
    print("Show RED, BLUE, or GREEN bricks to the sensor!")
    
    # Initialize counters
    red_count = 0
    blue_count = 0
    green_count = 0
    
    last_color = None  # Track last seen color to avoid double counting
    
    # Game runs for 20 seconds
    for i in range(200):
        detected = color_sensor.color(port.A)
        
        # Only count if color changed (avoid counting same color multiple times)
        if detected != last_color:
            if detected == color.RED:
                red_count += 1
                print(f"🔴 RED! Count: {red_count}")
                light_matrix.write(str(red_count))
                sound.beep(400, 100, 100)
                
            elif detected == color.BLUE:
                blue_count += 1
                print(f"🔵 BLUE! Count: {blue_count}")
                light_matrix.write(str(blue_count))
                sound.beep(600, 100, 100)
                
            elif detected == color.GREEN:
                green_count += 1
                print(f"🟢 GREEN! Count: {green_count}")
                light_matrix.write(str(green_count))
                sound.beep(800, 100, 100)
            
            last_color = detected
        
        await runloop.sleep_ms(100)
    
    # Game over - announce results!
    print("\n📊 FINAL SCORES:")
    print(f"🔴 RED: {red_count}")
    print(f"🔵 BLUE: {blue_count}")
    print(f"🟢 GREEN: {green_count}")
    
    # Determine winner
    if red_count > blue_count and red_count > green_count:
        winner = "RED"
        winner_color = "🔴"
    elif blue_count > red_count and blue_count > green_count:
        winner = "BLUE"
        winner_color = "🔵"
    elif green_count > red_count and green_count > blue_count:
        winner = "GREEN"
        winner_color = "🟢"
    else:
        winner = "TIE"
        winner_color = "🤝"
    
    # Announce winner
    print(f"\n🏆 WINNER: {winner_color} {winner}!")
    
    if winner != "TIE":
        light_matrix.show_image(light_matrix.IMAGE_YES)
        # Victory fanfare
        for i in range(3):
            sound.beep(800 + i * 200, 200, 100)
            await runloop.sleep_ms(300)
    else:
        light_matrix.show_image(light_matrix.IMAGE_HEART)
        sound.beep(700, 400, 100)
    
    await runloop.sleep_ms(2000)
    light_matrix.clear()
    print("✅ Challenge Complete!")

runloop.run(main())
