class PatternStore:
    """
    Persists synthesized patterns.
    """
    def __init__(self):
        self.patterns = {}

    def save_pattern(self, name: str, data: dict):
        self.patterns[name] = data

    def get_pattern(self, name: str):
        return self.patterns.get(name)
