
def total_salary(path):
    try: #перевірка на коректність пошуку файлу
        with open(path, 'w', encoding='utf-8') as file: # відкриття ФАЙЛУ
            file.write ('''Alex Korp,3000
    Nikita Borisenko,2000
    Sitarama Raju,1000''') # записала до файлу текст для перевірки коду 
        with open(path, 'r', encoding='utf-8') as file: 
            data_list =[]
            data = [el.strip().split(',') for el in file.readlines()] 
            for num in data:
                data_list.append (int (num[1])) #формування списку зарплат
    except FileNotFoundError:  #вивід у разі відсутності файлу або пошкодження
        return 'File with salaries is not found'
    total = sum (data_list)    
    average = total/len(data_list)
    return total, average


total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")







