sections = list()

section_template = """
<div class="section" id="section{index}">
    <div class="item" id="i{index}">
        <div class="polaroid">
            <img src="img/{img}">
            <div class="caption">{caption}</div>
        </div>
    </div>
</div>
"""

with open('input.csv', 'r') as arq:
    lines = arq.read().split('\n')

for index, line in enumerate(lines):
    img_caption = line.split(',')
    img = img_caption[0]
    caption = ','.join(img_caption[1:])
    sections.append(
        section_template.format(index=index+1, img=img, caption=caption)
    )

sections_text = ''.join(sections)
with open('template.html', 'r') as tplt, open('index.html', 'w') as index:
    template = tplt.read()
    index_content = template.replace('SECTIONS_HERE', sections_text)
    index.write(index_content)
