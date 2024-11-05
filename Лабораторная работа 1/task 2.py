# TODO Найдите количество книг, которое можно разместить на дискете
floppy_disk_memory_capacity_mb = 1.44
Number_of_pages_in_the_book = 100
Number_of_lines_per_page = 50
Number_of_characters_per_line = 25
memory_for_one_character = 4
floppy_disk_memory_capacity_b = floppy_disk_memory_capacity_mb * 1024 * 1024
number_of_bytes_in_the_book = Number_of_pages_in_the_book * Number_of_lines_per_page * Number_of_characters_per_line * memory_for_one_character
number_of_books = int(floppy_disk_memory_capacity_b // number_of_bytes_in_the_book)
print("Количество книг, помещающихся на дискету:", number_of_books)