class Directory:
    def __init__(self, name, parent_directory=None):
        self.name = name
        self.parent_directory = parent_directory
        self.subdirectories = []
        self.files = []

    def size(self):
        size = 0
        for file in self.files:
            size += file.size
        for subdirectory in self.subdirectories:
            size += subdirectory.size()
        return size


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


listing_directory = False
file_system = Directory('/')
current_directory = file_system


def parse_command(line):
    global current_directory, listing_directory

    if line == '$ cd /':
        current_directory = file_system
        return

    split = line.split(' ')

    command = split[1]

    if command == 'cd':
        argument = split[2]

        if argument == '..':
            current_directory = current_directory.parent_directory
        else:
            current_directory = next(
                x for x in current_directory.subdirectories if x.name == argument)

    elif command == 'ls':
        listing_directory = True


def parse_directory(line):
    global current_directory

    size_or_type, name = line.split(' ')

    if size_or_type == 'dir':
        try:
            d = next(x for x in current_directory.subdirectories if x.name == name)
        except:
            current_directory.subdirectories.append(
                Directory(name, current_directory))
        return

    try:
        f = next(x for x in current_directory.files if x.name == name)
    except:
        current_directory.files.append(
            File(name, int(size_or_type)))


def find_small_directories(directory, max_size):
    small_directories = []

    if directory.size() < max_size:
        small_directories.append(directory)

    for subdirectory in directory.subdirectories:
        small_directories += find_small_directories(subdirectory, max_size)

    return small_directories


def find_smallest_directory_for_deletion(directory, min_size):
    smallest_directory = directory

    if directory.size() >= min_size and directory.size() < smallest_directory.size():
        smallest_directory = directory

    for subdirectory in directory.subdirectories:
        d = find_smallest_directory_for_deletion(subdirectory, min_size)
        if d.size() < smallest_directory.size() and d.size() >= min_size:
            smallest_directory = d

    return smallest_directory


def main():
    global file_system, listing_directory
    with open('input.txt') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()

        if '$' in line:
            listing_directory = False
            parse_command(line)
        elif listing_directory:
            parse_directory(line)

    small_directories = find_small_directories(file_system, 100000)
    sum_of_small_directories = sum(map(lambda x: x.size(), small_directories))
    print(f'part 1: {sum_of_small_directories}')

    total_space = 70000000
    needed_space = 30000000
    available_space = total_space - file_system.size()
    directory_size_at_least = needed_space - available_space

    directory_to_be_deleted = find_smallest_directory_for_deletion(
        file_system, directory_size_at_least)
    print(f'part 2: {directory_to_be_deleted.size()}')


if __name__ == '__main__':
    main()
