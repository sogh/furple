
class Detritus:

    def __init__(self, description, synonyms=[], obtainable=False):
        self.description = description
        self.synonyms = synonyms
        self.obtainable = obtainable

    def is_obtainable(self):
        return self.obtainable
    
    def get_description(self):
        return self.description
    
    def get_synonyms(self):
        return self.synonyms