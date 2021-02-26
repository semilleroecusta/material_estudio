#Way too long words code 
#By:Bautista David, Rodriguez Sergio
word_list=[]  # clean list to add the users words 
code_list=[]  # clean list to add the codes of the words 

try:                                             
  number_words=int(input(f"Number of words: "))  # an "input" to the add the users words 
  for word in range (number_words):              # a "for" to generate "input" codes to add the number_words that the user register  
    words=input(f"word #{word+1} ")              
    word_list.append(words)
    
  for word in word_list:
    if any(chr.isdigit() for chr in word)==False: # an "if"  to verify that the words dont contain numbers  
      if len(word)>10:                            # an "if" to verify that the word contains more than 10 letters 
        code_list.append(f"{word[0]}{len(word)-2}{word[len(word)-1]}")    # this code creates the code of the words and adds them to the code_list   
      else:
        code_list.append(word)                   # this code add the words that contains less than 10 letters 
    else:
      
      print(f"word #{word_list.index(word) + 1} contains a number, value not supported.")   # this code is to show the error of inserting words with some number
      
      
  for code in code_list:
        print(code)

    
except ValueError:            # an "except" to catch an ValueError in the variable "number_words"
  print("value error.")
