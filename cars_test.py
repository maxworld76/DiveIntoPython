import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self.photo_file_ext = photo_file_name.split(".")[-1]
        # validate
        if self.carrying <=0:
            raise ValueError(f"carrying value must be > 0")
        if brand == '':
            raise ValueError(f"brand value cannot be empty")
        if self.photo_file_ext not in ("jpg", "jpeg", "png", "gif"):
            raise ValueError(f"photo_file_name extension is not valid: '{self.photo_file_ext}'")
        if ".".join(photo_file_name.split(".")[:-1]) == '':
            raise ValueError(f"photo_file_name is invalid: '{self.photo_file_name}'")

    def get_photo_file_ext(self):
        return '.' + self.photo_file_ext

    def __str__(self):
        return f"brand: {self.brand}, photo_file_name: {self.photo_file_name}, carrying: {self.carrying}"


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'
        if self.passenger_seats_count <= 0:
            raise ValueError("passenger_seats_count must be >= 1")

    def __str__(self):
        return super().__str__() + f", passenger_seats_count: {self.passenger_seats_count}"


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_length, self.body_width, self.body_height = 0.0, 0.0, 0.0
        try:
            dim = [float(n) for n in body_whl.split('x')]
            self.body_length, self.body_width, self.body_height = dim
        except ValueError:
            pass

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length

    def __str__(self):
        return super().__str__() \
               + f", body_length: {self.body_length}, body_width: {self.body_width}, body_height {self.body_height} "


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra: str):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra
        if extra == '':
            raise ValueError("attr extra for spec_machine cannot be empty")

    def __str__(self):
        return super().__str__() + f", extra: {self.extra}"


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if len(row) == 7:
                try:
                    car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row
                    if car_type == 'car':
                        car_list.append(Car(brand, photo_file_name, carrying, passenger_seats_count))
                    elif car_type == 'truck':
                        car_list.append(Truck(brand, photo_file_name, carrying, body_whl))
                    elif car_type == 'spec_machine':
                        car_list.append(SpecMachine(brand, photo_file_name, carrying, extra))
                except ValueError:
                    pass
    return car_list


if __name__ == '__main__':
    cars = get_car_list('coursera_week3_cars.csv')
    for c in cars:
        print(type(c), c)
