#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys,os

def load_file_dict(dfile):
	fp = open(dfile,'r');
	dic = dict();
	while True:
		line = fp.readline();
		if not line: break;
		if len(line) <= 0 or line[0] == '#': continue;
		line = line.strip('\n').strip('\r');
		sps = line.split(' ');
		tdic = dict();
		tdic['word'] = sps[0];
		tdic['pos'] = sps[1];
		tdic['posname'] = sps[2];
		tdic['frep'] = sps[3];
		tdic['rate'] = sps[4];
		tdic['arate'] = sps[5];
		dic[tdic['word']] = tdic;
	fp.close();
	return dic;

def load_dic_dict(dfile):
	fp = open(dfile,'r');
	dic = dict();
	while True:
		line = fp.readline();
		if not line: break;
		if len(line) <= 0 or line[0] == '#': continue;
		line = line.strip('\n').strip('\r');
		sps = line.split(' ');
		tdic = dict();
		tdic['lens'] = sps[0];
		tdic['word'] = sps[1];
		tdic['pos'] = sps[2];
		tdic['frep'] = sps[3];
		if dic.has_key(tdic['word']):
			tt = dic[tdic['word']];
			if tt['pos'] == 'unk' and tdic['pos'] <> 'unk':
				dic[tdic['word']] = tdic;
		else:
			dic[tdic['word']] = tdic;
	fp.close();
	return dic;

if __name__ == '__main__':
	if len(sys.argv) <= 2:
		print 'Usage: %s [-f|-d] infile' %sys.argv[0];
		sys.exit(-1);
	if sys.argv[1] == '-f':
		dic = load_file_dict(sys.argv[2]);
		for key,item in dic.items():
			print len(key)//3,key,item['pos'],item['frep'];
	elif sys.argv[1] == '-d':
		dic = load_dic_dict(sys.argv[2]);
		for key,item in dic.items():
			print item['lens'],item['word'],item['pos'],item['frep'];

