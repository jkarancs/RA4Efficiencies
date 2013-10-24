import sys
import os
import copy
import ROOT
from addWeightsToTPFile import addWeightsToFile

ROOT.gROOT.ProcessLine(".L ./tdrstyle.C")
ROOT.setTDRStyle()

#def calculateMCWeights(newDirectory = ""):
dirMC = [
    "../Ele_121008/MC/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/",
    "../Ele_121008/MC/QCD_HT-250To500_TuneZ2star_8TeV-madgraph-pythia6/",
    "../Ele_121008/MC/QCD_HT-500To1000_TuneZ2star_8TeV-madgraph-pythia6/",
    "../Ele_121008/MC/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/",
    "../Ele_121008/MC/TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola/",
    "../Ele_121008/MC/T_s-channel_TuneZ2star_8TeV-powheg-tauola/",
    "../Ele_121008/MC/T_t-channel_TuneZ2star_8TeV-powheg-tauola/",
    "../Ele_121008/MC/T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/",
    "../Ele_121008/MC/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/",
    "../Ele_121008/MC/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/",
    "../Ele_121008/MC/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/",
    "../Ele_121008/MC/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/",
    "../Ele_121008/MC/WW_TuneZ2star_8TeV_pythia6_tauola/",
    "../Ele_121008/MC/WZ_TuneZ2star_8TeV_pythia6_tauola/",
    "../Ele_121008/MC/ZZ_TuneZ2star_8TeV_pythia6_tauola/"
]

dirData = [
    #"../Ele_121008/Data/ElectronHad_Run2012A-13Jul2012-v1/",
    #"../Ele_121008/Data/ElectronHad_Run2012A-recover-06Aug2012-v1/",
    #"../Ele_121008/Data/ElectronHad_Run2012B-13Jul2012-v1/",
    #"../Ele_121008/Data/ElectronHad_Run2012C-24Aug2012-v1/",
    #"../Ele_121008/Data/ElectronHad_Run2012C-PromptReco-v2/",
    "../Ele_121008/Data/SingleElectron_Run2012A-13Jul2012-v1/",
    "../Ele_121008/Data/SingleElectron_Run2012A-recover-06Aug2012-v1/",
    "../Ele_121008/Data/SingleElectron_Run2012B-13Jul2012-v1/",
    "../Ele_121008/Data/SingleElectron_Run2012C-24Aug2012-v1/",
    "../Ele_121008/Data/SingleElectron_Run2012C-PromptReco-v2/"    
    ]

mcColors = [
            ROOT.kMagenta,
            ROOT.kBlue-4,
            ROOT.kBlue-4,
            ROOT.kBlue-4,
            ROOT.kRed,
            ROOT.kOrange,
            ROOT.kOrange,
            ROOT.kOrange,
            ROOT.kOrange,
            ROOT.kOrange,
            ROOT.kOrange,
            ROOT.kYellow,
            ROOT.kGreen+4,
            ROOT.kGreen,
            ROOT.kGreen-4
            ]

mcNames = [
    "DYJetsToLL_M-50",        
    "QCD_HT-250To500",
    "QCD_HT-500To1000",
    "QCD_HT-1000ToInf",
    "TTJets",
    "T_s",
    "T_t",
    "T_tW",
    "Tbar_s",
    "Tbar_t",
    "Tbar_tW",
    "WJetsToLNu",
    "WW",
    "WZ",
    "ZZ"
    ]

xSec = [
    3503.71,
    276000.0,
    8426.0,
    204.0,
    225.197,
    3.79,
    56.4,
    11.1,
    1.76,
    30.7,
    11.1,
    36257.2,
    55,
    32.3,
    8.1,
]
max_vtx = 45

nbins_mass = 60
min_mass = 60.
max_mass = 120.

nbins_relIso = 100
min_relIso = 0.
max_relIso = 100.

lumi = 1000.
dataDir = "goodPATEleToHLT"
useTree = "fitter_tree"

vtxLeaf = "tag_nVertices"
massLeaf = "mass"
combIsoLeaf = "probe_gsfEle_ecaliso"
common_cut = "(probe_gsfEle_et > 10 && abs(probe_gsfEle_eta) < 2.4 && " + vtxLeaf + " <= " + str(max_vtx) + " && " + vtxLeaf + " > 0 " + " && " + massLeaf + " > " + str(min_mass) + " && " + massLeaf + " < " + str(max_mass) + ")"


selectedAllMC = []
countChainsMC = []
dataChainsMC = []
weights = []
for (i,dir) in enumerate(dirMC):
    print "Adding MC files in " + dir + ":"
    filenames = os.listdir( dir )
    addedFiles = []
    selectedFiles = []
    for file in filenames:
       if (file.rpartition(".")[2] != "root"): continue
       fname = file.rpartition("_")[0].rpartition("_")[0]
       infile_mc = ROOT.TFile(dir+file,"OPEN")
       hasCounting = infile_mc.cd("countingHLTFilter")
       hasData = infile_mc.cd(dataDir)
       if (addedFiles.count(fname) > 0): 
           print "   omitting file " + file + "(dublicate)"
           continue
       elif (hasCounting == 0 or hasData == 0):
           print "   omitting file " + file + "(no counting or data tree)"
           continue
       else:
           addedFiles.append( fname )
           selectedFiles.append( dir + file )
#           print "   adding file " + dir + file
    selectedAllMC.append(selectedFiles)
    countChainsMC.append(ROOT.TChain("countingHLTFilter/CountTree"))
    dataChainsMC.append(ROOT.TChain(dataDir +"/"+ useTree))
    for file in selectedFiles:
        countChainsMC[i].Add( file )
        dataChainsMC[i].Add( file )
    entries = countChainsMC[i].GetEntries("passed")
    weights.append(xSec[i]*lumi/entries)
    print "      " + str(len(selectedFiles)) + " selected files have " + str(entries) + " entries, xsec = " + str(xSec[i])
    print "      with lumi = " + str(lumi) + " setting weight to " + str(weights[i])

print ""
selectedAllData = []
dataChainData = ROOT.TChain(dataDir +"/"+ useTree)
for (i,dir) in enumerate(dirData):
    print "Adding Data files in " + dir + ":"
    filenames = os.listdir( dir )
    addedFiles = []
    selectedFiles = []
    for file in filenames:
       if (file.rpartition(".")[2] != "root"): continue
       fname = file.rpartition("_")[0].rpartition("_")[0]
       infile_data = ROOT.TFile(dir+file,"OPEN")
       hasData = infile_data.cd(dataDir)
       if (addedFiles.count(fname) > 0): 
           print "   omitting file " + file + "(dublicate)"
           continue
       elif (hasData == 0):
           print "   omitting file " + file + "(no data tree)"
           continue
       else:
           addedFiles.append( fname )
           selectedFiles.append( dir + file )
#           print "   adding file " + dir + file
    for file in selectedFiles:
        dataChainData.Add( file )
        selectedAllData.append( file )
    print "      " + str(len(selectedFiles)) + " selected files"
    

    
vtxMC = ROOT.TH1F("vtxMC","vtxMC",max_vtx,0.5,max_vtx+0.5)
vtxMC.Sumw2()
vtxMC.SetLineStyle(ROOT.kDashed)
vtxMC.SetLineWidth(2)
vtxMCsingle = []
vtxMCStack = ROOT.THStack("vtxMCStack","vtxMCStack")

massMC = ROOT.TH1F("massMC","massMC",nbins_mass,min_mass,max_mass)
massMC.Sumw2()
massMC.SetLineStyle(ROOT.kDashed)
massMC.SetLineWidth(2)
massMCsingle = []
massMCStack = ROOT.THStack("massMCStack","massMCStack")

combIsoMC = ROOT.TH1F("combIsoMC","combIsoMC",nbins_relIso,min_relIso,max_relIso)    
combIsoMC.Sumw2()
combIsoMC.SetLineStyle(ROOT.kDashed)
combIsoMC.SetLineWidth(2)
combIsoMCsingle = []
combIsoMCStack = ROOT.THStack("combIsoMCStack","combIsoMCStack")

for (i,chain) in enumerate(dataChainsMC):
    if (i == 0): chain.Draw(vtxLeaf+">>vtxMC",str(weights[i]) + "*" + common_cut,"goff")
    else: chain.Draw(vtxLeaf+">>+vtxMC",str(weights[i]) + "*" + common_cut,"goff")
    if (i == 0): chain.Draw(massLeaf+">>massMC",str(weights[i]) + "*" + common_cut,"goff")
    else: chain.Draw(massLeaf+">>+massMC",str(weights[i]) + "*" + common_cut,"goff")
    if (i == 0): chain.Draw(combIsoLeaf+">>combIsoMC",str(weights[i]) + "*" + common_cut,"goff")
    else: chain.Draw(combIsoLeaf+">>+combIsoMC",str(weights[i]) + "*" + common_cut,"goff")

vtxData = ROOT.TH1F("vtxData","vtxData",max_vtx,0.5,max_vtx+0.5)
vtxData.SetMarkerStyle(20)
dataChainData.Draw(vtxLeaf+">>vtxData",common_cut,"goff")

massData = ROOT.TH1F("massData","massData",nbins_mass,min_mass,max_mass)    
massData.SetMarkerStyle(20)
dataChainData.Draw(massLeaf+">>massData",common_cut,"goff")

combIsoData = ROOT.TH1F("combIsoData","combIsoData",nbins_relIso,min_relIso,max_relIso)    
combIsoData.SetMarkerStyle(20)
dataChainData.Draw(combIsoLeaf+">>combIsoData",common_cut,"goff")

scale = massData.Integral()/massMC.Integral()
print "scale = ", scale
vtxMC.Scale(scale)
massMC.Scale(scale)
combIsoMC.Scale(scale)
print "vtxMC_integral = ", vtxMC.Integral(), " / vtxData_integral = ", vtxData.Integral()
print "massMC_integral = ", massMC.Integral(), " / massData_integral = ", massData.Integral()

for i in range(len(weights)):
    weights[i] *= scale

for (i,chain) in enumerate(dataChainsMC):
    vtxMCsingle.append(ROOT.TH1F("vtxMC"+mcNames[i],"vtxMC"+mcNames[i],max_vtx,0.5,max_vtx+0.5))
    vtxMCsingle[i].Sumw2()
    vtxMCsingle[i].SetFillColor(mcColors[i])
    chain.Draw(vtxLeaf+">>vtxMC"+mcNames[i],str(weights[i]) + "*" + common_cut,"goff")
    vtxMCStack.Add(vtxMCsingle[i],"histef")

    massMCsingle.append(ROOT.TH1F("massMC"+mcNames[i],"massMC"+mcNames[i],nbins_mass,min_mass,max_mass))
    massMCsingle[i].Sumw2()
    massMCsingle[i].SetFillColor(mcColors[i])
    chain.Draw(massLeaf+">>massMC"+mcNames[i],str(weights[i]) + "*" + common_cut,"goff")
    massMCStack.Add(massMCsingle[i],"histef")

    combIsoMCsingle.append(ROOT.TH1F("combIsoMC"+mcNames[i],"combIsoMC"+mcNames[i],nbins_relIso,min_relIso,max_relIso))
    combIsoMCsingle[i].Sumw2()
    combIsoMCsingle[i].SetFillColor(mcColors[i])
    chain.Draw(combIsoLeaf+">>combIsoMC"+mcNames[i],str(weights[i]) + "*" + common_cut,"goff")
    combIsoMCStack.Add(combIsoMCsingle[i],"histef")

cNoRW = ROOT.TCanvas("cNoRW","cNoRW",1500,500)
cNoRW.Divide(3,1)
cNoRW.cd(1)
vtxData.Draw("ep")
vtxMCStack.Draw("same")
vtxMC.Draw("ehistsame")
vtxData.Draw("epsame")
cNoRW.cd(2)
massData.Draw("ep")
massMCStack.Draw("same")
massMC.Draw("ehistsame")
massData.Draw("epsame")
cNoRW.cd(3)
combIsoMCStack.SetMinimum(10.)
combIsoMCStack.Draw()
combIsoMC.Draw("ehistsame")
combIsoData.Draw("epsame")
ROOT.gPad.SetLogy()
cNoRW.SaveAs("cNoRW.root")

vtxData_rw = vtxData.Clone()
vtxMC_rw = vtxMC.Clone()

for (i,dir) in enumerate(dirMC):
    savePath = dir + "/vtx_reweighted/"
    try: os.makedirs(savePath)
    except (OSError): 
        print "Warning: savePath already exists!" 
        existingFiles = os.listdir( savePath )
        for file in existingFiles:
            os.remove( savePath+file )
    
    filenames = os.listdir( dir )
    for file in filenames:
        #if (file.partition("_")[0] != "tnpZ" and file.partition("_")[2].partition("_")[0] != "MC"): continue 
        if (file.partition("_")[0] != "tpZEE" and file.partition("_")[2].partition("_")[0] != "MC.root"): continue 
        addWeightsToFile( dir+file, savePath+file, "", "fitter_tree", True, vtxData_rw, vtxMC_rw, vtxLeaf, weights[i])
      
selectedAllMC_rw = []
dataChainsMC_rw = []
for (i,dir) in enumerate(dirMC):
    print "Adding MC files in " + dir + "vtx_reweighted/" + ":"
    filenames = os.listdir( dir + "vtx_reweighted/" )
    addedFiles = []
    selectedFiles = []
    for file in filenames:
       if (file.rpartition(".")[2] != "root"): continue
       fname = file.rpartition("_")[0].rpartition("_")[0]
       infile_mc_rw = ROOT.TFile(dir + "vtx_reweighted/" + file,"OPEN")
       hasCounting = infile_mc_rw.cd("countingHLTFilter")
       hasData = infile_mc_rw.cd(dataDir)
       if (addedFiles.count(fname) > 0): 
           print "   omitting file " + file + "(dublicate)"
           continue
       elif (hasCounting == 0 or hasData == 0):
           print "   omitting file " + file + "(no counting or data tree)"
           continue
       else:
           addedFiles.append( fname )
           selectedFiles.append( dir + "vtx_reweighted/" + file )
#           print "   adding file " + dir + file
    dataChainsMC_rw.append(ROOT.TChain(dataDir +"/"+ useTree))
    for file in selectedFiles:
        dataChainsMC_rw[i].Add( file )
        selectedAllMC_rw.append(file)


vtxMC_rw = ROOT.TH1F("vtxMC_rw","vtxMC_rw",max_vtx,0.5,max_vtx+0.5)
vtxMC_rw.Sumw2()
vtxMC_rw.SetLineStyle(ROOT.kDashed)
vtxMC_rw.SetLineWidth(2)
vtxMCsingle_rw = []
vtxMCStack_rw = ROOT.THStack("vtxMCStack_rw","vtxMCStack_rw")

massMC_rw = ROOT.TH1F("massMC_rw","massMC_rw",nbins_mass,min_mass,max_mass)
massMC_rw.Sumw2()
massMC_rw.SetLineStyle(ROOT.kDashed)
massMC_rw.SetLineWidth(2)
massMCsingle_rw = []
massMCStack_rw = ROOT.THStack("massMCStack_rw","massMCStack_rw")

combIsoMC_rw = ROOT.TH1F("combIsoMC_rw","combIsoMC_rw",nbins_relIso,min_relIso,max_relIso)
combIsoMC_rw.Sumw2()
combIsoMC_rw.SetLineStyle(ROOT.kDashed)
combIsoMC_rw.SetLineWidth(2)
combIsoMCsingle_rw = []
combIsoMCStack_rw = ROOT.THStack("combIsoMCStack_rw","combIsoMCStack_rw")

dataChainsMC_rw[0].GetListOfLeaves().ls()
for (i,chain) in enumerate(dataChainsMC_rw):
    if (i == 0): chain.Draw(vtxLeaf+">>vtxMC_rw","weight*" + common_cut,"goff")
    else: chain.Draw(vtxLeaf+">>+vtxMC_rw","weight*" + common_cut,"goff")
    vtxMCsingle_rw.append(ROOT.TH1F("vtxMC_rw"+mcNames[i],"vtxMC_rw"+mcNames[i],max_vtx,0.5,max_vtx+0.5))
    vtxMCsingle_rw[i].Sumw2()
    vtxMCsingle_rw[i].SetFillColor(mcColors[i])
    chain.Draw(vtxLeaf+">>vtxMC_rw"+mcNames[i],"weight*" + common_cut,"goff")
    vtxMCStack_rw.Add(vtxMCsingle_rw[i],"histef")

    if (i == 0): chain.Draw(massLeaf+">>massMC_rw","weight*" + common_cut,"goff")
    else: chain.Draw(massLeaf+">>+massMC_rw","weight*" + common_cut,"goff")
    massMCsingle_rw.append(ROOT.TH1F("massMC_rw"+mcNames[i],"massMC"+mcNames[i],nbins_mass,min_mass,max_mass))
    massMCsingle_rw[i].Sumw2()
    massMCsingle_rw[i].SetFillColor(mcColors[i])
    chain.Draw(massLeaf+">>massMC_rw"+mcNames[i],"weight*" + common_cut,"goff")
    massMCStack_rw.Add(massMCsingle_rw[i],"histef")

    if (i == 0): chain.Draw(combIsoLeaf+">>combIsoMC_rw","weight*" + common_cut,"goff")
    else: chain.Draw(combIsoLeaf+">>+combIsoMC_rw","weight*" + common_cut,"goff")
    combIsoMCsingle_rw.append(ROOT.TH1F("combIsoMC_rw"+mcNames[i],"combIsoMC"+mcNames[i],nbins_relIso,min_relIso,max_relIso))
    combIsoMCsingle_rw[i].Sumw2()
    combIsoMCsingle_rw[i].SetFillColor(mcColors[i])
    chain.Draw(combIsoLeaf+">>combIsoMC_rw"+mcNames[i],"weight*" + common_cut,"goff")
    combIsoMCStack_rw.Add(combIsoMCsingle_rw[i],"histef")

cRW = ROOT.TCanvas("cRW","cRW",1500,500)
cRW.Divide(3,1)
cRW.cd(1)
vtxData.Draw("ep")
vtxMCStack_rw.Draw("same")
vtxMC_rw.Draw("ehistsame")
vtxData.Draw("epsame")
cRW.cd(2)
massData.Draw("ep")
massMCStack_rw.Draw("same")
massMC_rw.Draw("ehistsame")
massData.Draw("epsame")
cRW.cd(3)
combIsoMCStack_rw.SetMinimum(10.)
combIsoMCStack_rw.Draw()
combIsoMC_rw.Draw("ehistsame")
combIsoData.Draw("epsame")
ROOT.gPad.SetLogy()
cRW.SaveAs("cRW.root")

