import wordcloud
import os

root = "./arXivChatGPT_text/"
output_dir = "./arXivChatGPT_wordcloud/"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

skip_existing = False  # set this to True if you want to skip existing wordcloud files
only_all = True
txt = ''
filenames = os.listdir(root)

for name in filenames:
    input_path = os.path.join(root, name)
    output_path = os.path.join(output_dir, name[:-4] + ".png")

    if skip_existing and os.path.exists(output_path):
        print(f"Skipping {os.path.exists(output_path)} as it already exists.")
        continue
    print(f"Read this file {input_path} and convert this file to {output_path}")

    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    txt += text
    if not only_all:
        wd = wordcloud.WordCloud(scale=20)
        wd.generate(text)

        wd.to_file(output_path)
stopwords = wordcloud.STOPWORDS
content = ['A', 'D', 'show', 'even', 'number', 'use', 'based', 'example', 'training', 'different', 'data', 'dataset', 'three', 'shown', 'part', 'u', 'J', 'could', 'n', 'X', 'include', 'set', 'way', 'analysi', 'see', 'provide', 'first', 'L', 'R', 'make','Table','Therefore','including', 'arXiv', 'preprint', 'like', 'one', 'well', 'given','would', 'Figure', 'i', 'many', 'need', 'new', 'may', 'et al', 'two', 'et', 'also', 'however', 'al', 'm', 'e', 'g', 'M', 's', 'B', 'v', 'P', 'C', 'g', 'preprint.arXiv', 'using', 'f']
stopwords.update(content)
wd = wordcloud.WordCloud(max_words=70, scale=20, stopwords=stopwords)
wd.generate(txt)
wd.to_file(os.path.join(output_dir, "all.png"))