import cv2
import numpy as np
import librosa


def solution(audio_path):
    # LOGIC: The audio for a metal banging is typically louder than the sound of banging a cardboard, so I take the mean of the amplitudes of the given sample, removing the silent parts of the audio

    # load audio data
    time_series, sampling_rate = librosa.load(audio_path, sr=None)
    # generate melspectrogram
    melspec = librosa.feature.melspectrogram(y=time_series, sr=sampling_rate, n_fft=2048, hop_length=512, win_length=512, fmax=22000)
    # convert the power values to decibel
    melspec_db = librosa.power_to_db(melspec).astype(np.float64)
    # Filter the image for the points where there is no audio (i.e. amplitude is minimum)
    melspec_db_filtered = melspec_db[melspec_db > melspec_db.min()]

    # Set up a threshold learned from the given samples
    threshold = -25

    mean = np.mean(melspec_db_filtered)

    # If the mean is greater than the threshold, then the sound is a metal banging sound, else it is a cardboard sound
    if mean > threshold:
        return 'metal'
    else:
        return 'cardboard'
