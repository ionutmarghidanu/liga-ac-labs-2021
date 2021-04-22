def read_lines(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            print(line)

def read_lines_generator_function(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line

if __name__ == '__main__':
    #read_lines('pg100.txt')
    lines = read_lines_generator_function('pg100.txt')
    # for line in lines:
    #     print(line)
    try:
        while True:
            print(next(lines))
    except StopIteration:
        print('File was read successfully')

