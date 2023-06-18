import tensorflow as tf


def main():
    X = tf.random.normal((3, 4))
    print(X[-1])
    print(X[1:3])

    

if __name__ == "__main__":
    main()