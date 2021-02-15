import numpy as np 
import matplotlib.pyplot as plt 
from scipy.io.wavfile import write 

sampling_freq = 44100

def tone_synthesizer(freq, duration, amplitude=2**15-1): 
    time_axis = np.linspace(0, duration, int(duration * sampling_freq)) 
    signal = amplitude * np.sin(2 * np.pi * freq * time_axis) 
    return signal.astype(np.int16) 

tone_map = {
    "A": 440,
    "A#": 466,
    "B": 494,
    "C": 523,
    "C#": 554,
    "D": 587,
    "D#": 622,
    "E": 659,
    "F": 698,
    "F#": 740,
    "G": 784,
    "G#": 831
}

file_tone_single = 'generated_tone_single.wav' 
synthesized_tone = tone_synthesizer(tone_map['F'], 3) 
write(file_tone_single, sampling_freq, synthesized_tone)

tone_sequence = [('G', 0.4), ('D', 0.5), ('F', 0.3), ('C', 0.6), ('A', 0.4)] 

signal = np.array([], dtype=np.int16)

for tone_name, duration in tone_sequence: 
    freq = tone_map[tone_name] 
    synthesized_tone = tone_synthesizer(freq, duration)
    signal = np.append(signal, synthesized_tone, axis=0)  

file_tone_sequence = 'generated_tone_sequence.wav' 
write(file_tone_sequence, sampling_freq, signal)