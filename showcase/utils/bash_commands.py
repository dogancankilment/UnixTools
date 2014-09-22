# import subprocess
import os


def command_entry(command):
    command = str(command) + "> mynewfile.txt"
    os.system(command)
    read_data = command_analysis()
    return read_data


def command_analysis():
    with open('mynewfile.txt', 'r') as open_file:
        read_data = open_file.readlines()

    open_file.close()
    return read_data

if __name__ == '__main__':
    command_entry()