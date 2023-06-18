import tensorflow as tf


def main():
    x = tf.range(12, dtype=tf.float32)
    X = tf.reshape(x, (3, 4))
    X_var = tf.Variable(X)
    X_var[:2, :].assign(tf.ones(X_var[:2,:].shape, dtype=tf.float32) * 12)
    print(X_var)

    
if __name__ == "__main__":
    main()