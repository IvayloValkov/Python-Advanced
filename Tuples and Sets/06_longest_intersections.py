n = int(input())
intersections = []
for _ in range(n):
    data = input()

    first_sequence_data, second_sequence_data = data.split("-")
    start_1, stop_1 = [int(el) for el in first_sequence_data.split(",")]
    start_2, stop_2 = [int(el) for el in second_sequence_data.split(",")]
    intersection = range(max(start_1, start_2), min(stop_1, stop_2) + 1)
    # start, stop = [int(el) for el in first_sequence_data.split(",")]
    # first_seq = range(start, stop+1)
    # start, stop = [int(el) for el in second_sequence_data.split(",")]
    # second_seq = range(start, stop+1)
    # intersection = set(first_seq).intersection(second_seq)
    intersections.append(intersection)

longest = sorted(intersections, key=lambda x: -len(x))[0]
print(f"Longest intersection is {list(longest)} with length {len(longest)}")
