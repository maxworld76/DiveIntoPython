import os

class DirectorySize:

    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))

class Directory:

    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute


if __name__ == '__main__':
    d = Directory('D:\Projects\Python\DiveIntoPython')
    print(f'size of {d.dirname} : {d.size}')
