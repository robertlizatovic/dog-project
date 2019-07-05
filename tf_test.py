import tensorflow as tf

a = tf.constant(2, dtype="float32")
with tf.Session() as sess:
    print(sess.run(a))

