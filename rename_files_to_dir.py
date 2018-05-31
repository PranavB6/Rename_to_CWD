
SKIP = ['cwd_rename.py', 'README.md']
separator = " - "

import os, re, sys, time

cwd_path = os.getcwd()    
cwd = cwd_path.split('\\')[-1]      # get cwd name

def get_filename(path):
    return path.split('\\')[-1]

# For 'natural' sorting
def atoi(text):
    return int(text) if text.isdigit() else text

# For 'natural' sorting
def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [atoi(c) for c in re.split('(\d+)', text)]

def get_things():
    things = os.listdir(cwd_path)       # get a list of item in cwd
    things.sort(key=natural_keys)       # sort items in cwd 'naturally'
    return things

# get everything thats actually a file
def extract_files(things):
    return [thing for thing in things if (os.path.isfile(os.path.join(cwd_path, thing)) and (thing not in SKIP))]

# get new filenames, keep the old file extension
def get_new_filenames(files):
    new_filenames = []
    
    num = 1

    for file in files:
        ext = file.split('.')[-1]

        new_name = cwd + separator + str(num) + '.' + ext

        if new_name in files:
            raise ValueError('Fileame already in directory: {}'.format(new_name))
        
        new_filenames.append(new_name)

        num += 1

    return new_filenames

# show the user how it will change the files
def show_rename_files(files, new_filenames):    
    for idx in range(len(files)):
        print('{} --> {}'.format(files[idx], new_filenames[idx]))

def rename_files(files, new_filenames):       
    for idx in range(len(files)):        
        os.rename(os.path.join(cwd, files[idx]), os.path.join(cwd, new_filenames[idx]))

def main():

    things = get_things()

    files = extract_files(things)
    
    new_filenames = get_new_filenames(files)

    show_rename_files(files, new_filenames)

    print()
    confirm = input('Are you sure you want to continue (Y/n): ')
    print()
    
    if confirm == 'Y': 
        rename_files(files, new_filenames)
        print()
        print('Successfully Completed')
    else:
        print('Program Rejected')

    time.sleep(1.25)
    
    return

if __name__ == "__main__":
    cwd_path = sys.argv[1]

    if not os.path.isdir(cwd_path): 
        print('Not a directory')
        time.sleep(1)
        exit()   

    cwd = cwd_path.split('\\')[-1]

    main()

    