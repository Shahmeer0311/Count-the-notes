amount =  int(input("Please enter the amount"))
note_1 = amount // 100
note_2 =   (amount % 100) // 50         
note_3 = ((amount % 100) % 50)     // 10  
print("Number of 100 Rp notes:", note_1 , "Number of 50 Rp notes:" , note_2 , "Number of 10 Rp notes:" ,  note_3)