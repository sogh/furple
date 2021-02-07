class Graphics:
    def __init__(self):
        self.render_list = []

    def RenderText(self, s):
        if s is None:
            raise TypeError('RenderText only takes String-like arguments.')
        self.render_list.append(s)
    
    def Render(self):
        for r in self.render_list:
            # Fancy renderer, ray tracing coming soon.
            print(r)
            self.render_list = []        
