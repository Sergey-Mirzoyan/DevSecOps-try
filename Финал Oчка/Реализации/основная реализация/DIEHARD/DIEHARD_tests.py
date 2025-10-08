from __future__ import print_function

import argparse
import sys
import pickle


def read_bits_from_file(filename,bigendian):
    bitlist = list()
    if filename == None:
        f = sys.stdin
    else:
        f = open(filename, "rb")
    while True:
        bytes = f.read(16384)
        if bytes:
            for bytech in bytes:
                if sys.version_info > (3,0):
                    byte = bytech
                else:
                    byte = ord(bytech) 
                for i in range(8):
                    if bigendian:
                        bit = (byte & 0x80) >> 7
                        byte = byte << 1
                    else:
                        bit = (byte >> i) & 1
                    bitlist.append(bit)    
        else:
            break
    f.close()
    return bitlist

import argparse
import sys
parser = argparse.ArgumentParser(description='Test data for distinguishability form random, using NIST SP800-22Rev1a algorithms.')
parser.add_argument('filename', type=str, nargs='?', help='Filename of binary file to test')
parser.add_argument('--be', action='store_false',help='Treat data as big endian bits within bytes. Defaults to little endian')
parser.add_argument('-t', '--testname', default=None,help='Select the test to run. Defaults to running all tests. Use --list_tests to see the list')
parser.add_argument('--list_tests', action='store_true',help='Display the list of tests')

args = parser.parse_args()

bigendian = args.be
filename = args.filename

testlist = [
        'monobit_test',
        'frequency_within_block_test',
        'runs_test',
        'longest_run_ones_in_a_block_test',
        'binary_matrix_rank_test',
        'dft_test',
        'non_overlapping_template_matching_test',
        'overlapping_template_matching_test',
        'maurers_universal_test',
        'linear_complexity_test',
        'serial_test',
        'approximate_entropy_test',
        'cumulative_sums_test',
        'random_excursion_test',
        'random_excursion_variant_test']
        
print("Tests of Distinguishability from Random")
if args.list_tests:
    for i,testname in zip(range(len(testlist)),testlist):
        print(str(i+1).ljust(4)+": "+testname)
    exit()

f = open('../nums.txt','r')
bits = ''

for i in f:
    bits += i 
bits = list(bits)

for i in range(len(bits)):
    bits[i] = int(bits[i])
gotresult=False
if args.testname:
    if args.testname in testlist:    
        m = __import__ ("sp800_22_"+args.testname)
        func = getattr(m,args.testname)
        print("TEST: %s" % args.testname)
        success,p,plist = func(bits)
        gotresult = True
        if success:
            print("PASS")
        else:
            print("FAIL")
 
        if p:
            print("P="+str(p))

        if plist:
            for pval in plist:
                print("P="+str(pval))
    else:
        print("Test name (%s) not known" % args.ttestname)
        exit()
else:
    results = list()
    
    for testname in testlist:
        print("TEST: %s" % testname)
        m = __import__ ("sp800_22_"+testname)
        func = getattr(m,testname)
        
        (success,p,plist) = func(bits)

        summary_name = testname
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"
        
        if p != None:
            print("  P="+str(p))
            summary_p = str(p)
            
        if plist != None:
            for pval in plist:
                print("P="+str(pval))
            summary_p = str(min(plist))
        
        results.append((summary_name,summary_p, summary_result))
        
    print()
    print("SUMMARY")
    print("-------")
    
    for result in results:
        (summary_name,summary_p, summary_result) = result
        print(summary_name.ljust(40),summary_p.ljust(18),summary_result)