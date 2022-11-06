# shell编程入门

### 一、shell编程
1. 什么是shell？
shell是命令行解释器，在linux中使用的指令都需要通过shell进行编译后，再提供给操作系统内核执行。
2. 什么是shell编程？
   - 一种可以大批量执行指令的脚本，通常脚本会有 `.sh` 后缀 
   - 使用 `sh` 指令或者修改文件为可执行文件（直接调用）来进行调用
### 二、 变量
1. 系统变量（全局变量）
   - 通过 `env` 指令可以查看当前用户的系统变量。
   - 通过 `set` 指令可以查看所有系统变量，包括当前用户。
   - 通常使用`$`+`变量名`（大写）获取系统变量
   - `${变量名}`方法。
     - 更容易确定变量名范围，方便作一些拼接。
     ```
         PATHNAME=/home/shellDemo/
         echo ${PATHNAME}SJY
     ```
     ![avatar](/Linux/shell编程/拼接.png)
     - 对变量值的剪切
     ```
      PATHNAME=/home/home/shellDemo/
      #echo ${PATHNAME}SJY
      echo ${PATHNAME#/*}  #去除掉最左边的第一个斜杠及左边的内容
      echo ${PATHNAME##/*}SJY #去除掉最右边的第一个斜杠及左边的内容
      echo ${PATHNAME:0:6}  #剪切，从第0位开始剪切6位，并返回剪切的值
      echo ${PATHNAME/home/come} #替换第一个字符
      echo ${PATHNAME//home/come} #替换所有字符
     ```
     ![avatar](/Linux/shell编程/剪切.png)
   - 如果要针对所有用户设置环境变量，则设置修改 `etc/profile` 文件；如果只针对特定用户，则设置修改 `etc/bash_profile`文件。
      - 在这两个文件里面修改后，需要使用 `.` 或 `source` 指令使shell重新读取对应的文件，避免重新注销和登陆
      - 使用该方法设置的变量会长期存在
   - 建立临时变量。
      - `export [变量名]=[变量值]` 定义变量并赋值。
      - `export [变量名]` 定义变量
      - `export -p` 查看所有系统变量
2. 自定义变量
   - 设置自定义变量 `变量名=变量值`,调用或使用变量时要在变量名称面前使用 `$` *<font size=2>=左右两侧不能有空格</font>*
   ```
      bl="hello world"
      echo $bl
    ```
    ![avatar](/Linux/shell编程/自定义变量.png)
   - 使用 `unset [变量名]` 销毁变量名。*<font size=2>变量名前面不能加`$`</font>*
   ```
      bl="hello world"
      echo $bl
      unset bl
      echo $bl
   ```
   ![avatar](/Linux/shell编程/自定义变量unset.png)
   - 在变量名前面添加 `readonly` 关键字，可以避免变量被修改，也无法被撤销。*<font size=2>撤销时会跳出警告</font>*
   ```
      readonly BL="hello world"
      echo $BL
      unset BL
      echo $BL
   ```
   ![avatar](/Linux/shell编程/自定义变量readonly.png)
3. 返回指令值给变量
    通常使用 \`执行语句\` 和 `$(执行语句)` 来把指令的返回值赋予变量
    ```
      LIST=`ls /home`
      echo $LIST
      LIST1=$(ls /home|grep l)
      echo $LIST1
    ```
    ![avatar](/Linux/shell编程/返回指令值.png)

4. 注释
   - 单行注释 `#`
   - 多行注释 `<<! [ 内容 ] !`
   ```
      LIST=`ls /home`
      echo $LIST
      <<!
         LIST1=$(ls /home|grep l)
         echo $LIST1
      !
   ```
   ![avatar](/Linux/shell编程/注释.png)
5. 位置参数变量。传递参数给脚本里面的占位符。
   - 使用方法。`[脚本] [参数...]`
   - 主要占位符
     - `$0`和`basename` 获取脚本名
     - `$N`(N代表大于1的整数)  获取第几个参数，`$1` 为脚本后的第一个参数，超过9时需要使用`{}`
     - `$#` 参数个数
     - `$*` 获取所有参数（把所有参数当作一个整体）
     - `$@` 获取所有参数（以数组的形似组合参数）
     *<font size=2>以上几个参数也可以函数中使用</font>*
   ```
      echo $[$1+$2]
   ```
   ![avatar](/Linux/shell编程/位置参数.png)

6. 预定义变量
   - $$  获取当前进程的ID
   - $!  后台运行的最后一个进程的进程号
   - $?  判断最后一个进程是否执行正确，正确返回0，错误返回非0
   ```
       echo $$
      sh /home/shellDemo/place.sh 50 100
      echo $?
      echo $!
   ```
   ![avatar](/Linux/shell编程/预定义变量.png)

7. 运算符。三种方式，推荐第一种。
   - `$[公式]` 
   ```
       RESULT=$[5+3]
       echo $RESULT

       RESULT1=$[(5+3)*5]
       echo $RESULT1
   ```
    ![avatar](/Linux/shell编程/运算符1.png)
   
   - `$((公式))`
   ```
      RESULT2=$((5+3))
      echo $RESULT2

      RESULT3=$(((5+3)*5))
      echo $RESULT3

   ```
   ![avatar](/Linux/shell编程/运算符1.png)

   - `expr 公式`
     - 在每个特殊字符面前都要加上`\`
     - 每一个项都要加上`空格`
     - 整个运算都要放在反引号里面
   ```
       RESULT4= expr \( 5 + 3 \) \* 5
       echo $RESULT4
   ```
   ![avatar](/Linux/shell编程/运算符2.png)

### 三、条件判断与流程控制
1. 条件判断
   - 非空返回 `true`;空返回 `false`
   - 通过 `-a` 作为 `并且`，通过 `-o` 作为 `或者`来完成多个判断语句的拼接。
   ```
      RES=$1
      if [ $RES -ge 60 -a $RES -lt 80 ];
      then
            echo '及格'
      elif [ $RES -ge 80 ];
      then
            echo '优'
      else
            echo '不及格'
      fi
   ```
   - 通过 `&&` 作为 `并且`，通过 `||` 作为 `或者`来完成多个判断语句结果的拼接。
   ```
      RES=$1
      if [ $RES -ge 60 ] && [ $RES -lt 80 ];
      then
            echo '及格'
      elif [ $RES -ge 80 ];
      then
            echo '优'
      else
            echo '不及格'
      fi
   ```
   -  通过`-z`来判断字符串是否为空，通过`-n`来判断字符串是否不为空
2. `if`。条件为真时才进入 `then` 代码块
   - 语法
     - `if [ condition ]; then 代码块 fi` *<font size=2>如果then放置在同一行需要在中括号后加`;`;所以建议无论换行还是不换行都要加`;`</font>*  
     ```
      RES=$1
      if [ $RES -gt 60 ];then
           echo '及格'
      fi
     ```
     ![avatar](/Linux/shell编程/判断符.png)
     - `if [ condition ]; then 代码块 else 代码块 fi`
     ```
         RES=$1
         if [ $RES ]
         then
               echo 'RES不为空'
         else
               echo 'RES为空'
         fi
     ```
     ![avatar](/Linux/shell编程/判断.png)


     - `if [ condition ] then 代码块 elif then 代码块 fi` *有else*
     ```
         RES=$1
         if [ $RES -ge 60 -a $RES -lt 80 ]
         then
               echo '及格'
         elif [ $RES -ge 80 ]
         then
               echo '优'
         else
               echo '不及格'
         fi
     ```  
     ![avatar](/Linux/shell编程/判断2.png)

3. case流程控制,详细见下列案例。
   ```
      RES=$1
      case $RES in
         100)
            echo "满分"
         ;;
         *)
            echo "没有满分"
         ;;
      esac
   ```
    ![avatar](/Linux/shell编程/case.png)

4. for语句。
   - 主要两种结构。for in结构和数字结构
   - 数字结构
   ```
     S=$1
     RES=$2
     for((i=$S;i<$RES;i++));
     do
          echo $[$i*10]  
     done
   ```
   *<font size=2>在运算符里面，使用`$i` 和 `i` 效果是一样的，但推荐使用`$i`类型</font>*
     - 使用 `awk` 指令 `awk 'BEGIN{for(i=1; i<=10; i++) print i}'`
     ![avatar](/Linux/shell编程/for.png)
   - for in 结构
      - 使用指令生成要被便利的数组（姑且算是数组），再通过`for in`结构进行遍历。*<font size=2>通常是使用`$(命令行)`</font>*
      ```
          for i in $(seq 1 10)
          do
               echo $[$i*10]
          done
      ```          
      ![avatar](/Linux/shell编程/forin1.png)

      - 使用 `{1..10}` 生成要被遍历的数组。
      ```
         for i in {1..5}
         do
            echo $[$i*10]
         done
      ```
      *<font size=2>暂时只限制于数字数组</font>*
      ![avatar](/Linux/shell编程/forin2.png)
      
      - 直接使用数组
      ```
         LIST=(1 4 11)
         for i in ${LIST[*]}
         do
               echo $[$i*10]
         done
      ```
      ![avatar](/Linux/shell编程/forin3.png)

      - 使用反引号生成数组
      ```
         for i in `ls`
         do
            echo $i
         done
      ```
      ![avatar](/Linux/shell编程/forin4.png)

5. while语句
      ```RES=$1
         I=1
         while [ $I -lt $RES  ]
         do
               echo $I
               I=$[$I+1]
         done         
      ```
      ![avatar](/Linux/shell编程/while.png)
      *<font size=2>如果变量被赋值时，则不需要加上`$`,在调用时才加上`$` </font>*
      *<font size=2>也可以使用`(())`体换`[]`来对条件表达式进行运算</font>*
      *<font size=2>使用`let`关键字可以使用变量累加</font>*
      ```
         #!/bin/bash
         int=1
         while(( $int<=5 ))
         do
            echo $int
            let "int++"
         done
      ```
6. until语句
   跟`while`语句相反，`until`语句为条件为真时执行
   ```
      #!/bin/bash
      int=1
      until(( $int>5 ))
      do
         echo $int
         let "int++"
      done
   ```

6. 关系运算符
![avatar](/Linux/shell编程/关系运算符.png)
```
#!/bin/bash

a=10
b=20

if [ $a -eq $b ]
then
   echo "$a -eq $b : a == b"
else
   echo "$a -eq $b: a != b"
fi
```

7. 文件测试运算符
![avatar](/Linux/shell编程/文件测试运算符.png)

### 五、read指令
   - 主要语法: `read [选项] [变量][变量][变量][变量]....`
   - 等待用户输入值后才继续执行下一步操作。`[变量]`作为下一步操作的值
   - 写入时不能换行
   - 选项：
   ![avatar](/Linux/shell编程/read选项.png)
   - 实例：
   ```
      read -n 4 -sp '请输入密码>' password
      printf "\n"
      echo ‘第一次输入密码’
      read -n 4 -sp '请再次输入密码>' checkpassword
      printf "\n"

      if [ $password = $checkpassword ];
      then
            echo "密码输入正确"
      else
            echo "密码输入错误"
      fi
   ```
   ![avatar](/Linux/shell编程/read实例.png)

### 六、函数
1. 系统函数
   - `basename` 返回文件部分
   - `dirname` 返回路径部分
   - 实例：
   ```
      RES=`ls`
      for i in $RES
      do
            j=$(pwd $i)
            p=${j}/$i
            echo $p
            echo `dirname $p`
            echo `basename $p`
      done
   ```
   ![avatar](/Linux/shell编程/自定义函数.png)

2. 自定义函数
   - 结构:
      ```
         function name(){
            statements
            [return value]
         }
      ```
      - 可以不添加前缀`function`
      ```
         name(){
            statements
            [return value]
         }
      ```
      *<font size=2>`statements` 为代码块</font>*
      *<font size=2>`return value` 可以根据情况判断是否需要填写</font>*

   - 调用
     - 无参调用 `函数名`
     - 有参调用 `函数名 [参数] [参数] [参数]....`

   - 实例
   ```
      getTheFile(){

         FILES=()
         j=0
         for i in $(ls $1)
         do
            if [ -e $i ]
            then
                     FILES[j]=$i
                     j=$j+1
            fi
         done
         echo ${FILES[*]}

      }

      getTheFile $1
             
   ```
    ![avatar](/Linux/shell编程/自定义函数1.png)   
