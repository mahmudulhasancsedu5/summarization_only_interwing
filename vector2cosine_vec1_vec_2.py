"""
-------reade  vectore file and find cosine similarity-------
input_file:
------------
10 100
sent_1 1 . . . 100th
.
.
.
sent_10 1  . . . 100th

output file:
------------
sent_0 12
sent_1 .56
.
.
.
sent_10 5.6

"""
def vector2cosine(file_vec1,file_vec2):

    fileClose_flag=0
    if file_vec1==file_vec2:
        fileClose_flag=1
        inputFile=open(file_vec1,'r')
        outputFile=open(file_vec1+"_"+file_vec2+"_sentence_cosine_value.txt",'w')

        #lines_list=file_id.readlines()
        #print lines_list
        line_list=inputFile.readlines()
        line_1=line_list[0].split(' ')
        del line_list[0]

        row_count_file1=int(line_1[0])
        colum_count_file1=int(line_1[1])

        row_count_file2=row_count_file1
        colum_count_file2=colum_count_file1
        

        vec_mat1=[]
        vec_mat2=[]
        i=0
        """
        delete the first 2 length row , clm array and
        create only a vectore array
        """
        i=0
        for line in line_list:

            data_arr=line.replace('\n','').split(' ')
            data_arr.remove('sent_'+str(i))
            data_arr=[float(x) for x in data_arr]
            
            vec_mat1.append(data_arr)
            vec_mat2.append(data_arr)
            i+=1
    

    else:
        inputFile1=open(file_vec1,'r')
        inputFile2=open(file_vec2,'r')
        
        outputFile=open(file_vec1+"_"+file_vec2+"_sentence_cosine_value.txt",'w')

        #lines_list=file_id.readlines()
        #print lines_list
        line_list_file1=inputFile1.readlines()
        line_1_file1=line_list_file1[0].split(' ')
        del line_list_file1[0]

        row_count_file1=int(line_1_file1[0])
        colum_count_file1=int(line_1_file1[1])
        
        line_list_file2=inputFile2.readlines()
        line_1_file2=line_list_file2[0].split(' ')
        del line_list_file2[0]

        row_count_file2=int(line_1_file2[0])
        colum_count_file2=int(line_1_file2[1])

        
        vec_mat1=[]
        vec_mat2=[]
        """
        delete the first 2 length row , clm array and
        create only a vectore array
        """
        """
        1. remove sent_x string from front
        2. replace string value by int(str_value) value
        """
        i=0
        #print inputFile1.name
        #print line_list_file1[0]
        for line in line_list_file1:
            data_arr=line.replace('\n','').split(' ')
            data_arr.remove('sent_'+str(i))
            data_arr=[float(x) for x in data_arr]
            vec_mat1.append(data_arr)
            i+=1

        i=0
        #print inputFile2.name
        #print line_list_file2[0]
        for line in line_list_file2:
            data_arr=line.replace('\n','').split(' ')
            data_arr.remove('sent_'+str(i))
            data_arr=[float(x) for x in data_arr]
            vec_mat2.append(data_arr)
            i+=1

      
        #print len(mat[1])

    from scipy import spatial

    #-------test
    #cosine_val=1-spatial.distance.cosine(mat[1],mat[2])
    #print cosine_val

    """
    #test
    for x in mat:
        print len(x)
    """

    """
    1. calculate pair wise cosine(s1,s2) value
    """

    sent_cosine_val_array=[]
    i=0
    for u in vec_mat1:
        
        j=0
        sent_u_val=0.0
        for v in vec_mat2:

            #print i,j
            cosine_val=1-spatial.distance.cosine(u,v)
            sent_u_val+=cosine_val
            
            #cosine_val=float(cosine_val)
            #print "cosine(u,v) = "+str(cosine_val)+"\n"
            
            j+=1
        
        #print "sent_"+str(i)+" total cosine value = "+str(sent_u_val)
        sent_output=str("sent_"+str(i)+" "+str(sent_u_val/len(vec_mat2))+'\n')
        #sent_output=str(str(i)+" "+str(sent_u_val/len(mat))+'\n')
        outputFile.write(sent_output)
        #sent_cosine_val_array.append(sent_u_val/len(mat))
        
        i+=1
        
        
    #print "len-----> "+str(len(sent_cosine_val_array))
    if fileClose_flag==1:
        inputFile.close()
        outputFile.close()    
    elif fileClose_flag==2:
        inputFile1.close()
        inputFile2.close()
        outputFile.close()
    
#----------------------start execution from here-----
# --------------------------------run from consol---------------------
'''
import sys

num_inputFile=len(sys.argv)-1
if num_inputFile > 1:
    if num_inputFile==1:
        print sys.argv[1],' gives support to itself.'
        vector2cosine(sys.argv[1],sys.argv[1])
    elif num_inputFile==2:
        print sys.argv[1],' gives support to ',sys.argv[2]
        vector2cosine(sys.argv[1],sys.argv[2])
    else:
        print 'No input file'
        
        
else :

    print "Run For fixed dataset in vector2cosine.py \n"
    vecFileName_get_support='news1_tweet.txt_sentence.vec'
    vecFileName_give_support='news1_processed_data.txt_sentence.vec'
    vector2cosine(vecFileName_get_support,vecFileName_give_support)
    
'''


