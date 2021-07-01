import tensorflow.compat.v1 as tf

tf.compat.v1.disable_eager_execution()

# 데이터 플로우 그래프 구축하기 --- (※1)
a = tf.constant(20, name="a")
b = tf.constant(30, name="b")
mul_op = a * b

# 세션 생성하기 --- (※2)
sess = tf.Session()

# TensorBoard 사용하기 --- (※3)
tw = tf.summary.FileWriter("log_dir", graph=sess.graph)

# 세션 실행하기  --- (※4)
print(sess.run(mul_op))