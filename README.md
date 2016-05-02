# mmseg
基于libmmseg 并加入自己的词性和词频信息，增加对分词的歧义性处理能力
[build]
进去 mmseg-cpp 目录 运行下面命令会在 mmseg 目录下生成一个 _mmseg.so 动态库
./build.py build

[command]
进入tools有两个可执行文件 mmseg_batch,mmseg_test

运行 mmseg_test 对输入的字符串进行分词 并输出到屏幕
./mmseg_test -h 可以知道具体的参数

运行 mmseg_batch 对输入的文件 进行分词 并输出到文件
./mmseg_batch -h 可以知道具体的参数

