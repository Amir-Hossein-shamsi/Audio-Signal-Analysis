import wave
import numpy as np
import matplotlib.pyplot as plt

print("Analysis of Music")
obj=wave.open("assets/Naser Zeynali - Nafas.wav","rb")

sample_freq = obj.getframerate()
n_sample = obj.getnframes()
num_channels = obj.getnchannels()  # Get the number of channels
signal_wave = obj.readframes(-1)

obj.close()

t_audio = n_sample / sample_freq
print("Time of audio which Uploaded : ", t_audio)
signal_array = np.frombuffer(signal_wave, dtype=np.int16)

# Calculate total number of samples (frames * channels)
total_samples = n_sample * num_channels
times = np.linspace(0, t_audio, num=total_samples)

# matplotlib setup
plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time (s)")
plt.xlim(0, t_audio)
plt.savefig("test.png")
plt.show()