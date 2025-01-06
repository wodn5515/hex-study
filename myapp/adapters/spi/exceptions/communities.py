class BoardEntityNotFound(Exception):
    def __init__(self):
        super().__init__("Board Not Found")


class UserEntityNotFound(Exception):
    def __init__(self):
        super().__init__("Author Not Found")
