from typing import Final, NoReturn, Tuple
from uuid import uuid4

type Str = str
type Int = int
type NoInteraction = NoReturn | None
type Tires = Tuple[Tire, ...]

class Tire:
    # Size is the starting size of the tire... starts at 0
    def __init__(self, size: Int):
        self.tire_size: Final = size

        self.__size: Int = 0
        self.prev: Int = 0

    @property
    def size(self) -> Int:
        return self.__size

    @size.setter
    def size(self, amount: Int) -> NoReturn:
        raise Exception('Go through the pump method!')

    def get_pressure(self) -> Int:
        return self.__size

    # Pump also releases pressure!!
    def pump(self, amount: Int) -> NoInteraction:
        if (tmp := self.__size + amount) < 0:
            raise Exception(f'Negative pressure with {tmp}')

        self.__size += amount

    def __str__(self) -> Str:
        return f'This {self.tire_size} tire has {self.__size} psi in it!'
        
class Engine:
    def __init__(self, fuel_type: Str) -> None:
        self.fuel_type: Final = fuel_type
        
        self.__state: Str = 'stopped'

    @property
    def state(self) -> Str:
        return self.__state

    @state.setter
    def state(self, option: Str) -> NoReturn:
        raise Exception('Cant set internal state!')

    @state.deleter
    def state(self) -> NoReturn:
        raise Exception('Cant delete the internal state var!')

    def start(self) -> NoInteraction:
        if self.__state == 'running':
            print('Already on!')
        else:
            self.__state = 'running'

    def stop(self) -> NoInteraction:
        if self.__state == 'stopped':
            print('Already stopped!')
        else:
            self.__state = 'stopping'

    def get_state(self) -> Str:
        return self.__state

class Vehicle:
    def __init__(self, VIN: Str, engine: Engine, tires: Tires, no_tires: Int):
        self.vin: Final = VIN
        self.engine: Engine = engine
        self.tires: Tires = tires
        self.number_of_tires: Final = no_tires

if __name__ == "__main__":
    # Front (L, R) Back (L, R)
    atv_tires = tuple([Tire(15) for _ in range(4)])
    atv_engine = Engine('Electric')
    atv = Vehicle(str(uuid4()), atv_engine, atv_tires, 4)

    db_tires = tuple([Tire(18) for _ in range(2)])
    db_engine = Engine('2 Stroke, Single Cylinder, Gasoline')
    dirt_bike = Vehicle(str(uuid4()), db_engine, db_tires, 2)

    for obj, v_type in zip((atv, dirt_bike), ('ATV', 'Dirt Bike')):
        print(f'Working a {v_type} with a VIN of{obj.vin}')
        print('Putting air in the tires!')
        for idx in range(obj.number_of_tires):
            obj.tires[idx].pump(obj.tires[idx].tire_size)
            print(f'Tire {idx + 1} has an air pressure of {obj.tires[idx].get_pressure()}')

        obj.engine.start()
        print(f'Engine state: {obj.engine.get_state()}')
        obj.engine.stop()
        print(f'Engine state: {obj.engine.get_state()}')
        if v_type == 'ATV':
            print()
