from tempfile import gettempdir
import os.path
import uuid


class File:
    def __init__(self, path):
        """полный путь до файла на файловой системе
        Если файла с таким путем не существует, он должен быть создан при инициализации."""
        self.path = path
        open(path, 'a').close()

    def read(self):
        """метод read возвращает строку с текущим содержанием файла"""
        with open(self.path, 'r') as f:
            return f.read()

    def write(self, data):
        """метод write принимает в качестве аргумента строку с новым содержанием файла"""
        if 'iter' in self.__dict__:
            raise IOError("write file with active iterator is prohibited, finish iterator first")
        with open(self.path, 'w') as f:
            return f.write(data)

    def __str__(self):
        """возвращать в качестве строкового представления объекта класса File полный путь до файла"""
        return self.path

    def __iter__(self):
        return self

    def iter_generator(self):
        with open(self.path, 'r') as f:
            for line in f:
                yield line

    def __next__(self):
        """поддерживать протокол итерации, причем итерация проходит по строкам файла"""
        if 'iter' not in self.__dict__:
            self.iter = self.iter_generator()
        try:
            return next(self.iter)
        except StopIteration as exc:
            del self.iter
            raise exc

    def __add__(self, other):
        """"сложение объектов типа File, результатом сложения является объект класса File,
        при этом создается новый файл и файловый объект, в котором содержимое второго файла
        добавляется к содержимому первого файла. Новый файл должен создаваться в директории,
        полученной с помощью функции tempfile.gettempdir. Для получения нового пути можно использовать os.path.join."""
        new_file = File(os.path.join(gettempdir(), str(uuid.uuid4())))
        new_file.write(self.read() + other.read())
        return new_file


if __name__ == '__main__':
    obj = File('some_filename')
    obj.write('line1\nline2\nline3\n')
    print(ascii(next(obj)))
    for l in obj:
        print(ascii(l))
    obj.write('new1\nnew2\nnew3\n')
    print(ascii(next(obj)))
    print(ascii(next(obj)))
    print(ascii(next(obj)))




