import argparse
import heapq
import sys


# TODO validations
# 1. No file and empty input stream - print something instead of empty list
# 2. Invalid UID format
# 3. Invalid value format - non float
# 4. Invalid row format (split values is not exactly 2)
# 5. Duplicated uid
# 6. note that multiple lowest max values will only show the first uid if the heap is already full

def validate_input(line):
    try:
        uid, value = line.split()
    except ValueError:
        raise ValueError(f"Error: Malformed input line:\n{line}")
    try:
        value = float(value)
    except ValueError:
        raise ValueError(f"Error: Not numeric value `{value}`")

    return uid, value


def find_top_x_uids(file, x):
    heap = []
    uid_dict = {}  # keep track of UIDs in the heap and their values to avoid input UIDs duplication.

    for line in file:
        uid, value = validate_input(line)

        # If UID already in heap and value is larger than its current value, update it.
        if uid in uid_dict:
            if value > uid_dict[uid]:
                heap.remove((uid_dict[uid], uid))
                heapq.heapify(heap)
                heapq.heappush(heap, (value, uid))
                uid_dict[uid] = value

        elif len(heap) < x:
            # If heap size is smaller than X and the UID is not in the heap, push it.
            uid_dict[uid] = value
            heapq.heappush(heap, (value, uid))

        else:
            # If value is larger than the smallest value in heap,
            # pop heap and push new value into heap.
            if value > heap[0][0]:
                _, removed_uid = heapq.heappop(heap)
                uid_dict.pop(removed_uid)
                heapq.heappush(heap, (value, uid))
                uid_dict[uid] = value

    return [uid for _, uid in heap]


def main():
    parser = argparse.ArgumentParser(description="Find the IDs associated with the top X largest values.")
    parser.add_argument('-f', '--file', type=str, help='Path to the file.')
    parser.add_argument('-x', type=int, required=True, help='Number of top values to find.')
    args = parser.parse_args()

    if args.x <= 0:  # Handle invalid number of top values
        print("Error: X must be a positive integer.")
        return

    try:
        if args.file:
            with open(args.file) as f:
                print(find_top_x_uids(f, args.x))
        else:
            print(find_top_x_uids(sys.stdin, args.x))
    except FileNotFoundError:  # Handle nonexistent file
        print(f"Error: File {args.file} not found.")
    except ValueError as e:
        print(e.args[0])


if __name__ == "__main__":
    main()
