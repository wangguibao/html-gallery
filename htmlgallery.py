import glob
import sys
import os

CSS = '\
    .box-table {\
            border-collapse: collapse;\
            display: table;\
            width: 100%;\
            font-size: 14px;\
    }\
\
    .box-row {\
            border-bottom: 1px solid #EBEEF5;\
    }\
\
    .cell {\
            padding: 10px;\
            vertical-align: middle;\
            display: inline-block;\
            word-break: break-all;\
            color: #606266;\
            width: 30%;\
    }\
'

def write_css(f):
    f.write('<style>')
    f.write(CSS)
    f.write('</style>')

def write_html_head(f):
    f.write('<html lang=EN>')
    f.write('<head>')
    f.write('<meta charset="UTF-8">')
    f.write('<meta name="viewport" content="width=device-width,initial-scale=1.0">')
    f.write('<title>image gallery</title>')
    f.write('</head>')

    write_css(f)
    f.write('<body>')

def write_image_div(f, path):
    f.write('<div class="cell"><img src={} width=80%></img></div>'.format(path))

def write_html_foot(f):
    f.write('</body></html>')

def write_header(f, h_level, content):
    f.write('<{}>{}</{}>'.format(h_level, content, h_level))

def write_table(f):
    f.write('<div class="box-table">')

def finish_table(f):
    f.write('</div>')

def create_html(path):
    f = open('index.html', 'w')
    write_html_head(f)

    it = os.scandir(path)

    for entry in it:
        if not entry.is_dir():
            continue

        write_header(f, 'H1', entry.name)

        g = '{}/*.jpg'.format(entry.name)
        photos = glob.glob(g)

        write_table(f)
        for path in photos:
            write_image_div(f, path)

        finish_table(f)

    write_html_foot(f)
    f.close()

if __name__ == '__main__':
    path = './'
    create_html(path)
