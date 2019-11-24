text = input("Enter your text,please ")
num_of_let = len(text) - text.count(" ") - text.count(".") - text.count(",") - text.count("!") - text.count("?")
lower = 0
upper = 0
for x in range(0,len(text)):
    try:
        int(text[x])
        num_of_let -= 1
    except:
        if text[x] == ' ' or text[x] == ',':
            continue
        else:
            if ord(text[x]) > 96:
                lower += 1
            else:
                upper += 1
number_of_letters = upper + lower
percent_of_up = 100/number_of_letters * upper
percent_of_low = 100/number_of_letters * lower

print("Percent of upper letters: " + str(percent_of_up) + " Number of upper letters: " + str(upper))
print("Percent of lower letters: " + str(percent_of_low) + " Number of lower letters: " + str(lower))