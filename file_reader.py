class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return ""


if __name__ == '__main__':
    reader = FileReader('not_exist_file.txt')
    print(reader.read())

    with open('some_file.txt', 'w') as file:
        file.write('some text')
    reader = FileReader('some_file.txt')
    print(reader.read())

