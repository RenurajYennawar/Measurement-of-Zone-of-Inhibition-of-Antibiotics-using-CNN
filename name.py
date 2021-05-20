import os 
  
# Function to rename multiple files 
def main(): 
    i = 1
      
    for filename in os.listdir("images"): 
        dst = str(i) + ".jpg"
        src = 'images/'+ filename 
        dst = 'Renamed Images/'+ dst
        os.rename(src,dst)
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main()