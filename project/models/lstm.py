import tflearn
from tflearn.data_utils import *

def get_rnn(model_name, maxlen=25, char_idx_len=41):
    g = tflearn.input_data([None, maxlen, char_idx)])
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
