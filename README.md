# LED Control with MicroPython and ESP8266 NodeMCU

## Project Overview

This project provides a beginner-friendly guide to controlling an LED using an ESP8266 NodeMCU development board programmed with MicroPython.  By following the instructions in this guide, you'll learn how to set up the hardware, upload the necessary software, and interact with your microcontroller to turn an LED on and off via simple commands. This project serves as a fundamental introduction to microcontroller programming, GPIO control, and basic electronics.

## Hardware Required

To get started, you will need the following hardware components:

* **ESP8266 NodeMCU Development Board:** The ESP8266 NodeMCU is a popular, low-cost microcontroller board with built-in Wi-Fi capabilities.  We'll be using it as the "brain" of our project to execute the MicroPython code and control the LED.

* **Green LED:** A Light Emitting Diode (LED) is a semiconductor light source.  We'll use a standard green LED to visualize the output of our program.

* **220Ω Resistor:** A resistor is an electronic component that limits the flow of electrical current.  It's crucial to use a resistor in series with the LED to prevent it from burning out due to excessive current.  A 220Ω resistor is a good starting value for most standard LEDs and 3.3V microcontroller circuits.

* **Breadboard:** A breadboard is a solderless prototyping board with a grid of holes that allows you to easily connect electronic components together using jumper wires.  It provides a convenient way to build and test circuits without soldering.

* **Jumper Wires:** Jumper wires are small wires with connector pins at each end, used to connect components on a breadboard.

* **USB Cable:** A standard USB cable (Type-A to Micro-USB) is used to connect the ESP8266 NodeMCU to your computer.  This connection serves two purposes: it provides power to the NodeMCU, and it allows you to upload code and communicate with the board.

## Wiring Instructions

Follow these steps carefully to connect the hardware components:

1.  **Prepare the ESP8266 NodeMCU:**

    * Place the ESP8266 NodeMCU board on the breadboard.  The board has pins on both sides that fit into the breadboard's holes, providing electrical connections.

2.  **Connect the Resistor:**

    * Identify GPIO4 on the ESP8266 NodeMCU.  GPIO stands for General Purpose Input/Output.  These pins can be configured to either send or receive electrical signals.  In this project, we'll configure GPIO4 as an output pin to send a signal to the LED.  GPIO4 is typically labeled as "D2" on the NodeMCU board.

    * Insert one end of the 220Ω resistor into the breadboard row that corresponds to the D2 pin on the NodeMCU.

    * Insert the other end of the 220Ω resistor into any other empty row on the breadboard.  This row will serve as a connection point between the resistor and the LED.

3.  **Connect the LED:**

    * Identify the positive and negative legs of the LED.  The positive leg (called the anode) is usually longer than the negative leg (called the cathode).  Some LEDs may also have a flat side on the cathode side of the LED housing.

    * Connect the positive leg (anode) of the green LED to the same breadboard row as the free end of the 220Ω resistor.  This ensures that the resistor is connected in series with the LED, limiting the current flowing through it.

    * Connect the negative leg (cathode) of the green LED to a GND (ground) pin on the ESP8266 NodeMCU.  Ground provides a common reference voltage (0V) for the circuit.  The NodeMCU has several GND pins, and you can use any of them.

    **Example Wiring:**

    * Resistor: One end to NodeMCU pin D2 (GPIO4), other end to a separate breadboard row.

    * LED: Positive leg (anode) to the same breadboard row as the resistor, negative leg (cathode) to a GND pin on the NodeMCU.

## Circuit Diagram
![LED_Control_with_MicroPython_and_ESP8266_NodeMCU](circuit_image%20(3).png)


## Software

To program and interact with the ESP8266 NodeMCU, you'll need the following software:

* **MicroPython Firmware:** MicroPython is a lean and efficient implementation of the Python programming language, specifically designed for microcontrollers.  You'll need to flash (install) the MicroPython firmware onto the ESP8266 NodeMCU's flash memory.  This essentially replaces the board's original firmware with the MicroPython interpreter, allowing you to write and execute Python code on the device.  Detailed instructions on how to flash MicroPython to your ESP8266 NodeMCU can be found in various online tutorials and guides (search for "flash MicroPython ESP8266").

* **Serial Communication Program:** A serial communication program allows your computer to communicate with the MicroPython REPL (Read-Eval-Print Loop) running on the ESP8266 NodeMCU.  The REPL is an interactive command-line environment where you can type MicroPython code and see the results immediately.  Popular serial terminal programs include:

    * PuTTY (Windows)

    * Tera Term (Windows)

    * minicom (Linux, macOS)

    * The serial monitor included in the Arduino IDE (can also be used)

* **Tool to Upload MicroPython Code:** You'll need a tool to transfer your MicroPython code (the Python script that controls the LED) from your computer to the ESP8266 NodeMCU's file system.  Some commonly used tools include:

    * `ampy` (Adafruit MicroPython Tool): A command-line tool specifically designed for managing files on MicroPython devices.

    * Thonny: A Python IDE with built-in support for MicroPython, making it easy to write, upload, and run code on microcontrollers.

