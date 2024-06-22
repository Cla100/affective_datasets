#tentando processar os dados para ver os plots de valência e ECG 
import os
import numpy as np
import pickle

# Setup
# Navigate to the case_dataset root directory
# NOTE: please set this up for your case e.g.
# os.chdir('/home/<USER>/Documents/case_Dataset') -> altera o diretório para esse 
os.chdir('C:/Users/Clarissa Alves/Documents/Idor/dataset/case_dataset')

# verbose mode on (True) or off (False)
verbose = True

# Loading and Extracting data

# looping through all subjects
for subno in range(1, 31):
    tmp_daqfilename = f'./data/raw/physiological/sub{subno}_DAQ.txt'
    tmp_jsfilename = f'./data/raw/annotations/sub{subno}_joystick.txt'
    
    tmp_daqdata = np.loadtxt(tmp_daqfilename)
    tmp_jsdata = np.loadtxt(tmp_jsfilename)
    
    nrow_daqdata, ncol_daqdata = tmp_daqdata.shape
    nrow_jsdata, ncol_jsdata = tmp_jsdata.shape
    
    # verbose quality check
    if verbose:
        print(f'Sub {subno} nrows in loaded rawdata for daqdata = {nrow_daqdata} and jsdata = {nrow_jsdata}')
    
    # DAQ data
    # extracting data
    daqtime = tmp_daqdata[:, 0]
    ecg = tmp_daqdata[:, 1]
    bvp = tmp_daqdata[:, 2]
    gsr = tmp_daqdata[:, 3]
    rsp = tmp_daqdata[:, 4]
    skt = tmp_daqdata[:, 5]
    emg_zygo = tmp_daqdata[:, 6]
    emg_coru = tmp_daqdata[:, 7]
    emg_trap = tmp_daqdata[:, 8]
    
    # Joystick data
    # extracting data
    jstime = tmp_jsdata[:, 0]
    val = tmp_jsdata[:, 1]
    aro = tmp_jsdata[:, 2]
    
    # Saving data
    # list of variables to save in per subject pkl file
    data_to_save = {
        'daqtime': daqtime, 'ecg': ecg, 'bvp': bvp, 'gsr': gsr, 'rsp': rsp,
        'skt': skt, 'emg_zygo': emg_zygo, 'emg_coru': emg_coru, 'emg_trap': emg_trap,
        'jstime': jstime, 'val': val, 'aro': aro
    }
    
    # saving data to a file
    tmp_outfilename = f'./data/initial/sub_{subno}.pkl'
    with open(tmp_outfilename, 'wb') as outfile:
        pickle.dump(data_to_save, outfile)
 
#funcionou -> dps ver os passos certinhos 

'''
Output: subject-wise mat files containing both annotations and
 physiological data saved under data/intial sub-directory.

'''