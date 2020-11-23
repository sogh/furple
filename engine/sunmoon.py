class SunMoon:
    def __init__(self):
        self.phase = 0
        self.phase_strings = [
            "The sun is high in the sky.",
            "The sun is setting.",
            "The moon is rising.",
            "The moon is bright.",
            "Everything is dark.",
            "The sun begins to rise.",
        ]

    def Update(self, t):
        if t % 4 == 0:
            self.phase = self.phase + 1
        if self.phase >= len(self.phase_strings):
            self.phase = 0

    def toString(self):
        return self.phase_strings[self.phase]
        
