import math
import pandas as pd
import matplotlib.pyplot as plt


def default_function(x):
    """
    Функція за замовчуванням: f(x) = log10(x^2 + 3) / (2 * x).
    """
    if x == 0:
        raise ValueError("x cannot be zero as it leads to division by zero.")
    return math.log10(x * x + 3) / (2 * x)


def get_function():
    """
    Повертає функцію f(x), яку визначає користувач.
    """
    print("Enter the function. For example, the default function is f(x) = log10(x^2 + 3) / (2 * x).")
    user_input = input("f(x) = ")
    return lambda x: eval(user_input, {**vars(math), "x": x})


def simpsons_method(f, a, b, n):
    """
    Обчислення інтегралу функції f(x) на інтервалі [a, b] методом Сімпсона з n поділами.
    """
    if n % 2 != 0:
        raise ValueError("n must be an even number.")

    s1 = 0.0
    s2 = 0.0
    h = (b - a) / n

    # Сума для непарних індексів (1, 3, 5, ...)
    x = a + h
    for i in range(1, n, 2):
        s1 += f(x)
        x += 2 * h

    # Сума для парних індексів (2, 4, 6, ...)
    x = a + 2 * h
    for i in range(2, n, 2):
        s2 += f(x)
        x += 2 * h

    s = h / 3 * (f(a) + f(b) + 4 * s1 + 2 * s2)
    return s


def generate_xi_yi_table(f, a, b, n):
    """
    Генерація таблиці зі значеннями x_i та y_i = f(x_i) для кожного кроку в інтервалі [a, b].
    """
    h = (b - a) / n
    data = {
        "i": range(n + 1),
        "x_i": [round(a + i * h, 4) for i in range(n + 1)],
        "y_i": [round(f(a + i * h), 4) for i in range(n + 1)]
    }
    df = pd.DataFrame(data)
    return df.to_string(index=False, col_space=15)


def generate_simpsons_results(f, a, b, max_n):
    """
    Генерація таблиці з результатами інтегрування для різних значень n.
    """
    results = {
        "n": [],
        "Integral (S)": []
    }
    for n in range(2, max_n + 1, 2):
        results["n"].append(n)
        results["Integral (S)"].append(round(simpsons_method(f, a, b, n), 4))
    return pd.DataFrame(results)


def main():
    print("The Simpson's method")
    print("Default integration function: f(x) = log10(x^2 + 3) / (2 * x)")
    use_default = input("Do you want to continue with this function? (yes/no): ").strip().lower()

    if use_default == "yes":
        f = default_function
    else:
        f = get_function()

    a = float(input("Enter a (for 18 it's 1.2) = "))
    b = float(input("Enter b (for 18 it's 2) = "))
    max_n = int(input("Enter the maximum number of division segments n (even number) = "))

    # Таблиця значень xi та yi
    xi_yi_table = generate_xi_yi_table(f, a, b, max_n)
    print("\nTable of x_i and y_i values:")
    print(xi_yi_table)

    # Таблиця результатів для різних n
    simpsons_results = generate_simpsons_results(f, a, b, max_n)
    print("\nTable of Simpson's integration results for different n:")
    print(simpsons_results.to_string(index=False, col_space=15))

    # Побудова графіка для результатів методу Сімпсона
    plt.plot(simpsons_results["n"], simpsons_results["Integral (S)"], marker="o", linestyle="-", color="#ffbd00")
    plt.title("Integration results by Simpson's method for different n")
    plt.xlabel("Number of segments n")
    plt.ylabel("Integral (S)")
    plt.grid()
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.4f}"))
    plt.show()


if __name__ == "__main__":
    main()
