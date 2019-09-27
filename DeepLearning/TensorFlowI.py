import tensorflow as tf
# 尝试各种调整终于成功，GPU编程除了按要求进行操作之外，有个坑
# 那就是python3.7和默认anaconda装的numpy不匹配，需要先删了numpy再装最新的1.17（原来的可能是1.16）
sess = tf.Session()
a = tf.constant(1)
b = tf.constant(2)
print(sess.run(a + b))