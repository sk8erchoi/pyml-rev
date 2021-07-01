# TensorFlow 읽어 들이기 --- (※1)
import tensorflow as tf

# 상수 정의하기 --- (※2)
a = tf.constant(2)
b = tf.constant(3)
c = tf.constant(4)


# 연산 정의하기 --- (※3)
@tf.function
def calc1_op():
    return a + b * c

@tf.function
def calc2_op():
    return (a + b) * c


# 세션 시작하기 --- (※4)
res1 = calc1_op().numpy() # 식 평가하기
print(res1)
res2 = calc2_op().numpy() # 식 평가하기
print(res2)
