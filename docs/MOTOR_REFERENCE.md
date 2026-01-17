# 🤖 Motor Reference Guide

Learn how to control motors on your Spike robot!

---

## 📚 Import the Library

```python
import runloop
from hub import port, motion_sensor
import motor
import motor_pair
```

---

## 🔧 Single Motor Basics

### Connect to a Motor

```python
# Motor plugged into port A
# Use port.A, port.B, port.C, port.D, port.E, or port.F
```

### Run the Motor

```python
# Run forward for degrees (async)
async def main():
    await motor.run_for_degrees(port.A, 360, 500)  # 360 degrees at 500 speed

runloop.run(main())

# Or run to absolute position
async def main():
    await motor.run_to_absolute_position(port.A, 0, 500)  # Go to 0 degrees

runloop.run(main())
```

### Motor Direction

```python
async def main():
    # Run forward
    await motor.run_for_degrees(port.A, 360, 500)
    
    # Run backward (use negative degrees)
    await motor.run_for_degrees(port.A, -360, 500)

runloop.run(main())
```

### Check Motor Position

```python
# Get current position
position = motor.relative_position(port.A)
print(position)

# Reset position to 0
motor.reset_relative_position(port.A, 0)
```

---

## 🚗 Motor Pair (Two Motors Together)

Perfect for driving robots with two wheels!

### Connect Motor Pair

```python
# Pair motors in ports A and B
motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
```

### Drive Forward/Backward

```python
async def main():
    # Move forward for degrees
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, 0)  # 360 degrees, 0 steering
    
    # Move backward (use negative degrees)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -360, 0)

runloop.run(main())
```

### Turn the Robot

```python
async def main():
    # Turn right (positive steering)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, 100)
    
    # Turn left (negative steering)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, -100)
    
    # Gentle curve (steering -100 to 100)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 720, 50)

runloop.run(main())
```

### Start/Stop Motor Pair

```python
# Start moving (non-blocking)
motor_pair.move(motor_pair.PAIR_1, 0)  # 0 steering, default velocity

# Move with specific steering
motor_pair.move(motor_pair.PAIR_1, 50, velocity=500)  # 50 steering, 500 velocity

# Stop moving
motor_pair.stop(motor_pair.PAIR_1)
```

---

## 🎯 Quick Examples

### Example 1: Make Motor Spin

```python
import runloop
from hub import port
import motor

async def main():
    await motor.run_for_degrees(port.A, 360, 500)  # One full turn

runloop.run(main())
```

### Example 2: Drive Forward and Back

```python
import runloop
from hub import port
import motor_pair

motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

async def main():
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 720, 0)   # Forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -720, 0)  # Backward

runloop.run(main())
```

### Example 3: Square Drive Pattern

```python
import runloop
from hub import port
import motor_pair

motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

async def main():
    for i in range(4):
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, 0)    # Forward
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, 180, 100)  # Turn right

runloop.run(main())
```

---

**Happy Building! 🎉**
