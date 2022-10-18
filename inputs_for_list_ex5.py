try:
    '''
    def inputs_for_list():          # function definition
      lst=[]                         # creating empty list
      inp=input("Enter an Integer or enter 'exit': ")       # input a number or say exit
      while(inp!="exit"):         # running loop till user enters exit
        if inp.isdigit():       # checking if input is integer
          lst.append(inp)       # append to the list
        inp=input("Enter an Integer or enter 'exit': ")       # input a number or say exit

      return lst      # return the final list
    '''
    def inputs_for_list():          # function definition
      lst=[]                         # creating empty list
      inp=input("Enter an Integer or enter 'exit': ")       # input a number or say exit
      while(inp!="exit"):         # running loop till user enters exit
        if inp!="exit":       # checking if input is exit
          lst.append(int(inp))      # append to the list
        inp=input("Enter an Integer or enter 'exit': ")       # input a number or say exit

      return lst 
    def nth_smallest_value(lst, n):      # function definition

      small_lst= sorted(list(set(lst)))       # creating sorted unique list fron orginal list
      if n>len(small_lst):      # checking in n value is greater than actual list
        print("n value is greater than the lenth of list")
      else:
        return small_lst[n-1]   # returning the value


    def nth_largest_value(lst, n): 
      small_lst= sorted(list(set(lst)))       # creating sorted unique list fron orginal list
      
      if n>len(small_lst):      # checking in n value is greater than actual list
        print("n value is greater than the lenth of list")
      else:
        return small_lst[len(small_lst)-n]   # returning the value

    lst= inputs_for_list()

    print("List with Unique elements is: ",sorted(list(set(lst))))
    n_val= int(input("Enter n value: "))
    print(n_val,"th smallest value is: ", nth_smallest_value(lst, n_val))
    print(n_val,"th largest value is: ", nth_largest_value(lst, n_val))


except IndexError:            # Handling Index Error Exception
    print("Index error, Check your indexes in the lists")

except ValueError:         # Handling Value Error Exception
    print("Enter Integer Value for input")
    
except:             # other exceptions
    print("Some Exception occurred, Hope I covered all the exceptions above")