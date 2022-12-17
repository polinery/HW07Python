''' 4. Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат. '''


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f'\nМашина {self.name} поехала'

    def stop(self):
        return f'\nМашина {self.name} остановилась'

    def turn(self, direction):
        return f'\nМашина {self.name} повернула {direction}'

    def show_speed(self):
        return f'\nТекущая скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nСкорость превышена! Текущая скорость {self.speed}'
        else:
            return f'\nТекущая скорость {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nСкорость превышена! Текущая скорость {self.speed}'
        else:
            return f'\nТекущая скорость {self.speed}'


class PoliceCar(Car):
    pass


town = TownCar('Mazda', 'голубая', 70, False)
print('\n1:' + town.go(), town.show_speed(), town.turn('налево'),
      town.turn('направо'), town.stop())

sport = SportCar('AudiRS', 'красная', 170, False)
print('\n2:' + sport.go(), sport.show_speed(), sport.turn('налево'),
      sport.stop())

work = WorkCar('WAZ', 'зеленая', 30, False)
print('\n3:' + work.go(), work.show_speed(), work.turn('направо'),
      work.stop())

police = PoliceCar('Kia', 'желтая', 100, True)
print('\n4:' + police.go(), police.show_speed(), police.turn('напарво'),
      police.stop())
