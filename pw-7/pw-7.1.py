"""
Дано целое число N (32 < N < 126). Вывести символ с кодом, равным N
"""
while True:
    try:
        N = int(input("Введите целое число от 32 и до 126: "))
        print("от 32 и до 126") if N > 126 or N < 32 else print(f'Символ с кодом, равным N: {chr(N)}')
    except ValueError:
        print("Вводите целые числа")
