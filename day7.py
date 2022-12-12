import os
from inputreader import aocinput
from typing import List, Tuple, Optional, Dict


class Folder:
    def __init__(self, name: str, parent: Optional['Folder']):
        self.name = name
        self.parent = parent
        self._size = 0
        self.folders: Dict[str: 'Folder'] = {}
        self.total_size = 0

    def add_file(self, size: int):
        self._size += size

    def add_folder(self, name: str):
        self.folders[name] = Folder(name, self)

    def get_folder(self, name) -> 'Folder':
        return self.folders[name]

    def get_total_size(self) -> int:
        if not self.total_size:
            self.total_size = sum([folder.get_total_size() for folder in self.folders.values()]) + self._size
        return self.total_size

    def get_folders(self) -> List['Folder']:
        return list(self.folders.values())


def calculate_foldersize(data: List[str]) -> Tuple[int, int]:
    basefolder = Folder('/', None)
    current_folder = basefolder
    for line in data:
        parts = line.split()
        if parts[0] == '$':
            if parts[1] == 'cd':
                if parts[2] == '/':
                    current_folder = basefolder
                elif parts[2] == '..':
                    current_folder = current_folder.parent
                else:
                    current_folder = current_folder.get_folder(parts[2])
        elif parts[0] == 'dir':
            current_folder.add_folder(parts[1])
        else:
            current_folder.add_file(int(parts[0]))

    folder_sizes = []

    def get_sizes(folder: Folder):
        folder_sizes.append(folder.get_total_size())
        for f in folder.get_folders():
            get_sizes(f)

    get_sizes(basefolder)
    small_folders = [size for size in folder_sizes if size <= 100000]
    to_remove_size = min([folder_size for folder_size in folder_sizes if folder_size >= max(folder_sizes) - 40000000])

    return sum(small_folders), to_remove_size


def main(day):
    data = aocinput(day)
    result = calculate_foldersize(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
