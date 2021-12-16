import time
def citire_fisier(nume_fisier):
    with open(nume_fisier, "rb") as f:
        data = f.read()
        text = data.decode('utf-8')
    return text


def main():
    text = citire_fisier("output_ruxi12")
    valid_chars = []
    password_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    text_alphabet = password_alphabet + "-=~!@#$%^&*()_+,./;'[]\<>?:\"}{|—" + "\n" + " " + "\t"

    for cringe_char in text:
        vc = []
       
        for char in password_alphabet:
            if chr(ord(char) ^ ord(cringe_char)) in text_alphabet:
                vc.append(char)
        valid_chars.append(vc)

    for lg in range(10, 16):
        
        password = []
        found = 1
        
        cnt_ap = len(text) // lg
       
        for x in range(lg):
            freq = [0] * len(text_alphabet)
           
            for j in range(x, len(text), lg):
                for char in valid_chars[j]:
                    freq[text_alphabet.index(char)] += 1
            ok = 0
            
            for i in range(len(freq)):
                if freq[i] >= cnt_ap:
                    password.append(text_alphabet[i])
                    ok = 1
                    break
            if ok == 0:
                found = 0
                break
        if found == 1:
            return "".join(password)

    return "None"


if __name__ == "__main__":
    start_time = time.time()
    password = main()
    end_time = time.time()
    print(password)
    time_real = end_time - start_time
    print(f"Execution time: {time_real} seconds")
