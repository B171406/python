def extract_numbers(input_string):
    answer = []
    curr_num = ""

    for char in input_string:
        if char.isdigit():
            curr_num += char
        elif curr_num:
            answer.append(int(curr_num))
            curr_num = ""

    if curr_num:
        answer.append(current_number)

    return answer

input_string = "ijoYitvFDXrewst#Y$65u6&GyHJghfcjtey4w532a^$S85(*&ohinyuiy futdyrw6e 4e8t yuvftcrde7r%*^7gituvcYRey"
answer = extract_numbers(input_string)

for n in answer:
    print(n)

# Time Complexity: O(n)
# Space Complexity: O(k), where k is the number of extracted numbers (size of the answer list).