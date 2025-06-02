// === Pin Setup ===
const int fsrPin = A0;     // FSR sensor connected to analog pin A0
const int ledPin = 3;      // LED connected to digital pin 3

// === Threshold ===
const int pressureThreshold = 850;  // Value above which LED turns on

void setup() {
  pinMode(ledPin, OUTPUT);     // Set LED pin as output
  Serial.begin(9600);          // For debugging/logging if needed
}

void loop() {
  // Read the analog pressure value from the FSR
  int fsrReading = analogRead(fsrPin);

  // Optional: Print it to Serial Monitor for debugging
  Serial.print("FSR Reading: ");
  Serial.println(fsrReading);

  // Check pressure and control LED
  if (fsrReading > pressureThreshold) {
    digitalWrite(ledPin, HIGH);  // Turn LED ON
  } else {
    digitalWrite(ledPin, LOW);   // Turn LED OFF
  }

  delay(100); // Slow down the loop slightly (optional)
}