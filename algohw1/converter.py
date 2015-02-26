<<<<<<< HEAD
import time


def intro():
    print "Welcome! This program will convert inches to centimeters for you.\n"
    convert()


def convert():
    input_cm = input("Inches: ")
    inches_conv = input_cm * 2.54
    print "Centimeters: %f\n" % inches_conv
    time.sleep(3)
    restart = raw_input("Do you wish to make another conversion? [y]Yes or [n]no: ")
    if restart == 'y':
        convert()
    elif restart == 'n':
        end_fast()
    else:
        print "I didn't quite understand that answer. Terminating."
        end_slow()


def end_fast():
    print "This program will close in 5 seconds."
    time.sleep(5)


def end_slow():
    print "This program will close in 30 seconds."
    time.sleep(30)

=======
import time


def intro():
    print "Welcome! This program will convert inches to centimeters for you.\n"
    convert()


def convert():
    input_cm = input("Inches: ")
    inches_conv = input_cm * 2.54
    print "Centimeters: %f\n" % inches_conv
    time.sleep(3)
    restart = raw_input("Do you wish to make another conversion? [y]Yes or [n]no: ")
    if restart == 'y':
        convert()
    elif restart == 'n':
        end_fast()
    else:
        print "I didn't quite understand that answer. Terminating."
        end_slow()


def end_fast():
    print "This program will close in 5 seconds."
    time.sleep(5)


def end_slow():
    print "This program will close in 30 seconds."
    time.sleep(30)

>>>>>>> origin/master
intro()