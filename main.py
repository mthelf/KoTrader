import pyautogui
#
#
# This portion covers the initial setup screen and captures the users mouse locations for the
# Lorex's.
#
# Developed by Michael Helf
#
print("                                                                       ")
print("  _  __     _                     _     _______            _           ")
print(" | |/ /    ( )         /\        | |   |__   __|          | |          ")
print(" | ' / ___ |/ ___     /  \  _   _| |_ ___ | |_ __ __ _  __| | ___ _ __ ")
print(" |  < / _ \  / __|   / /\ \| | | | __/ _ \| | '__/ _` |/ _` |/ _ \ '__|")
print(" | . \ (_) | \__ \  / ____ \ |_| | || (_) | | | | (_| | (_| |  __/ |   ")
print(" |_|\_\___/  |___/ /_/    \_\__,_|\__\___/|_|_|  \__,_|\__,_|\___|_|   ")
print("                                                                       ")

print("Hello. Welcome to Ko's Autotrader. Ensure your program is up and running")
print("and we will perform a few basic setup procedures...")

print("________________________________________________________________________")
print("                                                                       ")

print("For the next three(3) steps, ensure your terminal is still the active window...\n")

input("Hover your mouse approximately over the center of long. Then hit enter ")
longLocation = pyautogui.position()
print("Long Location: %d", longLocation)

input("Hover over center of the location of short. Then hit enter...")
shortLocation = pyautogui.position()
print("Short Location: %d", shortLocation)

input("Hover over center of the location of the lorex's. Then hit enter...")
lorexValidLocation = pyautogui.position()
print("Valid Lorex Location: %d", lorexValidLocation)


while (True):

    # Resetting values to check again for a valid lorex
    lorex1Location = 0, 0
    lorex2Location = 0, 0
    lorexValid = False



    # Attempting to locate the lorex's on screen and then setting x, y center values to respective variables
    try:
        lorex1Location = pyautogui.locateCenterOnScreen('Lorex1.png', confidence=.80)
    except:
        print("No Lorex1 currently on screen...")

    try:
        lorex2Location = pyautogui.locateCenterOnScreen('Lorex2.png', confidence=.80)
    except:
        print("No Lorex2 currently on screen...")


    # Checks to see if the Lorex Locations are valid. Initially set to 0, 0 so the check will always fail when
    # the user selects the proper valid Lorex location in the candle position. At each loop it sets the value of
    # lorexValid to false and the locations back to 0, 0 for a repeated check of a valid lorex.
    if (((lorexValidLocation[0] - lorex1Location[0] < 5) and (lorexValidLocation[0] - lorex1Location[0] > -5)) and
            ((lorexValidLocation[1] - lorex1Location[1] < 20) and (lorexValidLocation[1] - lorex1Location[1] > -20))):
        lorexValid = True

    if (((lorexValidLocation[0] - lorex2Location[0] < 5) and (lorexValidLocation[0] - lorex2Location[0] > -5)) and
            ((lorexValidLocation[1] - lorex2Location[1] < 20) and (lorexValidLocation[1] - lorex2Location[1] > -20))):
        lorexValid = True



    try:
        longUnlitOnScreen = pyautogui.locateCenterOnScreen('longUnlit.png', confidence=.90)
    except:
        longUnlitOnScreen = 0, 0

    try:
        shortUnlitOnScreen = pyautogui.locateCenterOnScreen('shortUnlit.png', confidence=.90)
    except:
        shortUnlitOnScreen = 0, 0


    # The next two if statements check for a valid lorex and if the LONG/SHORT buttons are unlit, we click them
    if (lorexValid is True) and (
            ((longLocation[0] - longUnlitOnScreen[0] < 10) and
            (longLocation[0] - longUnlitOnScreen[0] > -10)) and
            (((longLocation[1] - longUnlitOnScreen[1] < 5) and
            (longLocation[1] - longUnlitOnScreen[1] > -5)))):
        pyautogui.moveTo(longLocation)
        pyautogui.click()

    if (lorexValid is True) and (
            ((shortLocation[0] - shortUnlitOnScreen[0] < 10) and
            (shortLocation[0] - shortUnlitOnScreen[0] > -10)) and
            (((shortLocation[1] - shortUnlitOnScreen[1] < 5) and
            (shortLocation[1] - shortUnlitOnScreen[1] > -5)))):
        pyautogui.moveTo(shortLocation)
        pyautogui.click()


    # The next two if statements check for an invalid Lorex and if the LONG/SHORT buttons are lit we click them
    try:
        longLitOnScreen = pyautogui.locateCenterOnScreen('longLit.png', confidence=.85)
    except:
        longLitOnScreen = 0, 0

    try:
        shortLitOnScreen = pyautogui.locateCenterOnScreen('shortLit.png', confidence=.85)
    except:
        shortLitOnScreen = 0, 0

    if (lorexValid is False and (
            ((longLocation[0] - longLitOnScreen[0] < 10) and
            (longLocation[0] - longLitOnScreen[0] > -10)) and
            (((longLocation[1] - longLitOnScreen[1] < 5) and
            (longLocation[1] - longLitOnScreen[1] > -5))))):
        pyautogui.moveTo(longLocation)
        pyautogui.click()

    if (lorexValid is False and (
            ((shortLocation[0] - shortLitOnScreen[0] < 10) and
            (shortLocation[0] - shortLitOnScreen[0] > -10)) and
            (((shortLocation[1] - shortLitOnScreen[1] < 5) and
            (shortLocation[1] - shortLitOnScreen[1] > -5))))):
        pyautogui.moveTo(shortLocation)
        pyautogui.click()
