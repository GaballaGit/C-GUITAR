import pyaudio as pa
import numpy as np

CHUNK = 1024
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100

p = pa.PyAudio()

stream = p.open
(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    frames_per_buffer = CHUNK
)
print recording


def record():
    print(pa.get_portaudio_version())

