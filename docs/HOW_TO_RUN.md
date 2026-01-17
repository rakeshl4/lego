# How to Run LEGO Spike Prime Programs

⚠️ **IMPORTANT:** These programs use **SPIKE 3 Python API** and must be run in the **LEGO Spike Prime App** (version 3.0+), not regular Python!

## Prerequisites

1. **LEGO Spike Prime Hub** - Charged and powered on
2. **LEGO Spike Prime App** - Downloaded on your computer/tablet
   - Download: <https://education.lego.com/en-us/downloads/spike-app/software>
3. **USB Cable or Bluetooth** - To connect hub to computer

## Method 1: Using LEGO Spike Prime App (Easiest)

### Step-by-Step

1. **Open the LEGO Spike Prime App**
   - Launch the app on your computer or tablet

2. **Connect Your Hub**
   - Turn on the Spike Prime hub (press center button)
   - Connect via USB cable OR Bluetooth
   - Wait for green connection indicator

3. **Create a New Project**
   - Click "New Project"
   - Switch to **Python** mode (toggle in top right)

4. **Copy the Code**
   - Open any `.py` file from this folder
   - Copy all the code
   - Paste into the Python editor in the app

5. **Run the Program**
   - Click the **Play** button (▶️)
   - Watch your robot come to life!

6. **Stop the Program**
   - Click the **Stop** button (⏹️)

## ⚠️ Important: About the "spike" Module

**The `spike` module ONLY works inside the LEGO Spike Prime App!**

You **cannot** run these programs with regular Python on your computer. The error `ModuleNotFoundError: No module named 'spike'` means you're trying to run the code outside the app.

### Why?

- The `spike` module is built into the LEGO Spike Prime App
- It's not available as a pip package
- It requires direct connection to the Spike Prime hub hardware

### Solution

**Always use Method 1** - Copy the code into the LEGO Spike Prime App's Python editor and run it there.

## Hardware Setup Tips

### Port Connections

Make sure your motors and sensors are plugged into the correct ports as specified in each program:

- **Port A** - Usually left motor
- **Port B** - Usually right motor or color sensor
- **Port C** - Usually distance sensor
- **Port D** - Usually force sensor or additional motor
- **Ports E & F** - Additional sensors/motors

### Common Issues

❌ **"Motor not found"** → Check motor is plugged into correct port
❌ **"No connection"** → Make sure hub is on and connected
❌ **"Syntax error"** → Make sure you copied all the code correctly
❌ **Program won't start** → Check hub battery level (should be green)

## Program Order (Recommended)

Learn in this sequence (check which files exist in your folder):

1. Start with basic motor control
2. Learn about reading sensors
3. Combine motors + sensors for robots
4. Try advanced features like motor pairs and async programming

## Tips for Learning

✅ **Experiment!** - Change numbers and see what happens
✅ **Read comments** - They explain what each line does
✅ **Start simple** - Begin with lesson 1, then progress
✅ **Build first** - Make sure your robot is built before coding

## Need Help?

- Check the official documentation: <https://spike.legoeducation.com>
- Review the lesson comments in each `.py` file
- Try the examples in the LEGO Spike app first

---

**Ready to code?** Start with `01_hello_motor.py`! 🚀
