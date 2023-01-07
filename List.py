## Lists positive number starts at the left 0 is the starting count
fruits_list = ["Apple", "Orange","Mango","Plum","Banana","Grapes","Melon"]
print(fruits_list)
##update a list
fruits_list[3]= 'Lemon'
print(fruits_list)
##Lemon replace Plum
fruits_list[-2]= 'Dragon fruit'
print(fruits_list)
##Dragon fruit replaced Grapes negative number starts from the right of the list
##add to a list append only add one item at a time
fruits_list.append('Grape')
print(fruits_list)
##insert an item in a position
fruits_list.insert (2,'Lime')
print(fruits_list)
## add multiple items on the list
fruits_list.extend(['Passion fruit','Lychee'])
print(fruits_list)

##combine two lists with the plus sign
fruits_list2 =['Plum','Cucumber','Apricot']
fruits_list = fruits_list2 + fruits_list
print(fruits_list)
##index Find the index of an item on a list.  Must be an exact match
fruits_list.index('Mango')
#comparison == 
for fruits in fruits_list2:
    if fruits =='Plum':

        print(fruits)

        fruits  = ['Apple', 'Orange', 'Plum']
        inventory =[12,7,9]
        for fruit,count in zip(fruits,inventory):
            print(f'{fruit},inventory:{count}')



