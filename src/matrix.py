# y - столбцы
# x - строки

from random import randint
from copy import deepcopy

class Matrix(list[list[int]]):

    def __init__(
        self, 
        *,
        y: int | None = None, 
        x: int | None = None, 
        value: list[list[int]] | None = None,
        auto_init_values: bool = False,
        random_range: tuple[int, int] = (0, 10)
    ):
        if value:
            super().__init__(value)
            return
        else:
            super().__init__()

        for _ in range(y):
            _array = []

            for _ in range(x):
                if auto_init_values:
                    _array.append(
                        randint(random_range[0], random_range[1])
                    )
                else:
                    _array.append(0)
            
            self.append(_array)

    def __str__(self):
        text = f"<Matrix [{len(self)} x {len(self[0])}] {id(self)}> = " + "[ \n   "

        for i in enumerate(self):
            if i[0] not in [0, len(self)]:
                text += "\n   "
            
            text += "["

            for number in enumerate(i[1]):
                text += f"{number[1]}"

                if number[0] != len(i[1]) - 1:
                    text += ", "
            
            text += "]"


        text += "\n]"

        return text
    
    def copy(self):
        return Matrix(
            value = deepcopy(self)
        )
    
    # Сумма
    def __add__(self, matrix: "Matrix"):
        if len(self) != len(matrix) or len(self[0]) != len(matrix[0]):
            raise ValueError()
        
        m = self.copy()

        for y in enumerate(matrix):
            for x in enumerate(y[1]):
                m[y[0]][x[0]] += x[1]
        
        return m

    # Вычитание
    def __sub__(self, matrix: "Matrix"):
        if len(self) != len(matrix) or len(self[0]) != len(matrix[0]):
            raise ValueError()
        
        m = self.copy()

        for y in enumerate(matrix):
            for x in enumerate(y[1]):
                m[y[0]][x[0]] -= x[1]
        
        return m
    
    # Умножение
    def __mul__(self, value: "Matrix | int | float"):
        m = self.copy()

        if isinstance(value, (int, float)):
            for y in enumerate(m):
                for x in enumerate(y[1]):
                    m[y[0]][x[0]] *= value
            
            result = m
        
        if isinstance(value, Matrix):
            # Кол-во столбцов первой матрицы
            # должно быть равно кол-ву строк второй
    
            columns = len(self) # Столбцы
            lines = len(value[0]) # Кол-во строк

            assert columns == lines

            result = Matrix(
                y=len(self), # Кол-во столбцов
                x=len(value[0]) # Длина строки
            )

            for i in range(len(self)):            # Перебор строк первой матрицы (по строкам результата)
                for j in range(len(value[0])):    # Перебор столбцов второй матрицы
                    sum = 0

                    for k in range(len(self[0])):  # Перебор элементов строки и столбца
                        sum += self[i][k] * value[k][j]
                    
                    result[i][j] = sum

        
        return result
    
    # Транспонирование
    def transponite(self):
        result = Matrix(y=len(self[0]), x=len(self))

        for line in enumerate(self):
            for number in enumerate(line[1]):
                result[number[0]][line[0]] = number[1]
                # номер элемента линии self матрицы теперь номер столбца result матрицы
                # а номер столбца self матрицы теперь номер элемента линии result матрицы
        
        return result
    
    # Определитель
    def det(self):
        if len(self) == 1 and len(self[0]) == 1:
            return self[0][0]
        
        if len(self) == 2 and len(self[0]) == 2:
            print(self[0][0], self[1][1], self[1][0], self[0][1])
            return (self[0][0] * self[1][1]) - (self[1][0] * self[0][1])
        
        # 3 на 3 потом...

if __name__ == "__main__":

    m = Matrix(x = 3, y = 2, auto_init_values=True)

    print(m)

    # print(m + Matrix(value = [[1, 1], [1, 1]]))
    # print(m - Matrix(value = [[1, 1], [1, 1]]))
    # print(m * Matrix(value= [[0, 0], [0, 0]]))

    l = Matrix(
        value=[
        [11, -3],
        [-15, -2]
        ]
    )

    print(l, l.det())

