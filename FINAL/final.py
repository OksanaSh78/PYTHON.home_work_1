import numpy as np
import matplotlib.pyplot as plt

limit = 100
step = 0.01
color = 'b'
line_s = '-'
direct_up = True

a, b, c, d, e = -12, -18, 5, 10, -30

x = np.arange(-limit, limit, step)
 
 
def switch_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color = 'b'
    return color


def switch_line():
    global line_s
    if line_s == '-':
        line_s = '--'
    else:
        line_s = '='
    return line_s


def func(x):
    return a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e
 

x_change = [(-limit, 'limit')]




for i in range(len(x)-1):
    if (func(x[i]) > 0 and func(x[i + 1]) < 0) or (func(x[i]) < 0 and func(x[i + 1]) > 0):
        x_change.append((x[i] if abs(0- x[i + 1]) else x[i+1], 'zero'))
    if direct_up:
        if func(x[i]) > func(x[i + 1]):
            x_change.append((x[i], 'direct')) 
            direct_up = False  
    else:
        if func(x[i]) < func(x[i+1]):
            x_change.append((x[i], 'direct')) 
            direct_up = True  

x_change.append((limit, 'limit'))

print(x_change)
for i in range(len(x_change) - 1):
    cur_x = np.arange(x_change[i][0], x_change[i + 1][0] + step, step)
    if x_change[i][1] == 'zero':
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, func(cur_x), color)
    else:
        plt.plot(cur_x, func(cur_x), switch_color())

min_y = min(func(x))
min_x = -limit
for x in x_change:
    if x[1] in ['direct', 'limit']:
        if abs(func(x[0]) - min_y) < abs(min_x - min_y):
            min_x = x[0]

roots = []
for x in x_change:
    if x[1] == 'zero':
        roots.append(str(round(x[0], 2)))
        plt.plot(x[0], func(x[0]), 'gx')   
        
plt.plot(min_x, min_y, 'yo', label=f'Экстремум функции на промежутке [{-limit};{limit}]: ({round(min_x, 2)}, {round(min_y, 2)})')

plt.rcParans['lines.linestyle'] = '-'
plt.plot(0, 0, 'b', label='Убывание > 0')
plt.plot(0, 0, 'r', label='Возрастание > 0')
plt.rcParans['lines.linestyle'] = '--'
plt.plot(0, 0, 'b', label='Убывание < 0')
plt.plot(0, 0, 'r', label='Возрастание < 0')
plt.title(f'Корни на промежутке [{-limit};{limit}]: {", ".join(roots)}')
plt.legend()
plt.show()

