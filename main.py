import PyPDF2

# Abra o arquivo PDF em modo de leitura binária
with open('teste3.pdf', 'rb') as file:
    # Crie um objeto PDF Reader
    pdf_reader = PyPDF2.PdfReader(file)

    # Obtenha a página atual
    page = pdf_reader.pages[0]

    # Extraia o texto da página
    text = page.extract_text()
    print(len(text))

    # Imprima o texto da página
    print(f"Texto da página:\n{text}\n")
