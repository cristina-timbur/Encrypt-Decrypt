# XOR Encryption / Decryption    
<p align="right">(<a href="#part-2">Jump to Part 2</a>)</p>  

# Part 1
## About the Project
Implemented two python scripts: 
- **encrypt.py**  
           &nbsp;  - encrypts the 'input.txt' file, using xor and a specific password, and writes the result in the 'output' file.  
           &nbsp;  - time complexity: _O(n)_ </br>
           &nbsp; - memory complexity: _O(n)_, where n is the length of the input text
            </br>
            </br>
- **decrypt.py**  
            &nbsp; - decrypts the aforementioned encrypted 'output' file and writes the result in the 'input_recuperat.txt' file.  
            &nbsp; - time complexity: _O(n)_ </br>
            &nbsp; - memory complexity: _O(n)_, where n is the length of the input text

## Usage

Choose a password and run the python script as shown below    
  *&nbsp;&nbsp;&nbsp;&nbsp; // your password must contain between 10 and 15 characters which can be digits or english letters (both uppercase and lowercase)*  
  *&nbsp;&nbsp;&nbsp;&nbsp; // instead of 'password', write your own chosen password*

## Encryption
```bash
python encrypt.py password input.txt output
```

## Decryption
```bash
python decrypt.py password output input_recuperat.txt
```
***
# Part 2
## Match
* Our Team: Asyncoders
* Enemy Team: Riga Crypto
* Enemy Team Password: ..............

## About the Project
Implemented two python scripts:
- <p align="left"><a href="cracker1.py">cracker1.py</a></p> 
           &nbsp; - gets the password of another team using xor between their _'input.txt'_ and _'output'_ files.
           </br>
           </br>
- <p align="left"><a href="cracker2.py">cracker2.py</a></p>   
           &nbsp; - gets the password of another team while using only their _'output'_ file and xor operation.

## Password Cracking 1

Deriving from the fact that the password has at least 10 and at most 15 characters, we have 6 possible lengths (e.g. with n-characters).  For each of these 6 cases we are xor-ing character by character the first 2n characters of the text (we're not xor-ing all the characters, inasmuch as we are assured that the first n-characters and the second n-characters of the text are different), so that we can verify if the first half of the xored result string is equal to the second half. If so, we've found our correct password.

We got the password of the Riga Crypto Team: (asteptam raspunsul lor)

## Password Cracking 2

Caracter valid!!!!!!!

Ideea pe care o utilizam este xorarea dintre output si alfabetul englez.
In cazul in care rezultatul xorarii este un caracter valid, atunci il adaugam in lista caracterelor posibile pentru parola la o anumita pozitie din text.  

Pentru o anumita lungime a parolei fixata dupa urmatorul algoritm:
           Cautam caracterul de pe o anumita pozitie din parola. Facem frecventa fiecarui caracter in fiecare lista de la pozitia x + k * lg, unde 0 <= k <= cnt_ap. 
Daca exista un caracter cu numarul de aparitii egal cu cnt_ap, atunci acesta e caracterul cautat si il adaugam la parola. Daca pentru o anumita pozitie din parola nu gasim un caracter cu frecventa cnt_ap, atunci lungimea fixata a parolei nu e cea buna si continuam sa cautam parola cu urmatoarea lungime.

Nota: In cazul in care lungimea parolei nu este 10-15 caractere si este comparabila cu lungimea textului, atunci exista posibilitatea ca algoritmul precedent sa dea mai multe parole. De aceea, facem un dictionar cu cele mai frecvente cuvinte ale limbii romane, pentru a gasi parola corecta (care prin xorare cu output-ul da un text in limba romana fara diacritice).

(Uitati va la comentarii in cod)


## Copyright © 2021

@vl4dio4n &nbsp;@cristina-timbur 

***
*<p align="center"><a>FMI UniBuc 2021</a></p>*

<p align="right">(<a href="#top">Back to Top</a>)</p>
