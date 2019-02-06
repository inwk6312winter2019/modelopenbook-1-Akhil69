def access_list():
    try: 
        fin = open("running-config.cfg",'r')

        fw = open("running-config-new.cfg", "w")

        for i in fin: #if it founds 255.255.255.0 replace to 255.255.0.0
            print(i)
            if "192" in i:
                i = i.replace("255" , "10")
                fw.write(i)
            elif "172" in i:
                i = i.replace("172" , "10")
                fw.write(i)
            elif "255.255.0.0" in i:
                i = i.replace("255.255.0.0" , "255.0.0.0")
                fw.write(i)
            elif "255.255.255.0" in i:
                i = i.replace("255.255.255.0" , "255.0.0.0")
                fw.write(i)
            else:
                fw.write(i)
    except:
        print("Check")  


access_list()

