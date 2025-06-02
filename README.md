# Tactile Logger – FSR Pressure + LED Feedback

This project builds a tactile sensing and logging system using:
- A Force Sensing Resistor (FSR) to detect pressure
- An LED to respond in real time to high pressure
- A Python script to log readings and generate a graph

---

## 🔧 Hardware
- Arduino Uno
- FSR (Force Sensing Resistor)
- 220Ω resistor
- LED
- Jumper wires + breadboard

---

## 🧠 What It Does
- Pressing on the FSR increases analog readings
- When pressure > threshold (800), LED turns on
- Python script logs readings in real time to CSV
- Auto-generates a line graph from your sensor data

---

## 🗂️ Files
| File                  | Description |
|-----------------------|-------------|
| `fsr_logger_final.py` | Python logger and grapher |
| `fsr_led_control.ino` | Arduino code to drive LED |
| `*.csv`               | Sample sensor data |
| `*.png`               | Sample graph |