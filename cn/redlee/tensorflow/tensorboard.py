import tensorflow as tf
hello = tf.constant('hello,tensorf')
sess = tf.Session()
print(sess.run(hello))