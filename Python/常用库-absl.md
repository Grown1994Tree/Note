### 一、作用
        用来定义、读取参数


### 二、安装

```shell
    pip install absl-py
```

###  三、引入

```python
    from absl import flags,app
```

### 四、简单例子

```python
    # test.py
    from absl import flags,app
    flags.DEFINE_integer("t",1,"参数说明")
    FLAGS=flags.FLAGS # 通过FLAGS进行调用

    def main(_):
        print(FLAGS.t)

    if __name__ == "__main__":
        app.run(main) # main一定要带参数，参数如果不使用可以_代替
```

### 五、使用
```python
    python test.py --t=5
```