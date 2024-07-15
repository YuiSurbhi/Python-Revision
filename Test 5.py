# DICTIONARIES

# 1) Using keys and indexing, grab the 'hello' from the following dictionaries:

# Dict 1.
d = {'simple_key' : 'hello'}    
# grabbing the (hello) 
print(d['simple_key']);

# Dict 2.
d = {'k1':{'k2':'hello'}}  
# grabbing the (hello)  
print(d['k1']['k2']);

# Dict 3.
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}     
# grabbing the (hello)
print(d['k1'][0]['nest_key'][1][0]);

# Dict 4.
d = {'k1':[1,2,{'k2':{'this is tricky',{'tough':[1,2,['hello']]}}}]}
# grabbing the (hello) 
print(['k1'][2]['k2'][1]['tough'][2][0]);