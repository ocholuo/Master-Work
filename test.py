# Python3 code to Check for 
# balanced parentheses in an expression

num = 27
requestTime = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]



def droppedRequest(num, requestTime):
    int ans = 0 ;
    for(int i = 0 ;  i < n; i++){

        if(i  >2 && requestTime[i] == requestTime[i-3]){
            ans++;
        } else if(i > 19 && (requestTime[i] - requestTime[i-20]) <10){
            ans++;
        } else if( i > 59 && (requestTime[i] - requestTime[i-60]) <60 ){
            ans++;
        }
    }
    # dropped = 0
	# # this is to keep track of any of the element that is already dropped due to any of 3 limit violation.
    # already_dropped = {} 

    # for i in range(num):
    #     if i > 2 and requestTime[i] == requestTime[i-3]:
    #         if requestTime[i] not in already_dropped or already_dropped[requestTime[i]] != i:
    #             already_dropped[requestTime[i]] = i
    #             dropped += 1
    #             print(i, requestTime[i])

    #     elif i > 19 and requestTime[i] - requestTime[i-20] < 10:
    #         if requestTime[i] not in already_dropped or already_dropped[requestTime[i]] != i:
    #             already_dropped[requestTime[i]] = i
    #             dropped += 1
    #             print(i, requestTime[i])

    #     elif i > 59 and requestTime[i] - requestTime[i-60] < 60:
    #         if requestTime[i] not in already_dropped or already_dropped[requestTime[i]] != i:
    #             already_dropped[requestTime[i]] = i
    #             dropped += 1
    #             print(i, requestTime[i])
    # return dropped

print(droppedRequest(num, requestTime))



# print(len(requestTime))

# def checkIfover3(listOfElems):
#     ''' Check if any second has more then 3 requests'''    
#     for elem in listOfElems:
#         if listOfElems.count(elem) > 3:
#             return False
#     return True


# def checkIflessThen3(num, listOfElems):
#     ''' Check if any second has more then 3 requests'''   
#     count = 0 
#     if listOfElems.count(num) > 3:
#         for i in listOfElems:
#             if i == num:
#                 count = i
#             else:
#                 return count, False
#     return 0, True

# def check(num, requestTime):
#     num = 27
#     requestTime = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]


#     i = 0
#     while i < 5:
#         stack = []
#         stack.append(requestTime[i])
#         received_request = 0

#         count, test = checkIflessThen3(i, requestTime)
#         print(count, test)

#         i+=1


#         # if requestTime[i] == requestTime[i+1]:
#         #     received_request +=1
#         #     stack.append(requestTime[i])

#         #     print(requestTime[i])
#         #     print(received_request)
#         #     print(stack)

#         # i+=1



    


        

# check(num, requestTime)

# # def check(inputString):
# #     open_letter = "("
# #     close_letter = ")"
    
# #     stack = []
# #     count = 0
# #     for i in inputString:
# #         # check the open letter
# #         if i == open_letter:
# #             stack.append(i)
# #         # check the close letter
# #         elif i == close_letter:
# #             pos = close_letter.index(i)
# #             if ((len(stack) > 0) and (open_letter[pos] == stack[len(stack)-1])):
# #                 stack.pop()
# #                 count += 1
# #             else:
# #                 return -1
# #     if len(stack) == 0:
# #         return count
# #     else:
# #         return -1
    
    
# # Driver code
# # string = "(()(())"
# # print(string,"-", check(string))
  
# # string = "(())"
# # print(string,"-", check(string))
# # string = "()("
# # print(string,"-", check(string))
  
# # string = "((()"
# # print(string,"-",check(string))