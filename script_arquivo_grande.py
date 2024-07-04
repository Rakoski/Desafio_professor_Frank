import csv
import random

num_linhas = 1000000

output_file = 'large_grades_file.csv'
def generate_row(student_id, year):
    return [
        student_id,
        random.randint(50, 100),
        random.randint(50, 100),
        random.randint(50, 100),
        random.randint(50, 100),
        year
    ]

with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Nota1', 'Nota2', 'Nota3', 'Nota4', 'Ano'])
    
    student_id = 101
    for i in range(num_linhas):
        year = 2023 if i % 2 == 0 else 2024
        row = generate_row(student_id, year)
        writer.writerow(row)
        student_id += 1

print(f"Arquivo {output_file} criado com sucesso.")
