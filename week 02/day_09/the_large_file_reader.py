## 7. Micro Challenge: The Large File Reader

## Goal: Write a generator to read a fake 100GB file line by line.


def fake_file(filepath):
    with open(filepath, "r") as file:
        for line in file:
            yield line

    """
    A generator that reads a file line by line.

    This function opens the file at the given `filepath` and yields one line at a time.
    It allows memory-efficient processing of large files without loading the entire file into memory.

    Args:
        filepath (str): Path to the file to read.

    Yields:
        str: The next line from the file, including the newline character.
    """

for line in fake_file("fake_file.txt"):
    print(line)

