class TextProcessor:
    def __init__(self, filename: str):
        with open(filename, "r", encoding="utf-8") as f:
            self.text = f.read()
        self.chars = sorted(list(set(self.text)))
        self.vocab_size = len(self.chars)
        self.stoi = {c: i for i, c in enumerate(self.chars)}
        self.itos = {i: c for i, c in enumerate(self.chars)}

    def map_to_int(self, text):
        return [self.stoi[c] for c in text]

    def decode_mapping(self, integer_representation):
        return "".join([self.itos[i] for i in integer_representation])
