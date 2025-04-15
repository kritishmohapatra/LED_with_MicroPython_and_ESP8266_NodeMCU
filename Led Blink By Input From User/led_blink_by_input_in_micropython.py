from machine import Pin  # Import the Pin class from the machine module, used for controlling GPIO pins.

led = Pin(4, Pin.OUT)  # Create a Pin object named 'led'.
                        # - 4: Specifies the GPIO pin number (in this case, GPIO4).
                        # - Pin.OUT: Configures the pin as an output pin, allowing you to control its voltage.

while True:  # Start an infinite loop, so the code inside will run continuously.
    try:
        user_input = input("Enter: 0 or 1-")  # Prompt the user to enter either '0' or '1' and store the input as a string in the 'user_input' variable.
        value = int(user_input)  # Convert the user's string input to an integer.

        if value == 0 or value == 1:  # Check if the entered value is either 0 or 1.
            led.value(value)  # Set the value of the 'led' pin to the integer entered by the user.
                                # - If the user entered '1', the pin will be set HIGH (typically 3.3V), turning the LED on (if wired correctly).
                                # - If the user entered '0', the pin will be set LOW (0V), turning the LED off.
        else:
            print("Invalid input. Please enter 0 or 1.")  # If the user enters anything other than '0' or '1', print an error message.

    except ValueError:
        print("Invalid input. Please enter a number (0 or 1).")  # If the user enters non-numeric input that cannot be converted to an integer, print a value error message.
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")  # If the user presses Ctrl+C, gracefully exit the loop and print a message.
        break  # Exit the while loop.0
    