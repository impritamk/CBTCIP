import sounddevice
from scipy.io.wavfile import write

#Asking user the time limit
i=int(input("Enter how many second you want to record the sound(in sec):"))
fs=44100
second=i

#Recording start
print("Sound recording started...")
record_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
sounddevice.wait()
write("Output.wav", fs,record_voice)

#Recording finished
print("Done")