from pathlib import Path
import string
import re
import markdown
from py_asciimath.translator.translator import ASCIIMath2Tex
from pymdownx.arithmatex import ArithmatexExtension

flashcards_file = Path('flashcards.md')
output_file = Path('content/flashcards-todo.html')

template = string.Template("""\
<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8" >
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Flashcards to Add</title>

<style>
body {
  font-size: 1.3em;
}
code {
  background-color: #eee;
}
</style>

<script>
window.MathJax = {
  startup: {
    typeset: true,
  },
  tex: {
    inlineMath: [
      ['\\\\(', '\\\\)'],
    ],
    displayMath: [
      ['\\\\[', '\\\\]'],
    ],
  },
  svg: {
    scale: 1.0,
    fontCache: 'global',
    displayAlign: 'left',
  }
};
</script>
<script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>

</head>
<body>
<h1>Flashcards to Add</h1>
<p style="color: gray; font-size: 0.8em;">Remember to add clozes in the appropriate places.</p>
<hr>

$content

</body>
</html>
""")

md = markdown.Markdown(extensions=[ArithmatexExtension(preview=False, generic=True)])

asciimath2tex = ASCIIMath2Tex(log=False, inplace=True)
def convert(s):
  # return TeX output without delimiters
  return asciimath2tex.translate(
    s,
    displaystyle=False,
    from_file=False,
    pprint=False,
  )[1:-1]

input_text = flashcards_file.read_text()
input_text = re.sub(r'\$\$([^$]+)\$\$', lambda m: r'\['+convert(m.group(1))+r'\]', input_text)
input_text = re.sub(r'\$([^$]+)\$', lambda m: r'\('+convert(m.group(1))+r'\)', input_text)

content = md.convert(input_text)

output_file.write_text(template.substitute(content=content))
