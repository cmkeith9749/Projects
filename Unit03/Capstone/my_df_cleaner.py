def clean_label(S):
	if '_' in S: 
	
	




dct = {'mssub':'sub', 'mszoning':'znng', 'mssub':'sub', '1st':'frst', '2nd':'scnd',
	'exterior2nd':'extr_scnd', 'exter':'extr','exterior1st':'extr_frst' }
dct0 = 


	   
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
# columns as index, columns are feature info
def df_feature_info(df)	
	C = [col for col in df.columns]
	S0 = [len(df[c].unique()) for c in C]
	S1 = [len(list(np.where(df[c].isna())[0])) for c in C]
	S2 = [str(df[c].dtype) for c in C]
	dct = {k:eval('S' + str(i)) for i,k in enumerate(['unq_cnt', 'nan_cnt', 'dtype'])}
	return pd.DataFrame(dct, index=C)

# transform using dictionary 
def fillna_transform_dct(srs, dict): 
    srs = srs.fillna('NA')
    return srs.apply(lambda x : dict[x])
	
	
	
df.value_counts()