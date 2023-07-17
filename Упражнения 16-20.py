# 16. Площадь и объем
# Напишите программу, которая будет запрашивать у пользователя радиус и сохранять его в переменной r.
# После этого она должна вычислить площадь круга с заданным радиусом и объем шара с тем же радиусом.
# Используйте в своих вычислениях константу pi из модуля math.

# Подсказка. Площадь круга вычисляется по формуле area = πr**2, а объем шара – по формуле volume = (4/3)πr**3

import math

R = float(input('Введите радиус (м): '))  # запрашиваем данные от пользователя

area = math.pi * (R ** 2)    # вычисляем площадь круга

volume = (4 / 3) * math.pi * (R ** 3)  # вычисляем объём шара

print(f'Площадь круга составляет {area:.2f} метров')   # результат программы
print(f'Объем шара {volume:.2f} метров')


# 17. Теплоемкость
# Количество энергии, требуемое для повышения температуры одного 
# грамма материала на один градус Цельсия, называется удельной теплоемкостью материала и обозначается буквой C. Общее количество энергии 
# (q), требуемое для повышения температуры m граммов материала на ΔT
# градусов Цельсия, может быть рассчитано по формуле: q = mCDT.

# Напишите программу, запрашивающую у  пользователя массу воды 
# и требуемую разницу температур. На выходе вы должны получить количество энергии, которое необходимо добавить или отнять для достижения 
# желаемого температурного изменения.

# Подсказка. Удельная теплоемкость воды равна 4,186 Дж / г*С. 
# Поскольку вода обладает плотностью 1 грамм на миллилитр, в данном упражнении можно взаимозаменять граммы и миллилитры

# Расширьте свою программу таким образом, чтобы выводилась также стоимость сопутствующего нагрева воды. Обычно принято измерять 
# электричество в кВт·ч, а не в джоулях. Для данного примера предположим, что электричество обходится нам в 8,9 цента за один кВт·ч. 
# Используйте свою программу для подсчета стоимости нагрева одной чашки кофе.

# Подсказка. Для решения второй части задачи вам придется найти способ перевода единиц электричества между джоулями и кВт·ч.

teplo_vody = 4.186         # определяем константы теплоёмкости воды, стоимости и потребления энергии
st_sveta = 8.9
rash_kofe = 3

massa_vody = float(input('Объем воды в миллилитрах: '))        # запрашиваем ввод от пользователя
temp_1 = float(input('Введите начальную температуру (С): '))
temp_2 = float(input('Введите температуру повышения (C): '))

q = massa_vody * teplo_vody * (temp_2 - temp_1)    # вычисляем количество энергии в Джоулях

kol_energi = q / 3600000        # переводим в кВт/ч

stoim = kol_energi * rash_kofe    # высчитываем стоимость

print(f'Количество энергии %d Дж' % q)                                       # выводим результат
print(f'Стоимость нагрева одной чашки кофе обойдётся %.7f цент' % stoim)


# 18. Объем цилиндра
# Объем цилиндра может быть рассчитан путем умножения площади круга, лежащего в его основе, на высоту. Напишите программу, в которой 
# пользователь будет задавать радиус цилиндра и его высоту, а в ответ получать его объем, округленный до одного знака после запятой.


# 19. Свободное падение
# Напишите программу для расчета скорости объекта во время его соприкосновения с землей. Пользователь должен задать высоту в метрах, с которой 
# объект будет отпущен. Поскольку объекту не будет придаваться ускорение, примем его начальную скорость за 0 м/с. Предположим, что ускорение 
# свободного падения равно 9,8 м/с2. При известных начальной скорости (vi), ускорении (a) и дистанции (d) можно вычислить скорость 
# при соприкосновении объекта с землей по формуле: vf = корень из vi**2 + 2ad 
