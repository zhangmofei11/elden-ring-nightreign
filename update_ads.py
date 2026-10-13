import os

ad_head = '''<script async="async" data-cfasync="false" src="https://bauval.org/21/5087bce5cfb6f958a410dba81c261e36"></script>
<script data-cfasync="false" src="https://bauval.org/14/090501b9230b280c4586e357cc260797"></script>
<script>
  atOptions = {
    'key' : 'b6e98724cc7754496dd555e5bbb88194',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/b6e98724cc7754496dd555e5bbb88194"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-5087bce5cfb6f958a410dba81c261e36"></div>
</div>'''

files = ['index.html', 'walkthrough.html', 'bosses.html', 'classes.html', 'builds.html', 'tips.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if 'b6e98724cc7754496dd555e5bbb88194' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    if 'container-5087bce5cfb6f958a410dba81c261e36' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')
