import re,glob,sys,os
TAG='tag=deskgear03-20'
for f in glob.glob('*.html'):
    t=open(f,encoding='utf-8').read()
    for u in re.findall(r'href="(https?://[^"]+)"',t):
        if 'amazon.com' in u and TAG not in u:
            print('bad tag',f,u);sys.exit(1)
    for href in re.findall(r'href="([^"]+)"',t):
        if href.startswith(('http://','https://','mailto:','#')): continue
        if not os.path.exists(href.split('#')[0]):
            print('broken',f,href);sys.exit(1)
print('ok')
