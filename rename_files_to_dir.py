
SKIP = ['cwd_rename.py', 'README.md']

default_sep_start = " - "
default_sep_end = ""
default_start_num = 1


sep_start = ''
sep_end = ''
start_num = ''
cwd_path = ""
cwd = ""

import os
import re
import sys
import time
import argparse


def get_sep():
    global sep_start, sep_end

    sep_str_lst = input(
        '(optional) Separator (where # is the number): ').split('#')

    if sep_str_lst == ['']:
        sep_str_lst = [default_sep_start, default_sep_end]

    elif len(sep_str_lst) != 2:
        print('Invalid Separator:', sep_str_lst)
        time.sleep(1)
        exit()

    sep_start, sep_end = sep_str_lst

    return


def get_start_num():
    global start_num, default_start_num

    _input = input('(optional) Starting number: ')
    if not _input:
        start_num = default_start_num
        return

    try:
        start_num = int(_input)
    except:
        print('Invalid number')
        time.sleep(1)
        exit()

    return


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

    num = start_num

    for file in files:
        ext = file.split('.')[-1]

        new_name = cwd + sep_start + str(num) + sep_end + '.' + ext

        if new_name in files:
            print('Fileame already in directory: {}'.format(new_name))
            time.sleep(1)
            exit()

        new_filenames.append(new_name)

        num += 1

    return new_filenames

# show the user how it will change the files


def show_rename_files(files, new_filenames):
    for idx in range(len(files)):
        print('{} --> {}'.format(files[idx], new_filenames[idx]))


def rename_files(files, new_filenames):
    for idx in range(len(files)):
        os.rename(os.path.join(cwd, files[idx]),
                  os.path.join(cwd, new_filenames[idx]))


def main():

    things = get_things()

    files = extract_files(things)

    new_filenames = get_new_filenames(files)

    show_rename_files(files, new_filenames)

    print()
    confirm = input('Are you sure you want to continue (Y/n): ').lower()
    print()

    if confirm == 'y':
        rename_files(files, new_filenames)
        print()
        print('Successfully Completed')
    else:
        print('Program Rejected')

    time.sleep(1.25)

    return


if __name__ == "__main__":

    cwd_path = sys.argv[1]
    cwd = cwd_path.split('\\')[-1]

    if not os.path.isdir(cwd_path):
        print('Not a directory')
        time.sleep(1)
        exit()

    get_sep()
    get_start_num()
    main()
