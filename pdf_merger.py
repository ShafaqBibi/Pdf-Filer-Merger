import PyPDF2

pdf_files = ['1.pdf', '2.pdf']
merger = PyPDF2.PdfMerger()
for P_Files in pdf_files:
   pdf_F = open(P_Files, 'rb')
   Pdf_Reader = PyPDF2.PdfReader(pdf_F)
   merger.append(Pdf_Reader)
pdf_F.close()
merger.write('Merged.pdf')