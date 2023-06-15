import tensorflow as tf


def main():
    x = tf.range(12, dtype=tf.float32)
    print(x.shape)


if __name__ == "__main__":
    main()