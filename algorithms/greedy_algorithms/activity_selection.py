# Given n activities with their start and finish times.
# Select the maximum number of activities that can be performed by a single person,
# assuming that a person can only work on a single activity at a time.

def max_activities(start: list[int], finish: list[int]):
    selected_activities = []

    n = len(finish)
    i = 0
    selected_activities.append(i)

    for j in range(1, n):
        if start[j] >= finish[i]:
            selected_activities.append(j)
            i = j
    return selected_activities


if __name__ == '__main__':
    start_time = [1, 2, 3, 4, 7, 8, 9, 9, 11, 12]
    finish_time = [3, 5, 4, 7, 10, 9, 11, 13, 12, 14]
    # start_time = [1, 3, 0, 5, 8, 5]
    # finish_time = [2, 4, 6, 7, 9, 9]
    selected_activities = max_activities(start_time, finish_time)
    print(selected_activities)