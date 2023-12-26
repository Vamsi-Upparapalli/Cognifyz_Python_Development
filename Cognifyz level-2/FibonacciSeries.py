def fibonacci_series(n):
    print("Fibonacci series up to {} terms:".format(n))

    if n == 1:
        print("0")
    elif n == 2:
        print("0, 1")
    else:
        series = [0, 1]
        for i in range(2, n):
            series.append(series[-1] + series[-2])
        print(", ".join(map(str, series)))

if __name__ == "__main__":
    fibonacci_series(int(input("Enter the number of terms for the Fibonacci series: ")))