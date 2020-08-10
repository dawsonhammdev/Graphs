# Print out all of the strings in the following array in alphabetical order, each on a separate line.

arr = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

# You may use whatever programming language you'd like.
#Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

def abc(arr):
    # sorts the list alph.
    arr.sort()
    
    # its an array we need a for loop to access each elements. 
    for x in arr:
        # search for how to oreder alphebetically.
        print(x)

print(abc(arr))