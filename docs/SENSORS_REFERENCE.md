# 🔍 Sensors Reference Guide

Learn how to use sensors on your Spike robot!

---

## 📚 Import the Library

```python
import runloop
from hub import port, motion_sensor
import color_sensor
import distance_sensor
import force_sensor
```

---

## 🎨 Color Sensor

Detects colors and light!

### Connect to Sensor

```python
# Color sensor in port C (use port.A, port.B, port.C, etc.)
```

### Read Color

```python
# Get the color value
detected = color_sensor.color(port.C)
print(detected)  # Prints color code

# Check for specific color
if color_sensor.color(port.C) == color_sensor.RED:
    print("I see red!")

# Color constants: RED, GREEN, BLUE, YELLOW, WHITE, BLACK
```

### Read Light Intensity

```python
# Get reflected light (0-100)
reflection = color_sensor.reflection(port.C)
print(reflection)

# Get RGB values
red, green, blue = color_sensor.rgbi(port.C)[:3]
print(f"R:{red} G:{green} B:{blue}")
```

### Wait for Color

```python
# Wait until you see red (use async)
async def main():
    while color_sensor.color(port.C) != color_sensor.RED:
        await runloop.sleep_ms(10)
    print("Found red!")

runloop.run(main())
```

---

## 📏 Distance Sensor

Measures how far away things are!

### Connect to Sensor

```python
# Distance sensor in port D (use port.A, port.B, port.C, etc.)
```

### Read Distance

```python
# Get distance in millimeters
mm = distance_sensor.distance(port.D)
print(f"Distance: {mm} mm")

# Convert to centimeters
cm = mm / 10
print(f"Distance: {cm} cm")

# Check if something is close
if distance_sensor.distance(port.D) < 100:  # Less than 10 cm
    print("Too close!")
```

### Wait for Object

```python
# Wait until something gets close (use async)
async def main():
    while distance_sensor.distance(port.D) > 200:  # More than 20 cm
        await runloop.sleep_ms(10)
    print("Something nearby!")

runloop.run(main())
```

---

## 💪 Force Sensor

Detects pushing and pressing!

### Connect to Sensor

```python
# Force sensor in port E (use port.A, port.B, port.C, etc.)
```

### Check if Pressed

```python
# Is button pressed?
if force_sensor.pressed(port.E):
    print("Button is pressed!")
```

### Read Force Amount

```python
# Get force value (0-10)
strength = force_sensor.force(port.E)
print(f"Force: {strength}")

# Convert to approximate newtons (multiply by 0.1)
newtons = strength * 0.1
print(f"Force: {newtons} N")
```

### Wait for Press

```python
# Wait until button is pressed (use async)
async def main():
    while not force_sensor.pressed(port.E):
        await runloop.sleep_ms(10)
    print("Button pressed!")

runloop.run(main())
```

---

## 🎯 Motion Sensor (Hub Sensor)

Detects tilting and shaking!

### Connect to Sensor

```python
# Built into the hub! Use motion_sensor module
```

### Check Orientation

```python
# Which way is the hub facing?
direction = motion_sensor.tilt_angles()[0]  # Yaw angle
print(direction)

# Get pitch and roll
pitch, roll, yaw = motion_sensor.tilt_angles()
print(f"Pitch: {pitch}, Roll: {roll}, Yaw: {yaw}")
```

### Detect Shaking

```python
# Get gesture (returns gesture code)
gesture = motion_sensor.gesture()

# Gesture constants:
# TAPPED, DOUBLE_TAPPED, SHAKEN, FALLING, UNKNOWN
if gesture == motion_sensor.SHAKEN:
    print("Hub was shaken!")
```

### Reset Position

```python
# Reset the yaw angle to 0
motion_sensor.reset_yaw(0)
```

---

## 🎯 Quick Examples

### Example 1: Color Reaction

```python
import runloop
from hub import port
import color_sensor

async def main():
    while True:
        color = color_sensor.color(port.C)
        if color == color_sensor.RED:
            print("STOP!")
        elif color == color_sensor.GREEN:
            print("GO!")
        await runloop.sleep_ms(100)

runloop.run(main())
```

### Example 2: Distance Alert

```python
import runloop
from hub import port
import distance_sensor

async def main():
    dist = distance_sensor.distance(port.D)  # in mm
    
    if dist < 100:  # Less than 10 cm
        print("DANGER! Too close!")
    elif dist < 200:  # Less than 20 cm
        print("Warning: Getting close")
    else:
        print("All clear")

runloop.run(main())
```

### Example 3: Force Counter

```python
import runloop
from hub import port
import force_sensor

count = 0

async def main():
    global count
    for i in range(5):
        # Wait for press
        while not force_sensor.pressed(port.E):
            await runloop.sleep_ms(10)
        
        count = count + 1
        print(f"Press count: {count}")
        
        # Wait for release
        while force_sensor.pressed(port.E):
            await runloop.sleep_ms(10)
    
    print(f"Total presses: {count}")

runloop.run(main())
```

### Example 4: Motion Control

```python
import runloop
from hub import motion_sensor

async def main():
    for i in range(10):
        if motion_sensor.gesture() == motion_sensor.SHAKEN:
            print("🎉 Hub shaken!")
        await runloop.sleep_ms(500)

runloop.run(main())
```

---

**Happy Sensing! 🎉**
