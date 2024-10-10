# dicionario
medias = { "Raphael": 6,
            "Mariana": 8,
            "Caroline": 10,
            "Gilsson": 9}
nome = input ("informe o nome do aluno: ")
if nome in medias:
    print(f"Media = {medias[nome]}" )
medias["sara"] = 8
print(medias.keys())
print(medias.values())
for abobora, falei in medias.items():
    if falei < 7:
        print(f"{abobora} reprovado!")