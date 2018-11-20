import argparse,sys
from pyfasta import Fasta
def getopt():
    '''parsing the opts'''
    parser=argparse.ArgumentParser(
                description='getFasta.py: A program to get fasta file accroding bed file',
                usage='pyGetFasta.py -g genomefile -b bedfile -o outputfile [-l int]'
            )
    parser.add_argument('-g','--genome',type=str,help="The path of genome file,should be a fasta file",required=True)
    parser.add_argument('-b','--bed',type=argparse.FileType('r'),help="bed file path",required=True)
    parser.add_argument('-o','--output',type=argparse.FileType('w'),help="output file path",required=True)
    parser.add_argument('-l','--length',type=int,help="The length of the sequence you want to get")
    args=parser.parse_args()
    return args
def splitBed(bed_list,length):
    splited_list=list()
    for line in bed_list:
        while (int(line[2])-int(line[1]))>length:
            temp=line[:]
            temp[2]=str(int(line[1])+length)
            splited_list.append(temp)
            line[1]=temp[2]
        splited_list.append(line)
    return splited_list
def writeFasta(bed_list,genome,output_file):
    n=len(bed_list)
    result=map(lambda i:'>{0}\n{1}'.format(bed_list[i][0]+':'+bed_list[i][1]+':'+bed_list[i][2]+':'+bed_list[i][3],genome.sequence({'chr':bed_list[i][0],'start':int(bed_list[i][1]),'stop':int(bed_list[i][2])},one_based=False)).upper(),range(len(bed_list)))
    output_file.write('\n'.join(result))
def getSequence(args):
    genome=Fasta(args.genome)
    bedfile=filter(lambda x:x.strip(),args.bed.readlines())
    bed_list=map(lambda x:x.strip().split(), bedfile)
    bed_list=list(bed_list)
    if args.length:
       bed_list=splitBed(bed_list,args.length)
    writeFasta(bed_list,genome,args.output)
if __name__=='__main__':
    args=getopt()
    print 'start\n'
    getSequence(args)
    print 'finshed'