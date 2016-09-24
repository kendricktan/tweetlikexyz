from __future__ import absolute_import, division, print_function

import os, sys
from six.moves import urllib

import tflearn
from tflearn.data_utils import *

path = "shakespeare_input.txt"

if not os.path.isfile(path):
    urllib.request.urlretrieve("https://raw.githubusercontent.com/tflearn/tflearn.github.io/master/resources/shakespeare_input.txt", path)

maxlen = 140

X, Y, char_idx = \
    textfile_to_semi_redundant_sequences(path, maxlen, 3, True)

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
                              checkpoint_path='model_shakespeare')

if len(sys.argv) > 1:
    m.load(sys.argv[1])

for i in range(47):
    seed = random_sequence_from_textfile(path, maxlen)
    m.fit(X, Y, validation_set=0.1, batch_size=128,
          n_epoch=1, run_id='shakespeare')
    try:
        print("-- TESTING...")
        print("-- Test with temperature of 1.0 --")
        print(m.generate(600, temperature=1.0, seq_seed=seed))
        print("-- Test with temperature of 0.5 --")
        print(m.generate(600, temperature=0.5, seq_seed=seed))
    except:
        pass

try:
    m.save('shakespeare.ckpt')
except:
    print('failed to save m')

try:
    g.save('shakespeare_regression.ckpt')
except:
    print('failed to save g')