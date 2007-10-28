# python -c 'from boopak import testing; testing.run()'

import sys
import unittest

import boopak.test_pinfo
import boopak.test_version
import boopak.test_pload
import boopak.test_sparse
import booman.create

testlist = [
	('version', boopak.test_version.TestVersion),
	('sparse', boopak.test_sparse.TestSParse),
	('pinfo', boopak.test_pinfo.TestPInfo),
	('pload', boopak.test_pload.TestPLoad),
	('create', booman.create.TestCreate),
]

def run(arglist=[]):
	if (type(arglist) == str):
		arglist = arglist.split()
		
	if (not arglist):
		tests = testlist
	else:
		tests = [(key, case) for (key, case) in testlist if key in arglist]
		
	ls = [ case for (key, case) in tests ]
	print 'Running:', (' '.join([ key for (key, case) in tests ]))
	suitels = [ unittest.makeSuite(case) for case in ls ]
	suite = unittest.TestSuite(suitels)
	unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
	run(sys.argv[1:])