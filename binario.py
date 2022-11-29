def esBinario(strbinario):
    try:
        return int(strbinario,2)
    except (ValueError, TypeError) as error:
        return "No ha introducido el valor de forma correcta"
        
numeroBinario = input("Introduce un numero en binario: ")
print(esBinario(numeroBinario))
