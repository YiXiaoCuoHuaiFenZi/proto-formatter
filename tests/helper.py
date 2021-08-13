def read_lines(file_path):
    with open(file_path) as f:
        content = f.read()
        content = content.strip()
        lines = content.split('\n')
        return lines


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def write_file(file_path, content):
    with open(file_path, 'w') as f:
        return f.write(content)
