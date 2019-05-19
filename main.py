#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:yiluzhang

#import tensorflow as tf
import starting
import mnist_train
import LeNet5_train

if __name__ == '__main__':
    # print("hello tensorflow")
    # starting.tensor_session_test()
    # mnist_train.mnist_normal_train()
    # LeNet5_train.mnist_normal_train()  # 半个多小时跑完1000个迭代（loss:4->0.7)
    # starting.namespace_test()
    starting.device_test()

