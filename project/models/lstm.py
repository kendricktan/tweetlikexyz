import os, sys
import tflearn

from tflearn.data_utils import *
from six.moves import urllib

# Checks for shakespeare inputs
shakespeare_path = os.path.join('models', 'shakespeare_input.txt')
if not os.path.isfile(shakespeare_path):
    urllib.request.urlretrieve("https://raw.githubusercontent.com/tflearn/tflearn.github.io/master/resources/shakespeare_input.txt", shakespeare_path)

def get_rnn(model_name, char_idx=None, maxlen=140):
    if char_idx is None:
        if 'shakespeare' in model_name:
            _, _, char_idx = textfile_to_semi_redundant_sequences(shakespeare_path, maxlen, 3, True)


    g = tflearn.input_data([None, maxlen, len(char_idx)])
    g = tflearn.lstm(g, 512, return_seq=True)
    g = tflearn.dropout(g, 0.5)
    g = tflearn.lstm(g, 512, return_seq=True)
    g = tflearn.dropout(g, 0.5)
    g = tflearn.lstm(g, 512)
    g = tflearn.dropout(g, 0.5)
    g = tflearn.fully_connected(g, len(char_idx), activation='softmax')
    g = tflearn.regression(g, optimizer='adam', loss='categorical_crossentropy',
                        learning_rate=0.001)

    m = tflearn.SequenceGenerator(g, dictionary=char_idx,
                                seq_maxlen=maxlen,
                                clip_gradients=5.0,
                                checkpoint_path=model_name)

    return m
