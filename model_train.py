import json
import numpy
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding , GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder


with open("intents.json") as file:
    data = json.load(file)

print(data)


training_sentences = []
training_labels = []
labels = []
responses = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        training_sentences.append(pattern)
        training_labels.append(intent['tag'])
    responses.append(intent['responses'])

    if intent['tag'] not in labels:
        labels.append(intent['tag'])

number_of_classes = len(labels)

print(number_of_classes)

label_encoder = LabelEncoder()
label_encoder.fit(training_labels)
training_labels = label_encoder.transform(training_labels)

vocab_size = 1000

ovv_token ="<OOV>"
enbedding_dim = 16

tokenizer = Tokenizer(num_words=vocab_size, oov_token=ovv_token)
tokenizer.fit_on_texts(training_sentences)
word_index = tokenizer.word_index
tokenizer.texts_to_sequences(training_sentences)

pad_sequences(sequences,truncating='post', maxlen=max_len)


moodel = Sequential()
moodel.add(Embedding(vocab_size,enbedding_dim, input_length=max_len))
moodel.add(GlobalAveragePoolingID())
moodel.add(Dense(16,activation="relu"))
moodel.add(Dense(16,activation="relu"))
moodel.add(Dense(number_of_classes, activation="softmax"))

moodel.compile(loss="sparse_catgorical_crossentropy", optimizer="adam",metrics=["accuracy"])

moodel.summary()