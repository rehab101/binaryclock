import os #For console commands
import time #For the time tuple

'''
filename: binaryclock.py
author: Prajjwal Srivastav aka rehab101
'''

#Each array is used to display binary of each digit in HH:MM:SS

b0 = [0, 0] #1st digit of H
b1 = [0, 0, 0, 0] #2nd digit of H
b2 = [0, 0, 0] #1st digit of M
b3 = [0, 0, 0, 0] #2nd digit of M
b4 = [0, 0, 0] #1st digit of S
b5 = [0, 0, 0, 0] #2nd digit of S

prev = None #Variable for previous value

#Do floor division and/or modulus division with 2 to get each bit and store it in array

def to_binary(h, m = None, s = None):

    global prev,b0,b1,b2,b3,b4,b5

    if s is None:

        if m == 1:

            if prev is None:

                i = 0
                prev = h
                while h != 1 and h != 0:
                    b0[i] = h % 2
                    h = h / 2
                    i = i + 1
                b0[i] = h

            elif prev > h: #If previous value is greater then reinitialise array with 0s

                b0 = [0, 0]
                i = 0
                prev = h
                while h != 1 and h != 0:
                    b0[i] = h % 2
                    h = h / 2
                    i = i + 1
                b0[i] = h

            else:
                i = 0
                prev = h
                while h != 1 and h != 0:
                    b0[i] = h % 2
                    h = h / 2
                    i = i + 1
                b0[i] = h

        elif m == 2:

            if prev is None:

                i = 0
                prev = h
                while h != 1 and h != 0:
                    b1[i] = h % 2
                    h = h / 2
                    i = i + 1
                b1[i] = h

            elif prev > h:

                b1 = [0, 0, 0, 0]
                i = 0
                prev = h
                while h != 1 and h != 0:
                    b1[i] = h % 2
                    h = h / 2
                    i = i + 1
                b1[i] = h

            else:
                i = 0
                prev = h
                while h != 1 and h != 0:
                    b1[i] = h % 2
                    h = h / 2
                    i = i + 1
                b1[i] = h

        elif m == 3:

            if prev is None:

                i = 0
                prev = h
                while h != 1 and h != 0:
                    b2[i] = h % 2
                    h = h / 2
                    i = i + 1
                b2[i] = h

            elif prev > h:

                b2 = [0, 0, 0]
                i = 0
                prev = h
                while h != 1 and h != 0:
                    b2[i] = h % 2
                    h = h / 2
                    i = i + 1
                b2[i] = h

            else:
                i = 0
                prev = h
                while h != 1 and h != 0:
                    b2[i] = h % 2
                    h = h / 2
                    i = i + 1
                b2[i] = h

        elif m == 4:

            if prev is None:

                i = 0
                prev = h
                while h != 1 and h != 0:
                    b3[i] = h % 2
                    h = h / 2
                    i = i + 1
                b3[i] = h

            elif prev > h:

                b3 = [0, 0, 0, 0]
                i = 0
                prev = h
                while h != 1 and h != 0:
                    b3[i] = h % 2
                    h = h / 2
                    i = i + 1
                b3[i] = h

            else:
                i = 0
                prev = h
                while h != 1 and h != 0:
                    b3[i] = h % 2
                    h = h / 2
                    i = i + 1
                b3[i] = h

        elif m == 5:

            if prev is None:

                i = 0
                prev = h
                while h != 1 and h != 0:
                    b4[i] = h % 2
                    h = h / 2
                    i = i + 1
                b4[i] = h

            elif prev > h:

                b4 = [0, 0, 0]
                i = 0
                prev = h
                while h != 1 and h != 0:
                    b4[i] = h % 2
                    h = h / 2
                    i = i + 1
                b4[i] = h

            else:
                i = 0
                prev = h
                while h != 1 and h != 0:
                    b4[i] = h % 2
                    h = h / 2
                    i = i + 1
                b4[i] = h

        elif m == 6:

            if prev is None:

                i = 0
                prev = h
                while h != 1 and h != 0:
                    b5[i] = h % 2
                    h = h / 2
                    i = i + 1
                b5[i] = h

            elif prev > h:

                b5 = [0, 0, 0, 0]
                i = 0
                prev = h
                while h != 1 and h != 0:
                    b5[i] = h % 2
                    h = h / 2
                    i = i + 1
                b5[i] = h

            else:
                i = 0
                prev = h
                while h != 1 and h != 0:
                    b5[i] = h % 2
                    h = h / 2
                    i = i + 1
                b5[i] = h

    else:

        if h < 10 == 0: #Check if H is single or double digit and call itself appropriate arguments
            to_binary(h, 2)
        else:
            to_binary(h / 10, 1)
            to_binary(h % 10, 2)

        if m < 10 == 0:
            to_binary(m, 4)
        else:
            to_binary(m / 10, 3)
            to_binary(m % 10, 4)

        if s < 10 == 0:
            to_binary(s, 6)
        else:
            to_binary(s / 10, 5)
            to_binary(s % 10, 6)

    return

while True:

    t1 = time.localtime(time.time()) #Get the time tuple

    to_binary(t1.tm_hour, t1.tm_min, t1.tm_sec) #Function call

    os.system("cls") #Clear the screen

    print "   %d     %d     %d" % (b1[3], b3[3], b5[3])
    print "   %d  %d  %d  %d  %d" % (b1[2], b2[2], b3[2], b4[2], b5[2])
    print "%d  %d  %d  %d  %d  %d" % (b0[1], b1[1], b2[1], b3[1], b4[1], b5[1])
    print "%d  %d  %d  %d  %d  %d" % (b0[0], b1[0], b2[0], b3[0], b4[0], b5[0])
    time.sleep(1)
