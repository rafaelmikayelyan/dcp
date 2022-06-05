secret_abstact = "Cyrnfr ernq guvf uryc znahny orsber pnyyvat zr ng 3 NZ jvgu gryrfpbcr rzretrapvrf."

def decipher_circle(text, step):
    output = ""

    for ch in text:
        if ch >= 'a' and ch <= 'z':
            output = output + decipher_single(ch, step, 122)
        elif ch >= 'A' and ch <= 'Z':
            output = output + decipher_single(ch, step, 90)
        else:
            output = output + ch
    return output


def decipher_single(ch, step, limit):
    ch = ord(ch) + step

    if ch > limit:
        ch -= step * 2
    return chr(ch)


def get_answer(text, step):
    output = decipher_circle(text, step)
    print(f'-> decipher circle: {step} steps (A => {chr(68 + step)})\n{text}\n\n{output}')


get_answer(secret_abstact, 13)
