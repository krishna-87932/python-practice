import pdf2image


a=pdf2image.pdfinfo_from_path('test.pdf')


for i in a:
    print(f'{i}: {a[i]}')
    
