import numpy as np

def sine_wave(frequency, amplitude, sample_rate, duration):
    # get equal spacings for each time slice
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # get the ampliture values for a time slice
    y = amplitude * np.abs(np.sin(2 * np.pi * frequency * t))  
    return t, y
