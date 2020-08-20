from abc import ABCMeta, abstractmethod


class Hardware(metaclass=ABCMeta):
    pass


class Motherboard(Hardware):
    hardware_name = 'Motherboard'


class Cpu(Hardware):
    hardware_name = 'CPU'


class Memory(Hardware):
    hardware_name = 'Memory'


class PowerSupply(Hardware):
    hardware_name = 'Power Supply'


class Gpu(Hardware):
    hardware_name = 'GPU'


class Desktop(metaclass=ABCMeta):
    def __init__(self):
        self.hardware_list = list()
        self.create_desktop()

    @abstractmethod
    def create_desktop(self):
        pass

    def get_hardware(self):
        return [type(s).hardware_name for s in self.hardware_list]

    def add_hardware(self, hardware: Hardware):
        self.hardware_list.append(hardware)


class DesktopGamer(Desktop):
    def create_desktop(self):
        self.add_hardware(Motherboard())
        self.add_hardware(Cpu())
        self.add_hardware(Gpu())
        self.add_hardware(Memory())
        self.add_hardware(PowerSupply())


class DesktopWork(Desktop):
    def create_desktop(self):
        self.add_hardware(Motherboard())
        self.add_hardware(Cpu())
        self.add_hardware(Memory())
        self.add_hardware(PowerSupply())


if __name__ == "__main__":

    desktop_work = DesktopWork()
    desktop_gamer = DesktopGamer()

    print("Creating Desktop...", type(desktop_work).__name__)
    print("Desktop has hardware --", desktop_work.get_hardware())

    print("Creating Desktop...", type(desktop_gamer).__name__)
    print("Desktop has hardware --", desktop_gamer.get_hardware())
