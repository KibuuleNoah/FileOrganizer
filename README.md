# File Organizer

A Python script that organizes files in a directory based on their file types. The file types and their corresponding folder names are defined in a JSON file (`file_types.json`), allowing easy customization.

## Features

- **Organizes files by type:** Moves files into separate folders based on their extensions.
- **Customizable folder structure:** Define destination folders for specific file types in `file_types.json`.
- **Command-line interface:** Configure source and destination directories through CLI arguments.

## Requirements

- Python 3.6 or higher

## Setup

1. Clone or download the repository.
2. Ensure `file_types.json` exists in the same directory as the script and defines file types like this:
   ```json
   {
     ".jpg": "images",
     ".png": "images",
     ".pdf": "pdfs",
     ".mp3": "music",
     ".zip": "zip",
     ".xlsx": "excel"
   }
   ```

## Usage

Run the script from the command line:

```bash
python organizer.py --rootsrc /path/to/source --rootdst /path/to/destination
```

### Arguments

- `-rs` or `--rootsrc` (required): Directory containing files to organize.
- `-rd` or `--rootdst` (optional): Directory to place organized folders. Defaults to the source directory if not provided.

## Example

```bash
python organizer.py --rootsrc ./Downloads --rootdst ./OrganizedDownloads
```

This example organizes files from `Downloads` into the `OrganizedDownloads` folder. Each file type (e.g., `.jpg`, `.pdf`) will be moved to its designated folder as specified in `file_types.json`.

## Notes

- Ensure `file_types.json` includes all desired file types; files with extensions not listed are ignored.
- `_cache` optimizes folder creation by caching destination folders for each file type, reducing redundant checks.

## License

Free to every one
