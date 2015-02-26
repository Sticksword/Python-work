<<<<<<< HEAD
import sys
from decimal import Decimal

if len(sys.argv) == 2:
    filename = sys.argv[1]
    infile = open(filename, 'r')
    line = infile.readline()
    while line != '':
        total = Decimal(line)
        if total == -1:
            break

        output = '$' + '{:,.2f}'.format(total)
        total %= 1
        total *= 100

        change = int(total)
        quarters = change / 25
        change %= 25
        for x in xrange(0, quarters):
            output += ' Q'

        dimes = change / 10
        change %= 10
        for x in xrange(0, dimes):
            output += ' D'

        nickels = change / 5
        change %= 5
        for x in xrange(0, nickels):
            output += ' N'

        pennies = int(change)
        for x in xrange(0, pennies):
            output += ' P'

        line = infile.readline()
=======
import sys
from decimal import Decimal

if len(sys.argv) == 2:
    filename = sys.argv[1]
    infile = open(filename, 'r')
    line = infile.readline()
    while line != '':
        total = Decimal(line)
        if total == -1:
            break

        output = '$' + '{:,.2f}'.format(total)
        total %= 1
        total *= 100

        change = int(total)
        quarters = change / 25
        change %= 25
        for x in xrange(0, quarters):
            output += ' Q'

        dimes = change / 10
        change %= 10
        for x in xrange(0, dimes):
            output += ' D'

        nickels = change / 5
        change %= 5
        for x in xrange(0, nickels):
            output += ' N'

        pennies = int(change)
        for x in xrange(0, pennies):
            output += ' P'

        line = infile.readline()
>>>>>>> origin/master
        print output