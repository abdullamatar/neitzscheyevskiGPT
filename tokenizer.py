class TextProcessor:
    def __init__(self, filename: str) -> None:
        with open(filename, "r", encoding="utf-8") as f:
            self.text: str = f.read()
        self.chars: list[str] = sorted(list(set(self.text)))
        self.vocab_size: int = len(self.chars)
        self.stoi: dict = {c: i for i, c in enumerate(self.chars)}
        self.itos: dict = {i: c for i, c in enumerate(self.chars)}

    def map_to_int(self, text: str) -> list[int]:
        return [self.stoi[c] for c in text]

    def decode_mapping(self, integer_representation: list[int]) -> str:
        return "".join([self.itos[i] for i in integer_representation])
