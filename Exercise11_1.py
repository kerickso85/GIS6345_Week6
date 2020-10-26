in_dict = False #declare a global variable so that the value remains after the function is called/executed

def test_dict():
    global in_dict #refer to global variable instead of creating a local instance of the same name
    test_word=input('What word would you like to test if it is included in the dictionary? >>>') #prompt user
    my_dict = dict() #define dictionary
    fin=open('words.txt') #read .txt file per exercise
    for line in fin: #iterate for each line in the list of words.txt
        word=line.strip()  #temp assign each word to a string variable
        type(word)
        my_dict[word]='' #assign each word as a key in dictionary, leave values blank
    #print('The contents of the words.txt dictionary are:',my_dict) #debug statement to view the dictionary: keys populated, values blank.
    print('Your test word was:',test_word) #debug statement to test user input
    if test_word in my_dict: 
        in_dict=True 
    else:
        in_dict=False #to make sure the variable is reset in the event of a negative result
    print('The result of this test is',in_dict) #output result to user
        





