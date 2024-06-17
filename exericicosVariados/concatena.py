def concatenate_files(data25M, data50M, data75M):
    with open(data75M, 'w') as output:
        with open(data25M, 'r') as f1:
            for line in f1:
                output.write(line)

        with open(data50M, 'r') as f2:
            for line in f2:
                output.write(line)

if __name__ == "__main__":
    input_data25M = "data25M.txt"  # Substitua pelo nome do primeiro arquivo
    input_data50M = "data50M.txt"  # Substitua pelo nome do segundo arquivo
    data75M = "data75M.txt"  # Nome do arquivo de saída

    concatenate_files(input_data25M, input_data50M, data75M)
    print("Arquivos concatenados com sucesso.")