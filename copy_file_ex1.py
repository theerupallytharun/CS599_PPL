import csv            # import csv module

try:
    
    def copy_file(file_from): # function definition
        with open('file_from.csv', newline='') as csvfile:       #  opening CSV file
            reader = csv.reader(csvfile)  # file handler
            for row in reader:            # traversing through the file
                with open('file_to.tsv', 'a') as to_file:            #  opening TSV file to write
                    tsv_writer = csv.writer(to_file, delimiter='\t')      # Setting delimiter to Tab space 
                    tsv_writer.writerow(row)         # Writing to a file            
     
    copy_file("file_from.csv")       
except FileNotFoundError:            # Handling file Exception
    print("File(s) not found")

except:               # other exceptions
    print("Some Exception occurred, Hope I covered all the exceptions above")






