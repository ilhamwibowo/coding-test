#soal nomor 1
def bilangan_cacah():
    
    N = int(input("N = "))
    ctr = 0
    i = 3
    
    while (ctr <= N) :
        if (i%3 == 0) :
            ctr += 1
            print(i, end=' ')
        elif (i%7 == 0):
            ctr += 1
            print(i, end=' ')      
        
        if (i%21 == 0):
            ctr += 1
            print('Z', end=' ')
        

    
        i += 1
    
    print()

#soal nomor 2 
def search_word():
    sentence = input()
    
    #sanitasi input
    sentence = sentence.replace('.', '').lower()
    sentence = sentence.split(' ')

    words = ['sang', 'serigala', 'harimau']

    for i in range(len(sentence)) :
        if (sentence[i] in words) :
            if (sentence[i] == 'sang'):
                if (sentence[i+1] == 'gajah'):
                    print(sentence[i], sentence[i+1], end=" - ")
            else :
                print(sentence[i], end=" - ")

    print()


#soal nomor 3
def check_password():

    pwd = input()
    msg = "Kata sandi valid"

    # Kata sandi minimal 8 karakter
    if (len(pwd) < 8):
        msg = "Kata sandi minimal sepanjang 8 karakter"
    # Kata sandi maksimal 32 karakter
    elif (len(pwd) > 32) :
        msg = "Kata sandi maksimal sepanjang 32 karakter"
    # Karakter awal tidak boleh angka
    elif (pwd[0].isdigit()) :
        msg = "Karakter awal tidak boleh angka"
    # Harus memiliki angka
    elif (not any(char.isdigit() for char in pwd)):
        msg = "Kata sandi harus memiliki angka"
    # Harus memiliki huruf kapital dan huruf kecil    
    elif (pwd.islower() or pwd.isupper()):
        msg = "Kata sandi harus memiliki huruf kapital dan huruf kecil"

    print(msg)


#soal nomor 4
#python sort algorithm
#asumsi format input : [1, 2, 4, 5, 6] atau 1 2 3 4 5 6
def smallest_integer() :
    
    raw_input = input()

    #sanitize
    numbers = raw_input.replace('[', '').replace(']', '').replace(',', '')

    numbers = numbers.split(' ')
    for i in range(len(numbers)) :
        numbers[i] = int(numbers[i])
    
    numbers.sort()
    for i in range(len(numbers)-1):
        if(numbers[i+1] != numbers[i]+1 and numbers[i+1] > numbers[i]):
            print(numbers[i]+1)
            break

#selection sort algorithm
def selection_sort(arr):
    for i in range(len(arr)):
        idx_min = i
        for j in range(i+1, len(arr)):
            if (arr[j] < arr[idx_min]):
                idx_min = j
        
        temp = arr[i]
        arr[i] = arr[idx_min]
        arr[idx_min] = temp

#soal nomor 4 menggunakan selection sort
def smallest_integer_v2() :
    
    raw_input = input()

    #sanitize
    numbers = raw_input.replace('[', '').replace(']', '').replace(',', '')

    numbers = numbers.split(' ')
    for i in range(len(numbers)) :
        numbers[i] = int(numbers[i])
    
    selection_sort(numbers)
    for i in range(len(numbers)-1):
        if(numbers[i+1] != numbers[i]+1 and numbers[i+1] > numbers[i]):
            print(numbers[i]+1)
            break

#soal nomor 5
def print_pattern(N, itr=0):
    
    #basis
    if (itr == N):
        print()
    #recursion
    else :
        if(0 < itr < N-1):
            for i in range(N):
                if(0 < i < N-1 and i != N-itr-1):
                    print('O', end='')
                else :
                    print('X', end='')
            print()
        else:
            for i in range(N):
                print('X', end='')
            print()
        print_pattern(N, itr+1)



# Driver code
if __name__ == '__main__':
    print('LOGIC TEST')
    print('1. Masukkan nomor soal untuk menjalankan fungsi.')
    print('2. Masukkan -1 untuk keluar')

    cont = True
    while cont:
        number = int(input("Nomor soal : "))
        if (number == 1):
            bilangan_cacah()
        elif (number == 2):
            search_word()
        elif (number == 3):
            check_password()
        elif (number == 4):
            smallest_integer_v2()
        elif (number == 5):
            N = int(input('N = '))
            if (N %2 == 0):
                print("N harus ganjil")
            else :
                print_pattern(N)

        elif (number == -1):
            cont = False
        else :
            print('invalid input')
        