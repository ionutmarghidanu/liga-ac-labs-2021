class FileReader():

    def __init__(self, fileName):
        self.fileName = fileName
        print("Init called")

    def __enter__(self):
        print("Enter called")
        self.file = open(self.fileName, 'r')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit called")
        self.file.close()


with FileReader('ex6.py') as fileReader:
    data = fileReader.readlines()
    for line in data:
        print(data)
    print("In context")

print('Outside context')