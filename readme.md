这个文件夹下存放用来处理fasta文件的工具

pyGetFasta.py:

	用于根据bed文件获取基因序列,基于bed文件中提供的基因位置信息
	
	得到的序列命名方式为：chr1：78900：79000：strong_enhancer 对应与bed文件的前四列
	
selectBed.py:

	用来从bed文件中随机提取出来一部分出来，根据基因的名字进行提取，可以控制提取的数量
	
selectFasta.py

	用来从fasta文件中随机提取一部分序列出来，可以根据fasta文件标识行信息提取
	
！[使用方法]（https://github.com/Liuyuan2018/fastaTools/wiki）
