# -*- coding: utf-8 -*-

import itertools as it

gematriaprimus = (
	(u'ᚠ',  u'f',   2),
	(u'ᚢ',  u'u',   3),
	(u'ᚦ',  u'th',  5),
	(u'ᚩ',  u'o',   7),
	(u'ᚱ',  u'r',   11),
	(u'ᚳ',  u'c',   13),
	(u'ᚷ',  u'g',   17),
	(u'ᚹ',  u'w',   19),
	(u'ᚻ',  u'h',   23),
	(u'ᚾ',  u'n',   29),
	(u'ᛁ',  u'i',   31),
	(u'ᛂ',  u'j',   37),
	(u'ᛇ',  u'eo',  41),
	(u'ᛈ',  u'p',   43),
	(u'ᛉ',  u'x',   47),
	(u'ᛋ',  u's',   53),
	(u'ᛏ',  u't',   59),
	(u'ᛒ',  u'b',   61),
	(u'ᛖ',  u'e',   67),
	(u'ᛗ',  u'm',   71),
	(u'ᛚ',  u'l',   73),
	(u'ᛝ',  u'ing', 79),
	(u'ᛟ',  u'oe',  83),
	(u'ᛞ',  u'd',   89),
	(u'ᚪ',  u'a',   97),
	(u'ᚫ',  u'ae',  101),
	(u'ᚣ',  u'y',   103),
	(u'ᛡ',  u'io',  107),
	(u'ᛠ',  u'ea',  109)
)
runes = [x[0] for x in gematriaprimus]
letters = [x[1] for x in gematriaprimus]

def primegen():
	D = {}
	yield 2
	for q in it.islice(it.count(3), 0, None, 2):
		p = D.pop(q, None)
		if p is None:
			D[q*q] = q
			yield q
		else:
			x = q + 2*p
			while x in D:
				x += 2*p
			D[x] = p

def shift(offset, direction): 
	return (offset + direction) % len(gematriaprimus)

page = u'''ᚫᛂ•ᛟᛋᚱ•ᛗᚣᛚᚩᚻ•ᚩᚫ•ᚳᚦᚷᚹ•ᚹᛚᚫ•ᛚ
ᚩᚪᛈ•ᛗᛞᛞᚢᚷᚹ•ᛚ•ᛞᚾᚣᛂ•ᚳᚠᛡ•ᚫᛏ
ᛈᛇᚪᚦ•ᚳᚫ
36367763ab73783c7af284446c
59466b4cd653239a311cb7116
d4618dee09a8425893dc7500b
464fdaf1672d7bef5e891c6e227
4568926a49fb4f45132c2a8b4

ᚳᛞ•ᚠᚾ•ᛡᛖ•ᚠᚾᚳᛝ•ᚱᚠ•ᚫᛁᚱᛞᛖ•ᛋᚣᛂᛠᚢ
ᛝᚹ•ᛉᚩ•ᛗᛠᚹᚠ•ᚱᚷᛡ•ᛝᚱᛒ•ᚫᚾᚢᛋ•'''

pg = primegen()
p = ''
n = 0
for c in page:
	if c in u'•':
		p += u' '
		continue
	if not c in runes:
		p += c
		continue
	o = runes.index(c)
	if n != 57-1: # 57th rune is unencrypted
		np = next(pg)
		o = shift(o, -(np + 57))
	p += letters[o]
	n += 1
print(p)
