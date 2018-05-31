
import os, re

cwd_path = os.getcwd()    
cwd = cwd_path.split('\\')[-1]      # get cwd name
separator = " - "


def get_filename(path):
    return path.split('\\')[-1]


def atoi(text):
    return int(text) if text.isdigit() else text


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

def extract_files(things):
    return [thing for thing in things if os.path.isfile(os.path.join(cwd_path, thing))]


def get_new_filenames(files):
    new_filenames = []

    num = 1

    for file in files:
        ext = file.split('.')[-1]

        new_name = cwd + separator + str(num) + '.' + ext

        if new_name in files:
            raise ValueError('Name already in dir: {}'.format(new_name))
        
        new_filenames.append(new_name)

        num += 1

    return new_filenames

def rename_files(files, new_filenames): pass

def main():
    # print('Current path:', cwd_path)
    # print('CWD:', cwd)

    print()
    print('--- Things in cwd ---')
    print()

    things = get_things()
    files = extract_files(things)
    
    new_filenames = get_new_filenames(files)

    rename_files(files, new_filenames)
    
    return

if __name__ == "__main__":
    main()
