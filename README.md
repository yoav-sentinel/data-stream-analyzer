# Data Stream Analyzer

## Introduction

The goal of this script is to read input data from a file (or standard input), and output the IDs associated with the
top X largest values.

Each input line has two fields, a string and a floating-point number, separated by a space.

## Getting Started

Follow these steps to install and set up the project:

### Prerequisites

Ensure that you have the following software installed on your system:

- Python 3.6 or later

### Steps

1. Clone the repository to your local machine:

```
git clone https://github.com/yoav-sentinel/data-stream-analyzer.git`
```

2. Navigate to the project directory:

```
cd data-stream-analyzer
```

3. Create a virtual environment and activate it:

```
python3 -m venv venv
. venv/bin/activate
```

4. Install the required dependencies:

```
pip install -r requirements.txt
```

### Usage

You can run the script using the following command:

```
python top_x_uids.py X [-f FILE]
```

Arguments:

X: The number of top values to find. X should be a positive integer.

FILE (optional): The path to the file to read the input data from. If no file is specified, the script will read from
standard input.

### Examples

Print the script command line documentation:

```
python top_x_uids.py --help
```

Running the script with a file as input:

```
python top_x_uids.py 5 -f input.txt
```

Running the script with standard input:

```
python top_x_uids.py 5
```

After running the command, you can then type your input directly into the terminal. End the input by pressing CTRL+D.

## How It Works

The script works by using a min heap data structure to keep track of the top X values and their associated IDs. It reads
each line of the input, validates it, and then either adds it to the heap (if the heap has less than X items), or
compares it to the smallest item in the heap (if the heap has X items) and replaces it if it's larger. This way, the
heap always contains the top X values, and the root of the heap is always the smallest value among the top values.

## Error Handling

The script includes error handling for the following scenarios:

- Invalid arguments (non-positive X, non-existent file, no read permissions, etc)

- Malformed input lines

- Non-numeric values

In any of these cases, it will print an error message and exit with a status code of 2.

## Time and Space Complexity

The time complexity of the script is O(n log x + p), where n is the number of lines in the file, x is the heap size, and
p is the length of the arguments string. The space complexity is O(x + p), dominated by the size of the heap in memory
and the space required to store the program arguments.

In practical terms, p is typically small and its contribution to the time and space complexity can often be ignored.

Therefore, the time complexity of the script would be O(n log x) and the space complexity would be O(x).

## Testing

This project includes comprehensive unit tests to ensure correct functionality. These tests are found in the
`test_main.py` and `test_top_x_uids.py` files.

`test_main.py` contains tests for the command-line interface, including the handling of arguments and input/output
redirection.

`test_top_x_uids.py` contains tests for the core logic of finding the top X UIDs, including tests for validating input
lines and finding the top X UIDs from an input file or stream.

To run tests, run the following in the project root:

```
pytest
```

## Duplicate UID Handling

The script currently operates under the assumption that UID values are unique in the input file (Ignore duplicates).
However, there is a possibility that the input file may contain duplicate UIDs. The following alternatives were
considered for handling such cases:

### Reject duplicate UIDs:

Raise an error if a duplicate UID is encountered. This approach ensures the uniqueness of UIDs but could interrupt the
script's operation with valid input that happens to contain duplicates. However, this comes with a major computational
cost, increasing the space complexity by O(n) to keep track of the input UIDs, which is inefficient for extremely large
files.

### Update existing UIDs:

If a duplicate UID is encountered, update the value associated with that UID in our data structure. This approach
ensures we always have the most recent data but also increases the computational cost. Specifically, it increases the
time complexity for processing each line from O(log X) to O(X) in the worst-case scenario.

### Ignore duplicates:

If a duplicate UID is encountered, simply ignore the duplication and address it as any other line. This is the most
efficient way in terms of computation but could affect the output as we may have duplicate UIDs in the final result.
This is the approach currently taken.

## Notes

1. The script does not include tests to cover read permission errors on the input file, as behavior may vary across
   different operating systems, potentially causing issues with the file system.
2. Complexity comments found within top_x_uids.py are for educational purposes relating to this specific task. These
   comments typically wouldn't be included in a production code base.
3. If the input contains multiple entries with the smallest maximum values, the script will only return the first
   instance encountered.
4. To maintain the lightweight nature of the project and ensure rapid testing, performance tests for extremely large  
   input files have not been included. Users are encouraged to consider the time and space complexities mentioned when
   dealing with larger inputs.