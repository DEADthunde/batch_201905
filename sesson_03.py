# print ("create a score board")
# runs = 0
# wicets = 0
# current = 0
# no0fball = 0
# overs = 0
# max_overs = 2
# maxwicet = 0
#
# type_of_runs = ["1","2","3","4","5","6"]
# extra = ["nb","wb"]
# twicet = ["lbw","b","c","ro","stump","htw"]
#
#
# while True :
#     print("--------------------")
#     print(f"{runs}/{wicets}")
#     print(f"{overs}({current})")
#     print("---------------------")
#     _input = str(input("enter run:")).strip()
#     if wicets == 10 or overs == max_overs:
#         break
#
#     if _input in extra :
#         runs += 1
#     elif _input in type_of_runs :
#        runs += int(_input)
#        current += 1
#     elif _input in twicet:
#         wicets += 1
#         current  += 1
#     if current == 6 :
#         overs += 1
#         current =+ 1
# ------------------------------,end =""

# for i in range (1,5):
#      for j in range(1,3):
#          print("#" ,end = "")
#      print("#")
# for i in range(4,-1,-1):
#     space = "  " * i
#     print(space, end="")
#     for j in range(5, i, -1):
#         print("1", end="   ")
#     print("")
row in range(7):
for col in range(7):
    if col ==0 or col ==6 or ((row==col) and (col>0 and col <4)) or (row==1 and col==5) or row==2 and col==4:
    print("*", end="")
    else :
        print(end="")
print()