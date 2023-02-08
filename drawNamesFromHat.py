#!/usr/bin/env python3
import random

if __name__=='__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('nameFile')
	args = parser.parse_args()

	print('\n*** Loading name file...')
	nameFile = open(args.nameFile, 'rt')
	lines = nameFile.readlines()

	names = []
	for line in lines:
		name = line.strip()
		if len(name):
			names.append(name)

	print('*** Deduplicating names...')
	names = list(set(names))

	print(f'*** {len(names)} names loaded:')
	for name in names:
		print(f'    {name}')

	print(f'\n*** Seeding random number generator...')
	random.seed()

	print(f'*** Shuffling names...')
	random.shuffle(names)

	print(f'\n*** Ready to draw! Press Enter to continue:')
	for i, name in enumerate(names, 1):
		input()
		print(f'    {i}) {name}')

	print(f'\n*** Done.')
	