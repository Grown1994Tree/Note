# wargame汇总


# 一、level8-level9:
bandit8
cvX2JJa4CFALtqS87jk27qwqGhBM9plV

A:`sort -d data.txt  | uniq -u`

![avatar](/wargame/bandit8.png)

# 二、level9-level10:
bandit9
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

A:`strings  data.txt  | grep '='`  <!-- strings 和  cat  差异   -->
![avatar](/wargame/bandit9.png)

# 三、level10-level11:
bandit10
truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

A: 使用解密工具进行解密

# 四、level11-level12:
bandit11
IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

A:cat data.txt | tr  'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'  'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
<!--tr sed-->


# 五、level12-level13
bandit12
5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

A:
难点：使用xxd -r 把十六进制的文件改为十进制，并判断是否为压缩包
知识点：xxd、file 、gzip -d 解压



# 六、level13-level14
bandit13
8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

A:ssh -i sshkey.private bandit14@localhost 
知识点：ssh使用私钥连接、连接本地主机

# 七、level14-level15
bandit14
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

A：telnet localhost 30000
知识点：telnet

# 八、level15-level16
bandit15
BfMYroe26WYalil77FoDi9qh59eK5xNr

A:openssl s_client -crlf -connect  localhost:30001 -servername localhost
知识点：如何使用openssl


# 九、level16-level17
bandit16
cluFn7wTiGryunymYOu4RcffSxQluehd

A:
1、使用nmap扫描出开放端口
2、使用openssl对端口进行连接后上传数据。
3、最后获得证书，并保存在本地。要记得修改证书权限

### 十、level17-level18
bandit17
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----



### 11 level18-level19
bandit18
kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
a:ssh bandit18@bandit.labs.overthewire.org -p 2220 'bash'
知识点：使用ssh登录时，在命令行后面加上`bash`命令可以越过`.bashrc`文件

### 12 level19-level20
bandit19
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x

a:
![avatar](/wargame/bandit19.png)
知识点：setuid、bandit20-do的使用方法、特殊权限s


### 12 level20-level21
bandit20
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
a:  使用该命令建立服务 `echo 'GbKksEFF4yrVs6il55v6gwY5aVje5f0j' | nc  -l localhost -p  61200 &`

知识点：
1. 命令`nc`的使用方法
2. 命令行中，`&`是什么意思


### 13 level21-level22
bandit21
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

a:
1. 找到关于bandit22的任务计划,查看执行语句
2. 由于该执行语句读取密码到某一个文件里面，所以需要读取该文件

知识点：
1. 直接使用语句读取,不需要查看是否存在，密码比较重要可能设置不可见


### 14 level22-level23
bandit22
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

知识点：
1. 设置变量，把任务里面的语句进行执行
2. cut


### 15 level23-level24
bandit23
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
A：

知识点：
1. shell脚本要设置为可执行


### 15 level24-level25
bandit24

UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

### 15 level24-level25
bandit25

1   for i in $( seq 2 9999)
  2  do                                                                                               
  3          firstValue=0000000${i};
  4          level_pass="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ "
  5          pincode=${firstValue:0-4};
  6          lastValue=$level_pass$pincode
  7          $(echo -e "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ111Z" | nc localhost 30002 )
  8  done             
  9                                                          











































