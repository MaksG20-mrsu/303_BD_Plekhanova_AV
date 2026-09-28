import csv

min_id = None
max_id = None
min_count = 0
max_count = 0

with open('Task01/ratings.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    try:
        header = next(reader)
    except StopIteration:
        pass
        
    for row in reader:
        if not row: continue
        try:
            user_id = int(row[0])
        except ValueError:
            continue
            
        if min_id is None or user_id < min_id:
            min_id = user_id
            min_count = 1
        elif user_id == min_id:
            min_count += 1
            
        if max_id is None or user_id > max_id:
            max_id = user_id
            max_count = 1
        elif user_id == max_id:
            max_count += 1

with open('Task01/ratings_count.txt', 'w', encoding='utf-8') as f:
    f.write(f"{min_id} {min_count}\n")
    f.write(f"{max_id} {max_count}\n")

print("Файл ratings_count.txt успешно создан в папке Task01!")