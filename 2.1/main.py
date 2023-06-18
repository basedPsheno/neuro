import tensorflow as tf


def main():
    X = tf.random.normal((3, 4))
    X_var = tf.Variable(X)
    X_var[1, 2].assign(9)
    print(X_var)

    
if __name__ == "__main__":
    main()