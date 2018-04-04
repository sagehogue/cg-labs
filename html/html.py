with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_sym = '{{'
end_sym = '}}'
# start = print(content.find(start_sym))
# end = print(content.find(end_sym))
name = 'Sage'
replace = content[content.find(start_sym): content.find(end_sym) + 2]
first_half = content[:content.find(start_sym)]
second_half = content[content[content.find(end_sym) + 2]:]
total = '{} {} {}'.format(first_half, name, second_half)
print(content[start:end+2])

with open('index.html', 'w', encoding='utf-8') as f:
    
