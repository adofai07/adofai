import random
import time

def logging_time(original_fn):
  def wrapper_fn(*args):
    start_time = time.time()
    result = original_fn(*args)
    end_time = time.time()
    print(f"[{original_fn.__name__}]  \t실행시간 : %.5f sec" % (end_time-start_time))
    return result
  return wrapper_fn

# 리스트의 원소를 랜덤하게 섞기
def shuffle(inp):
    n = len(inp)
    for i in range(0, n):
        r = random.randint(0, n-1)
        inp[i], inp[r] = inp[r], inp[i]

    return inp

# 리스트가 정렬되었는지 확인하기
def check(inp):
    for i in range(len(inp) - 1):
        if inp[i] > inp[i+1]:
            return False

    return True

# 정렬될 때까지 리스트의 순서 섞기
@logging_time
def BogoSort(array):
    while not check(array):
        array = shuffle(array)

if __name__ == "__main__":
    data = [4, 2, 2, 8, 3, 3, 1, 5, 7, 6]
    BogoSort(data)