import os
import time

lol = None

b0 = [0, 0]
b1 = [0, 0, 0, 0]
b2 = [0, 0, 0]
b3 = [0, 0, 0, 0]
b4 = [0, 0, 0]
b5 = [0, 0, 0, 0]

def to_binary(h, m = None, s = None):

    if s is None:

        if m == 1:

            i = 0
            while h != 1 and h != 0:

                b0[i] = h % 2
                h = h / 2
                i = i + 1
            b0[i] = h

        elif m == 2:

            i = 0
            while h != 1 and h != 0:

                b1[i] = h % 2
                h = h / 2
                i = i + 1
            b1[i] = h

        elif m == 3:

            i = 0
            while h != 1 and h != 0:

                b2[i] = h % 2
                h = h / 2
                i = i + 1
            b2[i] = h

        elif m == 4:

            i = 0
            while h != 1 and h != 0:

                b3[i] = h % 2
                h = h / 2
                i = i + 1
            b3[i] = h

        elif m == 5:

            i = 0
            while h != 1 and h != 0:

                b4[i] = h % 2
                h = h / 2
                i = i + 1
            b4[i] = h

        elif m == 6:

            i = 0
            while h != 1 and h != 0:

                b5[i] = h % 2
                h = h / 2
                i = i + 1
            b5[i] = h

    else:

        if lol is None:

            if h < 10 == 0:
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
                to_binary(h / 10, 5)
                to_binary(h % 10, 6)

            lol = s



    return

while True:

    t1 = time.localtime(time.time())

    to_binary(t1.tm_hour, t1.tm_min, t1.tm_sec)

    os.system("cls")
    print "   %d     %d     %d" % (b1[3], b3[3], b5[3])
    print "   %d  %d  %d  %d  %d" % (b1[2], b2[2], b3[2], b4[2], b5[2])
    print "%d  %d  %d  %d  %d  %d" % (b0[1], b1[1], b2[1], b3[1], b4[1], b5[1])
    print "%d  %d  %d  %d  %d  %d" % (b0[0], b1[0], b2[0], b3[0], b4[0], b5[0])

    #print "%d %d %d\n" % (t.tm_hour,t.tm_min,t.tm_sec)
