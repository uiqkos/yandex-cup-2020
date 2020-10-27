s = input()

alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def reg_equal(c1, c2):
    return (c1 in alphabet_lower) ^ (c2 in alphabet_upper)

result = [len(s)]
s = 'a' + s.replace(' ', '')
regs = [0]

for i in range(1, len(s)):
    if reg_equal(s[i], s[i - 1]):
        regs[-1] += 1
    else:
        regs.append(1)

change_reg = lambda reg: 'u' if reg == 'l' else 'l'

cur_reg = 'l'
for i in range(len(regs)):
    if (cur_reg == 'l' and (i + 1) % 2 == 0) or (cur_reg == 'u' and (i + 1) % 2 != 0):
        if regs[i] >= 2:
            for i in range(len(result)):
                if regs[i] > 2:
                    result[i] += 2
                    result.append(result[i] + 2)
                elif regs[i] == 2:
                    result[i] += 2
                    result.append(result[i] + 2)
            cur_reg = change_reg(cur_reg)
        else:
            result += regs[i]

print(result)
