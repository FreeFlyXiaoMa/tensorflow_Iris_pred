from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import urllib

import numpy as np
import tensorflow as tf

IRIS_TRAINING = "iris_training.csv"
IRIS_TEST = "iris_test.csv"


#IRIS_TRAINING_URL="http://download.tensorflow.org/data/iris_training.csv"

#IRIS_TEST_URL="http://download.tensorflow.org/data/iris_test.csv"

#raw=urllib.urlopen(IRIS_TRAINING_URL).read()
#with open(IRIS_TRAINING,'w') as f:
#    f.write(raw)

#raw=urllib.urlopen(IRIS_TEST_URL).read()
#with open(IRIS_TEST,'w') as f:
#    f.write(raw)

training_set=tf.contrib.learn.datasets.base.load_csv_with_header(
    filename=IRIS_TRAINING,
    target_dtype=np.int,
    features_dtype=np.float32
)
test_set=tf.contrib.learn.datasets.base.load_csv_with_header(
    filename=IRIS_TEST,
    target_dtype=np.int,
    features_dtype=np.float32
)

#特征列，维度为4
feature_columns=[tf.contrib.layers.real_valued_column("",dimension=4)]

#构建分类器
classifier=tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                          hidden_units=[10,20,10],
                                          n_classes=3,
                                          model_dir="/tmp/iris_model")
#训练模型
classifier.fit(x=training_set.data,
               y=training_set.target,
               steps=2000)
accuracy_score=classifier.evaluate(x=test_set.data,
                                   y=test_set.target)['accuracy']
print('Accuracy:{0:f}'.format(accuracy_score))

#对两个样本特征进行分类
new_samples=np.array([
    [6.4,3.2,4.5,1.5],[5.8,3.1,5.0,1.7]
],dtype=float)
y=list(classifier.predict(new_samples,as_iterable=True))
print('Predictions:{}'.format(str(y)))










