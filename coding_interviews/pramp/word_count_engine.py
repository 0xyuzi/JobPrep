'''
1. case-insentive
2. punctuation if in the middle, just remove out 
3. punctuation be remove out
4. 

"FDSAabcd".lower()
"fdsaabcd"
 
 ["youll", "1", 4], ["only", "1",5], 
          ["get", "1"], ["by", "1"], ["just", "1"] ]
'''


from collections import defaultdict

def word_count_engine(document):
    
    document = document.lower()
    
    document = document.split()
    # print(document)
    word_counter = defaultdict(int)
    
    
    temp_word = ''
    max_count = 0
    
    for word in document:
      for c in word:
        if c>='a' and c<='z':
          temp_word +=c
        
      word_counter[temp_word] += 1
      if word_counter[temp_word] > max_count:
        max_count = word_counter[temp_word]
      
      
      temp_word = ''
    
    print(word_counter)
    
    # bucket sort
    
    # caret bucket of max size of max_count + 1 
    bucket_list = [0]*(max_count+1)
    
    for k,v in word_counter.items():
      if bucket_list[v] == 0:
        bucket_list[v] = [k]
      else:
        bucket_list[v].append(k)
    
    res = []
    
    for i in range(max_count,0,-1):
      if bucket_list[i] == 0:
        continue
        
      for word in bucket_list[i]:
        res.append([word, str(i)])
                              
    return res 
                              
     
        
    

document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
   
print(word_count_engine(document))
        
       