# Program to demonstrate encoding and decoding of a file - Andy Blankley
# Created out of inspiration for the LZW algorithm.


def GetKey(val, dictt):
    for key, value in dictt.items():
      if val == value:
         return key

    return "key doesn't exist"


def addIndex (i, a):
    return i + a

#### Test samples for LZW logic
#s =  "ABABBABAABABBABA"
s =  "AAABBAAAAABCCBAAABCDDCBABCDAADCBBCDAADCBABCDDCBAAABCCBAAAAABBAAA"
#s = "AAABBAAAAABCCBAAABCDDDBABCDEEDCBBDEBBEDBABDCCDBAAABDCBAAAAABBAAA"

#rootdir = {1 : 'A', 2: 'B'}
rootdir = {1 : 'A', 2: 'B', 3: 'C', 4: 'D'}
#rootdir = {1 : 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}
codestream = []
p = ''
c = ''
pc = ''
i = 0

### Copy of root dir for decoding purposes:
copy_of_dict = rootdir.copy()
###

done = False

# We want to loop through the string of characters. We will access them at index positions.
while not done:

    # set p to be value of character before c
    if i == 0:
        c = s[i]
    # Set c to be the value index position
    else:
        # Set P value
        p = c

        # if i is less than the length of the string -1 , then set c as the next value. I has already been incremented.
        if i < (len(s)-2):
            c = s[i]
        else:
            done = True
            continue

    # Add p and c values together
    pc = p + c
    while True:

        # Checks for the values in the dictionary
        if pc in rootdir.values():
            try:
                i = addIndex(i, 1)
                p = p + c
                c = s[i]

                # Add p and c values together
                pc = p + c

                # Changed will only be set if no exception occurs.
                changed = True
            except IndexError:
                print("End of string")
                # end of string so we can clear c
                pc = "EncodingFinished"
                c = ""

        else:
            pc = p + c
            # Not found, so add to dictionary
            rootdir[len(rootdir) + 1] = pc

            # Take P value and add index to the code stream
            codestream.append(GetKey(p, rootdir))
            break

    i = addIndex(i, 1)


for key, value in rootdir.items():
    print(f"Key: {key} | Value: {value}")

print(codestream)

### Decoding the codestring
print()
print("Decoding the string using LZW Method...\n")

# initialize the variables...
cw = ""
pw = ""
c = ""
p = ""
i = 0
charstream = ""


done = False

# We want to loop through the string of characters. We will access them at index positions.
while not done:

    if i == 0:
        cw = codestream[i]
    else:
        # Set P value
        pw = cw

        if i < (len(codestream)):
            cw = codestream[i]
        else:
            done = True
            continue

    while True:
        # Checks for the values in the dictionary
        if cw in copy_of_dict.keys():
            # output code of cw to char stream
            charstream += copy_of_dict[cw]
            # p will be contents of pw.  c will take first character of p.
            if pw:
                p = copy_of_dict[pw]

            # c takes on the first character of cw value
            c = copy_of_dict[cw][:1]

            # add p and c to dictionary.
            pc = p + c

            # check if P is initial -> If so then we dont need to add pc as c will already be in the dictionary
            if p:
                copy_of_dict[len(copy_of_dict)+1] = pc

            # Break from loop round.
            break
        else:

            # check pw . set p to value of pw.  set c = to 1st character of p
            # add p and c together. add pc to the dictionary. Output value of pc to the char string.
            try:
                if pw:
                    p = copy_of_dict[pw]

                c = p[:1]

                pc = p + c
                copy_of_dict[len(copy_of_dict) + 1] = pc

                charstream += pc
                break
            except KeyError:
                print("Done Decoding")


    i = addIndex(i, 1)


for key, value in copy_of_dict.items():
    print(f"Key: {key} | Value: {value}")

print(charstream)