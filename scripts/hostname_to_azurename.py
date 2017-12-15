#!/usr/bin/python

import sys

# how to use:
# Run './hostname_to_azurename.py <hostname of a node>'
# Prints the corresponding instance name found in azure portal

def main(hostname):
    hostname_backwards = str(hostname[::-1])
    total_number = 36 * int(hostname_backwards[1])
    first_char = hostname_backwards[0]
    if first_char.isalpha():
        total_number += ord(first_char) - 55
    else:
        total_number += int(first_char)
    print hostname[:26] + "-vmss0_" + str(total_number)

if __name__ == "__main__":
   main(sys.argv[1])
