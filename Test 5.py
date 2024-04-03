# DICTIONARIES

# 1) Using keys and indexing, grab the 'hello' from the following dictionaries:

# 1.
#d = {'simple_key' : 'hello'}   
#"grab the 'hello'"
#print(d['simple_key']);

# 2.
#d = {'k1':{'k2':'hello'}}
#"grab the 'hello'"
#print(d['k1']['k2']);

# 3.
#d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#"grab the 'hello'"
#print(d['k1'][0]['nest_key'][1][0]);

# 4.
d = {'k1':[1,2,{'k2':{'this is tricky',{'tough':[1,2,['hello']]}}}]}
#"grab the 'hello'"
print(['k1'][2]['k2'][1]['tough'][2][0]);