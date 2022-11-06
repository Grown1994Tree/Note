# PHP安装

### 一、下载安装包
版本：7.4


### PHP安装扩展
1. 进入需要安装的扩展模块的目录`php-NN/etx/模块名/`。
2. 执行`phpize`命令生成模块的配置文件，本例的路径为`/usr/local/bin/phpize`,然后会在路径下生成`configure`配置文件。
3. 使用`./configure --with-php-config=/usr/local/bin/php-config 扩展模块`增加所需的模块。
4. 使用指令`make & make install`对扩展模块进行安装,安装完成后会在扩展目录生成`*.so`文件
5. 修改`php.ini`文件，增加`extension=扩展模块路径`后重启Apache。