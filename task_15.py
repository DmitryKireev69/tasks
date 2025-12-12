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
        """Возвращает перестановку для шифрования"""
        permutation = sorted(range(len(self.key)), key=lambda i: self.key[i])
        if not self.decrypt:
            return permutation

        inv = [0] * self.block_size
        for item, p in enumerate(permutation):
            inv[p] = item
        return inv

    def __iter__(self):
        """Итератор по блокам (зашифрованным или расшифрованным)."""
        padded = self.text.ljust(
            len(self.text) + (-len(self.text) % self.block_size)
        )
        total_blocks = len(padded) // self.block_size

        for block_index in range(total_blocks):
            block = padded[block_index * self.block_size:(block_index + 1) * self.block_size]

            result = ''.join(block[self.permutation[j]] for j in range(self.block_size))

            if self.decrypt and block_index == total_blocks - 1:
                result = result.rstrip()

            yield result
