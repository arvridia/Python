def conta_unicos(filename):
    unicos = set()

    with open(filename, 'r') as file:
        for linha in file:
            integer = int(linha.strip())
            unicos.add(integer)

    return len(unicos)

if __name__ == "__main__":
    input_filename = "data75M.txt"
    contador = conta_unicos(input_filename)
    print(f"O arquivo possui {contador} elementos diferentes.")


