import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

examples = ['brahms', 'choice', 'fishin', 'humpback', 'libri1', 'libri2', 'libri3',
            'nutcracker', 'pistachio', 'robin', 'sweetwaltz', 'trumpet', 'vibeace']
data = []
for s in examples:
    data.append(librosa.util.example(s))

