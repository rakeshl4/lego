"""
🎯 CHALLENGE 10: Multi-Sensor Orchestra
Concept: Multiple conditions, async programming, complex logic
Difficulty: ⭐⭐⭐⭐ Expert
Hardware: Force Sensor on port B, Distance Sensor on port C, Motor on port A

CHALLENGE:
Create a musical instrument using multiple sensors at once!
- Force Sensor: Controls note pitch (harder press = higher note)
- Distance Sensor: Controls motor speed (closer = faster)
- Display shows visual feedback based on force level
- Combine both sensors to create music!

This is the ultimate challenge - combine everything you've learned!
"""

import force_sensor
import distance_sensor
import motor
import runloop
from hub import port, light_matrix, sound

def calculate_note(force_value):
    """Calculate musical note frequency based on force"""
    # Map force (0-100) to musical notes
    if force_value < 10:
        return 0  # No sound
    elif force_value < 20:
        return 262  # C
    elif force_value < 30:
        return 294  # D
    elif force_value < 40:
        return 330  # E
    elif force_value < 50:
        return 349  # F
    elif force_value < 60:
        return 392  # G
    elif force_value < 70:
        return 440  # A
    elif force_value < 80:
        return 494  # B
    else:
        return 523  # High C

def get_display_for_force(force_value):
    """Get display image based on force level"""
    if force_value < 10:
        return light_matrix.IMAGE_ASLEEP
    elif force_value < 30:
        return light_matrix.IMAGE_SAD
    elif force_value < 50:
        return None  # Will show number
    elif force_value < 70:
        return light_matrix.IMAGE_HAPPY
    else:
        return light_matrix.IMAGE_SURPRISED

def calculate_motor_speed(distance_mm):
    """Calculate motor speed based on distance"""
    if distance_mm == -1 or distance_mm > 300:
        return 0  # No object or too far
    elif distance_mm > 200:
        return 200  # Slow
    elif distance_mm > 100:
        return 400  # Medium
    else:
        return 800  # Fast!

async def main():
    print("🎵 Multi-Sensor Orchestra Challenge Started!")
    print("🎹 Force Sensor = Note Pitch")
    print("📏 Distance Sensor = Motor Speed")
    print("\nPress force sensor and move hand near distance sensor!")
    
    light_matrix.show_image(light_matrix.IMAGE_MUSIC_QUAVER)
    await runloop.sleep_ms(2000)
    
    last_note = 0
    note_playing = False
    
    # Orchestra runs for 30 seconds
    for i in range(300):
        # Read both sensors
        force = force_sensor.force(port.B)
        dist = distance_sensor.distance(port.C)
        
        # Calculate note from force
        note_freq = calculate_note(force)
        
        # Update display based on force
        display_img = get_display_for_force(force)
        if display_img is not None:
            light_matrix.show_image(display_img)
        else:
            # Show force value for medium force
            light_matrix.write(str(force // 10))
        
        # Play note if force applied and note changed
        if note_freq > 0:
            if note_freq != last_note or not note_playing:
                sound.beep(note_freq, 200, 100)
                note_playing = True
                last_note = note_freq
                
                # Print what's playing
                notes = {262: 'C', 294: 'D', 330: 'E', 349: 'F', 
                        392: 'G', 440: 'A', 494: 'B', 523: 'C+'}
                note_name = notes.get(note_freq, '?')
                print(f"🎵 Playing: {note_name} (Force: {force} dN)")
        else:
            note_playing = False
            last_note = 0
        
        # Control motor based on distance
        motor_speed = calculate_motor_speed(dist)
        if motor_speed > 0:
            motor.run(port.A, motor_speed)
            if i % 10 == 0:  # Print occasionally to avoid spam
                print(f"🎡 Motor: {motor_speed} deg/s (Distance: {dist}mm)")
        else:
            motor.stop(port.A)
        
        await runloop.sleep_ms(100)
    
    # Stop everything
    motor.stop(port.A)
    
    # Grand finale!
    print("\n🎉 Orchestra Performance Complete!")
    print("Finale!")
    
    # Play victory melody
    finale_notes = [523, 587, 659, 784, 880, 784, 659, 587, 523]
    for note in finale_notes:
        light_matrix.show_image(light_matrix.IMAGE_MUSIC_QUAVER)
        sound.beep(note, 200, 100)
        await runloop.sleep_ms(250)
    
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    await runloop.sleep_ms(2000)
    light_matrix.clear()
    print("✅ Challenge Complete! You're a programming master! 🏆")

runloop.run(main())
