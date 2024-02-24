sample = open(r"C:\Users\deept\Downloads\stop_words.txt", "r")
l=str(sample.readlines())
k=list(l.split(","))
print(len(k))
#l1=set(l.split())
#print(l1)
#sample.close()


#import os

#path =r"C:\Users\deept\Downloads\files\files"
#os.chdir(path)

#def read_files(file_path):
 #  with open(file_path, 'r') as file:
  #    print(file.read())
      
#for file in os.listdir():
 #  if file.endswith('.txt'):
  #    file_path =f"{path}/{file}"

#read_files(file_path)