#Escreva uma função que gagueje uma palavra como se alguém estivesse lutando para lê-la. As duas primeiras letras são repetidas duas vezes com reticências ... e espaço após cada uma, e então a palavra é pronunciada com um ponto de interrogação ?.
#Suponha que todas as entradas estejam em letras minúsculas e tenham pelo menos dois caracteres.

def stutter(word):
    return '{0}... {0}... {1}?'.format(word[:2], word)