"""
🎯 CHALLENGE 4: Force Strength Meter
Concept: WHILE loops and conditions
Difficulty: ⭐⭐ Intermediate
Hardware: Force Sensor on port B

CHALLENGE:
Create a strength meter game!
- Press the force sensor as hard as you can
- Display shows strength level:
  * 0-20: "Weak" (sad face)
  * 21-50: "Good" (neutral)
  * 51-80: "Strong!" (happy face)
  * 81+: "SUPER!" (yes/check mark)
- Game runs until you achieve "SUPER!" strength 3 times

Keep pressing to reach SUPER strength!
"""

import force_sensor
import runloop
from hub import port, light_matrix, sound

async def main():
    print("💪 Force Strength Meter Challenge Started!")
    print("Press the force sensor hard to reach SUPER strength!")
    
    super_count = 0  # Count how many times we reached SUPER
    
    # Loop until we get 3 SUPER presses
    while super_count < 3:
        # Read force value (0-100 decinewtons)
        force = force_sensor.force(port.B)
        
        # Classify strength level
        if force == 0:
            # No press
            light_matrix.write("?")
            
        elif force <= 20:
            # Weak press
            print(f"Weak: {force} dN")
            light_matrix.show_image(light_matrix.IMAGE_SAD)
            
        elif force <= 50:
            # Good press
            print(f"Good: {force} dN")
            light_matrix.write("!")
            sound.beep(500, 100, 100)
            
        elif force <= 80:
            # Strong press
            print(f"Strong: {force} dN!")
            light_matrix.show_image(light_matrix.IMAGE_HAPPY)
            sound.beep(700, 150, 100)
            
        else:
            # SUPER press!
            print(f"⚡ SUPER: {force} dN! ({super_count + 1}/3)")
            light_matrix.show_image(light_matrix.IMAGE_YES)
            sound.beep(1000, 300, 100)
            
            # Increment counter
            super_count += 1
            
            # Wait for release before counting next one
            while force_sensor.force(port.B) > 80:
                await runloop.sleep_ms(50)
            
            await runloop.sleep_ms(500)  # Pause between counts
        
        await runloop.sleep_ms(100)
    
    # Victory celebration!
    print("🎉 You reached SUPER strength 3 times!")
    for i in range(3):
        light_matrix.show_image(light_matrix.IMAGE_YES)
        sound.beep(800 + i * 200, 200, 100)
        await runloop.sleep_ms(300)
    
    light_matrix.clear()
    print("✅ Challenge Complete!")

runloop.run(main())
