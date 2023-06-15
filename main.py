import tensorflow as tf


def main():
    x = tf.range(12, dtype=tf.float32)
    print(x)
    X = tf.reshape(x, (3, 4))
    print(X)


if __name__ == "__main__":
    main()