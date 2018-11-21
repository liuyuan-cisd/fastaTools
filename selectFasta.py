# coding: utf-8
import argparse
import random
def getopt():
    '''parsing the opts'''
    parser=argparse.ArgumentParser(
                description='selectFasta.py: A program to select sequence from fasta file',
                usage='selectFasta.py -i inputfile -o outputfile -n number [-k keyword]'
            )
    parser.add_argument('-key','--keyword',type=str,help="The name of sequences which you want to get",required=False)
    parser.add_argument('-i','--input',type=argparse.FileType('r'),help="inpuut file path",required=True)
    parser.add_argument('-o','--output',type=argparse.FileType('w'),help="output file path",required=True)
    parser.add_argument('-n','--number',type=int,help="The number of the sequence you want get")
    args=parser.parse_args()
    return args
def select_random(input_file,number):
    '''
    used for select a certain number of sequence randomly
    '''
    seq=[]
    input_file_len=int(len(input_file)/2)
    random.seed(100)
    index=random.sample(range(input_file_len),number)
    for i in index:
        seq.append(input_file[2*i])
        seq.append(input_file[2*i+1])
    for line in seq:
        args.output.write(line)
def selectByKey(args):
    seq=[]
    input_file_list = list(args.input)
    input_file_len = int(len(input_file_list) / 2)
    for index,line in enumerate(input_file_list):
        if line.startswith('>') and args.keyword in line:
            seq.append(line)
            seq.append(input_file_list[index+1])
    return seq
if __name__=='__main__':
    args=getopt()
    print('start')
    if args.keyword:
        result=selectByKey(args)
        select_random(result,args.number)
    else:
        input_file=list(args.input)
        select_random(input_file,args.number)
    print ('finished')