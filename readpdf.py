import os
import PyPDF2
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

root = "./arXivChatGPT/"
filenames = os.listdir(root)

output_dir = "./arXivChatGPT_text/"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

stopwords_dir = os.path.join(nltk.data.find('corpora'), 'stopwords')
if not os.path.exists(stopwords_dir):
    nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

skip_existing = True  # whether to skip the conversion if the file already exists
filter_reference = True

for name in filenames:
    if name.endswith(".pdf"):
        txt_name = name[:-4] + ".txt"
        if skip_existing and os.path.exists(os.path.join(output_dir, txt_name)):
            print(f"Skipping {txt_name} as it already exists.")
            continue

        with open(os.path.join(root, name), 'rb') as pdf_file:
            print(f"Read the pdf file {os.path.join(root, name)} and convert this file to {os.path.join(output_dir, txt_name)}")
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            num_pages = len(pdf_reader.pages)
            for i in range(num_pages):
                page = pdf_reader.pages[i]
                text += page.extract_text()

            # filter the reference.
            if filter_reference:
                text = re.sub(r'References\s*\n?.*$', '', text, flags=re.MULTILINE | re.DOTALL)

            words = word_tokenize(text)
            filtered_words = [word for word in words if word.lower() not in stop_words]

        with open(os.path.join(output_dir, txt_name), "w", encoding='utf-8') as f:
            f.write(" ".join(filtered_words))

print("All files converted successfully.")