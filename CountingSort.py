import time

def logging_time(original_fn):
  def wrapper_fn(*args):
    start_time = time.time()
    result = original_fn(*args)
    end_time = time.time()
    print(f"[{original_fn.__name__}]  \t실행시간 : %.5f sec" % (end_time-start_time))
    return result
  return wrapper_fn

@logging_time
def CountingSort(array, max_val):
    size = len(array)
    output = [0 for _ in range(size)]

    # 개수를 셀 리스트 초기화
    count = [0 for _ in range(max_val+1)]

    # 개수 세기
    for i in range(0, size):
        count[array[i]] += 1

    # 누적합 저장하기
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 리턴할 배열에 저장하기
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    return output


if __name__ == "__main__":
    import random

    data = [random.randrange(0, 1000) for _ in range(10)]
    data = CountingSort(data, 1002)
