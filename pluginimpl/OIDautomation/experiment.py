import tensorflow as tf

a = tf.constant(5)
b= tf.constant(6)

c = a *b

with tf.Session() as sess:
    print(sess.run(c))

