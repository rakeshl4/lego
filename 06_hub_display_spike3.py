"""
Lesson 6: Hub Display Fun (SPIKE 3)
Learn: Show images and text on the hub's light matrix
Time: 5 minutes
Hardware: Just the hub!
"""

import runloop
from hub import light_matrix

async def main():
    # Show a happy face
    print("Showing happy face...")
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    await runloop.sleep_ms(2000)
    
    # Show a heart
    print("Showing heart...")
    light_matrix.show_image(light_matrix.IMAGE_HEART)
    await runloop.sleep_ms(2000)
    
    # Write text
    print("Writing message...")
    await light_matrix.write("Hello!")
    await runloop.sleep_ms(500)
    
    # Show multiple images in sequence
    images = [
        light_matrix.IMAGE_ARROW_N,
        light_matrix.IMAGE_ARROW_E,
        light_matrix.IMAGE_ARROW_S,
        light_matrix.IMAGE_ARROW_W
    ]
    
    print("Showing arrows...")
    for img in images:
        light_matrix.show_image(img)
        await runloop.sleep_ms(500)
    
    # Clear the display
    light_matrix.clear()
    print("Display cleared!")

runloop.run(main())
