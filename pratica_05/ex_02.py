def palindromo(texto):

    texto_limpo = ""
    for char in texto:
        if char.isalnum():
            texto_limpo += char.lower()

    return texto_limpo == texto_limpo[::-1]


print(palindromo("ovo"))
print(palindromo("arara"))
print(palindromo("Ame a ema"))
print(palindromo("Python"))
print(palindromo("12321"))
print(palindromo("Ola, mundo!"))
print(palindromo("Socorram-me, subi no onibus em Marrocos"))
