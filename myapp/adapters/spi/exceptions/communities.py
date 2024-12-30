class BoardNotFound(Exception):
    def __init__(self):
        super().__init__("Board Not Found")
