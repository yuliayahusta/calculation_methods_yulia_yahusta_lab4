import math
import pandas as pd
import matplotlib.pyplot as plt


def default_function(x):
    """
    Функція за замовчуванням: f(x) = 1 / sqrt(x^2 + 0.6).
    """
    return 1 / math.sqrt(x * x + 0.6)


def get_function():
    """
    Повертає функцію f(x), яку визначає користувач.
    """
    print("Enter the function. For example, the default function is f(x) = 1 / sqrt(x * x + 0.6).")
    user_input = input("f(x) = ")
    return lambda x: eval(user_input, {**vars(math), "x": x})


def trapezoidal_method(f, a, b, n):
    """
    Обчислення інтегралу функції f(x) на інтервалі [a, b] методом трапецій з n поділами.
    """
    s = 0.0
    h = (b - a) / n
    for i in range(1, n):
        x = a + i * h
        s += f(x)
    s += (f(a) + f(b)) / 2
    s *= h
    return s


def generate_xi_yi_table(f, a, b, n):
    """
    Генерація таблиці зі значеннями x_i та y_i = f(x_i) для кожного кроку в інтервалі [a, b].
    """
    h = (b - a) / n
    data = {
        "i": range(n + 1),
        "x_i": [round(a + i * h, 2) for i in range(n + 1)],
        "y_i": [round(f(a + i * h), 4) for i in range(n + 1)]
    }
    return pd.DataFrame(data)


def generate_trapezoidal_results(f, a, b, max_n):
    """
    Генерація таблиці з результатами інтегрування для різних значень n.
    """
    results = {
        "n": [],
        "Integral (S)": []
    }
    for n in range(2, max_n + 1, 2):
        results["n"].append(n)
        results["Integral (S)"].append(round(trapezoidal_method(f, a, b, n), 4))
    return pd.DataFrame(results)


def main():
    print("The method of trapezoids")
    print("Default integration function: f(x) = 1 / sqrt(x * x + 0.6)")
    use_default = input("Do you want to continue with this function? (yes/no): ").strip().lower()

    if use_default == "yes":
        f = default_function
    else:
        f = get_function()

    a = float(input("a = "))
    b = float(input("b = "))
    max_n = int(input("Enter the maximum number of division segments n = "))

    # Таблиця значень xi та yi
    xi_yi_table = generate_xi_yi_table(f, a, b, max_n)
    print("\nTable of x_i and y_i values:")
    print(xi_yi_table)

    # Таблиця результатів для різних n
    trapezoidal_results = generate_trapezoidal_results(f, a, b, max_n)
    print("\nTable of trapezoidal integration results for different n:")
    print(trapezoidal_results)

    # Побудова графіка
    plt.plot(xi_yi_table["x_i"], xi_yi_table["y_i"], marker="o", linestyle="-", color="#cdb4db")
    plt.title("Graph of f(x) over [a, b]")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
