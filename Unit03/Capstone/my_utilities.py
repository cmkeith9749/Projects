
	   
def label_uncap_split (string):
	dct = {'mssub':'sub', 'mszoning':'znng', 'mssub':'sub', '1st':'frst', '2nd':'scnd',
	'exterior2nd':'extr_scnd', 'exter':'extr','exterior1st':'extr_frst' }
	S = []   
	for (i,c) in enumerate(string): 
		if not i:
			sub = c.lower(); c = ''; prv_upr = True
		else:
			if c.isupper():
					if prv_upr:
						prv_upr = True
					else:
						S.append(sub); sub = c.lower() ; c = ''; prv_upr = True
			else:
				prv_upr = False                
			sub += c.lower()
		if (i + 1 == len(string)):  
			S.append(sub)
		for (i, s) in enumerate(S):
			if s in dct:
				S[i] = dct[s]     
	return '_'.join(S)

# transform using dictionary 
def fillna_transform_dct(srs, dict): 
    srs = srs.fillna('NA')
    return srs.apply(lambda x : dict[x])