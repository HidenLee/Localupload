def scale(list1,t):
    if list1 == []:  
        return t
    print(list1.pop())
    scale(list1,t)    # 다시 hello에 넣음

mugechu = [34 , 22, 11]
scale(mugechu,2)
