print(" ")
print(" ___       ___     __     __       ___    ___  __   __          ")
print("  |  |__| |__     |__) | / _` |__|  |      |  /  \ /  \ |       ")
print("  |  |  | |___    |  \ | \__> |  |  |      |  \__/ \__/ |___ ...")
print(" ")
                                                        

# This program starts off with the list of systems eg. Raspberry Pi and Microbit. Each question will help eliminate systems that are not suitable for your project idea eg. no camera or no WiFi.
                                                               
#  The weird looking code that looks like this \x1b[6;30;42m is a built in python feature that lets you add colour text. You could also use the colorama module to do this


print("This program helps you narrow down the right system to use for your project ")

listOfSystems = ["Desktop", "Raspberry Pi", "Microbit", "Arduino Uno", "Pico", "RaspberryPiZeroW", "Arduino ESP32"]

print("\n \x1b[6;30;42m" + "Your current options are...", listOfSystems, '\x1b[0m', "\n")


# Q1: Does it General Inputs and Outputs?
print(" ### Q1/8: GPIO")
print("\n Does you idea involve things like wired sensors, GPIO (input and output pins), wires or other non USB components?")
answer = input("\n (Y)es or (N)o?")

if answer.upper() == "Y" or answer.upper() == "YES":
  print("")
  print("We can elimnate Desktop PC as that has nowhere to easily connect wired sensors.")
  print("Note: Some sensors can be connected via USB or you could use the PC with another system eg. Micro:bit")

  if "Desktop" in listOfSystems:
    listOfSystems.remove("Desktop")


print("\n \x1b[6;30;42m" + "Your current options are...", listOfSystems, '\x1b[0m', "\n")

print(" ### Q2/8: INTERNET")
# Q2: Easy Internet?
print("Does it need to easily and directly connect to the internet without going through a PC?")
answer = input("\n (Y)es or (N)o?")

if answer.upper() == "Y" or answer.upper() == "YES":
  print("We can elimnate Microbit because that would need to connect to the internet through a PC")
  print("We can elimnate the Raspberry Pi Pico because that would need to connect to the internet through a PC")
  print("We can elimnate the Arduino (although you could use an add=on board for WiFi, it's not the obvious choice)")

# removes eliminated options
  if "Microbit" in listOfSystems:
    listOfSystems.remove("Microbit")
  if "Pico" in listOfSystems:
    listOfSystems.remove("Pico")
  if "Arduino Uno" in listOfSystems:
    listOfSystems.remove("Arduino Uno")


print("\n \x1b[6;30;42m" + "Your current options are...", listOfSystems, '\x1b[0m', "\n")

print(" ### Q3/8: CAMERA")
# Q3: Easy to use a Camera?
print("\n Does it need to use a camera without going through a PC?")
answer = input("\n (Y)es or (N)o?")

if answer.upper() == "Y" or answer.upper() == "YES":
  print("")
  print("We can elimnate the Raspberry Pi Pico & Microbit because they have no camera connector")
  print("We can drop Arduino boards because their camera modules can't save pictures without going through a PC or adding a memory storage module. Yes it's technically possible but it's not the obvious choice here.")

  if "Microbit" in listOfSystems:
    listOfSystems.remove("Microbit")
  if "Pico" in listOfSystems:
    listOfSystems.remove("Pico")
  if "Arduino Uno" in listOfSystems:
    listOfSystems.remove("Arduino Uno")
  if "Arduino ESP32" in listOfSystems:
    listOfSystems.remove("Arduino ESP32")

print("\n \x1b[6;30;42m" + "Your current options are...", listOfSystems, '\x1b[0m', "\n")


# Q4: Analogue inputs?
print(" ### Q4/8: ANALOGUE INPUTS")
print("\n Does it need to easily connect to an analogue sensor?")
answer = input("\n (Y)es or (N)o?")

if answer.upper() == "Y" or answer.upper() == "YES":
  print("")
  print("We can elimnate Raspberry Pi, RaspberryPiZeroW because they have no analogue inputs.")
  print("You can add an analogue to digial converter but it'd be a good bit more work!")

  if "Raspberry Pi" in listOfSystems:
    listOfSystems.remove("Raspberry Pi")
  if "Pico" in listOfSystems:
    listOfSystems.remove("Pico")
  if "RaspberryPiZeroW" in listOfSystems:
    listOfSystems.remove("RaspberryPiZeroW")

print("\n \x1b[6;30;42m" + "Your current options are...", listOfSystems, '\x1b[0m', "\n")


print(" ### Q5/8: MORE COMPLEX i2C SENSORS")
# Q5: Does it need to work with more complex i2C sensors?
print("\n Does the idea use larger i2C sensors? (If examples use the SDA and SCL pins, then you are indeed using a fancy i2C sensor) ")
answer = input("\n (Y)es or (N)o?")

if answer.upper() == "Y" or answer.upper() == "YES":
  print("")
  print("We can elimnate the Micro:bit because that has limited i2C support.")
  print("Note: There is one set of i2C pins on it but it's not well supported outside if the extensions on makecode.org")

  if "Microbit" in listOfSystems:
    listOfSystems.remove("Microbit")

print("\n \x1b[6;30;42m" + "Your current options are...", listOfSystems, '\x1b[0m', "\n")




print(" ### Q6/8: POWER")
# Q6: Power needed
print("\n Does your project need be light enough to wear?")
answer = input("\n (Y)es or (N)o?")

if answer.upper() == "Y" or answer.upper() == "YES":
  print("")
  print("We can elimnate everything but the smallest boards")
  print("Note: You can use Raspberry Pi and 5V powerpack but the battery doesn't last very long. A 5V pack is usally heavy")
  print("Note: The Arduino Uno can be used with a 9V battery but you'd be best going down to a smaller version like an Arduino Nano for wearables.")

  if "Desktop" in listOfSystems:
    listOfSystems.remove("Desktop")
  if "Raspberry Pi" in listOfSystems:
    listOfSystems.remove("Raspberry Pi")
  if "Arduino Uno" in listOfSystems:
    listOfSystems.remove("Arduino Uno")

print("\n \x1b[6;30;42m" + "Your current options are...", listOfSystems, '\x1b[0m', "\n")



print(" ### Q7/8: PROGRAMMING LANGUAGE")
# Q7: Programming Language
print("\n Would you be terribly upset if you had to program in Arduino's language C instead of python?")
answer = input("\n (Y)es or (N)o?")

if answer.upper() == "Y" or answer.upper() == "YES":
  print("")
  print("Well you can get rid of mist arduino boards so. They use C instead of python.")
  print("Note: You can use adafruit's circuit python and micropython on ESP32 but there would be a bit more work there.")

  if "Arduino ESP32" in listOfSystems:
    listOfSystems.remove("Arduino ESP32")
  if "Arduino Uno" in listOfSystems:
    listOfSystems.remove("Arduino Uno")

print("\n \x1b[6;30;42m" + "Your current options are...", listOfSystems, '\x1b[0m', "\n")



print(" ### Q8/8: SOUND AND MEDIA")
# Q8: Audio out
print("\n Does your device need to easily output digital audio such as voice or mp3?")
answer = input("\n (Y)es or (N)o?")

if answer.upper() == "Y" or answer.upper() == "YES":
  print("")
  print("Well you can get rid of everything except Raspberry Pi or Desktop PC")
  print("Note: The smaller boards can get addons and modules to play audio files but these are extras. The Raspberry Pi Zero has two HDMI outputs which carry audio along with video (so fine with a TV or Monitor with built in speakers) but the RaspiZero has no quick and easy 3mm audio out jack.")

  if "Arduino ESP32" in listOfSystems:
    listOfSystems.remove("Arduino ESP32")
  if "Arduino Uno" in listOfSystems:
    listOfSystems.remove("Arduino Uno")
  if "Pico" in listOfSystems:
    listOfSystems.remove("Pico")
  if "Microbit" in listOfSystems:
    listOfSystems.remove("Microbit")
  if "RaspberryPiZeroW" in listOfSystems:
    listOfSystems.remove("RaspberryPiZeroW")

print("\n \x1b[6;30;42m" + "Your current options are...", listOfSystems, '\x1b[0m', "\n")






########### THE VERDICT


if len(listOfSystems) == 0:
  print("Hmmm it looks like there is no one single system that can be used to solve this problem. You might need to use a combination of different systems eg. Mirobit + Raspberry Pi.")

  print("     .--------.          ")
  print("   .'          '.        ")
  print("  /   O      O   \        ")
  print(" :           `    :        ")
  print(" |                |           ")
  print(" :    .------.    :        ")
  print("  \  '        '  /        ")
  print("   '.          .'        ")
  print("     '-......-'        ")

elif len(listOfSystems) == 1:
 print("       It's a perfect match! ")
 print("")
 print(" ______$¦$¦$¦$ ____ $¦$¦$¦$    ")
 print(" ____$¦$_____$$__$$_____$¦$     ")
 print("___$¦$________$$________$¦$    ")
 print("__ $¦$___________________$¦$    ")
 print("___$¦$__________________$¦$    ")
 print("_(¯`.´¯)$¦$___________$¦$(¯`.´¯)    ")
 print("(¯≻ ✦ ≺¯)$¦$_______$¦$(¯≻ ✦ ≺¯)    ")
 print("_(_.^._)____$¦$___$¦$____ (_.^._)    ")
 print("_____(¯`.´¯) __$¦$__ (¯`.´¯)    ")
 print("___ (¯≻ ✦ ≺¯) _ $_ (¯≻ ✦ ≺¯)    ")
 print("_____(_.^._) (¯`.´¯)_(_.^._)    ")
 print("__________(¯≻ ✦ ≺¯)    ")
 print("_____(¯`.´¯) (_.^._) (¯`.´¯)    ")
 print("___ (¯≻ ✦ ≺¯) ____(¯≻ ✦ ≺¯)    ")
 print("_____(_.^._) ______ (_.^._)    ")

 print("\n Go forth with your", listOfSystems[0], "and dare mighty things!")

elif len(listOfSystems) > 1:
 print("You've got a few options! Maybe go with the easiest to use? Or the best deal on ebay?")