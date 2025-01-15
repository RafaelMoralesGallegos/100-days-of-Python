import time

# current_time = time.time()
# print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        fist_run = time.time()
        function()
        second_run = time.time()
        time_difference = second_run - fist_run
        print(f"{function.__name__} run speed: {time_difference}s")
        return time_difference

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        b = i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        b = i * i


def main():
    fast_speed = fast_function()
    slow_speed = slow_function()
    speed_differece = slow_speed - fast_speed  # type: ignore
    print(f"The diference between functions is: {speed_differece}")


if __name__ == "__main__":
    main()
