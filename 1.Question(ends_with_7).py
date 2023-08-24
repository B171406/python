answer_list=[]
def find(input_list):
    for i in input_list:
        if(i%10==7):
            answer_list.append(i)
input_list=[135,2,45,24,57,6,765,45,13,65,7,68,98,9764322,47687,87,98,9,98]
find(input_list)
print(answer_list)