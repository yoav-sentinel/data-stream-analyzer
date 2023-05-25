# import argparse
# import heapq
# import sys
#
#
# # TODO validations
# # 1. No file and empty input stream - print something instead of empty list
# # 2. Invalid UID format
# # 3. Invalid value format - non float
# # 4. Invalid row format (split values is not exactly 2)
# # 5. Duplicated uid
# # 6. note that multiple lowest max values will only show the first uid if the heap is already full
#
# def validate_input(line, uid_set):
#     try:
#         uid, value = line.split()
#     except ValueError:
#         raise ValueError(f"Error: Malformed input line:\n{line}")
#     try:
#         value = float(value)
#     except ValueError:
#         raise ValueError(f"Error: Not numeric value `{value}`")
#
#     if uid in uid_set:
#         raise ValueError(f"Error: Duplicated UID found `{uid}`")
#
#     return uid, value
#
#
# def process_line(line, heap, uid_set, x):
#     uid, value = validate_input(line)
#
#     # If the UID already exists in the dictionary and its new value is larger, update it.
#     if uid in uid_dict and value > uid_dict[uid]:  # O(1) for checking in dictionary
#         heap.remove((uid_dict[uid], uid))  # O(n) for removal from heap
#         heapq.heapify(heap)  # O(x) for heapifying
#         uid_dict[uid] = value  # O(1) for updating dictionary
#         heapq.heappush(heap, (value, uid))  # O(logX) for pushing into heap
#
#     elif uid not in uid_dict and len(heap) < x:  # checking in dictionary O(1)
#         uid_dict[uid] = value  # O(1) for updating dictionary
#         heapq.heappush(heap, (value, uid))  # O(logx) for pushing into heap
#
#     elif uid not in uid_dict and value > heap[0][0]:  # checking in dictionary O(1)
#         _, removed_uid = heapq.heappop(heap)  # O(logx) for popping from heap
#         del uid_dict[removed_uid]  # O(1) for deleting from dictionary
#         uid_dict[uid] = value  # O(1) for updating dictionary
#         heapq.heappush(heap, (value, uid))  # O(logx) for pushing into heap
#
#
# def find_top_x_uids(input_stream, x):
#     heap = []
#     uid_set = set()
#
#     for line in input_stream:  # O(n) for iterating the input stream
#         process_line(line, heap, uid_set, x)
#
#     return [uid for _, uid in heap]
#
#
# def main():
#     parser = argparse.ArgumentParser(description="Find the IDs associated with the top X largest values.")
#     parser.add_argument('-f', '--file', type=str, help='Path to the file.')
#     parser.add_argument('-x', type=int, required=True, help='Number of top values to find.')
#     args = parser.parse_args()
#
#     if args.x <= 0:  # Handle invalid number of top values
#         print("Error: X must be a positive integer.")
#         return
#
#     try:
#         if args.file:
#             with open(args.file) as f:
#                 print(find_top_x_uids(f, args.x))
#         else:
#             print(find_top_x_uids(sys.stdin, args.x))
#     except FileNotFoundError:  # Handle nonexistent file
#         print(f"Error: File {args.file} not found.")
#     except ValueError as e:
#         print(e.args[0])
#
#
# if __name__ == "__main__":
#     main()
