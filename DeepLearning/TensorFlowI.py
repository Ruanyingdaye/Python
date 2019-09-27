import tensorflow as tf
# 尝试各种调整终于成功，GPU编程除了按要求进行操作之外，有个坑
# 那就是python3.7和默认anaconda装的numpy不匹配，需要先删了numpy再装最新的1.17（原来的可能是1.16）
# 第一个代码尝试
sess = tf.Session()
a = tf.constant(1)
b = tf.constant(2)
print(sess.run(a + b))

#检测可用设备为
def is_gpu_available(cuda_only=True):
  """
  code from https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/platform/test.py
  Returns whether TensorFlow can access a GPU.
  Args:
    cuda_only: limit the search to CUDA gpus.
  Returns:
    True iff a gpu device of the requested kind is available.
  """
  from tensorflow.python.client import device_lib as _device_lib

  if cuda_only:
    return any((x.device_type == 'GPU')
               for x in _device_lib.list_local_devices())

  else:
    return any((x.device_type == 'GPU' or x.device_type == 'SYCL')
               for x in _device_lib.list_local_devices())