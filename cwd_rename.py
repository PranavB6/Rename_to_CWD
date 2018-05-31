
import os, re

print('Program Start')

# Get path 
cwd_path = os.getcwd()
print('Current path:', cwd_path)

# get cwd name
cwd = cwd_path.split('\\')[-1]
print('CWD:',cwd)


print()
print('--- Things in cwd ---')
print()

# Get list of things in cwd
things = os.listdir(cwd_path)

#-------------- Sort them by file name
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

things.sort(key=natural_keys)

#--------------


thing_paths = [os.path.join(cwd_path, thing) for thing in things]

for idx, thing_path in enumerate(thing_paths):
    if os.path.isfile(thing_path): print('file: {}'.format(things[idx]) )
    else: print('not file: {}'.format(things[idx]) )



print() 

alist=[
    "some1thing",
    "some12thing",
    "some17thing",
    "some2thing",
    "some25thing",
    "some29thing"]

alist.sort(key=natural_keys)
print(alist)

# print(item_paths)



# get list of files in cwd
# sort files
# rename all files

