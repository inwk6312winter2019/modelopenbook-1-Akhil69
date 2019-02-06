def create_list():
    myfile  = open("running-config.cfg","r")
    transit_access_in = []
    fw_management_access_in = []
    global_access = []
    for i in myfile:
       if "transit_access_in" in i:
           i = i.strip()
           transit_access_in.append(i)
       if "fw-management_access_in" in i:
           i = i.strip()
           fw_management_access_in.append(i)
       if  "global_access" in i:
           i = i.strip()
           global_access.append(i)
print("\ntransit_accesslist:" , transit_access_in)
print("\fw management_list:" , fw_management_access_in)
print("\global_access:" , global_access)
create_list()


