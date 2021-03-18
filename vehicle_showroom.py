print('Vehicle Management')
# Adding vehicles to


class Vehicle_Insertion:
    def __init__(self):
        self._model = ''
        self._engine = ''
        self._power = 0
        self._tire = 0

    # Adding normal vehicle
    def create_normal_vehicle(self):
        try:
            self._model = input('Enter Vehicle Model Number: ')
            self._engine = input('Enter Engine Type: ')
            self._power = int(input('Enter Engine Power: '))
            self._tire = int(input('Enter Tire Size: '))
            return True
        except Error:
            print('Please Enter Accurate Vehicle Information')
            return False

    def __str__(self):
        return '\t'.join(str(a) for a in [self._model, self._engine, self._power, self._tire])


# Vehicle Management UI
class Vehicle_Management:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self):
        vehicle = Vehicle_Insertion()
        if vehicle.create_normal_vehicle() == True:
            self.vehicles.append(vehicle)
            print()
            print('The vehicle data has been successfully inserted!')

    def vehicle_display_panel(self):
        print('\t'.join(['', 'Model', 'Engine', 'Power', 'Tire']))
        for idx, vehicle in enumerate(self.vehicles):
            print(idx + 1, end='\t')
            print(vehicle)


inventory = Vehicle_Management()

while True:
    print('Choice 1: Add Vehicle to Showroom')
    print('Choice 2: View Current Showroom')
    user_choice = input('Please enter your choice of action: ')

    if user_choice == '1':
        inventory.add_vehicle()

    elif user_choice == '2':
        if len(inventory.vehicles) < 1:
            print('No Vehicles in the showroom')
            continue

        inventory.vehicle_display_panel()

    elif user_choice == '3':
        if len(inventory.vehicles) < 1:
            print('No Vehicles in the showroom')
            continue

        inventory.vehicle_display_panel()
        deleted_vehicle = int(input('Please Enter Vehicle Number To Delete: '))
        if deleted_vehicle - 1 > len(inventory.vehicles):
            print('Invalid Vehicle Number')
        else:
            inventory.vehicles.remove(inventory.vehicles[deleted_vehicle - 1])
            print()
            print('The Vehicle Data Has Been Successfully Deleted')
