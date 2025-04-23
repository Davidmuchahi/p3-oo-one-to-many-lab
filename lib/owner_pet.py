class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=None) -> None:
        self.name = name
        self.pet_type = pet_type
        
        if self.pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        Pet.all.append(self)
        self.owner = owner





class Owner:
     def __init__(self, name) -> None:
        self.name = name

    
     def pets (self):
        return [pet for pet in Pet.all if self == pet.owner]
    
    
     def add_pet (self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet: Must be an instance of Pet class")
        pet.owner = self
    
     def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)