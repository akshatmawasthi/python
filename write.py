# Write the text “Take it easy” to a file
# Write the line open(“text.txt”) to a file

#!/usr/bin/env python

# create and open file
f = open("test.txt","w")

# write data to file 
f.write("Take it easy")
f.write("This data will be written to the file.")

# close file
f.close()


