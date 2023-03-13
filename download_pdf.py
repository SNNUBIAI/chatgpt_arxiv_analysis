import os
import pandas as pd
import requests

output_dir = "arxivChatGPT/"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
df = pd.read_excel("articles.xlsx")
existing_files = os.listdir(output_dir)
df = df[~df["Link"].apply(lambda link: link.split("/")[-1] + ".pdf" in existing_files)]
print("Need to download {} pdf files.".format(df.shape[0]))

for index, row in df.iterrows():
    link = row["Link"]
    article_link = "https://arxiv.org/pdf/" + link.split("/")[-1] + ".pdf"
    print("Downloading the article -> {}".format(article_link))
    file_name = output_dir + link.split("/")[-1] + ".pdf"
    response = requests.get(article_link)
    with open(file_name, 'wb') as f:
        f.write(response.content)