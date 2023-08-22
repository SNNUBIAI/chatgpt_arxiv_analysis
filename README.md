# chatgpt_arxiv_analysis
[Summary of ChatGPT-Related Research and Perspective Towards the Future of Large Language Models](https://www.sciencedirect.com/science/article/pii/S2950162823000176)

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

## Citation
```
@article{liu2023summary,
  title={Summary of ChatGPT-Related Research and Perspective Towards the Future of Large Language Models},
  author={Liu, Yiheng and Han, Tianle and Ma, Siyuan and Zhang, Jiayue and Yang, Yuanyuan and Tian, Jiaming and He, Hao and Li, Antong and He, Mengshen and Liu, Zhengliang and others},
  journal={Meta-Radiology},
  pages={100017},
  year={2023},
  publisher={Elsevier}
}
```
