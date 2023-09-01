class GreenLineTransport:
    total_bus = 0
    total_water_bus = 0

    def __init__(self, name, max_passenger):
        self.name = name
        self.max_passenger = max_passenger

    @classmethod
    def details(cls):
        return f'Total Bus: {cls.total_bus}\nTotal Cruise: {cls.total_water_bus}'


class GreenLine_Bus(GreenLineTransport):
    bus_info = {}

    def __init__(self, name, route, max_passenger):
        super().__init__(name, max_passenger)
        self.route = route
        GreenLine_Bus.total_bus += 1
        GreenLine_Bus.bus_info[self.name] = {'Route': self.route, 'Max Passenger': self.max_passenger}

    def changeRoutes(self, new_route):
        self.route = new_route
        GreenLine_Bus.bus_info[self.name]['Route'] = self.route

    @classmethod
    def details(cls):
        for bus_name, bus_data in cls.bus_info.items():
            print(f'{bus_name}: {bus_data}')
        print('-----------')


class GreenLine_WaterBus(GreenLineTransport):
    water_bus_info = {}

    def __init__(self, name, route, max_passenger, departure_time=None):
        super().__init__(name, max_passenger)
        self.route = route
        self.departure_time = departure_time
        GreenLine_WaterBus.total_water_bus += 1
        GreenLine_WaterBus.water_bus_info[self.name] = {'Route': self.route, 'Max Passenger': self.max_passenger, 'Departure Time': self.departure_time}

    @classmethod
    def details(cls):
        for water_bus_name, water_bus_data in cls.water_bus_info.items():
            print(f'{water_bus_name}: {water_bus_data}')
        print('-----------')

    @classmethod
    def waterBus_Creation(cls, info_string):
        info_list = info_string.split('_')
        name = info_list[0]
        route = info_list[1]
        max_passenger = int(info_list[2])
        departure_time = info_list[3]
        return cls(name, route, max_passenger, departure_time)


gL1 = GreenLineTransport('Green Line Paribahan', 2000)
print(GreenLineTransport.details())
print('-----------1-----------')

print(f'Green Line Bus Info: {GreenLine_Bus.bus_info}')
bus1 = GreenLine_Bus('Bus 1', 'Dhaka-Khulna', 27)
print('-----------2-----------')
GreenLine_Bus.details()

bus2 = GreenLine_Bus('Bus 2', 'Barishal-Rangamati', 32)
print('-----------3-----------')
GreenLine_Bus.details()

print('-----------4-----------')
bus1.changeRoutes('Dhaka-Rajshahi')
print('-----------5-----------')

print(f'Green Line Water Bus Info: {GreenLine_WaterBus.water_bus_info}')
water_bus1 = GreenLine_WaterBus('Water Bus 1', 'Dhaka-Bhola', 400)
print('-----------6-----------')
GreenLine_WaterBus.details()

print('-----------7-----------')
water_bus2 = GreenLine_WaterBus.waterBus_Creation('Water Bus 2_Bhola-Dhaka_350_10:30 AM')
print('-----------8-----------')
GreenLine_WaterBus.details()

print('-----------9-----------')
water_bus3 = GreenLine_WaterBus('Water Bus 3', 'Barishal-Dhaka', 430, '7:30 AM')
print(GreenLineTransport.details())
