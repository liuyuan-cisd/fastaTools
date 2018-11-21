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

selectBed.py:
	
	用来从bed文件中随机挑选出来一部分出来
	
	使用方法：selectBed.py -b bedfile -o outputfile -key keyword -n number
	
	依赖：
		python3.6（如在python2中运行修改print语句即可）
	参数说明：
		-b:bed文件，必选参数
		-o:输出文件，必选参数
		-key：关键字，必选参数
		-n:选取数量，可选参数
	ps：
		1.程序用来根据提供的关键字从bed文件中提取相应的序列，如果提供 -n 参数则会选择相应的数量出来
		2.不要在pycharm中运行此程序，在pycharm中运行时不知道为什么不能把所有选取得行完全写到输出文件，
		  目前为止原因，应该是pycharm内存原因之类的

selectFasta.py
	
	用来从fasta文件中提取一部分序列出来

	使用方法：selectFasta.py -i inputfile -o outputfile -n number [-k keyword]

	依赖：
		python3.6（如在python2中运行修改print语句即可）
	参数说明：
		-i:输入文件，必选参数
		-o:输出文件，必选参数
		-n:选取数量，必选参数
		-key：关键字，可选参数
	ps：
		1.如果不选参数 -k 则在所有序列中提取，如果选择 -k参数，程序会在包含输入关键字的序列中选择
