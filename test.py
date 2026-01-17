import force_sensor
import motor
import color
from hub import port, light
import time
import runloop
 
async def show_color():
    print('showing green')
    await light.color(light.POWER, color.GREEN)
    print('pausing . . . ')
    await runloop.sleep_ms(1000)
    print('showing red')
    await light.color(light.POWER, color.RED)
 
async def main():
    while True:
        force = force_sensor.force(port.B)
        if force > 80:
            await show_color()
        else:
            light.color(light.POWER, color.WHITE)
 
runloop.run(main())