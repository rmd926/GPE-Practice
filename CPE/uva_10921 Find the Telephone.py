'''

input_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
output_string= '22233344455566677778889999'

while True:
    target = input()
    temp = []
    dash_count = 0
    num_count = 0
    for char in target:
        if char in input_string:
            temp.append(output_string[input_string.index(char)])
        elif char == '0' or char == '1':
            num_count += 1
            temp.append(char)
        else:
            dash_count += 1
            temp.append(char)
            
    print("".join(temp), len(target) - (dash_count+num_count), dash_count)

'''

input_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
output_string= '22233344455566677778889999'

while True:
    target = input()
    temp = []
    letter_count = 0
    dash_count = 0

    for char in target:
        if char in input_string:
            temp.append(output_string[input_string.index(char)])
            letter_count += 1
            
        else:
            temp.append(char)
            if char == '-':
                dash_count += 1
            
    print("".join(temp), letter_count, dash_count)
            
