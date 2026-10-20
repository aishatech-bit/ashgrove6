"""Rebuilds ../index.html. Run:  python3 build.py
Edit index.src.html (text, listings, team, reviews), swap files in images/ (WebP, same names), then rebuild."""
import base64, glob, json, os
S = os.path.dirname(os.path.abspath(__file__))
def uri(path, mime): return 'data:%s;base64,%s' % (mime, base64.b64encode(open(path, 'rb').read()).decode())
t = open(S + '/index.src.html').read()
imgs = {os.path.basename(p)[:-5]: uri(p, 'image/webp') for p in sorted(glob.glob(S + '/images/*.webp'))}
for key, val in {'{{LOGO_DARK}}': uri(S + '/logo-dark.svg', 'image/svg+xml'), '{{LOGO_LIGHT}}': uri(S + '/logo-light.svg', 'image/svg+xml'),
                 '{{FAVICON}}': uri(S + '/favicon.svg', 'image/svg+xml'), '{{POSTER}}': uri(S + '/poster.jpg', 'image/jpeg'),
                 '{{IMGS_JSON}}': json.dumps(imgs, separators=(',', ':'))}.items():
    t = t.replace(key, val)
open(S + '/../index.html', 'w').write(t)
print('built index.html  %.2f MB, %d images embedded' % (len(t) / 1e6, len(imgs)))
