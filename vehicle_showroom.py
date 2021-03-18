print('Vehicle Management')
# Vehicle Class


class Vehicle_Insertion:
    def __init__(self):
        self._type = ''
        self._model = ''
        self._engine = ''
        self._power = 0
        self._tire = 0
        self._weight = 0
        self._turbo = 0

    # Adding vehicle
    def create_vehicle(self, vehicle_choice, engine_choice):

        try:
            # Assigning the type of vehicle
            if vehicle_choice == '1':
                vehicle_type = 'Normal Vehicle'
                # Engine Selection
                if engine_choice == '1':
                    engine_type = 'Oil'
                elif engine_choice == '2':
                    engine_type = 'Gas'
                elif engine_choice == '3':
                    engine_type = 'Diesel'
                else:
                    print('Wrong')

                weight = 'N/A'
                turbo = 'N/A'

            elif vehicle_choice == '2':
                vehicle_type = 'Sports Car'
                engine_type = 'Oil'
                weight = 'N/A'
                turbo = float(input('Enter Turbo (Bar): '))

            elif vehicle_choice == '3':
                vehicle_type = 'Heavy Vehicle'
                engine_type = 'Diesel'
                weight = float(input('Enter Weight (Kg): '))
                turbo = 'N/A'

            else:
                print('Wrong Vehicle Selection')

            self._type = vehicle_type
            self._model = input('Enter Vehicle Model Number: ')
            self._engine = engine_type
            self._power = int(input('Enter Engine Power: '))
            self._tire = int(input('Enter Tire Size: '))
            self._weight = weight
            self._turbo = turbo
            return True

        except Exception:
            print('Please Enter Accurate Vehicle Information')
            return False

    def __str__(self):
        return '\t'.join(str(a) for a in [self._type, self._model, self._engine, self._power, self._tire, self._weight, self._turbo])


# Vehicle Management Main
class Vehicle_Management:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle_choice, engine_choice):
        vehicle = Vehicle_Insertion()
        if vehicle.create_vehicle(vehicle_choice, engine_choice) == True:
            self.vehicles.append(vehicle)
            print()
            print('The Vehicle Data Has Been Successfully Inserted!')

    def vehicle_display_panel(self):
        print('\t'.join(['', 'Type', '', 'Model', 'Engine',
              'Power', 'Tire', 'Weight(kg)', 'Turbo(bar)']))
        for idx, vehicle in enumerate(self.vehicles):
            print(idx + 1, end='\t')
            print(vehicle)


inventory = Vehicle_Management()

# Main App
while True:
    # Application Navigation choices
    print('Choice 1: Add Vehicle to Showroom')
    print('Choice 2: View Current Showroom')
    print('Choice 3: Delete Vehicle from Inventory')
    print('Choice 4: Quit')
    user_choice = input('Please enter your choice of action: ')

    # Adding Vehicle
    if user_choice == '1':
        # User choice for vehicle choice
        print('Choice 1: Add A Normal Vehicle')
        print('Choice 2: Add A Sports Vehicle')
        print('Choice 3: Add A Heavy Vehicle')
        vehicle_choice = input('Please Choose The Vehicle You Wish To Enter: ')

        # Engine Type for normal vehicle
        if vehicle_choice == '1':
            print('Choice 1: Oil Engine')
            print('Choice 2: Gas Engine')
            print('Choice 3: Diesel Engine')
            engine_choice = input('Please Enter Vehicle Engine: ')

        inventory.add_vehicle(vehicle_choice, engine_choice)

        # Viewing inventory records
    elif user_choice == '2':
        if len(inventory.vehicles) < 1:
            print('No Vehicles in the showroom')
            continue

        inventory.vehicle_display_panel()

        # Removing single record
    elif user_choice == '3':
        if len(inventory.vehicles) < 1:
            print('No Vehicles in the showroom')
            continue

            # Display of inventory
        inventory.vehicle_display_panel()
        deleted_vehicle = int(input('Please Enter Vehicle Number To Delete: '))

        # Removing selected inventory record
        if deleted_vehicle - 1 > len(inventory.vehicles):
            print('Invalid Vehicle Number')
        else:
            inventory.vehicles.remove(inventory.vehicles[deleted_vehicle - 1])
            print()
            print('The Vehicle Data Has Been Successfully Deleted')

        # Breaking the loop to exit
    elif user_choice == '4':
        print('Exiting From The Vehicle Management System')
        break

        # Choice Error Handling
    else:
        print('Invalid Choice Input. Please Enter A Valid Choice')
