class BlockTranspositionCipher:
    """
    Класс для шифрования и дешифрования методом блочной перестановки.
    """

    def __init__(self, text: str, key: str, decrypt: bool = False):
        self.text = text
        self.key = key.lower()
        self.decrypt = decrypt
        self.validate_key()
        self.block_size = len(key)
        self.permutation = self._get_permutation()

    def validate_key(self):
        """Валидация ключа"""
        if not self.key.isalpha():
            raise ValueError("Ключ должен содержать только английские буквы")
        if len(set(self.key)) != len(self.key):
            raise ValueError("Буквы в ключе должны быть уникальны")

    def _get_permutation(self) -> list[int]:
        """Возвращает перестановку для шифрования и дешифрования"""
        permutation = sorted(range(self.block_size), key=lambda i: self.key[i])

        if self.decrypt:
            inverse = [0] * self.block_size
            for index, p in enumerate(permutation):
                inverse[p] = index
            return inverse
        return permutation

    def __iter__(self):
        """Итератор по блокам (зашифрованным или расшифрованным)."""
        padding_needed = -len(self.text) % self.block_size
        padded_text = self.text.ljust(len(self.text) + padding_needed)

        for start in range(0, len(padded_text), self.block_size):
            block = padded_text[start:start + self.block_size]

            encrypted_block = [''] * self.block_size
            for index in range(self.block_size):
                encrypted_block[self.permutation[index]] = block[index]

            result = ''.join(encrypted_block)
            if self.decrypt and start == len(padded_text) - self.block_size:
                result = result.rstrip()

            yield result
