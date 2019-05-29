#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:yiluzhang

#import tensorflow as tf
# import starting
import mnist_train
import LeNet5_train

import numpy as np
import tensorflow as tf
import seq2seq_train
import seq2seq_test
#import pattern.en as patt

# from tensorflow.python.ops.nn import dynamic_rnn
# from tensorflow.contrib.rnn.python.ops.core_rnn_cell import GRUCell, LSTMCell, MultiRNNCell
# import attention_decoder_fn
# from tensorflow.contrib.seq2seq.python.ops.seq2seq import dynamic_rnn_decoder
# from tensorflow.contrib.seq2seq.python.ops.loss import sequence_loss
# from tensorflow.contrib.lookup.lookup_ops import HashTable, KeyValueTensorInitializer
# from tensorflow.contrib.layers.python.layers import layers
# from output_projection import output_projection_layer
# from tensorflow.python.ops import variable_scope

if __name__ == '__main__':
    # print("hello tensorflow")
    # starting.tensor_session_test()
    # mnist_train.mnist_normal_train()
    # LeNet5_train.mnist_normal_train()  # 半个多小时跑完1000个迭代（loss:4->0.7)
    # starting.namespace_test()
    # starting.device_test()
    #seq2seq_train.main()
    seq2seq_test.main()









    # HashTable.lookup()
    # tf.concat
    # tf.cumsum
    # tf.one_hot
    # tf.reshape
    # tf.shape


