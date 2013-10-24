import ROOT
#ROOT.gROOT.SetBatch(True)

import sys
import os
from ctypes import *


def addWeightsToFile( file, newFile, directory = "", tree = "", doVtx = True, VtxChainData = ROOT.TH1F(), VtxChainMC = ROOT.TH1F(), nVtxLeave = "", MCWeight = 1): 
    print "Input: " + file
    input  = ROOT.TFile( file , "WRITE")

#    (path, sep, filename) = file.rpartition("/")
    output = ROOT.TFile( newFile, "RECREATE")
    print "Output: " + newFile
    
    branchName = "weight"

    try:
        histoDataCN = VtxChainData.ClassName() 
        histoMCCN = VtxChainMC.ClassName()
    except:
        print "Vtx-histogram objects not valid"
        doVtx = False 
    if (doVtx and histoDataCN.find("TH1") > -1 and histoMCCN.find("TH1") > -1):
        if (VtxChainData.GetNbinsX() != VtxChainMC.GetNbinsX() or VtxChainData.GetNbinsX() == 0 or VtxChainMC.GetNbinsX() == 0): 
            print "Vtx-histograms number of bins"
            doVtx = False
        else:
            nVtxBins = VtxChainData.GetNbinsX()
    else: 
        print "Vtx-histogram not of type TH1"
        doVtx = False        
    if (not doVtx): print "No Vtx-reweighting will be done!"
    
    for k in input.GetListOfKeys():
        print k.GetName(), " of type ", k.GetClassName()
        if k.GetClassName() == "TDirectoryFile":
            print "  processing directory ",k.GetName()
            din  = input.Get(k.GetName())
            dout = output.mkdir(k.GetName())
            for i in din.GetListOfKeys():
                print "    processing element ",i.GetName()
                if (i.GetClassName() == "TTree" and (i.GetName() == tree or tree == "") ):    
                    src = din.Get(i.GetName())
                    if (directory == k.GetName() or directory == ""):

                        leaveList = src.GetListOfLeaves();
                        treeName = src.GetName();
                        newTree = ROOT.TTree(treeName+"_new",i.GetTitle(),1)
                        varInit = []
                        for leave in leaveList:
#                            print "       ", leave.GetName(), len(varInit)
                            if (leave.ClassName() == "TLeafF"): 
                                varType = "/F"
                                varInit.append(POINTER(c_float)(c_float(0.)))
                            elif (leave.ClassName() == "TLeafI"): 
                                varType = "/I"
                                varInit.append(POINTER(c_int)(c_int(0)))
                            leaveName = leave.GetName()
                            src.GetLeaf(leaveName).SetAddress(varInit[len(varInit)-1])
                            newTree.Branch(leaveName, varInit[len(varInit)-1], leaveName+varType)
                            
                        bufNewVal = c_float(0.)                  
                        newTree.Branch(branchName, addressof(bufNewVal), branchName)
                        for entry in range(src.GetEntries()):
                            src.GetEntry(entry)
                            if (doVtx):
                                nVtx = src.GetLeaf(nVtxLeave).GetValue()
                                if (nVtx <= nVtxBins and nVtx > 0):
                                    vtxWeight = VtxChainData.GetBinContent(int(nVtx))/VtxChainMC.GetBinContent(int(nVtx))
                                else: vtxWeight = 0. 
                            bufNewVal.value = vtxWeight*MCWeight
                            newTree.Fill()
                        newTree.SetName(treeName)
                        dout.WriteTObject(newTree, i.GetName())
                        print "      Added Branch " + branchName + " to Tree " + i.GetName()
                    else :
                        cloned = src.CloneTree()
                        dout.WriteTObject(cloned, i.GetName())       

                elif i.GetClassName() != "TDirectory":
                    dout.WriteTObject(i.ReadObj(), i.GetName())
                    print "      copied ",i.GetClassName(),i.GetName()

    
#                        except TypeError:
#                            if i.GetClassName() != "TDirectory":
#                                dout.WriteTObject(i.ReadObj(), i.GetName())
#                                print "      copied ",i.GetClassName(),i.GetName() + " (a varaible contained in '" + formula + "' is not in " + i.GetName() + ")"
#                            continue
