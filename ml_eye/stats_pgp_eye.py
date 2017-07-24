
import numpy as np


# loads the tiled genome name file

arr = np.load('names.npy')
arrlst = np.ndarray.tolist(arr)

# formats the tile 

def format(npint):
    s = ""
    string = str(npint)
    for char in range(len(string)):
        if string[char] == "-":
            break
        elif string[char] != "b" and string[char] != "'":
            s += string[char]
        else:
            pass
    return s


# runs formatting on all names

def formatall():

    tiled_partic = [] 
    for i in range(len(arrlst)):
        tiled_partic.append(format(arrlst[i]))
        
    return tiled_partic



tiled_names = formatall()


# In[9]:

# opens the PGP survey and dumps the participant list
import csv 

with open('pgp_eye.csv', newline='') as eye:
    reader = csv.DictReader(eye)
    eye_names = []
    for row in reader:
        eye_names.append(row['name'])


# In[11]:

# makes a list of names that are in both the PGP survey name list and the tiled genomes list

tiled_and_eyecolor = [x for x in eye_names if x in tiled_names]



import csv 


def colorfreq():   
    color_freq = {}
    color = 1
    while color < 25:
        
        with open('pgp_eye.csv', newline='') as eye:
            reader = csv.DictReader(eye)
            count = 0
        
            for row in reader:
                if row["left"] == str(color) and row["name"] in tiled_and_eyecolor:
                    count += 1
                else:
                    pass
                    
            color_freq[count]
            print("count: ",color, count)
        color += 1
    print(color_freq)
        
colorfreq()
