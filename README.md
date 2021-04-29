# SmartSensorPython
MicroPython Code for playing with microcontroller especially to experiment with M5stack devices

This example shows how to push data to external portal once montion is detected. I have used blynk for this project.

**What you will need:**
1. M5stack device ( M5sstick, M5Stack Core , M5Atom) - ESP32
2. Firmware burned to device (Refer to M5stack documentation : https://docs.m5stack.com/en/products)
3. Import BlynkLib.py to your device (You will need this to M5stack device have a bug of crashing while sending data to blynk server). 
- https://github.com/vshymanskyy/blynk-library-python
- REPL: For me rshell worked ( to connect to device and copy python file ). Make sure you are in app / settings mode in M5stack device otherwise rshell will not connect
- rshell serial COM5
4. Passive Infrared Sensor (PIR) motion sensor to detect human motion
5. blynk account to upload data from device to blynk server (https://blynk.io/)
6. blynk API credentials


