def showDan(dan):
    print(f'****{dan}단****\n')
    for i in range(1,9+1):
        print(f'{dan} * {i} = {dan*i}')


showDan(7)

print("")
#---------------------------------------------------
def showDan2(dan):
    print("****{} 단****\n".format(dan))
    print("{} * {} = {}".format(dan,1,1*dan))
    print("{} * {} = {}".format(dan,2,2*dan))
    print("{} * {} = {}".format(dan,3,3*dan))
    print("{} * {} = {}".format(dan,4,4*dan))
    print("{} * {} = {}".format(dan,5,5*dan))
    print("{} * {} = {}".format(dan,6,6*dan))
    print("{} * {} = {}".format(dan,7,7*dan))
    print("{} * {} = {}".format(dan,8,8*dan))
    print("{} * {} = {}".format(dan,9,9*dan))
    
showDan2(8)