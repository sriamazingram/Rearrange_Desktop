import heapq
import shutil
import os

# Getting home directory
home=os.path.expanduser('~')
place=home

# Getting the top 10 files based on size
#     lookup:contains the file path and the size in MB as tuples
lookup=[]
for root, dirs, files in os.walk(place):
    files = [f for f in files if (f[0] != '.' and f[0:1]!="__")]
    dirs[:] = [d for d in dirs if d[0] != '.']
    for filename in files:
        p=os.path.abspath(os.path.join(root,filename))
        lookup.append((os.path.getsize(p)/(1024*1024.0),p))

# Using priority queue to get top 10 largest
# Printing file path and size in MB
print("Top 10 files in system\n")
top10=heapq.nlargest(10,lookup)
ct=1
for i in top10:
    print(ct,":File:",i[1],"\tSize:",i[0],"MB")
    ct+=1

# Going through all the files in Desktop
# checking for extensions and storing in dictionary
#     items:dictionary containing key-extension and value-list of file paths
print("\nReading files in Desktop\n")
items=dict()
place_2=os.path.join(place,"Desktop")
for f in os.listdir(place_2):
    if os.path.isdir(f)==False:
        fname,fext=os.path.splitext(os.path.join(place_2,f))
        if fext!="" and fext!=".exe":
            if fext[1:].upper() in items:
                items[fext[1:].upper()].append(os.path.join(place_2,f))
            else:
                items[fext[1:].upper()]=list([os.path.join(place_2,f)])

# Making directories in Documents for every key in items
# shutil to move file from source to destination
print("Moving files to Documents")
place_3=os.path.join(place,"Documents")
for i in items:
    if os.path.exists(os.path.join(place_3,i))==False:
        os.makedirs(os.path.join(place_3,i))
    for j in items[i]:
        fname=j.split(os.sep)[-1]
        shutil.move(j,os.path.join(place_3,i,fname))
