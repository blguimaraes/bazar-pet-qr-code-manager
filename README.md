# bazar-pet-qr-code-manager
Gerador e leitor de QR code para o projeto Bazar Pet JF

# Gerador e Leitor de QR Code

Este projeto consiste em um sistema que gera QR Codes para identificar itens do inventário de um bazar e realiza a leitura dos códigos utilizando um celular ou um **Raspberry Pi**. O projeto foi desenvolvido com o objetivo de ajudar no gerenciamento de inventário do BazarPet JF, permitindo o rastreamento eficiente de itens.

## Funcionalidades

- **Gerador de QR Code**: Cria QR Codes únicos para cada item com base em um `item_id` gerado no sistema.
- **Leitor de QR Code com Raspberry Pi**: Lê o QR Code através de uma câmera conectada ao Raspberry Pi, utilizando Python.

---

## 1. Gerador de QR Code

### Pré-requisitos

- **Python 3.x**
- Bibliotecas necessárias: `qrcode`

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/projeto-qr-code.git
cd projeto-qr-code
```

2. Instale as dependências:
```bash
pip install qrcode[pil]
```

### Utilização
O gerador de QR Codes recebe um item_id único (gerado em Java, seguindo o padrão especificado) e cria um QR Code correspondente.
- Parâmetro: item_id - String contendo o ID único do item.
- Saída: Um arquivo PNG contendo o QR Code gerado.

  

##  2. Leitor de QR Code compatível com Raspberry Pi e WebCam (PC)
Componentes Necessários
- **Raspberry Pi** (qualquer modelo com câmera) **OU** Desktop ou Notebook com **Python 3.x**.
- **Raspberry Pi:** Câmera compatível | **Desktop/Notebook:** Câmera compatível.
- Bibliotecas Python: `opencv-python`, `pyzbar`
  
Instalação

### Raspberry Pi ###
https://core-electronics.com.au/guides/raspberry-pi/QR-codes-raspberry-pi/
https://www.youtube.com/watch?v=Qf55aUgfLfQ


### Desktop/Notebook
1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/projeto-qr-code.git
cd projeto-qr-code
```

2. Instale as dependências:
```
pip3 install opencv-python pyzbar
```

### Utilização

A câmera precisa estar ligada.
Saída: O código lê o QR Code da WebCam e exibe o valor na tela.
Finalização: Pressione 'q' para fechar a janela de leitura.
