#### use cvmfs for root ####                                                                                                      
export CMS_PATH=/cvmfs/cms.cern.ch
source $CMS_PATH/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc900
#export SCRAM_ARCH=slc7_amd64_gcc820
#export SCRAM_ARCH=slc7_amd64_gcc700
export cmsswrel='cmssw/CMSSW_11_2_5'
#export cmsswrel='cmssw/CMSSW_10_6_4'
#export cmsswrel='cmssw/CMSSW_10_2_6'




cd /cvmfs/cms.cern.ch/$SCRAM_ARCH/cms/$cmsswrel/src
echo "@@@@ SCRAM_ARCH = "$SCRAM_ARCH
echo "@@@@ cmsswrel = "$cmsswrel
echo "@@@@ scram..."
eval `scramv1 runtime -sh`
cd -
source /cvmfs/cms.cern.ch/$SCRAM_ARCH/cms/$cmsswrel/external/$SCRAM_ARCH/bin/thisroot.sh
