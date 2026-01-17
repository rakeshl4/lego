# 🤖 Motor Reference Guide

Learn how to control motors on your Spike robot!

---

## 📚 Import the Library

```python
from spike import Motor, MotorPair
```

---

## 🔧 Single Motor Basics

### Connect to a Motor

```python
my_motor = Motor('A')  # Motor plugged into port A
```

### Run the Motor

```python
# Run forward
my_motor.run_for_degrees(360)  # Turn 1 full rotation

# Run at a speed (0-100)
my_motor.start(50)  # Run at 50% speed

# Stop the motor
my_motor.stop()
```

### Motor Direction

```python
# Run forward
my_motor.run_for_degrees(360)

# Run backward (use negative)
my_motor.run_for_degrees(-360)
```

### Check Motor Position

```python
# Get current position
position = my_motor.get_position()
print(position)
```

---

## 🚗 Motor Pair (Two Motors Together)

Perfect for driving robots with two wheels!

### Connect Motor Pair

```python
wheels = MotorPair('A', 'B')  # Left motor in A, Right motor in B
```

### Drive Forward/Backward

```python
# Move forward
wheels.move(10, 'cm')  # Move 10 centimeters

# Move backward (negative)
wheels.move(-10, 'cm')
```

### Turn the Robot

```python
# Turn right
wheels.move(5, 'cm', steering=100)

# Turn left
wheels.move(5, 'cm', steering=-100)

# Gentle curve (steering 0-100)
wheels.move(10, 'cm', steering=50)
```

### Start/Stop Motor Pair

```python
# Start moving
wheels.start(speed=50)

# Stop moving
wheels.stop()
```

---

## 🎯 Quick Examples

### Example 1: Make Motor Spin

```python
from spike import Motor

motor = Motor('A')
motor.run_for_degrees(360)  # One full turn
```

### Example 2: Drive Forward and Back

```python
from spike import MotorPair

wheels = MotorPair('A', 'B')
wheels.move(20, 'cm')   # Forward
wheels.move(-20, 'cm')  # Backward
```

### Example 3: Square Drive Pattern

```python
from spike import MotorPair

wheels = MotorPair('A', 'B')

for i in range(4):
    wheels.move(10, 'cm')              # Forward
    wheels.move(5, 'cm', steering=100) # Turn right
```

---

**Happy Building! 🎉**
