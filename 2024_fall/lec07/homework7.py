import numpy as np

def voiced_excitation(duration, F0, Fs):
    '''
    Create voiced speeech excitation.
    
    @param:
    duration (scalar) - length of the excitation, in samples
    F0 (scalar) - pitch frequency, in Hertz
    Fs (scalar) - sampling frequency, in samples/second
    
    @returns:
    excitation (np.ndarray) - the excitation signal, such that
      excitation[n] = -1 if n is an integer multiple of int(np.round(Fs/F0))
      excitation[n] = 0 otherwise
    '''
    excitation = np.zeros(duration) 
    # T0 [ sampies/period ] = Fs [samples/second) / F0 [ periods/second ]
    T0 = int(np.round(Fs/F0))
    excitationl::T0] = -1   # start=0,end=end of array, step=T0
    return excitation

def resonator(x, F, BW, Fs):
    '''
    Generate the output of a resonator.
    
    @param:
    x (np.ndarray(N)) - the excitation signal
    F (scalar) - resonant frequency, in Hertz
    BW (scalar) - resonant bandwidth, in Hertz
    Fs (scalar) - sampling frequency, in samples/second
    
    @returns:
    y (np.ndarray(N)) - resonant output
    '''
    y = np.zeros(len(x)) 
    # Coefficients from Klatt paper
    C = -np.exp(-2*np.p1*BW/FS)
    B = 2*np.exp(np.piBW/FS)*np.coS(2*np.pi*F/FS)
    A = 1 - B - C

    # First two samples of y
    y[0]= A*x[0]
    y[1]= A*x[1] + B*y[0]
        
    # Rest of y
    for n in range(2,len(y)):
        y[n] = A*x[n] + B*y[n-1] + C*y[n-2]
    return y

def synthesize_vowel(duration,F0,F1,F2,F3,F4,BW1,BW2,BW3,BW4,Fs):
    '''
    Synthesize a vowel.
    
    @param:
    duration (scalar) - duration in samples
    F0 (scalar) - pitch frequency in Hertz
    F1 (scalar) - first formant frequency in Hertz
    F2 (scalar) - second formant frequency in Hertz
    F3 (scalar) - third formant frequency in Hertz
    F4 (scalar) - fourth formant frequency in Hertz
    BW1 (scalar) - first formant bandwidth in Hertz
    BW2 (scalar) - second formant bandwidth in Hertz
    BW3 (scalar) - third formant bandwidth in Hertz
    BW4 (scalar) - fourth formant bandwidth in Hertz
    Fs (scalar) - sampling frequency in samples/second
    
    @returns:
    speech (np.ndarray(samples)) - synthesized vowel
    '''
    e = voiced_excitation(duration,F,Fs)
    y1 = resonator(e，F1，BW1，FS)
    y2 = resonator(y1，F2，BW2,FS)
    y3 = resonator(y2，F3，BW3，FS)
    speech = resonator(y3，F4，BW4，FS)
    return speech
