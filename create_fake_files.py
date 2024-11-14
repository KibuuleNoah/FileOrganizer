import os
from string import ascii_letters
from random import choices, randrange

exts = [
    '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.pdf',
    '.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma', '.zip', '.rar',
    '.tar', '.gz', '.7z', '.bz2', '.xls', '.xlsx', '.xlsm', '.csv', '.ods'
]

if not os.path.isdir("Fake_dir"):
    os.mkdir("Fake_dir")

for i in range(100):
    ext = exts[randrange(0, len(exts) - 1)]
    name = "".join(choices(ascii_letters, k=10))

    filename = name + ext
    with open("Fake_dir/" + filename, "w") as f:
        ...
