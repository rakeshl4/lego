# 🎮 Hub Reference Guide

Learn how to use the Spike Hub display and buttons!

---

## 📚 Import the Library

```python
from spike import PrimeHub
```

---

## 🖥️ Hub Display Basics

### Connect to Hub

```python
hub = PrimeHub()
```

### Show Images

```python
# Show a built-in image
hub.light_matrix.show_image('HAPPY')

# Other images you can use:
# 'HAPPY', 'SAD', 'ANGRY', 'SMILE', 'HEART'
# 'YES', 'NO', 'ARROW_N', 'ARROW_E', 'ARROW_S', 'ARROW_W'
```

### Show Text

```python
# Show a single character
hub.light_matrix.write('A')

# Scroll text across the display
hub.light_matrix.write('HELLO')
```

### Custom Patterns

```python
# Create your own 5x5 pattern (0=off, 9=brightest)
pattern = [
    [0, 0, 9, 0, 0],
    [0, 9, 0, 9, 0],
    [9, 0, 0, 0, 9],
    [0, 9, 0, 9, 0],
    [0, 0, 9, 0, 0]
]
hub.light_matrix.show(pattern)
```

### Turn Off Display

```python
hub.light_matrix.off()
```

---

## 🔘 Hub Buttons

### Check Left Button

```python
# Is left button pressed?
if hub.left_button.is_pressed():
    print("Left button pressed!")

# Wait for left button
hub.left_button.wait_until_pressed()
print("Left button was pressed!")
```

### Check Right Button

```python
# Is right button pressed?
if hub.right_button.is_pressed():
    print("Right button pressed!")

# Wait for right button
hub.right_button.wait_until_pressed()
print("Right button was pressed!")
```

### Button Release

```python
# Wait until button is released
hub.left_button.wait_until_released()
print("Button released!")
```

---

## 🔊 Hub Speaker

### Play Beep

```python
# Simple beep
hub.speaker.beep(60, 0.5)  # Note 60, for 0.5 seconds

# Higher pitch
hub.speaker.beep(72, 0.5)
```

### Change Volume

```python
# Set volume (0-100)
hub.speaker.set_volume(80)
```

---

## 💡 Status Light

The light around the center button!

### Change Color

```python
# Turn on status light
hub.status_light.on('green')

# Other colors: 'red', 'blue', 'yellow', 'cyan', 'magenta', 'white'
```

### Turn Off

```python
hub.status_light.off()
```

---

## 🎯 Quick Examples

### Example 1: Button Counter

```python
from spike import PrimeHub

hub = PrimeHub()
count = 0

while count < 5:
    hub.left_button.wait_until_pressed()
    count = count + 1
    hub.light_matrix.write(str(count))
    hub.left_button.wait_until_released()

hub.light_matrix.show_image('HAPPY')
```

### Example 2: Emoji Faces

```python
from spike import PrimeHub

hub = PrimeHub()

while True:
    if hub.left_button.is_pressed():
        hub.light_matrix.show_image('HAPPY')
    elif hub.right_button.is_pressed():
        hub.light_matrix.show_image('SAD')
    else:
        hub.light_matrix.show_image('SMILE')
```

### Example 3: Countdown Timer

```python
from spike import PrimeHub
import time

hub = PrimeHub()

for i in range(5, 0, -1):
    hub.light_matrix.write(str(i))
    hub.speaker.beep(60, 0.2)
    time.sleep(1)

hub.light_matrix.show_image('YES')
hub.speaker.beep(72, 1)
```

### Example 4: Animation Loop

```python
from spike import PrimeHub
import time

hub = PrimeHub()

images = ['ARROW_N', 'ARROW_E', 'ARROW_S', 'ARROW_W']

for i in range(8):  # Loop twice
    for image in images:
        hub.light_matrix.show_image(image)
        time.sleep(0.3)
```

### Example 5: Traffic Light

```python
from spike import PrimeHub
import time

hub = PrimeHub()

# Red light
hub.status_light.on('red')
hub.light_matrix.write('STOP')
time.sleep(2)

# Yellow light
hub.status_light.on('yellow')
hub.light_matrix.write('WAIT')
time.sleep(1)

# Green light
hub.status_light.on('green')
hub.light_matrix.write('GO')
time.sleep(2)
```

---

## 🎨 Common Display Patterns

### Smiley Face

```python
smiley = [
    [0, 9, 0, 9, 0],
    [0, 9, 0, 9, 0],
    [0, 0, 0, 0, 0],
    [9, 0, 0, 0, 9],
    [0, 9, 9, 9, 0]
]
hub.light_matrix.show(smiley)
```

### Heart

```python
heart = [
    [0, 9, 9, 0, 0],
    [9, 9, 9, 9, 0],
    [9, 9, 9, 9, 9],
    [0, 9, 9, 9, 0],
    [0, 0, 9, 0, 0]
]
hub.light_matrix.show(heart)
```

### X Pattern

```python
x_pattern = [
    [9, 0, 0, 0, 9],
    [0, 9, 0, 9, 0],
    [0, 0, 9, 0, 0],
    [0, 9, 0, 9, 0],
    [9, 0, 0, 0, 9]
]
hub.light_matrix.show(x_pattern)
```

---

**Happy Coding! 🎉**
