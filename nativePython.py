
#itreating in list


list =[1,2,3]

for v in list:
    print(v)
"""
#  for name in iterable:                   #iterable produce a strem of values,agssign stream value to name,execute statement
#        statements
Iterable decides what values it produce 
if you iterate through list it will give elements
list => element
string=> character
dic   => keys  in suprising order but also have d.itervalues():, d.iteritems():
files => lines
stblib intresting iters
re    => for match in re.finditer(pattern,string)  #string of match object once for each regex match
for root, dirs, files in os.walk('some/dir')       #once for each sub-directories or tree of directories
for num in itertools.count():                      #once for each integer.... infinte!  (we cannot check how many values you have)
for itertools import chain, repeat, cycle
seq = chain(repeat(17,3), cycle(range(4)))          #build pipeline together 
form num in seq:
#17,17,17,0,1,2,3,0,1,2,3..... 

other use:    # loop over data without having explict loop
new_list =list(iterable)
sum(iterable), min(iterable), max(iterable)
combined= "".join(iterable)
            
"""
#how i  get the index----> range(len(list)) ---better way to do it ---> we have enumarate

for i,v in enumerate(list):             # give 2 values index and value , it give list of tuples
    print(i,v)