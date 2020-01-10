"""Your goal in this kata is to create complete the mouth_size method this method take one argument animal which corresponds to the animal encountered by frog. If this one is an alligator (case insensitive) return small otherwise return wide."""

def mouth_size(animal):
    return "small" if animal.lower() == "alligator" else "wide"
