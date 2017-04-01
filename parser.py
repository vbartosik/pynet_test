from ciscoconfparse import CiscoConfParse

cfg = CiscoConfParse('cisco.cfg')

crypto = cfg.find_objects(r"^crypto map CRYPTO")

print("Task 1: Find all of the crypto map entries in the file (lines that begin with 'crypto map CRYPTO') and for each crypto map entry print out its children:\n")

for map in crypto:
    print(map.text + "configuration is:")
    for child in map.children:
        print(child.text)

print("\nTask 2: Find all of the crypto map entries that are using PFS group2:\n")
pfs = cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")
for map in pfs:
    print map.text
 
print("\nTask 3: Find the crypto maps that are not using AES (based-on the transform set name). Print these entries and their corresponding transform set name.\n") 
trans = cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES-SHA") 
for map in trans:
    print map.text 
    print(map.re_search_children(r"set transform-set")[0].text)
     
