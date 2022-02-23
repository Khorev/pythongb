# Задание 8-456. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс Оргтехника, который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# Продолжить работу над первым заданием. Разработать методы,
# отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.
#
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Warehouse:
    __storage = []
    __summary = {}

    def push(self, equipment):
        if not isinstance(equipment, OfficeEquipment):
            raise Exception('Склад может принимать только оргтехнику')
        self.__storage.append(equipment)
        if self.__summary.get(equipment.type) is not None:
            self.__summary[equipment.type] += 1
        else:
            self.__summary.setdefault(equipment.type, 1)

    def report_items(self):
        for item in self.__storage:
            print(item)

    def report_total(self):
        for k, v in self.__summary.items():
            print(f'{k}: {v} шт')


class OfficeEquipment:
    def __init__(self, type: str, model: str, cost: float, sn: str):
        self.type = str(type)
        self.model = str(model)
        self.cost = float(cost)
        self.sn = str(sn)

    def __str__(self):
        return f"{self.type} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, model: str, cost: float, is_colorful: bool, sn: str):
        self.is_colorful = is_colorful
        super().__init__('Принтер', model, cost, sn)


class MFP(OfficeEquipment):
    def __init__(self, model: str, cost: float, dpi: str, sn: str):
        self.dpi = dpi
        super().__init__('МФУ', model, cost, sn)


class Scanner(OfficeEquipment):
    def __init__(self, model: str, cost: float, is_colorful: bool, dpi: str, velocity: int, sn: str):
        self.is_colorful = is_colorful
        self.dpi = dpi
        self.velocity = velocity
        super().__init__('Сканер', model, cost, sn)


if __name__ == '__main__':
    printer01 = Printer('Epson L805', 28499, True, 'EPL123456789')
    printer02 = Printer('Epson L1800 ', 69999, False, 'EPL987654321')
    MFP01 = MFP('HP LaserJet M141w', 15999, '4800x4800', 'MFPHP123456789')
    MFP02 = MFP('HP LaserJet Pro M28a', 13999, '2400x2400', 'MFPHP987654321')
    scanner01 = Scanner('Plustek OpticFilm 8100', 24999, True, '4800x600', 8, 'POF123456789')
    scanner02 = Scanner('Fujitsu ScanSnap S1100i', 14299, False, '2400x600', 30, 'FSS123456789')
    scanner03 = Scanner('Fujitsu Fi-7260', 101336, False, '1200x1200', 22, 'FF987654321')

    warehouse = Warehouse()
    warehouse.push(printer01)
    warehouse.push(printer02)
    warehouse.push(MFP01)
    warehouse.push(MFP02)
    warehouse.push(scanner01)
    warehouse.push(scanner02)
    warehouse.push(scanner03)

    warehouse.report_items()
    warehouse.report_total()
