#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fontforge
import psMat
import os
import sys
import math
from logging import getLogger, StreamHandler, Formatter, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
formatter = Formatter('%(asctime)s [%(levelname)s] : %(message)s')
handler.setFormatter(formatter)
logger.setLevel(DEBUG)
logger.addHandler(handler)

# ASCENT = 850
# DESCENT = 174
ASCENT = 820
DESCENT = 204
SOURCE = './sourceFonts'
DIST = './dist'
LICENSE = open('./LICENSE.txt').read()
COPYRIGHT = open('./COPYRIGHT.txt').read()
VERSION = '2.0.4'

fonts = [
    {
         'family': 'Cica',
         'name': 'Cica-Regular',
         'filename': 'Cica-Regular.ttf',
         'weight': 400,
         'weight_name': 'Regular',
         'style_name': 'Regular',
         'ubuntu_mono': 'UbuntuMono-R.ttf',
         'mgen_plus': 'rounded-mgenplus-1m-regular.ttf',
         'ubuntu_weight_reduce': 0,
         'mgen_weight_add': 0,
         'italic': False,
     }, {
         'family': 'Cica',
         'name': 'Cica-RegularItalic',
         'filename': 'Cica-RegularItalic.ttf',
         'weight': 400,
         'weight_name': 'Regular',
         'style_name': 'Italic',
         'ubuntu_mono': 'UbuntuMono-R.ttf',
         'mgen_plus': 'rounded-mgenplus-1m-regular.ttf',
         'ubuntu_weight_reduce': 0,
         'mgen_weight_add': 0,
         'italic': True,
    }, {
        'family': 'Cica',
        'name': 'Cica-Bold',
        'filename': 'Cica-Bold.ttf',
        'weight': 700,
        'weight_name': 'Bold',
         'style_name': 'Bold',
        'ubuntu_mono': 'UbuntuMono-B.ttf',
        'mgen_plus': 'rounded-mgenplus-1m-bold.ttf',
        'ubuntu_weight_reduce': 0,
        'mgen_weight_add': 0,
        'italic': False,
    }, {
        'family': 'Cica',
        'name': 'Cica-BoldItalic',
        'filename': 'Cica-BoldItalic.ttf',
        'weight': 700,
        'weight_name': 'Bold',
        'style_name': 'Bold Italic',
        'ubuntu_mono': 'UbuntuMono-B.ttf',
        'mgen_plus': 'rounded-mgenplus-1m-bold.ttf',
        'ubuntu_weight_reduce': 0,
        'mgen_weight_add': 0,
        'italic': True,
#   }, {
#       'family': 'Cica',
#       'name': 'Cica-DemiLight',
#       'filename': 'Cica-DemiLight.ttf',
#       'weight': 300,
#       'weight_name': 'DemiLight',
#       'style_name': 'DemiLight',
#       'ubuntu_mono': 'UbuntuMono-R.ttf',
#       'mgen_plus': 'rounded-mgenplus-1m-light.ttf',
#       'ubuntu_weight_reduce': 10,
#       'mgen_weight_add': 20,
#       'italic': False,
#   }, {
#       'family': 'Cica',
#       'name': 'Cica-DemiLightItalic',
#       'filename': 'Cica-DemiLightItalic.ttf',
#       'weight': 300,
#       'weight_name': 'DemiLight',
#       'style_name': 'DemiLight Italic',
#       'ubuntu_mono': 'UbuntuMono-R.ttf',
#       'mgen_plus': 'rounded-mgenplus-1m-light.ttf',
#       'ubuntu_weight_reduce': 10,
#       'mgen_weight_add': 20,
#       'italic': True,
#   }, {
#       'family': 'Cica',
#       'name': 'Cica-Light',
#       'filename': 'Cica-Light.ttf',
#       'weight': 200,
#       'weight_name': 'Light',
#       'style_name': 'Light',
#       'ubuntu_mono': 'UbuntuMono-R.ttf',
#       'mgen_plus': 'rounded-mgenplus-1m-thin.ttf',
#       'ubuntu_weight_reduce': 20,
#       'mgen_weight_add': 10,
#       'italic': False,
#   }, {
#       'family': 'Cica',
#       'name': 'Cica-LightItalic',
#       'filename': 'Cica-LightItalic.ttf',
#       'weight': 200,
#       'weight_name': 'Light',
#       'style_name': 'Light Italic',
#       'ubuntu_mono': 'UbuntuMono-R.ttf',
#       'mgen_plus': 'rounded-mgenplus-1m-thin.ttf',
#       'ubuntu_weight_reduce': 20,
#       'mgen_weight_add': 10,
#       'italic': True,
    }
]

def log(str):
    logger.debug(str)

def remove_glyph_from_ubuntu(_font):
    u"""Rounded Mgen+を採用したいグリフをUbuntuMonoから削除
    """
    log('remove_ambiguous() : %s' % _font.fontname)

    glyphs = [
            0x2026, # …
            ]

    for g in glyphs:
        _font.selection.select(g)
        _font.clear()

    return _font


def check_files():
    err = 0
    for f in fonts:
        if not os.path.isfile('./sourceFonts/%s' % f.get('ubuntu_mono')):
            logger.error('%s not exists.' % f)
            err = 1

        if not os.path.isfile('./sourceFonts/%s' % f.get('mgen_plus')):
            logger.error('%s not exists.' % f)
            err = 1


    if err > 0:
        sys.exit(err)

def modify_usfont():
    pass

def modify_jpfont():
    pass

def set_os2_values(_font, _info):
    weight = _info.get('weight')
    style_name = _info.get('style_name')
    _font.os2_weight = weight
    _font.os2_width = 5
    _font.os2_fstype = 0
    if style_name == 'Regular':
        _font.os2_stylemap = 64
    elif style_name == 'Bold':
        _font.os2_stylemap = 32
    elif style_name == 'Italic':
        _font.os2_stylemap = 1
    elif style_name == 'Bold Italic':
        _font.os2_stylemap = 33
    _font.os2_vendor = 'TMNM'
    _font.os2_version = 1
    _font.os2_winascent = ASCENT
    _font.os2_winascent_add = False
    _font.os2_windescent = DESCENT
    _font.os2_windescent_add = False

    _font.os2_typoascent = -150
    _font.os2_typoascent_add = True
    _font.os2_typodescent = 100
    _font.os2_typodescent_add = True
    _font.os2_typolinegap = 0

    _font.hhea_ascent = -150
    _font.hhea_ascent_add = True
    _font.hhea_descent = 100
    _font.hhea_descent_add = True
    _font.hhea_linegap = 0
    _font.os2_panose = (2, 11, weight / 100, 9, 2, 2, 3, 2, 2, 7)
    return _font

def align_to_center(_g):
    width = 0

    if _g.width > 700:
        width = 1024
    else:
        width = 512

    _g.width = width
    _g.left_side_bearing = _g.right_side_bearing = (_g.left_side_bearing + _g.right_side_bearing)/2
    _g.width = width

    return _g

def align_to_left(_g):
    width = _g.width
    _g.left_side_bearing = 0
    _g.width = width

def align_to_right(_g):
    width = _g.width
    bb = _g.boundingBox()
    left = width - (bb[2] - bb[0])
    _g.left_side_bearing = left
    _g.width = width


def modify_nerd(_g):
    align_left = [
        0xe0b0, 0xe0b1, 0xe0b4, 0xe0b5, 0xe0b8, 0xe0b9, 0xe0bc,
        0xe0bd, 0xe0c0, 0xe0c1, 0xe0c4, 0xe0c6, 0xe0c8, 0xe0cc, 0xe0cd,
        0xe0d1, 0xe0d2,
    ]
    align_right = [
        0xe0b2, 0xe0b3, 0xe0b6, 0xe0b7, 0xe0b7, 0xe0ba, 0xe0bb, 0xe0be,
        0xe0bf, 0xe0c2, 0xe0c3, 0xe0c5, 0xe0c7, 0xe0ca, 0xe0ce, 0xe0d4,
    ]
    # Powerline
    if _g.encoding >= 0xe0b0 and _g.encoding <= 0xe0d4:
        _g.transform(psMat.translate(0, -55))
        _g.width = 1024

        if _g.encoding >= 0xe0b0 and _g.encoding <= 0xe0b7:
            _g.transform(psMat.compose(psMat.scale(1.0, 0.982), psMat.translate(0, -1)))
            if _g.encoding in align_right:
                bb = _g.boundingBox()
                left = 1024 - (bb[2] - bb[0])
                _g.left_side_bearing = left
                _g.width = 1024
            if _g.encoding in align_left:
                _g.left_side_bearing = 0
                _g.width = 1024

        if _g.encoding >= 0xe0b8 and _g.encoding <= 0xe0bf:
            _g.transform(psMat.compose(psMat.scale(0.8, 0.982), psMat.translate(0, -1)))
            if _g.encoding in align_right:
                bb = _g.boundingBox()
                left = 1024 - (bb[2] - bb[0])
                _g.left_side_bearing = left
                _g.width = 1024
            if _g.encoding in align_left:
                _g.left_side_bearing = 0
                _g.width = 1024

        if _g.encoding >= 0xe0c0 and _g.encoding <= 0xe0c3:
            _g.transform(psMat.scale(0.7, 1.0))
            if _g.encoding in align_right:
                bb = _g.boundingBox()
                left = 1024 - (bb[2] - bb[0])
                _g.left_side_bearing = left
                _g.width = 1024
            if _g.encoding in align_left:
                _g.left_side_bearing = 0
                _g.width = 1024
        if _g.encoding >= 0xe0c4 and _g.encoding <= 0xe0c7:
            if _g.encoding in align_right:
                bb = _g.boundingBox()
                left = 1024 - (bb[2] - bb[0])
                _g.left_side_bearing = left
                _g.width = 1024
            if _g.encoding in align_left:
                _g.left_side_bearing = 0
                _g.width = 1024
        if _g.encoding == 0xe0c8 or _g.encoding == 0xe0ca:
            _g.transform(psMat.scale(0.7, 1.0))
            if _g.encoding in align_right:
                bb = _g.boundingBox()
                left = 1024 - (bb[2] - bb[0])
                _g.left_side_bearing = left
                _g.width = 1024
            if _g.encoding in align_left:
                _g.left_side_bearing = 0
                _g.width = 1024
        if _g.encoding == 0xe0ce:
            _g.transform(psMat.scale(0.8, 1.0))
            bb = _g.boundingBox()
            left = 1024 - (bb[2] - bb[0])
            _g.left_side_bearing = left
            _g.width = 1024
        if _g.encoding == 0xe0cf:
            _g.transform(psMat.scale(0.9, 1.0))
            _g = align_to_center(_g)
        if _g.encoding == 0xe0d0:
            _g = align_to_center(_g)
        if _g.encoding == 0xe0d1:
            _g.transform(psMat.compose(psMat.scale(1.0, 0.982), psMat.translate(0, -1)))
            _g.left_side_bearing = 0
            _g.width = 1024
        if _g.encoding == 0xe0d2 or _g.encoding == 0xe0d4:
            _g.transform(psMat.compose(psMat.scale(1.0, 0.982), psMat.translate(0, -1)))
            if _g.encoding in align_right:
                bb = _g.boundingBox()
                left = 1024 - (bb[2] - bb[0])
                _g.left_side_bearing = left
                _g.width = 1024
            if _g.encoding in align_left:
                _g.left_side_bearing = 0
                _g.width = 1024
    else:
        _g.transform(psMat.translate(0, -55))
        _g.width = 1024
        _g = align_to_center(_g)

    return _g



def vertical_line_to_broken_bar(_f):
    _f.selection.select(0x00a6)
    _f.copy()
    _f.selection.select(0x007c)
    _f.paste()
    return _f

def emdash_to_broken_dash(_f):
    _f.selection.select(0x006c)
    _f.copy()
    _f.selection.select(0x2014)
    _f.pasteInto()
    _f.intersect()
    return _f

def mathglyph_to_double(_f):
    pass

def zenkaku_space(_f):
    _f.selection.select(0x2610)
    _f.copy()
    _f.selection.select(0x3000)
    _f.paste()
    _f.selection.select(0x271a)
    _f.copy()
    _f.selection.select(0x3000)
    _f.pasteInto()
    _f.intersect()
    for g in _f.selection.byGlyphs:
        g = align_to_center(g)
    return _f

def add_smalltriangle(_f):
    _f.selection.select(0x25bc)
    _f.copy()
    _f.selection.select(0x25be)
    _f.paste()
    _f.transform(psMat.compose(psMat.scale(0.64), psMat.translate(0, 68)))
    _f.copy()
    _f.selection.select(0x25b8)
    _f.paste()
    _f.transform(psMat.rotate(math.radians(90)))

    for g in _f.glyphs():
        if g.encoding == 0x25be or g.encoding == 0x25b8:
            g.width = 512
            g = align_to_center(g)

    return _f

def fix_box_drawings(_f):
    left = [
        0x2510, 0x2518, 0x2524, 0x2555, 0x2556, 0x2557, 0x255b, 0x255c, 0x255d,
        0x2561, 0x2562, 0x2563,
    ]
    right = [
        0x250c, 0x2514, 0x251c, 0x2552, 0x2553, 0x2554, 0x2558, 0x2559, 0x255a,
        0x255e, 0x255f, 0x2560,
    ]

    for g in _f.glyphs():
        if g.encoding < 0x2500 or g.encoding > 0x256c:
            continue
        if g.encoding in left:
            align_to_left(g)
        elif g.encoding in right:
            align_to_right(g)

    return _f


def build_font(_f):
    log('Generating %s ...' % _f.get('weight_name'))
    ubuntu = fontforge.open('./sourceFonts/%s' % _f.get('ubuntu_mono'))
    ubuntu = remove_glyph_from_ubuntu(ubuntu)
    cica = fontforge.open('./sourceFonts/%s' % _f.get('mgen_plus'))
    nerd = fontforge.open('./sourceFonts/nerd.ttf')

    for g in ubuntu.glyphs():
        if _f.get('ubuntu_weight_reduce') != 0:
            # g.changeWeight(_f.get('ubuntu_weight_reduce'), 'auto', 0, 0, 'auto')
            g.stroke("circular", _f.get('ubuntu_weight_reduce'), 'butt', 'round', 'removeexternal')
        g = align_to_center(g)


    alternate_expands = [
        0x306e,
    ]

    if _f.get('mgen_weight_add') != 0:
        for g in cica.glyphs():
            # g.changeWeight(_f.get('mgen_weight_add'), 'auto', 0, 0, 'auto')
            g.stroke("caligraphic", _f.get('mgen_weight_add'), _f.get('mgen_weight_add'), 45, 'removeinternal')
            # g.stroke("circular", _f.get('mgen_weight_add'), 'butt', 'round', 'removeinternal')


    ignoring_center = [
        0x3001, 0x3002, 0x3008, 0x3009, 0x300a, 0x300b, 0x300c, 0x300d,
        0x300e, 0x300f, 0x3010, 0x3011, 0x3014, 0x3015, 0x3016, 0x3017,
        0x3018, 0x3019, 0x301a, 0x301b, 0x301d, 0x301e, 0x3099, 0x309a,
        0x309b, 0x309c,
    ]
    for g in cica.glyphs():
        g.transform((0.91,0,0,0.91,0,0))
        if _f.get('italic'):
            g.transform(psMat.skew(0.25))
        if g.encoding in ignoring_center:
            pass
        else:
            g = align_to_center(g)

    for g in ubuntu.glyphs():
        if  g.isWorthOutputting:
            if _f.get('italic'):
                g.transform(psMat.skew(0.25))
            if g.encoding >= 0x2500 and g.encoding <= 0x25af:
                g.transform(psMat.compose(psMat.scale(1.024, 1.024), psMat.translate(0, -30)))
                g = align_to_center(g)
            ubuntu.selection.select(g.encoding)
            ubuntu.copy()
            cica.selection.select(g.encoding)
            cica.paste()

    for g in nerd.glyphs():
        if g.encoding < 0xe0a0 or g.encoding > 0xf4ff:
            continue
        g = modify_nerd(g)
        nerd.selection.select(g.encoding)
        nerd.copy()
        cica.selection.select(g.encoding)
        cica.paste()

    cica = fix_box_drawings(cica)
    cica = zenkaku_space(cica)
    cica = vertical_line_to_broken_bar(cica)
    cica = emdash_to_broken_dash(cica)
    cica = add_notoemoji(cica)
    cica = add_smalltriangle(cica)

    cica.ascent = ASCENT
    cica.descent = DESCENT
    cica.upos = 45
    cica.fontname = _f.get('family')
    cica.familyname = _f.get('family')
    cica.fullname = _f.get('name')
    cica.weight = _f.get('weight_name')
    cica = set_os2_values(cica, _f)
    cica.appendSFNTName(0x411,0, COPYRIGHT)
    cica.appendSFNTName(0x411,1, _f.get('family'))
    cica.appendSFNTName(0x411,2, _f.get('style_name'))
    # cica.appendSFNTName(0x411,3, "")
    cica.appendSFNTName(0x411,4, _f.get('name'))
    cica.appendSFNTName(0x411,5, "Version " + VERSION)
    cica.appendSFNTName(0x411,6, _f.get('family') + "-" + _f.get('weight_name'))
    # cica.appendSFNTName(0x411,7, "")
    # cica.appendSFNTName(0x411,8, "")
    # cica.appendSFNTName(0x411,9, "")
    # cica.appendSFNTName(0x411,10, "")
    # cica.appendSFNTName(0x411,11, "")
    # cica.appendSFNTName(0x411,12, "")
    cica.appendSFNTName(0x411,13, LICENSE)
    # cica.appendSFNTName(0x411,14, "")
    # cica.appendSFNTName(0x411,15, "")
    cica.appendSFNTName(0x411,16, _f.get('family'))
    cica.appendSFNTName(0x411,17, _f.get('style_name'))
    cica.appendSFNTName(0x409,0, COPYRIGHT)
    cica.appendSFNTName(0x409,1, _f.get('family'))
    cica.appendSFNTName(0x409,2, _f.get('style_name'))
    cica.appendSFNTName(0x409,3, VERSION + ";" + _f.get('family') + "-" + _f.get('style_name'))
    cica.appendSFNTName(0x409,4, _f.get('name'))
    cica.appendSFNTName(0x409,5, "Version " + VERSION)
    cica.appendSFNTName(0x409,6, _f.get('name'))
    # cica.appendSFNTName(0x409,7, "")
    # cica.appendSFNTName(0x409,8, "")
    # cica.appendSFNTName(0x409,9, "")
    # cica.appendSFNTName(0x409,10, "")
    # cica.appendSFNTName(0x409,11, "")
    # cica.appendSFNTName(0x409,12, "")
    cica.appendSFNTName(0x409,13, LICENSE)
    # cica.appendSFNTName(0x409,14, "")
    # cica.appendSFNTName(0x409,15, "")
    cica.appendSFNTName(0x409,16, _f.get('family'))
    cica.appendSFNTName(0x409,17, _f.get('style_name'))
    fontpath = './dist/%s' % _f.get('filename')
    cica.generate(fontpath)

    cica.close()
    ubuntu.close()
    nerd.close()


def add_notoemoji(_f):
    notoemoji = fontforge.open('./sourceFonts/NotoEmoji-Regular.ttf')
    for g in notoemoji.glyphs():
        if g.isWorthOutputting and g.encoding > 0x04f9:
            g.transform((0.42,0,0,0.42,0,0))
            g = align_to_center(g)
            notoemoji.selection.select(g.encoding)
            notoemoji.copy()
            _f.selection.select(g.encoding)
            _f.paste()
    notoemoji.close()
    return _f

def add_devicons(_f):
    devicon = fontforge.open('./sourceFonts/devicon.ttf')
    current = 0xE160
    for g in devicon.glyphs():
        if g.isWorthOutputting:
            g.transform(psMat.compose(psMat.scale(0.8, 0.8), psMat.translate(0, -55)))
            g = align_to_center(g)
            devicon.selection.select(g.encoding)
            devicon.copy()
            _f.selection.select(current)
            _f.paste()
            current = current + 1
    devicon.close()
    gopher = fontforge.open('./sourceFonts/gopher.sfd')
    for g in gopher.glyphs():
        if g.isWorthOutputting:
            gopher.selection.select(0x40)
            gopher.copy()
            _f.selection.select(0xE160)
            _f.paste()
            g.transform(psMat.compose(psMat.scale(-1, 1), psMat.translate(g.width, 0)))
            gopher.copy()
            _f.selection.select(0xE161)
            _f.paste()
    gopher.close()
    return _f

def main():
    print('')
    print('### Generating Cica started. ###')
    check_files()

    for _f in fonts:
        build_font(_f)

    print('### Succeeded ###')


if __name__ == '__main__':
    main()
