import matplotlib.pyplot as plt
import nuplot as np



def build_chart (x, y, sigma_x, sigma_y, x_label = "x-axis", y_label = "y-axis", title = "The title", approx_line = 0):
    plt.plot (x, y)
    plt.xlabel (x_label)
    plt.ylabel (y_label)
    plt.title (title)

    if (approx_line != 0):
        k, b, sigma_b, sigma_k = MNK (x, y)

        approx_line_x = [1, 2]
        approx_line_y = [k * x[i] + b for i in range(2)]
        plt.plot (line_x, line_y)

        print ("drawing approximate line with:")
        print ("k = ", k, ", b = ", b)
        print ("sigma_k = ", sigma_k, ", sigma_b = ", sigma_b)

def MNK (x, y, cross_origin = 0):
    if (cross_origin == 1):
        k = np.mean (x) * np.mean (y) / np.mean (x ^ 2)
        sigma_k = 1 / x.size ** 0.5 * (np.mean (y ** 2) / np.mean (x ** 2) - k ** 2) ** 0.5

        return k, 0, sigma_k, 0

    b = (np.mean(x * y) - np.mean (x) * np.mean (y)) / (np.mean (x ** 2) - np.mean (x) ** 2)
    k = np.mean (y) - b * np.mean (x)

    sigma_b = 1 / (x.size) ** 0.5 * ((np.mean (y ** 2) - np.mean (y) ** 2) / (np.mean (x ** 2) - np.mean (x) ** 2) - b ** 2) ** 0.5
    sigma_k = sigma_b (np.mean (x ** 2) - np.mean (x) ** 2) ** 0.5

    return k, b, sigma_f, sigma_b


x = [1, 2, 2, 1]
y = [1, 1, 2, 2]
build_chart(x, y)
