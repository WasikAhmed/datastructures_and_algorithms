# Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline.
# It is also given that every job takes a single unit of time, so the minimum possible deadline for any job is 1.
# Maximize the total profit if only one job can be scheduled at a time.


# Step1 −  Find the maximum deadline value from the input set
# of jobs.
# Step2 −  Once, the deadline is decided, arrange the jobs
# in descending order of their profits.
# Step3 −  Selects the jobs with highest profits, their time
# periods not exceeding the maximum deadline.
# Step4 −  The selected set of jobs are the output.

def job_scheduling(arr, t):
    n = len(arr)

    # sort all the jobs according to decreasing order of profit
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # tracking the free time slots
    result = [False] * t

    # store the result (sequence of jobs)
    job = ['-1'] * t

    # iterating through all jobs
    for i in range(n):
        # find a free slot for this job
        # (start from the last possible slot)
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):

            # free slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break

    print(job)


if __name__ == '__main__':
    jobs = [
        ['a', 2, 100],
        ['b', 2, 20],
        ['c', 1, 40],
        ['d', 3, 35],
        ['e', 1, 25]
    ]

    job_scheduling(jobs, 3)

    # jobs = [
    #     ['a', 2, 100],  # Job Array
    #     ['b', 1, 19],
    #     ['c', 2, 27],
    #     ['d', 1, 25],
    #     ['e', 3, 15]]
    #
    # job_scheduling(jobs, 3)
