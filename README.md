# chatgpt_arxiv_analysis
Analyzing chatgpt research trends.

## Example
You can get the result by following the steps below.
1. Get the latest articles from the arxiv. 
```
python articles_info.py
```

2. Based on the articles information your get from the above code, download the pdf file from arxiv.
```
python download_pdf.py
```

3. Based on the pdf your download, you can extract the word from the pdf files and save them on the txt files.
```
python readpdf.py
```

4. We can get the word cloud from the extracting words.
```
python txt2wordcloud.py
```