A = False
B = False
C = True

result_a = (not A or not B) and not C
result_b = (not A or not B) and (A or B)
result_c = (A and B) or (A and C) or (not C)

print("""
Задача: Вычислить значение логического выражения при следующих значениях 
 Логических величин А, В и С:
      
   А = Ложь, В = Ложь, С = Истина:
      
    а) (не А или не В) и не С;          б) (не А или не В) и (А или В);

    в) А и В или А и С или не С.
      
Ответ: 
      """)
print(f"A) {result_a}")
print(f"B) {result_b}")
print(f"C) {result_c}")
