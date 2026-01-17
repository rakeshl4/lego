# 🔍 Sensors Reference Guide

Learn how to use sensors on your Spike robot!

---

## 📚 Import the Library

```python
from spike import ColorSensor, DistanceSensor, ForceSensor, MotionSensor
```

---

## 🎨 Color Sensor

Detects colors and light!

### Connect to Sensor

```python
color = ColorSensor('C')  # Color sensor in port C
```

### Read Color

```python
# Get the color name
detected = color.get_color()
print(detected)  # Prints: "red", "blue", "green", etc.

# Check for specific color
if color.get_color() == "red":
    print("I see red!")
```

### Read Light Intensity

```python
# Get brightness (0-100)
brightness = color.get_ambient_light()
print(brightness)
```

### Wait for Color

```python
# Wait until you see red
color.wait_until_color("red")
print("Found red!")
```

---

## 📏 Distance Sensor

Measures how far away things are!

### Connect to Sensor

```python
distance = DistanceSensor('D')  # Distance sensor in port D
```

### Read Distance

```python
# Get distance in centimeters
cm = distance.get_distance_cm()
print(f"Distance: {cm} cm")

# Check if something is close
if distance.get_distance_cm() < 10:
    print("Too close!")
```

### Wait for Object

```python
# Wait until something gets close
distance.wait_for_distance_closer_than(20, 'cm')
print("Something nearby!")
```

---

## 💪 Force Sensor

Detects pushing and pressing!

### Connect to Sensor

```python
force = ForceSensor('E')  # Force sensor in port E
```

### Check if Pressed

```python
# Is button pressed?
if force.is_pressed():
    print("Button is pressed!")
```

### Read Force Amount

```python
# Get force in newtons
strength = force.get_force_newton()
print(f"Force: {strength} N")

# Get force as percentage
percent = force.get_force_percentage()
print(f"Force: {percent}%")
```

### Wait for Press

```python
# Wait until button is pressed
force.wait_until_pressed()
print("Button pressed!")
```

---

## 🎯 Motion Sensor (Hub Sensor)

Detects tilting and shaking!

### Connect to Sensor

```python
motion = MotionSensor()  # Built into the hub!
```

### Check Orientation

```python
# Which way is the hub facing?
direction = motion.get_yaw_angle()
print(direction)

# Is hub tilted?
tilt = motion.get_pitch_angle()
print(tilt)
```

### Detect Shaking

```python
# Check if shaking
if motion.was_gesture('shaken'):
    print("Hub was shaken!")
```

### Reset Position

```python
# Reset the motion sensor
motion.reset_yaw_angle()
```

---

## 🎯 Quick Examples

### Example 1: Color Reaction

```python
from spike import ColorSensor

color = ColorSensor('C')

while True:
    if color.get_color() == "red":
        print("STOP!")
    elif color.get_color() == "green":
        print("GO!")
```

### Example 2: Distance Alert

```python
from spike import DistanceSensor

distance = DistanceSensor('D')

dist = distance.get_distance_cm()

if dist < 10:
    print("DANGER! Too close!")
elif dist < 20:
    print("Warning: Getting close")
else:
    print("All clear")
```

### Example 3: Force Counter

```python
from spike import ForceSensor

force = ForceSensor('E')
count = 0

for i in range(5):
    force.wait_until_pressed()
    count = count + 1
    print(f"Press count: {count}")
    force.wait_until_released()

print(f"Total presses: {count}")
```

### Example 4: Motion Control

```python
from spike import MotionSensor
import time

motion = MotionSensor()

for i in range(10):
    if motion.was_gesture('shaken'):
        print("🎉 Hub shaken!")
    time.sleep(0.5)
```

---

**Happy Sensing! 🎉**
