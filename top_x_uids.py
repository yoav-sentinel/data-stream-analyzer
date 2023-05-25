import argparse
import heapq
import sys


def validate_input_line(line):  # O(m) time complexity where m is the length of line
    try:
        uid, value = line.split()  # O(m)
    except ValueError:
        raise ValueError(f"error: malformed input line:\n{line}")
    try:
        value = float(value)
    except ValueError:
        raise ValueError(f"error: not numeric value `{value}`")

    return uid, value


def find_top_x_uids(file, x):  # O(n log x) time complexity where n is number of lines in the file
    heap = []

    for line in file:
        uid, value = validate_input_line(line)  # O(m) where m is length of line

        if len(heap) < x:  # O(n)
            # If heap is not full, push value into heap
            heapq.heappush(heap, (value, uid))  # O(log x)
        elif value > heap[0][0]:
            # If value is larger than the smallest value in heap,
            # pop heap and push new value into heap.
            heapq.heappop(heap)  # O(log x)
            heapq.heappush(heap, (value, uid))  # O(log x)

    return '\n'.join(uid for _, uid in heap) if heap else "No input lines found."


def main(args=None):  # O(n log x) + O(p)
    parser = argparse.ArgumentParser(description="Find the IDs associated with the top X largest values.")
    parser.add_argument('x', type=int, help='Number of top values to find.')
    parser.add_argument('-f', '--file', type=str, help='Path to the file.')
    args = parser.parse_args(args)  # O(p) where p is the length of arguments

    if args.x <= 0:
        print("error: x must be a positive number.")
        sys.exit(2)

    try:
        if args.file:
            with open(args.file) as f:  # O(1)
                print(find_top_x_uids(f, args.x))  # O(n log x)
        else:
            print(find_top_x_uids(sys.stdin, args.x))  # O(n log x)
    except FileNotFoundError:
        print(f"error: file {args.file} not found.")
        sys.exit(2)
    except PermissionError:
        print(f"error: file {args.file} cannot be accessed due to insufficient permissions.")
        sys.exit(2)
    except ValueError as e:
        print(e.args[0])
        sys.exit(2)
    except Exception as e:
        print(f"error: An unexpected error occurred:\n{str(e)}")
        sys.exit(2)


if __name__ == "__main__":
    main()
