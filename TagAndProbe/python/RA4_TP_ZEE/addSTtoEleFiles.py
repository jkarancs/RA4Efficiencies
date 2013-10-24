import os
import ROOT
ROOT.gROOT.LoadMacro("Add_Stlep.C")

path = 'Ele_121008'

files = []
dirlist = os.listdir(path+'/Data/')
for dir in dirlist:
    if not os.path.isdir(path+'/Data/'+dir):
        continue
    for file in os.listdir(path+'/Data/'+dir):
        if not file.partition(".")[2] == "root":
            continue
        files.append(str(path+'/Data/'+dir+'/'+file))
        
dirlist = os.listdir(path+'/MC/')
for dir in dirlist:
    if not os.path.isdir(path+'/MC/'+dir):
        continue
    for file in os.listdir(path+'/MC/'+dir+'/vtx_reweighted/'):
        if not file.partition(".")[2] == "root":
            continue
        files.append(str(path+'/MC/'+dir+'/vtx_reweighted/'+file))

print 'Adding stlep to files:'
for file in files:
    print file
    ROOT.Add_Stlep(file)
