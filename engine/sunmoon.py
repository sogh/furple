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
        # 5 minutes per phase change, convert to milliseconds
        self.phase_length_millis = 1 * 30 * 1000
        self.last_phase_change = 0

    def Update(self, t):
        if t - self.last_phase_change > self.phase_length_millis:
            self.phase = self.phase + 1
            self.last_phase_change = t
        if self.phase >= len(self.phase_strings):
            self.phase = 0

    def toString(self):
        return self.phase_strings[self.phase]
        
