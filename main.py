'''
this file will take 2 file 



'''


from text2sentVec import text2sentenceVec
from vector2cosine_vec1_vec_2 import vector2cosine

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

    summary11=sent_vec_file1+'_'+sent_vec_file1+'_sentence_cosine_value.txt'
    summary12=sent_vec_file1+'_'+sent_vec_file2+'_sentence_cosine_value.txt'
    summary22=sent_vec_file2+'_'+sent_vec_file2+'_sentence_cosine_value.txt'
    summary21=sent_vec_file2+'_'+sent_vec_file1+'_sentence_cosine_value.txt'

    dataFile=inputFile1
    create_summary(summary11,dataFile,10)
    dataFile=inputFile1
    create_summary(summary12,dataFile,10)
    dataFile=inputFile2
    create_summary(summary22,dataFile,10)
    dataFile=inputFile2
    create_summary(summary21,dataFile,10)
    
    
    
    


main()
'''
ff='news1_processed_data.txt_sentence.vec_news1_processed_tweet.txt_sentence.vec_sentence_cosine_value.txt'
dataFile='news1_processed_data.txt'
create_summary(ff,dataFile,10)
'''
