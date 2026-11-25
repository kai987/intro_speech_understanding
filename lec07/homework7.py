import numpy as np


def major_chord(f, Fs):
    '''
    Generate a one-half-second major chord, based at frequency f, with sampling frequency Fs.

    @param:
    f (scalar): frequency of the root tone, in Hertz
    Fs (scalar): sampling frequency, in samples/second

    @return:
    x (array): a one-half-second waveform containing the chord
    
    A major chord is three notes, played at the same time:
    (1) The root tone (f)
    (2) A major third, i.e., four semitones above f
    (3) A major fifth, i.e., seven semitones above f
    '''
    N = int(Fs / 2)
    n = np.arange(N)
    f2 = f * np.power(2, 4 / 12)
    f3 = f * np.power(2, 7 / 12)
    x = (np.cos(2 * np.pi * f * n / Fs)
         + np.cos(2 * np.pi * f2 * n / Fs)
         + np.cos(2 * np.pi * f3 * n / Fs))
    return x

def dft_matrix(N):
    '''
    Create a DFT transform matrix, W, of size N.
    
    @param:
    N (scalar): number of columns in the transform matrix
    
    @result:
    W (NxN array): a matrix of dtype='complex' whose (k,n)^th element is:
           W[k,n] = cos(2*np.pi*k*n/N) - j*sin(2*np.pi*k*n/N)
    '''
    n = np.arange(N)
    k = n[:, None]
    W = np.exp(-2j * np.pi * k * n / N)
    return W

def spectral_analysis(x, Fs):
    '''
    Find the three loudest frequencies in x.

    @param:
    x (array): the waveform
    Fs (scalar): sampling frequency (samples/second)

    @return:
    f1, f2, f3: The three loudest frequencies (in Hertz)
      These should be sorted so f1 < f2 < f3.
    '''
    N = len(x)
    # A real-valued waveform has mirror-image FFT peaks at negative frequencies.
    # rfft keeps only the nonnegative-frequency bins so each tone is counted once.
    magnitudes = np.abs(np.fft.rfft(x))
    freqs = np.fft.rfftfreq(N, d=1 / Fs)

    peaks = []
    for _ in range(3):
        k = np.argmax(magnitudes)
        peaks.append(freqs[k])
        magnitudes[k] = 0

    f1, f2, f3 = sorted(peaks)
    return f1, f2, f3
