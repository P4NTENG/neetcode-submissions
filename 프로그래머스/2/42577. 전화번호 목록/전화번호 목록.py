class MyString:
    def __init__(self, value):
        self.value = value

    def __hash__(self) -> int:
        return hash(self.value)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, MyString):
            return self.value == other.value
        if isinstance(other, str):
            return self.value == other
        return False

    def __iter__(self):
        yield from self.value

    def __len__(self):
        return len(self.value)

    def __getitem__(self, key):
        return MyString(self.value[key])


def solution(phone_book):
    phone_set = {MyString(phone) for phone in phone_book}

    for phone_number in phone_set:
        for num in range(1, len(phone_number)):
            if phone_number[:num] in phone_set:
                return False

    return True