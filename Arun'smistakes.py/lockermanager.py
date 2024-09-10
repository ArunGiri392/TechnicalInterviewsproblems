class Locker:
    def __init__(self, locker_id, size):
        self.locker_id = locker_id
        self.size = size
        self.is_occupied = False
        self.package_id = None

    def occupy(self, package_id):
        self.is_occupied = True
        self.package_id = package_id

    def release(self):
        self.is_occupied = False
        self.package_id = None

class Package:
    def __init__(self, package_id, size):
        self.package_id = package_id
        self.size = size
        self.locker_id = None
        self.pickup_code = None
import random

class LockerManager:
    def __init__(self):
        self.lockers = []
        self.packages = {}

    def add_locker(self, locker):
        self.lockers.append(locker)

    def find_optimal_locker(self, package_size):
        for locker in self.lockers:
            if not locker.is_occupied and locker.size >= package_size:
                return locker
        return None

    def allocate_locker(self, package):
        locker = self.find_optimal_locker(package.size)
        if locker:
            locker.occupy(package.package_id)
            package.locker_id = locker.locker_id
            package.pickup_code = self.generate_code()
            self.packages[package.package_id] = package
            return package.pickup_code, locker.locker_id
        return None

    def release_locker(self, locker_id):
        for locker in self.lockers:
            if locker.locker_id == locker_id:
                locker.release()
                return True
        return False

    def generate_code(self):
        return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
    
class UserInterface:
    def __init__(self, locker_manager):
        self.locker_manager = locker_manager

    def pickup_package(self, code):
        for package in self.locker_manager.packages.values():
            if package.pickup_code == code:
                locker_id = package.locker_id
                self.locker_manager.release_locker(locker_id)
                return f"Package {package.package_id} picked up from locker {locker_id}"
        return "Invalid code"

class DeliveryInterface:
    def __init__(self, locker_manager):
        self.locker_manager = locker_manager

    def place_package(self, package_id, package_size):
        package = Package(package_id, package_size)
        result = self.locker_manager.allocate_locker(package)
        if result:
            code, locker_id = result
            return f"Package {package_id} placed in locker {locker_id}. Pickup code: {code}"
        return "No available locker"

locker_manager = LockerManager()
locker_manager.add_locker(Locker(1, 'medium'))
locker_manager.add_locker(Locker(2, 'large'))

delivery_interface = DeliveryInterface(locker_manager)
user_interface = UserInterface(locker_manager)

# Delivery person places a package
print(delivery_interface.place_package('PKG1', 'medium'))  # Output: Package PKG1 placed in locker 1. Pickup code: XYZ123

# User picks up the package
print(user_interface.pickup_package('XYZ123'))  # Output: Package PKG1 picked up from locker 1