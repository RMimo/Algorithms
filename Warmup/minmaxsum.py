def miniMaxSum(arr):
    arr = sorted(arr)
    min_sim = sum(arr[0:4])
    max_sum = sum(arr[-4:])
    print(f'{min_sim} {max_sum}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
