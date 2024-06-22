import os
import pandas as pd
import matplotlib.pyplot as plt


# Função para plotar dados fisiológicos com opção de zoom
def plot_physiological_data(subject_data, subject_id, zoom_ecg=None, zoom_bvp=None, apply_zoom=True):
    time_physio = subject_data['daqtime']  # originalmente em milisegundos
    ecg = subject_data['ecg']
    bvp = subject_data['bvp']
    
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    plt.plot(time_physio, ecg, label='ECG')
    plt.xlabel('Tempo (ms)')
    plt.ylabel('Valor (mV)')
    plt.title(f'Dados ECG do Sujeito {subject_id}')
    plt.legend()
    plt.tight_layout()
    plt.grid(True)

    if apply_zoom and zoom_ecg:
        plt.xlim(zoom_ecg)  # Zoom no eixo x do ECG
        plt.title(f'Dados ECG (zoom) do Sujeito {subject_id}')

    plt.subplot(2, 1, 2)
    plt.plot(time_physio, bvp, label='BVP')
    plt.xlabel('Tempo (ms)')
    plt.ylabel('Valor')
    plt.title(f'Dados BVP do Sujeito {subject_id}')
    plt.legend()
    plt.grid(True)
    
    if apply_zoom and zoom_bvp:
        plt.xlim(zoom_bvp)  # Zoom no eixo x do BVP
        plt.title(f'Dados BVP (zoom) do Sujeito {subject_id}')

    plt.tight_layout()
    plt.show()

# Função para plotar dados do joystick com o mesmo intervalo de zoom
def plot_joystick_data(subject_data, subject_id, zoom=None, apply_zoom=True):
    time_joystick = subject_data['jstime']
    valence = subject_data['valence']
    arousal = subject_data['arousal']

    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    plt.scatter(time_joystick, valence, label='Valência')
    plt.scatter(time_joystick, arousal, label='Arousal')
    plt.xlabel('Tempo (ms)')
    plt.ylabel('Valor')
    plt.title(f'Dados do Joystick do Sujeito {subject_id}')
    plt.legend()
    plt.grid(True)
    
    if apply_zoom and zoom:
        plt.xlim(zoom)  # Aplica o mesmo zoom definido para ECG e BVP
        plt.title(f'Dados do Joystick (Zoom) do Sujeito {subject_id}')

    plt.tight_layout()
    plt.show()

    plt.show()

# Diretórios contendo os dados
physiological_dir = 'C:/Users/Clarissa Alves/Documents/Idor/dataset/case_dataset/data/non-interpolated/physiological'
annotations_dir = 'C:/Users/Clarissa Alves/Documents/Idor/dataset/case_dataset/data/non-interpolated/annotations'

# Iterar sobre cada sujeito (assumindo que há 30 sujeitos)
num_subjects = 30
for subject_id in range(1, num_subjects + 1):
    # Caminhos dos arquivos CSV para o sujeito atual
    physiological_file = os.path.join(physiological_dir, f'sub_{subject_id}.csv')
    annotations_file = os.path.join(annotations_dir, f'sub_{subject_id}.csv')

    # Carregar dados fisiológicos
    physiological_data = pd.read_csv(physiological_file)

    # Carregar dados do joystick (annotations)
    joystick_data = pd.read_csv(annotations_file)

    # Determinar o zoom para ECG e BVP 
    zoom_interval = (0000, 2000)

    # Plotar dados fisiológicos com opção de zoom e sem zoom
    plot_physiological_data(physiological_data, subject_id, zoom_ecg=zoom_interval, zoom_bvp=zoom_interval, apply_zoom=True)
    plot_physiological_data(physiological_data, subject_id, apply_zoom=False)  # Sem zoom

    # Plotar dados do joystick com o mesmo intervalo de zoom e sem zoom
    plot_joystick_data(joystick_data, subject_id, zoom=zoom_interval, apply_zoom=True)
    plot_joystick_data(joystick_data, subject_id, apply_zoom=False)  # Sem zoom
