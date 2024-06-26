﻿# Дано в задаче
p = 23  # модуль криптосистемы
g = 5   # примитивный элемент
xa = 2  # секретный ключ абонента A
xb = 3  # секретный ключ абонента B


# Вычисляем открытые ключи для абонентов A и B
ya = pow(g, xa, p)
yb = pow(g, xb, p)

# Общий секретный ключ у, полученный абонентом A
u_a = pow(yb, xa, p)

# Общий секретный ключ у, полученный абонентом B
u_b = pow(ya, xb, p)

(ya, yb, u_a, u_b, u_a == u_b)  # Проверяем, что ключи, полученные абонентами A и B, совпадают

