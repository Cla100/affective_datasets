#processando porém sem a parte dos vídeos 
import os
import pickle
import numpy as np
import pandas as pd

# Assuming f_labelData function is defined here or imported
def f_labelData(time_data, subno):
    # Implement your labeling logic here
    # As we don't have the exact labeling data, we'll create dummy labels
    # This is just an example; adjust it according to your actual logic
    labels = np.zeros(len(time_data))
    video_length = 5000  # Dummy video length in ms
    num_videos = 5  # Dummy number of videos
    for i in range(num_videos):
        start_idx = i * (len(time_data) // num_videos)
        end_idx = (i + 1) * (len(time_data) // num_videos)
        labels[start_idx:end_idx] = i + 1  # Label videos from 1 to num_videos
    return labels

# Setup
os.chdir('C:/Users/Clarissa Alves/Documents/Idor/dataset/case_dataset')

# Verbose mode
verbose = True

# Function for rounding to 3 decimal places
round3func = np.vectorize(lambda x: round(x, 3))

# Loop through all subjects
for subno in range(1, 31):
    # Load data for the subject from .pkl file
    with open(f'./data/initial/sub_{subno}.pkl', 'rb') as file:
        indata = pickle.load(file)

    if verbose:
        print(f'Sub {subno} nrows in initial pkl files for daqdata = {len(indata["daqtime"])} and jsdata = {len(indata["jstime"])}')

    # Transforming Data
    # DAQ data
    tmp_daqtime = indata['daqtime'] * 1000 #transformou em milisegundos 
    tmp_ecg = ((indata['ecg'] - 2.8) / 50) * 1000 #transgformou em mv
    tmp_bvp = (58.962 * indata['bvp']) - 115.09
    tmp_gsr = (24 * indata['gsr']) - 49.2
    tmp_rsp = (58.923 * indata['rsp']) - 115.01
    tmp_skt = (21.341 * indata['skt']) - 32.085
    tmp_zygo = ((indata['emg_zygo'] - 2.0) / 4000) * 1000000
    tmp_coru = ((indata['emg_coru'] - 2.0) / 4000) * 1000000
    tmp_trap = ((indata['emg_trap'] - 2.0) / 4000) * 1000000

    # Joystick data
    tmp_jstime = indata['jstime'] * 1000
    tmp_val = 0.5 + 9 * (indata['val'] + 26225) / 52450
    tmp_aro = 0.5 + 9 * (indata['aro'] + 26225) / 52450

    # Labeling the data
    # Using dummy labels here as we don't have the actual vidsDuration and seqsOrder
    csub_daqlabels = f_labelData(tmp_daqtime, subno)

    csub_daqtable = pd.DataFrame({
        'daqtime': tmp_daqtime.flatten(), 'ecg': tmp_ecg.flatten(), 'bvp': tmp_bvp.flatten(), 'gsr': tmp_gsr.flatten(),
        'rsp': tmp_rsp.flatten(), 'skt': tmp_skt.flatten(), 'emg_zygo': tmp_zygo.flatten(),
        'emg_coru': tmp_coru.flatten(), 'emg_trap': tmp_trap.flatten(), 'video': csub_daqlabels.flatten()
    })

    # Trimming csub_daqtable
    csub_daqtable = csub_daqtable[csub_daqtable['video'] != 0]

    if verbose:
        print(f'Sub {subno} nrows for trimmed csub_daqtable= {len(csub_daqtable)}')

    # Joystick data labeling
    csub_jslabels = f_labelData(tmp_jstime, subno)

    csub_jstable = pd.DataFrame({
        'jstime': tmp_jstime.flatten(), 'valence': tmp_val.flatten(), 'arousal': tmp_aro.flatten(), 'video': csub_jslabels.flatten()
    })

    # Trimming csub_jstable
    csub_jstable = csub_jstable[csub_jstable['video'] != 0]

    if verbose:
        print(f'Sub {subno} nrows for trimmed csub_jstable= {len(csub_jstable)}')

    # Saving data for the csub
    # DAQ data
    mod_csub_daqDT = csub_daqtable.apply(round3func)
    mod_csub_daqDT.to_csv(f'./data/non-interpolated/physiological/sub_{subno}.csv', index=False)

    # Annotation data
    mod_csub_jsDT = csub_jstable.apply(round3func)
    mod_csub_jsDT.to_csv(f'./data/non-interpolated/annotations/sub_{subno}.csv', index=False)

'''
No final vou ter os dados processados como 'non_interpolated' contendo os dados fisiológicos e os dados
do joystick -> vou tentar fazer um plot com esses agr. 
Cada sujeito tem o seu CSV correspondente
ao dados fisiológicos e de anotações do joystick 

'''