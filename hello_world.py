



# -*- coding:utf-8 -*-
def print_palmtrees(num):
        for i in range(num):
                sys.stdout.write(' /|\\')
        sys.stdout.write('\n')
        for i in range(num):
                sys.stdout.write('  | ')
        sys.stdout.write('\n\n')


def print_rabbit_range(num):
	for i in range(num):
		sys.stdout.write(' \\/ ')
	sys.stdout.write('\n')
	for i in range(num):
		sys.stdout.write(' oo ')
	sys.stdout.write('\n')
	for i in range(num):
		sys.stdout.write(' ** ')
	sys.stdout.write('\n')




import sys
import monkey
if __name__ == "__main__":
    print('Bye bye rabbits')
    monkey.print_monkeys([0,1,2,3,4,5])
    print_palmtrees(10)
    print_rabbit_range(10)
