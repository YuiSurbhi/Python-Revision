# LISTS

# 1) Build the list[0,0,0], two seperate ways.

#Ans) Way1
list1 = [0,0,0];
print(list1);
# way2
list1 = [0]*3;
print(list1);

# 2) Reassign 'hello' in this nested list to say 'goodbye' instead.
#    list3 = [1,2[3,4,'hello']]

# Ans) 
list3 = [1,2,[3,4,'hello']];
list3[2].pop(2);
print(list3);
list3[2].append('goodbye');
print(list3);

# 3) sort the list below.
#    list4 = [5,3,4,6,1]

# Ans) 
list4 = [5,3,4,6,1];
list4.sort();
print(list4);