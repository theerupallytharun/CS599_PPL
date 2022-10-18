import csv             # importing module

try:
    def count_above(file, threshold):       # function Definition
        with open(file, 'r') as read_obj:     # opening file in read mode
            csv_read = csv.reader(read_obj)     # creating file handler
            list_of_students = list(csv_read)       # creating a list of rows from CSV file
        #print(list_of_students)
        
        print("The Details of Students above Threshold are:")
        
        for i in range(len(list_of_students)):            #  traversing through the student list.
            if float(list_of_students[i][2])>threshold:   #  checking if marks are greater than the threshold value 
                print(list_of_students[i])         # printing Student Details
                
        print("The Details of Students below Threshold are:")
        for i in range(len(list_of_students)):             #  traversing through the student list.
            if float(list_of_students[i][2])<threshold:    #  checking if marks are greater than the threshold value 
                print(list_of_students[i])         # printing Student Details
                
    thresh=float(input("Enter the mark Threshold: "))     # input Marks Threshold
    count_above('count_above.csv', thresh)             #calling function
    
    
except FileNotFoundError:              # Handling file Exception
    print("File not found") 
    
except IndexError:            # Handling Index Error Exception
    print("Index error, Check your indexes in the lists")

except ValueError:         # Handling Value Error Exception
    print("Enter Integer for the Threshold")
    
except:             # other exceptions
    print("Some Exception occurred, Hope I covered all the exceptions above")

