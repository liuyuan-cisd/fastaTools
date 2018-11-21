"""
Created on Mon Nov 19 10:01:48 2018

@author: liuyuan
"""
import argparse,sys
import random
def getopt():
    '''parsing the opts'''
    parser=argparse.ArgumentParser(
                description='selectBed.py: A program to get select bed file accroding seqname',
                usage='selectBed.py -b bedfile -o outputfile -n number'
            )
    parser.add_argument('-key','--keyword',type=str,help="The name of sequences which you want wo get",required=True)
    parser.add_argument('-b','--bed',type=argparse.FileType('r'),help="bed file path",required=True)
    parser.add_argument('-o','--output',type=argparse.FileType('w'),help="output file path",required=True)
    parser.add_argument('-n','--number',type=int,help="The number of the sequence you want get")
    args=parser.parse_args()
    return args
def transform_line(line):
    '''used to transform the line of ded file from list to str'''
    com_line=''
    for i in line:
        com_line+=i
        com_line+='\t'
    com_line+='\n'
    return com_line        
def getAll(args):
    '''used to get all of the line in bed file according keyword'''
    keyword=args.keyword
    getbed_list=list()
    bedfile=filter(lambda x:x.strip(),args.bed.readlines())
    bed_list=map(lambda x:x.strip().split(), bedfile)
    bed_list=list(bed_list)
    for line in bed_list:
        if keyword in line[3]:
            getbed_list.append(line)
    result=map(transform_line,getbed_list)
    return result
def getSub(args):
    '''used to get a certain number of line from bed file'''
    keyword=args.keyword
    all_result=getAll(args)
    all_result=list(all_result)
    result=list()
    random.seed(100)
    get_indexs=random.sample(range(len(list(all_result))),args.number)
    for i in get_indexs:
        result.append(all_result[i])
    return  result
if __name__=='__main__':
    args=getopt()
    print ("start")
    if args.number:
        result=getSub(args)
        args.output.writelines(result)
    else:
        result=getAll(args)
        args.output.writelines(result)
    print ('finished')