import serial
import time
import csv
import matplotlib.pyplot as plt
import datetime

# === SETUP ===
port = "COM3"  
baud_rate = 9600

# Create timestamped filename
timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
filename = f"fsr_log_{timestamp}.csv"

# === CONNECT TO ARDUINO ===
arduino = serial.Serial(port, baud_rate)
time.sleep(2)

# Prepare CSV and data lists
times = []
readings = []

print(f"Logging to {filename}... Press Ctrl+C to stop.")

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "FSR Reading"])

    try:
        while True:
            raw = arduino.readline()
            line = raw.decode("utf-8", errors="ignore").strip()

            if "FSR Reading:" in line:
                try:
                    reading = int(line.split(":")[1].strip())
                    t = time.time()
                    times.append(t)
                    readings.append(reading)
                    writer.writerow([t, reading])
                    print(f"{t}: {reading}")
                except Exception as e:
                    print(f"Parse error: {e}")
    except KeyboardInterrupt:
        print("\nLogging stopped.")
        arduino.close()

# === AUTO-GENERATE GRAPH ===
plt.plot(times, readings)
plt.title("FSR Pressure Readings Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Pressure (0–1023)")
plt.grid(True)
plt.savefig(f"fsr_graph_{timestamp}.png")
plt.show()