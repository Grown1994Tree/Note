# Selinux模块

# Selinux模块的设置
1. 权限检验流程：先经历`DAC`系统的控制，如果允许再进行`Selinux`系统的检验

2. 模式
    - 配置路径：`/etc/selinux/config`
    - 查看模式：
        - `getenforce` 查看当前模式
        - `sestatus` 查看当前模式、策略以及原始模式，内容更加详细
    - 切换模式：使用`setenforce [0|1]`
        - `0` 设置为宽容模式
        - `1` 设置为严格模式
    *<font size=2>使用指令切换时，只能临时使用，要长期保存则需要更改配置文件</font>*


