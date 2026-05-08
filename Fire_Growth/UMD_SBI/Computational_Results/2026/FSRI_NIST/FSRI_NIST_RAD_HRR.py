
import numpy as np
import pandas as pd

expdir = '../../../Experimental_Data/'
outdir = './Outputs/'
pltdir = './Plots/'

xvals = ['05','15']
zvals = ['30','90']
rvals = ['10','35','60','85','110','135']
tvals=[0,5,15,25,35,45,55,65,75,85,95,105,115,125,135,145,155,165,175,185]

zindex=[[60,30,15,8],[180,90,45,22]]
zinterp=[[0.5,0.5,0.5,0],[0.5,0.5,0.5,1]]

rindex=[2,7,12,17,22,27]

fdsp5cm = pd.read_csv(outdir + 'sbi_p5cm_blowing_devc.csv', skiprows=1)
fds1cm = pd.read_csv(outdir + 'sbi_1cm_blowing_devc.csv', skiprows=1)
fds2cm = pd.read_csv(outdir + 'sbi_2cm_blowing_devc.csv', skiprows=1)
fds4cm = pd.read_csv(outdir + 'sbi_4cm_blowing_devc.csv', skiprows=1)

procdata = pd.DataFrame(tvals,columns=['Time'])
columndata = np.zeros(20)
hrrdata = np.zeros(20)
for i in range(4):
   if(i==0):
      data = fdsp5cm
      file = outdir+'HF_HRR_p5cm.csv'
   elif(i==1):
      data = fds1cm
      file = outdir+'HF_HRR_1cm.csv'
   elif(i==2):
      data = fds2cm
      file = outdir+'HF_HRR_2cm.csv'
   elif(i==3):
      data = fds4cm
      file = outdir+'HF_HRR_4cm.csv'
   for j in range(len(tvals)):
      if (j>0):
         mask = (data['Time']>=tvals[j]-5) & (data['Time']<=tvals[j]+5.1)
         data_cull = data.loc[mask]
         data_mean = data_cull.mean()
         hrrdata[j] = data_mean['DC HRR']
   procdata['HRR']=hrrdata
   for k in range(len(xvals)):
      for l in range(len(zvals)):
         name = 'HFG_x'+xvals[k]+'_y'+zvals[l]
         for j in range(len(tvals)):
            if (j>0):
               mask = (data['Time']>=tvals[j]-5) & (data['Time']<=tvals[j]+5.1)
               data_cull = data.loc[mask]
               data_mean = data_cull.mean()
               loc1 = 'GHF_x'+xvals[k]+'-'+str(zindex[l][i])
               loc2 = 'GHF_x'+xvals[k]+'-'+str(zindex[l][i]+1)
               columndata[j] = data_mean[loc1]+(data_mean[loc2]-data_mean[loc1])*zinterp[l][i]
         procdata[name]=columndata
   for k in range(len(rvals)):
      name = 'HFG_y'+rvals[k]
      for j in range(len(tvals)):
         if (j>0):
            mask = (data['Time']>=tvals[j]-5) & (data['Time']<=tvals[j]+5.1)
            data_cull = data.loc[mask]
            data_mean = data_cull.mean()
            loc1 = 'CORNER RHF-'+str(rindex[k])
            columndata[j] = data_mean[loc1]
      procdata[name]=columndata
   procdata.to_csv(file,index=False)




