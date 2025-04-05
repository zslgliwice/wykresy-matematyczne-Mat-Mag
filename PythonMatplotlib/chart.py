import numpy as np
import matplotlib.pyplot as plt



# 1. Kolumnowy z wynikami dla każdej partii wyborów parlamentarnych w Polsce z roku 2023
partie = ['PiS', 'KO', 'Trzecia Droga', 'Lewica', 'Konfederacja']
wyniki = [35.38, 30.70, 14.40, 8.61, 7.16]

plt.bar(partie, wyniki, color='cyan')
plt.title('Wyniki wyborów parlamentarnych 2023 w Polsce', fontsize=14)
plt.ylabel('Procent głosów [%]')
plt.xlabel('Partie')
plt.grid(axis='y', linestyle='--')

plt.show()



# 2. Matematyczny dla funkcji y = sin(x) i y = cos(x) - jeśli potrafisz to na jednym wykresie
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(12, 3))

plt.plot(x, y_sin, label='sin(x)', color='cyan')
plt.plot(x, y_cos, label='cos(x)', color='magenta')
plt.axhline(0, color='black', linewidth=.5)
plt.axvline(0, color='black', linewidth=.5)

ticks = np.arange(-2*np.pi, 2.1*np.pi, np.pi/2)
tick_labels = [r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$',    r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']
plt.xticks(ticks, tick_labels)

plt.title('Wykres funkcji sin(x) i cos(x)', fontsize=14)
plt.legend()
plt.grid(True)

plt.show()

# 3. Dowolny fraktal: Mandelbrot    [ https://www.youtube.com/shorts/zNzAbYmS-EQ ]
from matplotlib.animation import FuncAnimation

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter):
    real = np.linspace(xmin, xmax, width)
    imag = np.linspace(ymin, ymax, height)
    fractal = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            fractal[i, j] = mandelbrot(real[i] + 1j * imag[j], max_iter)
    return fractal

# Parametry fraktala
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 800, 600
max_iter = 50

# Tworzenie okna
fig, ax = plt.subplots()
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.set_title("Mandelbrot Set")
ax.set_xlabel("Re")
ax.set_ylabel("Im")

# Obraz fraktala
fractal_image = np.zeros((width, height))

# Aktualizacja klatki
def update(frame):
    global fractal_image
    if frame < max_iter:
        fractal_image = generate_fractal(xmin, xmax, ymin, ymax, width, height, frame)
        ax.clear()
        ax.imshow(
            fractal_image.T,
            cmap='gist_earth',
            extent=(xmin, xmax, ymin, ymax),
            origin='lower'
        )
        ax.set_title(f"Mandelbrot Set (Iteracja: {frame})")
        ax.set_xlabel("Re")
        ax.set_ylabel("Im")
    return ax

# animacja
ani = FuncAnimation(
    fig, update, frames=range(max_iter),
    repeat=False
)

plt.show()



