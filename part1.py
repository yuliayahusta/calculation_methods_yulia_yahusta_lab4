import math
import matplotlib.pyplot as plt
import pandas as pd


def get_function() -> callable:
    """
    Повертає функцію f(x), яку визначає користувач.
    """
    print("Enter the function. For example, the default function is f(x) = 1 / sqrt(0.5 * x + 1.5).")
    user_input = input("f(x) = ")
    return lambda x: eval(user_input, {**vars(math), "x": x})


def f_default(x: float) -> float:
    """
    Стандартна функція для інтегрування.
    """
    return 1 / math.sqrt(0.5 * x + 1.5)


def rectangle_methods(f: callable, a: float, b: float, n: int) -> dict:
    """
    Обчислює інтеграл для функції f(x) на інтервалі [a, b] методами лівих, правих та середніх прямокутників.
    """
    h = (b - a) / n

    # Метод лівих прямокутників
    left_s = sum(f(a + i * h) for i in range(n)) * h

    # Метод правих прямокутників
    right_s = sum(f(a + (i + 1) * h) for i in range(n)) * h

    # Метод середніх прямокутників
    mid_s = sum(f(a + (i + 0.5) * h) for i in range(n)) * h

    return {"Left Rectangle": left_s, "Right Rectangle": right_s, "Midpoint Rectangle": mid_s}


def generate_results(f: callable, a: float, b: float, max_n: int) -> pd.DataFrame:
    """
    Генерує таблицю результатів інтегрування за різними методами для різних n.
    """
    results = {"n": [], "Left Rectangle": [], "Right Rectangle": [], "Midpoint Rectangle": []}

    for n in range(1, max_n + 1):
        methods = rectangle_methods(f, a, b, n)
        results["n"].append(n)
        results["Left Rectangle"].append(round(methods["Left Rectangle"], 4))
        results["Right Rectangle"].append(round(methods["Right Rectangle"], 4))
        results["Midpoint Rectangle"].append(round(methods["Midpoint Rectangle"], 4))

    return pd.DataFrame(results)


def generate_xy_table(f: callable, a: float, b: float, n: int) -> pd.DataFrame:
    """
    Генерує таблицю значень x та відповідних значень y = f(x) на інтервалі [a; b].
    """
    h = (b - a) / n
    data = {"i": [], "x_i": [], "y_i": []}

    for i in range(n + 1):
        x_i = a + i * h
        y_i = f(x_i)
        data["i"].append(i)
        data["x_i"].append(round(x_i, 4))
        data["y_i"].append(round(y_i, 4))

    return pd.DataFrame(data)


def display_results_table(df: pd.DataFrame) -> None:
    """
    Виводить таблицю результатів інтегрування у форматованому вигляді.
    """
    print("\nIntegration Results with different values of n:")
    print("{:<10} {:<20} {:<20} {:<20}".format("n", "Left Rectangle", "Right Rectangle", "Midpoint Rectangle"))
    print("-" * 70)
    for index, row in df.iterrows():
        print("{:<10} {:<20} {:<20} {:<20}".format(row["n"], row["Left Rectangle"], row["Right Rectangle"],
                                                   row["Midpoint Rectangle"]))


def display_xy_table(df: pd.DataFrame) -> None:
    """
    Виводить таблицю значень x та y у форматованому вигляді.
    """
    print("\nTable of x and y values:")
    print("{:<10} {:<10} {:<10}".format("i", "x_i", "y_i"))
    print("-" * 30)
    for index, row in df.iterrows():
        print("{:<10} {:<10} {:<10}".format(row["i"], row["x_i"], row["y_i"]))


def plot_results(df: pd.DataFrame) -> None:
    """
    Створює графік для візуалізації результатів інтегрування.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(df["n"], df["Left Rectangle"], label="Left Rectangle", color="pink", marker="o")
    plt.plot(df["n"], df["Right Rectangle"], label="Right Rectangle", color="fuchsia", marker="o")
    plt.plot(df["n"], df["Midpoint Rectangle"], label="Midpoint Rectangle", color="red", marker="o")

    plt.title("Rectangle Integration Methods")
    plt.xlabel("Number of Segments (n)")
    plt.ylabel("Estimated Integral (S)")
    plt.legend()
    plt.grid()
    plt.xticks(df["n"])
    plt.show()


def main() -> None:
    """
    Головна функція програми: отримує вхідні дані, обчислює результати, виводить таблицю та будує графік.
    """
    print("\nThe method of rectangles")
    print("Default integration function: f(x) = 1 / sqrt(0.5 * x + 1.5)")

    use_default = input("Do you want to continue with this function? (yes/no): ").strip().lower()

    if use_default == "yes":
        f = f_default
    else:
        f = get_function()

    a = float(input("Enter a (for 18 it's 1.2) = "))
    b = float(input("Enter b (for it's 2) = "))
    max_n = int(input("Enter the maximum number of division segments n = "))

    # Генерація та виведення таблиці x та y
    xy_table_df = generate_xy_table(f, a, b, max_n)
    display_xy_table(xy_table_df)

    # Виведення таблиці інтегрування функцій при різних значеннях n
    results_df = generate_results(f, a, b, max_n)
    display_results_table(results_df)

    plot_results(results_df)


if __name__ == "__main__":
    main()
