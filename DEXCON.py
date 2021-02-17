SongName = "TEST-secondlas "
NCODE = "0 E4 1 0;4 C5 1 0;8 B4 1 0;10 C5 1 0;14 B4 1 0;16 A4 4 0;24 G4 1 0;28 F4 4 0;32 E4 1 0;35 C5 1 0;39 B4 1 0;41 C5 1 0;45 B4 1 0;47 A4 4 0;59 G4 1 0;63 G4 1 0;65 A4 1 0;67 B4 1 0;75 B4 1 0;79 B4 1 0;81 C5 1 0;83 A4 1 0;91 G4 1 0;95 G4 1 0;97 A4 1 0;99 B4 1 0;107 B4 1 0;111 B4 1 0;113 C5 1 0;115 A4 1 0;"
COD1 = ""
COD2 = ""
COD3 = ""
COD4 = ""
COD5 = ""
COD6 = ""
COD7 = ""
i = 0
c1 = "C5"
c2 = "A4"
c3 = "E4"
c4 = "B4"
c5 = "G4"
c6 = "F4"
c7 = "KI"
tmp = ""
while i < len(NCODE):
    if NCODE[i] != ';':
        tmp = tmp+NCODE[i]
        i = i+1
    else:

        if tmp.find(c1) != -1:
            COD1 = COD1+tmp+";"
        elif tmp.find(c2) != -1:
            COD2 = COD2+tmp+";"
        elif tmp.find(c3) != -1:
            COD3 = COD3+tmp+";"
        elif tmp.find(c4) != -1:
            COD4 = COD4+tmp+";"
        elif tmp.find(c5) != -1:
            COD5 = COD5+tmp+";"
        elif tmp.find(c6) != -1:
            COD6 = COD6+tmp+";"
        elif tmp.find(c7) != -1:
            COD7 = COD7+tmp+";"
        else:
            print("ERROR COULD NOT FIND : "+tmp+"\n")
        tmp = ""
        i = i+1


# remover
i = 0
mt = 0
tmp = ""
t = ""
f = ""


while i < len(COD1):
    t = ""
    f = ""

    while COD1[i] != " ":
        t = t+COD1[i]
        i = i+1
    i = i+1

    while COD1[i] != " ":
        i = i+1
    i = i+1
    while COD1[i] != " ":
        f = f+COD1[i]
        i = i+1
    i = i+1
    while COD1[i] != ";":
        i = i+1
    i = i+1
    c = 0

    while c < (int(t)-mt):
        tmp = tmp+"0"
        c = c+1
    mt = int(t)
    c = 0
    while c < (int(f)-1):
        tmp = tmp+"1"
        c = c+1
    if int(f) > 0:
        tmp = tmp+"b"
    mt = mt+int(f)
COD1 = tmp

# for cod2

i = 0
mt = 0
tmp = ""
t = ""
f = ""

while i < len(COD2):
    t = ""
    f = ""
    while COD2[i] != " ":
        t = t+COD2[i]
        i = i+1
    i = i+1
    while COD2[i] != " ":
        i = i+1
    i = i+1
    while COD2[i] != " ":
        f = f+COD2[i]
        i = i+1
    i = i+1
    while COD2[i] != ";":
        i = i+1
    i = i+1
    c = 0

    while c < (int(t)-mt):
        tmp = tmp+"0"
        c = c+1
    mt = int(t)
    c = 0
    while c < (int(f)-1):
        tmp = tmp+"1"
        c = c+1
    if int(f) > 0:
        tmp = tmp+"b"
    mt = mt+int(f)
COD2 = tmp

# FOr COD3

i = 0
mt = 0
tmp = ""
t = ""
f = ""

while i < len(COD3):
    t = ""
    f = ""
    while COD3[i] != " ":
        t = t+COD3[i]
        i = i+1
    i = i+1
    while COD3[i] != " ":
        i = i+1
    i = i+1
    while COD3[i] != " ":
        f = f+COD3[i]
        i = i+1
    i = i+1
    while COD3[i] != ";":
        i = i+1
    i = i+1
    c = 0

    while c < (int(t)-mt):
        tmp = tmp+"0"
        c = c+1
    mt = int(t)
    c = 0
    while c < (int(f)-1):
        tmp = tmp+"1"
        c = c+1
    if int(f) > 0:
        tmp = tmp+"b"
    mt = mt+int(f)
COD3 = tmp


# For COD4
i = 0
mt = 0
tmp = ""
t = ""
f = ""

while i < len(COD4):
    t = ""
    f = ""
    while COD4[i] != " ":
        t = t+COD4[i]
        i = i+1
    i = i+1
    while COD4[i] != " ":
        i = i+1
    i = i+1
    while COD4[i] != " ":
        f = f+COD4[i]
        i = i+1
    i = i+1
    while COD4[i] != ";":
        i = i+1
    i = i+1
    c = 0

    while c < (int(t)-mt):
        tmp = tmp+"0"
        c = c+1
    mt = int(t)
    c = 0
    while c < (int(f)-1):
        tmp = tmp+"1"
        c = c+1
    if int(f) > 0:
        tmp = tmp+"b"
    mt = mt+int(f)
COD4 = tmp


# for COD5
i = 0
mt = 0
tmp = ""
t = ""
f = ""

while i < len(COD5):
    t = ""
    f = ""
    while COD5[i] != " ":
        t = t+COD5[i]
        i = i+1
    i = i+1
    while COD5[i] != " ":
        i = i+1
    i = i+1
    while COD5[i] != " ":
        f = f+COD5[i]
        i = i+1
    i = i+1
    while COD5[i] != ";":
        i = i+1
    i = i+1
    c = 0

    while c < (int(t)-mt):
        tmp = tmp+"0"
        c = c+1
    mt = int(t)
    c = 0
    while c < (int(f)-1):
        tmp = tmp+"1"
        c = c+1
    if int(f) > 0:
        tmp = tmp+"b"
    mt = mt+int(f)
COD5 = tmp


# FOR COD6

i = 0
mt = 0
tmp = ""
t = ""
f = ""

while i < len(COD6):
    t = ""
    f = ""
    while COD6[i] != " ":
        t = t+COD6[i]
        i = i+1
    i = i+1
    while COD6[i] != " ":
        i = i+1
    i = i+1
    while COD6[i] != " ":
        f = f+COD6[i]
        i = i+1
    i = i+1
    while COD6[i] != ";":
        i = i+1
    i = i+1
    c = 0

    while c < (int(t)-mt):
        tmp = tmp+"0"
        c = c+1
    mt = int(t)
    c = 0
    while c < (int(f)-1):
        tmp = tmp+"1"
        c = c+1
    if int(f) > 0:
        tmp = tmp+"b"
    mt = mt+int(f)
COD6 = tmp

# For COD7

i = 0
mt = 0
tmp = ""
t = ""
f = ""

while i < len(COD7):
    t = ""
    f = ""
    while COD7[i] != " ":
        t = t+COD7[i]
        i = i+1
    i = i+1
    while COD7[i] != " ":
        i = i+1
    i = i+1
    while COD7[i] != " ":
        f = f+COD7[i]
        i = i+1
    i = i+1
    while COD7[i] != ";":
        i = i+1
    i = i+1
    c = 0

    while c < (int(t)-mt):
        tmp = tmp+"0"
        c = c+1
    mt = int(t)
    c = 0
    while c < (int(f)-1):
        tmp = tmp+"1"
        c = c+1
    if int(f) > 0:
        tmp = tmp+"b"
    mt = mt+int(f)
COD7 = tmp

# set element length SAME


cnmax = len(COD1)

if cnmax < len(COD2):
    cnmax = len(COD2)
if cnmax < len(COD3):
    cnmax = len(COD3)
if cnmax < len(COD4):
    cnmax = len(COD4)
if cnmax < len(COD5):
    cnmax = len(COD5)
if cnmax < len(COD6):
    cnmax = len(COD6)
if cnmax < len(COD7):
    cnmax = len(COD7)

while cnmax % 7 != 0:
    cnmax = cnmax+1

c = len(COD1)
while c < cnmax:
    COD1 = COD1+"0"
    c = c+1
c = len(COD2)
while c < cnmax:
    COD2 = COD2+"0"
    c = c+1
c = len(COD3)
while c < cnmax:
    COD3 = COD3+"0"
    c = c+1
c = len(COD4)
while c < cnmax:
    COD4 = COD4+"0"
    c = c+1
c = len(COD5)
while c < cnmax:
    COD5 = COD5+"0"
    c = c+1
c = len(COD6)
while c < cnmax:
    COD6 = COD6+"0"
    c = c+1
c = len(COD7)
while c < cnmax:
    COD7 = COD7+"0"
    c = c+1


##################################################################
######                      MIXER                       ##########
#################################################################

r = len(COD1)
c = 0
tmp = ""
while c < r:
    tmp = tmp+COD1[c]
    tmp = tmp+COD2[c]
    tmp = tmp+COD3[c]
    tmp = tmp+COD4[c]
    tmp = tmp+COD5[c]
    tmp = tmp+COD6[c]
    tmp = tmp+COD7[c]
    c = c+1


f = open(SongName+" fullconverted code.txt", "w+")
f.write(tmp)
f.close()
f = open(SongName+" d5code.txt", "w+")
f.write(COD1)
f.close()
