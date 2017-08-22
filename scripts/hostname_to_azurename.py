#!/usr/bin/python

import sys

# how to use:
# Run './hostname_to_azurename.py <hostname of a node>'
# Prints the corresponding instance name found in azure portal

def main(hostname):
    hostname_backwards = str(hostname[::-1])
    total_number = 0
    i = 0
    for character in hostname_backwards:
        if character.isalpha():
            number = ord(character) - 55
        else:
            number = int(character)
            if number == 0:
                break
        if i > 0:
            total_number += 35
        total_number += number
        i += 1
    print hostname[:26] + "-vmss0_" + str(total_number)

if __name__ == "__main__":
   main(sys.argv[1])
