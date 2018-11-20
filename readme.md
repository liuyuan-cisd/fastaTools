这个文件夹下存放用来处理fasta文件的工具

pyGetFasta.py 

	用于根据bed文件获取基因序列

	使用方法：pyGetFasta.py -g genomefile -b bedfile -o outputfile [-l int]

	依赖：
		python2.7(如在python3中运行修改print语句即可)
		pyfasta

	参数说明：
			-g:基因组文件，必选参数
			-b:bed文件，必选参数
			-o:输出文件，必选参数
			-l：序列长度，可选参数

	ps：
		1.bed文件必须包含第四列（name列）
		2.如果bed中的序列多请分多次提取，如果序列过多会Fasta模块中的数据结构会溢出，
		 一次提取10W条数据应该没问题
		3.如果选择参数 -l 会根据 -l 的值将序列进行分段，默认不分段
