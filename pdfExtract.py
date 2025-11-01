import fitz

doc = fitz.open(r"Files\नेपालको_संविधान_२०७२(1).pdf")
out = open(r"txt_files\pdf_extract.txt", "w")  # Open text file for writing

for page in doc:
    text = page.get_text()  # Extract text from the page
    out.write(text)  # Write the extracted text to the text file
    out.write('\n\n')  # Add some separation between pages

out.close()


