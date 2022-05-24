class Conversation:
    def __init__(self, value):
        self._value = value

    # getting the values
    @property
    def value(self):
        print('---Getting response---')
        return self._value

    # setting the values
    @value.setter
    def value(self, value):
        print('---Setting response---')
        print(value)
        self._value = value

    # deleting the values
    @value.deleter
    def value(self):
        print('---Deleting response---')
        print(self._value)
        del self._value


def main():
    x = Conversation('Hello there, whats your name?')
    print(x.value)

    x.value = 'My name is Javier'
    del x.value
    x.value = 'My name is Samuel'
    del x.value


if __name__ == '__main__':
    main()
