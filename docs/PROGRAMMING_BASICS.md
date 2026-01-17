# 🎮 Programming Basics - Quick Reference

A simple guide to learn programming concepts!

---

## 📦 Variables

Variables are like boxes that store information.

```python
# Store a number
speed = 50

# Store text
robot_name = "Spike"

# Store True/False
is_moving = True
```

---

## ❓ If Statement

Use `if` to make decisions - "If this is true, do that!"

```python
distance = 10

if distance < 20:
    print("Something is close!")
```

---

## 🔀 Else Statement

Use `else` for "otherwise, do this instead!"

```python
color = "red"

if color == "red":
    print("Stop!")
else:
    print("Go!")
```

---

## 🎯 Elif Statement

Use `elif` to check multiple conditions.

```python
score = 75

if score >= 90:
    print("Amazing!")
elif score >= 70:
    print("Good job!")
else:
    print("Keep trying!")
```

---

## 🔗 Logical Operators

Combine multiple conditions together!

### AND (both must be true)

```python
color = "green"
distance = 30

if color == "green" and distance > 20:
    print("Safe to move!")
```

### OR (at least one must be true)

```python
color = "red"

if color == "red" or color == "yellow":
    print("Slow down!")
```

### NOT (opposite)

```python
moving = False

if not moving:
    print("Robot is stopped")
```

---

## 🔁 For Loop

Repeat something a specific number of times.

```python
# Count to 5
for i in range(5):
    print(i)  # Prints: 0, 1, 2, 3, 4

# Repeat 3 times
for i in range(3):
    print("Hello!")
```

---

## 🔄 While Loop

Keep doing something while a condition is true.

```python
count = 0

while count < 3:
    print("Loop number:", count)
    count = count + 1
```

---

## 🎪 Functions

Functions are reusable blocks of code - like recipes!

```python
# Create a function
def say_hello():
    print("Hello, friend!")

# Use the function
say_hello()
```

### Functions with Parameters

Give the function information to work with.

```python
def greet(name):
    print("Hi", name)

greet("Alex")  # Prints: Hi Alex
greet("Sam")   # Prints: Hi Sam
```

---

## 📤 Return Statement

Functions can give back (return) a value!

```python
def add_numbers(a, b):
    result = a + b
    return result

answer = add_numbers(5, 3)
print(answer)  # Prints: 8
```

### Another Example

```python
def is_close(distance):
    if distance < 10:
        return True
    else:
        return False

close = is_close(5)
print(close)  # Prints: True
```

---

## 🧮 Comparison Operators

Compare values to each other!

```python
==  # Equal to
!=  # Not equal to
>   # Greater than
<   # Less than
>=  # Greater than or equal to
<=  # Less than or equal to
```

### Examples

```python
if 5 == 5:          # True
if 5 != 3:          # True
if 10 > 5:          # True
if 3 < 7:           # True
if speed >= 50:     # Check if speed is 50 or more
if distance <= 20:  # Check if distance is 20 or less
```

---

## 📝 Lists

Store multiple items in one variable!

```python
# Create a list
colors = ["red", "green", "blue"]

# Access items (starts at 0)
print(colors[0])  # Prints: red
print(colors[1])  # Prints: green

# Add to list
colors.append("yellow")

# Loop through list
for color in colors:
    print(color)
```

---

## 💡 Quick Tips

- **Indentation matters!** Use spaces to show what's inside if/for/functions
- **Use clear names** - `robot_speed` is better than `x`
- **Test small pieces** - run your code often to catch mistakes early
- **Comments help** - use `#` to write notes in your code

---

## 🚀 Putting It All Together

### Example 1: Robot Safety Check

```python
def check_sensor(distance, color):
    """Check sensors and decide what to do"""
    
    if distance < 10 and color == "red":
        return "STOP NOW!"
    elif distance < 20:
        return "Slow down"
    else:
        return "All clear"

# Use the function
result = check_sensor(15, "green")
print(result)  # Prints: Slow down
```

### Example 2: Score Calculator

```python
def calculate_grade(score):
    """Turn a score into a letter grade"""
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "Keep practicing!"

# Test with different scores
for test_score in [95, 85, 72, 65]:
    grade = calculate_grade(test_score)
    print(f"Score {test_score} = Grade {grade}")
```

### Example 3: Traffic Light System

```python
def traffic_light(light, pedestrian_waiting):
    """Decide what to do at a traffic light"""
    
    if light == "red" or pedestrian_waiting:
        return "STOP"
    elif light == "yellow":
        return "SLOW DOWN"
    elif light == "green" and not pedestrian_waiting:
        return "GO"
    else:
        return "BE CAREFUL"

# Test different situations
print(traffic_light("green", False))  # GO
print(traffic_light("red", False))    # STOP
print(traffic_light("green", True))   # STOP
```

### Example 4: List with Loop and If

```python
def find_red_objects(colors):
    """Count how many red objects we found"""
    
    red_count = 0
    
    for color in colors:
        if color == "red":
            red_count = red_count + 1
            print("Found a red one!")
    
    return red_count

# Test it
sensor_readings = ["blue", "red", "green", "red", "red"]
total = find_red_objects(sensor_readings)
print(f"Total red objects: {total}")
```

### Example 5: Distance Alert System

```python
def distance_alert(distance):
    """Alert based on how close something is"""
    
    alerts = []  # Empty list to store alerts
    
    if distance < 5:
        alerts.append("DANGER! Too close!")
        alerts.append("Back up now!")
    elif distance < 15:
        alerts.append("Warning: Getting close")
    else:
        alerts.append("All clear")
    
    return alerts

# Check different distances
for dist in [3, 12, 25]:
    messages = distance_alert(dist)
    print(f"\nDistance {dist}cm:")
    for message in messages:
        print(f"  - {message}")
```

### Example 6: Game Score Tracker

```python
def play_game():
    """Simple number guessing game"""
    
    secret_number = 7
    score = 0
    guesses = [5, 8, 7]
    
    for guess in guesses:
        if guess == secret_number:
            print(f"🎉 You got it! The number was {secret_number}")
            score = score + 10
            return score
        elif guess < secret_number:
            print(f"❌ {guess} is too low")
        else:
            print(f"❌ {guess} is too high")
    
    print("Game over!")
    return score

final_score = play_game()
print(f"Your score: {final_score}")
```

---

**Happy Coding! 🎉**
