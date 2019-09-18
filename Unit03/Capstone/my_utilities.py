
def label_uncap_split (string):
    dct = {'mssub':'sub', 'mszoning':'znng', 'mssub':'sub', 'frontage':'frtg','exposure':'xpsr',
           'exterior':'xtrr', 'exter':'xtrr', 'garage':'grg', 'year':'yr','condition':'cond',
           'heating':'htng', 'qc':'qual'}
    S=[]
    for (i,c) in enumerate(string): 
        # first char
        if not i:
            prv = True; bgn = i
        # last char
        elif i+1 == len(string):
            if (c.isupper() or c.isdigit()) and not prv:
                S.append(string[bgn:i].lower()); S.append(c.lower())
            else:   
                S.append(string[bgn:].lower())
        # all the others        
        else:
            if c.isupper() or c.isdigit():
                if not prv:
                    S.append(string[bgn:i].lower()); bgn = i; prv = True
            else:
                prv = False
    S = [dct[s] if s in dct else s for s in S]            
    return '_'.join(S)
# transform using dictionary 

def fillna_transform_dct(srs, dict): 
    srs = srs.fillna('NA')
    return srs.apply(lambda x : dict[x])