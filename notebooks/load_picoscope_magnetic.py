#load picoscope

import numpy as np
import scipy.integrate as sp
import matplotlib.pylab as plt

#data = '061615'
#shot = 1
#time_range = [20.0,80.0] #in us

def load_picoscope_magnetic(date,shot_number,time_range=[20.0,80.0],plot=True):

    #load file
    filename='picoscope_'+date+'r ('
    
    Btotave = np.zeros([25003])
    data = np.loadtxt(filename+str(shot_number)+').txt',skiprows=2,unpack=True)
    
    #timerange 
    time = data[0,:]
        
    Bxdot = data[1,:]-np.mean(data[1,0:2500])
    neginfs = np.isneginf(Bxdot)
    Bxdot[np.where(neginfs)] = -2
    posinfs = np.isinf(Bxdot)
    Bxdot[np.where(posinfs)] = 2
        
    Bydot = data[2,:]-np.mean(data[2,0:2500])
    neginfs = np.isneginf(Bydot)
    Bydot[np.where(neginfs)] = -2
    posinfs = np.isinf(Bydot)
    Bydot[np.where(posinfs)] = 2
        
    Bzdot = data[3,:]-np.mean(data[3,0:2500])
    neginfs = np.isneginf(Bzdot)
    Bzdot[np.where(neginfs)] = -2
    posinfs = np.isinf(Bzdot)
    Bzdot[np.where(posinfs)] = 2
        
    Bx =sp.cumtrapz(Bxdot,data[0,:])
    Bx = 3.162*Bx/1.192485591065652224e-03
        
    By =sp.cumtrapz(Bydot,data[0,:])
    By = 3.162*By/1.784763055992550198e-03
        
    Bz =sp.cumtrapz(Bzdot,data[0,:])
    Bz = 3.162*Bz/1.297485014039849059e-03
        
    Btot = np.sqrt(Bx**2+By**2+Bz**2)
    Btotave=Btotave+Btot
    
    if plot:
        plt.figure(1)
        plt.plot(time,data[1,:])
        plt.xlabel('Time [us]',fontsize=9)
        plt.ylabel('Bdot',fontsize=9)
        plt.figure(2)
        plt.plot(time[1:],Btot)
        plt.xlabel('Time [us]',fontsize=9)
        plt.ylabel('B-field [G]',fontsize=9)
        
    return time,Bxdot,Bydot,Bzdot,Bx,By,Bz,Btot