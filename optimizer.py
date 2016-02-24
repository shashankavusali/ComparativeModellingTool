import numpy as np
import re


def calculateDifference(x1, y1, z1, x2, y2, z2):
    a = np.array((x1, y1, z1))
    b = np.array((x2, y2, z2))
    return np.linalg.nomr(a - b)


def calculateXDifference(x1, x2, d1, d2):
    return ((d1 - d2) / d1) * 2 * (x1 - x2)


def calculateYDifference(y1, y2, d1, d2):
    return ((d1 - d2) / d1) * 2 * (y1 - y2)


def calculateZDifference(z1, z2, d1, d2):
    return ((d1 - d2) / d1) * 2 * (z1 - z2)


def optimize(index, length):
    return


def determineGaps(target, template):
    has_gap = False
    gap_length = 0
    gaps = []
    for i in range(len(target)):
        if target[i] != '-' and template[i] == '-':
            has_gap = True
            gap_length += 1
        else:
            if has_gap:
                gaps.append((i - gap_length, gap_length))
                has_gap = False
                gap_length = 0
    return gaps


def extractCAlphaCoordinates(lines):
	charged_res_coords = []
	regex = re.compile(
	    "^ATOM\s([0-9]{4})\s([A-Z0-9]+)\s([A-Z]{3})\s([A-Z]{1}\s{0,1}[0-9]+)\s([0-9\.-]+)\s([0-9\.-]+)\s([0-9\.-]+)\s([0-9\.-]+)\s([0-9\.-]+)\s([A-Z]{1})$")
	for line in lines:
		if line.startswith('ATOM'):
			if 'CA' in line:
				match = regex.match(line)
				third_spatial = match.group(7)
				print(third_spatial)
				charged_res_coords.append(match.groups()[0:-3])

def readfile():
    file1 = open('OR414-2ctf.ali', 'r')
    file2 = open('OR414-4rrf.ali', 'r')
    template2Pdb = open('4rrf.pdb')
    lines1 = list(file1)
    lines2 = list(file2)
    templateLines = list(template2Pdb)
    template1 = lines1[2]
    target1 = lines1[6]
    print(target1)
    print(template1)
    gaps = determineGaps(target1, template1)
    for (index, length) in gaps:
        optimize(index, length)
    extractCAlphaCoordinates(templateLines)
    return

if __name__ == '__main__':
    readfile()
