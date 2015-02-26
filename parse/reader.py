<<<<<<< HEAD
__author__ = 'Michael'

from lxml import html
from clint.textui import puts, indent, colored
import requests

if __name__ == '__main__':
    page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
    tree = html.fromstring(page.text)

    #This will create a list of buyers:
    buyers = tree.xpath('//div[@title="buyer-name"]/text()')
    #This will create a list of prices
    prices = tree.xpath('//span[@class="item-price"]/text()')

    print 'Buyers: ', buyers
    print 'Prices: ', prices

    puts(colored.magenta('red text'))

    puts('not indented text')
    with indent(4, quote=' >'):
        puts('quoted text')
=======
__author__ = 'Michael'

from lxml import html
from clint.textui import puts, indent, colored
import requests

if __name__ == '__main__':
    page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
    tree = html.fromstring(page.text)

    #This will create a list of buyers:
    buyers = tree.xpath('//div[@title="buyer-name"]/text()')
    #This will create a list of prices
    prices = tree.xpath('//span[@class="item-price"]/text()')

    print 'Buyers: ', buyers
    print 'Prices: ', prices

    puts(colored.magenta('red text'))

    puts('not indented text')
    with indent(4, quote=' >'):
        puts('quoted text')
>>>>>>> origin/master
        puts('pretty cool, eh?')