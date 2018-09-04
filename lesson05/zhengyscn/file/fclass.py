class fileopen(object):
    def __init__(self, filename, mode):
        print("__init__")
        self.filename = filename
        self.mode = mode
        self.fd = None

    def __enter__(self):
        print("__enter__")
        self.fd = open(self.filename, self.mode)
        return self.fd

    def __exit__(self, exc_type, exc_value, traceback):
        print("__exit__")
        self.fd.close()




# obj = fileopen('../ngxlog/access.log', 'r')
# obj.__enter__()

with fileopen('../ngxlog/access.log', 'r') as fd:
    pass