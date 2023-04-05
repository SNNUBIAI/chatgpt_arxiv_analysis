# chatgpt_arxiv_analysis
Summary of ChatGPT/GPT-4 Research and Perspective Towards the Future of Large Language Models [arxiv](https://arxiv.org/abs/2304.01852)

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
      title={Summary of ChatGPT/GPT-4 Research and Perspective Towards the Future of Large Language Models}, 
      author={Liu, Yiheng and Han, Tianle and Ma, Siyuan and Zhang, Jiayue and Yang, Yuanyuan and Tian, Jiaming and He, Hao and Li, Antong and He, Mengshen and Liu, Zhengliang and Wu, Zihao and Zhu, Dajiang and Li, Xiang and Qiang, Ning and Shen, Dingang and Liu, Tianming and Ge, Bao},
      journal={arXiv preprint arXiv:2304.01852},
      year={2023}
}
```
