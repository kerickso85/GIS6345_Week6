hist = dict() #define global, empty histogram dictionary
frequency = dict() #define global, empty frequency dictionary

def most_frequent():
    global hist #histogram created will remain even after function is executed
    global frequency #frequency ditto ^^^
    
    text_doc=input('Enter the name of the text document in this directory which you would like to evaluate character frequences (format is filename.txt: >>>') #promt user which file they want to test
    string = open(text_doc).read() #open the text file
    #print(string) #debug statement for my sanity check
    # print(type(string)) #ditto ^^^
    for character in string: #loop through each character in the text file
        if character not in hist: #test if a key has been created in the histogram dictionary
            hist[character]=1 #if not, initiate the key at count 1
        else:
            hist[character]=hist[character]+1 #if so, incrememnt count by 1
    #print(hist) #debug statement for testing
    
    #sum all characters in histogram (except the \n representing spaces...)
    sum_chars = 0 #initiate local sum variable
    for key in hist: 
        if key!='\n': #as long as it's not a space
            sum_chars = sum_chars+hist[key] #add value for each key
    print('The total sum of characters in that text file, excluding spaces is:',sum_chars) #debug statement for testing
    
    #calculate frequency each character appears, as a percentage
    for key in hist:
        if key!='\n': #as long as it's not a space
            if key not in frequency: #test if letter has been added to frequency dictionary yet
                frequency[key]=round(100*hist[key]/sum_chars,2)
    print('The frequency each character appears in the text file, as a percentage are:',frequency)
    #test to make sure sum of frequencies add up to 100...
    prcnt_100 = 0 #init local variable to tally all the invidiual frequencies
    for portion in frequency:
        prcnt_100 = prcnt_100+frequency[portion] #add up all individual percentages
    #print('Total percentage of all characters',round(prcnt_100,0)) #debug statement

        
    
    


# In[38]:


most_frequent()


# In[ ]:




