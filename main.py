'''
this file will take 2 file 



'''


from text2sentVec import text2sentenceVec
from vector2cosine_vec1_vec_2 import vector2cosine

def dualWing_summary(file_cosine_value1,file_cosine_value2,dataFile,length):
    inputFile1=open(file_cosine_value1,'r')
    inputFile2=open(file_cosine_value2,'r')
    sentenceFile=open(dataFile,'r')
    out_name=str('summary_DualWing_'+file_cosine_value1[:21]+file_cosine_value1[:21]+'___.txt')
    outputFile=open(out_name,'w')

    line_listFile1=inputFile1.readlines()
    line_listFile2=inputFile2.readlines()

    val_File1=[]
    val_File2=[]
    
    for i in range(len(line_listFile1)):
        line1=line_listFile1[i]
        line1=line1.replace('\n','').split(' ')
        del line1[0]
        val_File1.append(float(line1[0]))

        line2=line_listFile2[i]
        line2=line2.replace('\n','').split(' ')
        del line2[0]
        val_File2.append(float(line2[0]))


    val_arr=[(val_File1[i]+val_File2[i],i) for i in range(len(val_File1))]
    vall_arr=sorted(val_arr)
    val_arr.reverse()
    
    sentences=sentenceFile.readlines()

    summ=''
    
    for i in range(0,length):
        summ+=str(sentences[val_arr[i][1]]+'\n')

    outputFile.write(summ)
    

    inputFile1.close()
    inputFile2.close()
    outputFile.close()
    
def create_summary(file_cosine_value,dataFile,length):
    inputFile=open(file_cosine_value,'r')
    sentenceFile=open(dataFile,'r')
    outputFile=open('summary_'+file_cosine_value,'w')

    line_list=inputFile.readlines()
    #print line_list
    val_arr=[]
    
    i=0
    
    for line in line_list:

        line=line.replace('\n','').split(' ')
        del line[0]
        val_arr.append((float(line[0]),i))
        #print i,line
        i+=1
    arr=sorted(val_arr)
    arr.reverse()

    
    sentences=sentenceFile.readlines()

    summ=''
    
    for i in range(0,length):
        summ+=str(sentences[arr[i][1]]+'\n')

    outputFile.write(summ)
        
    #print arr

        
        
    

    inputFile.close()
    outputFile.close()
    
def main():

    inputFile1='news1_processed_data.txt'
    inputFile2='news1_processed_tweet.txt'

    text2sentenceVec(inputFile1,inputFile2)
    text2sentenceVec(inputFile2,inputFile1)
    
    sent_vec_file1=inputFile1+'_sentence.vec'
    sent_vec_file2=inputFile2+'_sentence.vec'
    
    vector2cosine(sent_vec_file1,sent_vec_file1)
    vector2cosine(sent_vec_file2,sent_vec_file2)
    vector2cosine(sent_vec_file1,sent_vec_file2)
    vector2cosine(sent_vec_file2,sent_vec_file1)
    
    cosine11=sent_vec_file1+'_'+sent_vec_file1+'_sentence_cosine_value.txt'
    cosine12=sent_vec_file1+'_'+sent_vec_file2+'_sentence_cosine_value.txt'
    cosine22=sent_vec_file2+'_'+sent_vec_file2+'_sentence_cosine_value.txt'
    cosine21=sent_vec_file2+'_'+sent_vec_file1+'_sentence_cosine_value.txt'
    
    summary_length=10
    dataFile=inputFile1
    create_summary(cosine11,dataFile,summary_length)
    create_summary(cosine12,dataFile,summary_length)
    dualWing_summary(cosine11,cosine12,dataFile,summary_length)
    
    dataFile=inputFile2
    create_summary(cosine22,dataFile,summary_length)
    create_summary(cosine21,dataFile,summary_length)
    dualWing_summary(cosine22,cosine21,dataFile,summary_length)
    
        
    
#-----------------------------------------------------------------    


main()
'''
ff='news1_processed_data.txt_sentence.vec_news1_processed_tweet.txt_sentence.vec_sentence_cosine_value.txt'
dataFile='news1_processed_data.txt'
create_summary(ff,dataFile,10)
'''
