"""
🎯 CHALLENGE 6: Smart Distance Guard
Concept: Nested IF statements and logic
Difficulty: ⭐⭐⭐ Advanced
Hardware: Distance Sensor on port C, Motor on port A

CHALLENGE:
Create a smart guard that reacts based on distance AND color detection!
Logic:
- If distance > 200mm: Show happy, motor slow spin (200 speed)
- If distance 100-200mm: Show arrow, motor medium spin (400 speed)
- If distance < 100mm:
    * If too close (< 50mm): Show NO, stop motor, beep alarm!
    * Else: Show caution, motor fast spin (600 speed)

Place your hand at different distances and watch it react!
"""

import distance_sensor
import motor
import runloop
from hub import port, light_matrix, sound

async def main():
    print("🛡️ Smart Distance Guard Challenge Started!")
    print("Move your hand closer and farther from the sensor!")
    
    alarm_active = False
    
    # Run for 30 seconds
    for i in range(300):
        # Read distance in millimeters
        dist = distance_sensor.distance(port.C)
        
        # Check if distance is valid
        if dist == -1:
            # No object detected
            light_matrix.show_image(light_matrix.IMAGE_CONFUSED)
            motor.stop(port.A)
            
        elif dist > 200:
            # FAR AWAY - All clear!
            print(f"✅ Safe zone: {dist}mm")
            light_matrix.show_image(light_matrix.IMAGE_HAPPY)
            motor.run(port.A, 200)  # Slow patrol
            alarm_active = False
            
        elif dist >= 100:
            # MEDIUM DISTANCE - Alert mode
            print(f"⚠️ Alert zone: {dist}mm")
            light_matrix.show_image(light_matrix.IMAGE_ARROW_N)
            motor.run(port.A, 400)  # Medium speed
            alarm_active = False
            
        else:
            # CLOSE - Nested condition!
            if dist < 50:
                # VERY CLOSE - DANGER!
                print(f"🚨 DANGER! Too close: {dist}mm")
                light_matrix.show_image(light_matrix.IMAGE_NO)
                motor.stop(port.A)
                
                # Sound alarm only when entering danger zone
                if not alarm_active:
                    alarm_active = True
                    # Play warning beeps
                    for j in range(3):
                        sound.beep(1000, 100, 100)
                        await runloop.sleep_ms(150)
            else:
                # CLOSE but not too close - Caution!
                print(f"⚠️ Caution zone: {dist}mm")
                light_matrix.write("!")
                motor.run(port.A, 600)  # Fast spin as warning
                alarm_active = False
        
        await runloop.sleep_ms(100)
    
    # Stop motor and clear display
    motor.stop(port.A)
    light_matrix.clear()
    print("✅ Challenge Complete!")

runloop.run(main())
