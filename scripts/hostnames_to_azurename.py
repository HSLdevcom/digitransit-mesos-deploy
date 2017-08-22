#!/usr/bin/python

# how to use:
# Store hostnames in a file called hosts.txt in this directory
# (one host name on each line, empty line at the end)
# Prints the corresponding instance names found in azure portal
# in a sorted order

def mycmp(a, b):
    hosts1 = int(a.split('_')[-1])
    hosts2 = int(b.split('_')[-1])
    return cmp(hosts1, hosts2)

def main():
    f = open('hosts.txt', 'r')
    priv_hosts = []
    pub_hosts = []
    for line in f:
        if len(line) < 26:
            break
        hostname = line[:-1]
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
        if "private" in hostname[:26]:
            priv_hosts.append(hostname[:26] + "-vmss0_" + str(total_number))
        else:
            pub_hosts.append(hostname[:26] + "-vmss0_" + str(total_number))
    f.close()
    priv_hosts.sort(mycmp)
    pub_hosts.sort(mycmp)
    for host in priv_hosts:
        print(host)
    for host in pub_hosts:
        print(host)
    
if __name__ == "__main__":
   main()
