import re

ruler_labels = [
    ("1998", 5),
    ("2011", 18),
    ("2015", 30),
    ("2019", 45),
    ("2023", 60),
    ("2024", 75),
    ("2025", 85),
    ("2026", 95),
]

def make_ruler(layer_class, extra_attrs=""):
    s = f'           <div class="story-ruler {layer_class}" {extra_attrs}>\n'
    s += '             <div class="story-ruler-ticks"></div>\n'
    for label, pct in ruler_labels:
        s += f'             <div class="story-ruler-tick-label" style="left: {pct}%;">{label}</div>\n'
    s += '           </div>\n'
    return s

html_parts = []
html_parts.append('        <div class="story-ruler-container">\n')
html_parts.append(make_ruler('base'))
html_parts.append(make_ruler('filled', 'id="story-ruler-filled" style="clip-path: polygon(0 0, 0% 0, 0% 100%, 0 100%);"'))
html_parts.append('        </div>\n')

new_timeline_html = "".join(html_parts)

with open('about.html', 'r') as f:
    content = f.read()

pattern = re.compile(r'        <div class="story-ruler-container">.*?        </div>\n', re.DOTALL)
content = pattern.sub(new_timeline_html, content)

with open('about.html', 'w') as f:
    f.write(content)

print("Updated HTML")
