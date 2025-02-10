#Sorting
#linear_merge
def linear_merge(list1, list2):
    new_list = []
    while len(list1) and len(list2): #runs the code below until it finishes running through each element in the lists
        if list1[0] < list2[0]: #if an element of list1 is less than list2...
            new_list.append(list1.pop(0)) #then it is removed from list1 and added to new_list
        else:
            new_list.append(list2.pop(0)) #otherwise, it is removed from list2 and added to new_list
    #both of the lines below add whatever elements are left to new_list
    new_list.extend(list1)
    new_list.extend(list2)
    return new_list
        
print(linear_merge([2, 4, 6, 8], [3, 5, 7, 10]))
print(linear_merge(['aa', 'bb', 'cc'], ['ee', 'xx', 'dd']))

#front_x
def front_x(words):
    words_1 = [] #the list containing the strings starting with x
    words_2 = [] #the list containing the strings that don't start with x
    for i in words:
        if i.startswith('x'): #checks if any of the strings in words start with x
            words_1.append(i) #if they do, they are added to words_1
        else:
            words_2.append(i) #if they do not start with x, they are added to words_2
    return sorted(words_1) + sorted(words_2) #returns a list that combines the sorted versions of words_1 and words_2

print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))

#sort_last
def last(i): #function that extracts the second element in each tuple 
    return i[-1] #-1 is the position of the second element

def sort_last(tuples):
    return sorted(tuples, key=last) #sorted returns the list with its elements in order, also calls the last function
                                    #so it is ordered by the last element in each tuple

print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))
    
    
#Dictionary Files
#word_count
import sys

def word_count_dict(filename):
    word_count = {} #empty dictionary
    input_file = open(filename, encoding= 'utf-8') #opens the test_file
    for line in input_file:
        words = line.split() #removes whitespace around the words
        for word in words: #goes over each word in the line
            word = word.lower() #.lower is used so that words like "The" and "the" are considered the same word
            if not word in word_count: #this checks for multiple instances of a word
                word_count[word] = 1 #if the current word being looked at isn't a duplicate, that word's count stays as 1
            else:
                word_count[word] = word_count[word] + 1 #otherwise, its count increases
    input_file.close() #closes the file
    return word_count

def print_the_words(filename): #prints one "'word' 'count': per line that is sorted by the word
    word_count = word_count_dict(filename) #calls the word_count_dict function for test_file
    words = sorted(word_count.keys())
    for word in words:
        print(word, word_count[word])

def get_count(word_count_tuple): #returns the count ([1]) from a dict "'word' 'count'" tuple
    return word_count_tuple[1]

def print_the_top(filename): #prints the most common words
    word_count = word_count_dict(filename)
    items = sorted(word_count.items(), key=get_count, reverse=True)
    for item in items[:20]: #this prints out the top 20 most common words
        print(item[0], item[1])
        
def main(): #had to change the code for the main() function because sys.argv commands don't work in Thonny
    filename = "test_file.txt" 
    print("\nChoose an option:")
    print("1 - Print all the counts of the words(sorted alphabetically)")
    print("2 - Print the top 20 most common words")
    choice = int(input("Enter 1 or 2: "))
    if choice == 1:
        print_the_words(filename)
    elif choice == 2:
        print_the_top(filename)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == '__main__':
  main()
    

        
        
    
    