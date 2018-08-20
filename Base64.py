#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# Standart encrypting code table
base64_code_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
    "abcdefghijklmnopqrstuvwxyz" \
    "0123456789+/"


def Encrypt(input):

    # Verifies if the input file exists
    if not os.path.exists(input):
        print("The file '{0}' does not exist.".format(input))
        return

    ''' Open the input file and create a output file by adding "_enc".
    Ex.: Input file name = foo.txt -> output file name = foo_enc.txt '''
    inFile = open(input, 'r')
    outFile = open(os.path.splitext(inFile.name)[0] + "_enc.txt", "w")
    # Reads the input file
    inString = inFile.read()
    # Checks if the input file isn't empty
    if not inString:
        print ("The input file is empty")
        return

    '''Gets every character in inString and get it ASCII number
    then get the binary representation with 8 digit,
    adding 0's at the beginning if necessary
    and assign it to outString  '''
    outString = [bin(ord(x))[2:].zfill(8) for x in inString]
    # Converts a list into a string
    outString = "".join(outString)
    # Checks if the length is multiple of 6, adding 0's at the end if necessary
    outString = outString + "0" * (6 - len(outString) % 6)
    # Creates a list by split the string into 6 bits segments
    outString = [outString[i: i + 6] for i in range(0, len(outString), 6)]
    ''' Each segment is converted to integer and used to access the index
    in base64_code_table  '''
    outString = [base64_code_table[int(c, 2)] for c in outString]
    # Converts the list into a string
    outString = "".join(outString)
    ''' Checks if the length is multiple of 4,
    adding "="'s at the end if necessary  '''
    outString = outString + "=" * (4 - len(outString) % 4)
    # Writes the output file
    outFile.write(outString)
    # Closes the files
    inFile.close()
    outFile.close()

    return


def Decrypt(input):

    # Verifies if the input file exists
    if not os.path.exists(input):
        print("The file '{0}' does not exist.".format(input))
        return
    ''' Opens the input file and create a output file by adding "_dec".
    Ex.: Input file name = foo.txt -> output file name = foo_dec.txt '''
    inFile = open(input, "r")
    outFile = open(os.path.splitext(inFile.name)[0] + "_dec.txt", "w")
    # Reads the input file
    inString = inFile.read()
    # Checks if the input file isn't empty
    if not inString:
        print("The file is empty.")
        return
    # Removes every "=" at the end
    inString = "".join([x if x != "=" else "" for x in inString])
    ''' Matches the character to its index from the
    base64_code_table and stores the index  '''
    outString = [base64_code_table.index(x) for x in inString]
    '''Casts the index stored into binary then checks if the length
    is multiples of 6, adding 0's at the beginning if necessary  '''
    outString = [bin(x)[2:].zfill(6) for x in outString]
    # Converts a list into a string
    outString = "".join(outString)
    # Creates a list by split the string into 8 bits segments
    outString = [outString[i:i + 8] for i in range(0, len(outString), 8)]
    ''' Removes the last element of outString if it's sizes isn't multiple of 8.
    0's added at line 37  '''
    if len(outString[-1]) != 8:
        outString = outString[:-1]
    ''' Converts the binaries in the list into integer,
    then using ASCII table converts into a character  '''
    outString = [chr(int(x, 2)) for x in outString]
    # Converts a list into a string
    outString = "".join(outString)
    # Writes the output file
    outFile.write(outString)
    # Closes the files
    inFile.close()
    outFile.close()

    return
