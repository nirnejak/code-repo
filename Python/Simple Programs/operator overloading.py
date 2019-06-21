def main():
    a = Name('Jittu')
    b = Name('Jittu')

    if a == b:
        print("hell yeah, I did it ;)")
    else:
        print("oh no shoot! :(")

class Name():
    def __init__(self, name):
        self.name = name
    def __eq__(self, obj):
        if isinstance(obj, Name):
            return self.name == obj.name
        return NotImplemented

if __name__ == '__main__':
    main()
