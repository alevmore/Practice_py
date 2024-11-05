def get_cats_info(path):
    try: 
        with open(path, 'w', encoding='utf-8') as file: 
            file.write ('''60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5''') 
        with open(path, 'r', encoding='utf-8') as file: 
            cats_dict = []
            cats_data = [el.strip().split(',') for el in file.readlines()] 
            for data in cats_data:
                cats_dict.append ({'id': data [0], 'name': data[1], 'age': data[2]})  
                print (cats_data)
     
    except FileNotFoundError:  
        return 'File with salaries is not found'
    return cats_dict

cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
