class FileInput:
    def __init__(self, filepath):
        self.filepath = filepath

    def collect_data(self):
        with open(self.filepath, "r") as f:
            return {"data": f.read().strip()}