import math
def list_ifname_ip():
    fin = open('running-config.cfg')
    res=dict()

    for line in fin:
        if "nameif" in line:
            mytemplist = line.split()

            next(fin)
            templine = next(fin)
            mylist= templine.split()

            if mytemplist[0]=='nameif':
                if mylist[0] == 'ip':
                    mytuple=(mylist[2:])
                    newdict[mytemplist[1]]=mytuple

    return (res)

ipconfigs = list_ifname_ip()
print(ipconfigs)
