# Copyright (C) 2025 Wang Guibao

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import glob
import sys
import os
import mimetypes

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
    fname = os.path.join(path, 'index.html')
    f = open(fname, 'w')
    write_html_head(f)

    it = os.scandir(path)

    top_level_images = []
    for entry in it:
        # print(entry.path)
        if not entry.is_dir():
            if (mimetypes.guess_type(entry.path)[0].startswith('image')):
                top_level_images.append(os.path.relpath(entry.path, path))
            continue

        write_header(f, 'H1', entry.name)

        subpath = os.path.join(path, entry.name)
        # print(subpath)
        subentries = os.scandir(subpath)

        write_table(f)
        for p in subentries:
            # print(p.path)
            if mimetypes.guess_type(p.path)[0].startswith('image'):
                write_image_div(f, p.path)

        finish_table(f)

    if len(top_level_images) > 0:
        write_header(f, 'H1', 'At top level')
        write_table(f)
        for p in top_level_images:
            write_image_div(f, p)
        finish_table(f)

    write_html_foot(f)
    f.close()

if __name__ == '__main__':
    # print(len(sys.argv))
    if len(sys.argv) != 2:
        print('Usage: python3 htmlgallery.py PATH/')
        sys.exit(0)
    path = sys.argv[1].rstrip('/\\')
    create_html(path)
    print('Your HTML is at ' + os.path.abspath(path))
