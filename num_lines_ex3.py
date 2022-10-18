try:
    def file_read_from_tail(fname, num_lines):       # function Definition
        with open(fname, "r") as f:          # opening file in read mode
            all_lines = f.readlines()        # creating a list of all lines from the file
            if num_lines> len(all_lines):         # checking if the lines in file are less than the requested lines
                print("There are only", len(all_lines),"lines in the file.")
            else:
                print("The last ",num_lines," of the file are: ")
            #print("Here: ",len(all_lines)-3, len(all_lines))
                for i in range(len(all_lines)-num_lines, len(all_lines)):  # traversing through the list of lines needed to print
                    #print(i)
                    print(all_lines[i])


    num_lines=int(input("Enter Number of lines you want to print: "))  # input for number of lines
    file_read_from_tail("lines_of_text.txt",num_lines)       # calling function
    
    
except FileNotFoundError:              # Handling file Exception
    print("File not found") 
    
except IndexError:            # Handling Index Error Exception
    print("Index error, Check your indexes in the lists")

except ValueError:         # Handling Value Error Exception
    print("Enter Integer for the number of lines")
    
except:             # other exceptions
    print("Some Exception occurred, Hope I covered all the exceptions above")

    