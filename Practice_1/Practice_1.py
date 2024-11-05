
def total_salary(path):
    try: 
        with open(path, 'w', encoding='utf-8') as file: # відкриття ФАЙЛУ
            file.write ('''Alex Korp,3000
    Nikita Borisenko,2000
    Sitarama Raju,1000''') 
        with open(path, 'r', encoding='utf-8') as file: 
            data_list =[]
            data = [el.strip().split(',') for el in file.readlines()] 
            for num in data:
                data_list.append (int (num[1])) 
    except FileNotFoundError: 
        return 'File with salaries is not found'
    total = sum (data_list)    
    average = total/len(data_list)
    return total, average


total, average = total_salary("path/to/salary_file.txt")
print(f"Total salary amount: {total}, Average salary: {average}")







