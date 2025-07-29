# open webbrowser with python
import webbrowser

url = 'https://docs.python.org/'

# webbrowser.open_new(url)

# specify which browser you want to use
chrom = webbrowser.get('chrome')
chrom.open(url)
