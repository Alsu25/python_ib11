num_cats = 0
first_cat_line = -1
line_num = 0

while True:
    line = input()
    line_num += 1
    if line == "СТОП":
        break
    if "кот" in line:
        num_cats += 1
        if first_cat_line == -1:
            first_cat_line = line_num

print(num_cats, first_cat_line)
