import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Função para converter a imagem para escala de cinza (se não for já)
def carregar_imagem_cinza(caminho_imagem):
    img = Image.open(caminho_imagem).convert('L')  # 'L' é para imagem em escala de cinza
    return np.array(img)

# Função para dividir a imagem em planos de bits
def fatiar_planos_bits(imagem):
    planos_bits = []
    for i in range(8):
        # Máscara para pegar o i-ésimo bit (0 a 7)
        mascara = 1 << i
        plano = (imagem & mascara) >> i
        planos_bits.append(plano)
    return planos_bits

# Função para gerar as imagens binárias (1 bit por plano)
def gerar_imagens_binarias(planos_bits):
    imagens_binarias = []
    for i, plano in enumerate(planos_bits):
        imagem_binaria = np.where(plano == 1, 255, 0)  # 1 vira 255, 0 vira 0
        imagens_binarias.append(imagem_binaria)
    return imagens_binarias

# Função para gerar imagens com intensidade de 0 a 255 (8 bits por plano)
def gerar_imagens_8bits(planos_bits):
    imagens_8bits = []
    for i, plano in enumerate(planos_bits):
        imagem_8bits = plano * (2 ** i)  # Multiplica cada plano pelo valor posicional
        imagens_8bits.append(imagem_8bits)
    return imagens_8bits

# Função para gerar imagem com 3 bits mais significativos
def gerar_imagem_3bits(planos_bits):
    imagem_3bits = planos_bits[7] * 128 + planos_bits[6] * 64 + planos_bits[5] * 32
    return imagem_3bits

# Função para salvar as imagens
def salvar_imagens(imagens, prefixo, titulos):
    for i, img in enumerate(imagens):
        Image.fromarray(img.astype(np.uint8)).save(f"{prefixo}_{titulos[i]}.png")

# Caminho para a imagem (substitua pelo caminho correto)
caminho_imagem = 'Fig0314(a)(100-dollars).tif'

# Carregar a imagem
imagem = carregar_imagem_cinza(caminho_imagem)

# Fatiar a imagem em planos de bits
planos_bits = fatiar_planos_bits(imagem)

# Gerar as imagens binárias (1 bit por plano)
imagens_binarias = gerar_imagens_binarias(planos_bits)

# Gerar as imagens com intensidade de 0 a 255 (8 bits por plano)
imagens_8bits = gerar_imagens_8bits(planos_bits)

# Gerar a imagem com os 3 bits mais significativos
imagem_3bits = gerar_imagem_3bits(planos_bits)

# Definir títulos para os arquivos
titulos_binarios = [f"bit_plane_{i+1}_binary" for i in range(8)]
titulos_8bits = [f"bit_plane_{i+1}_8bits" for i in range(8)]
titulo_3bits = "3_most_significant_bits"

# Salvar as imagens binárias
salvar_imagens(imagens_binarias, "binary_planes", titulos_binarios)

# Salvar as imagens de 8 bits
salvar_imagens(imagens_8bits, "8bit_planes", titulos_8bits)

# Salvar a imagem com os 3 bits mais significativos
Image.fromarray(imagem_3bits.astype(np.uint8)).save(f"{titulo_3bits}.png")

print("Todas as imagens foram salvas com sucesso!")
