import wordcloud
import os

root = "./arXivChatGPT_text/"
output_dir = "./arXivChatGPT_wordcloud/"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

skip_existing = True  # set this to True if you want to skip existing wordcloud files

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

    wd = wordcloud.WordCloud()
    wd.generate(text)

    wd.to_file(output_path)

wd = wordcloud.WordCloud()
wd.generate(txt)
wd.to_file(os.path.join(output_dir, "all.png"))