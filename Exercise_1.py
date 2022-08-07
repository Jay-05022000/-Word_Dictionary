'''write a your one dictionary and then ask user to give you a key and you have
to print value of that key.assume-user will give key that is defined in dictionary'''

Dict={'kids':'ofsprings',
    'conversely' : 'contrarory',
    'country':'nation',
    'parents':'gaurdians',
    'explain':'elaborate'}

while(True):
    user_search=input("enter a key: ")
    if user_search in Dict:
        print("The synonym of your word is ",Dict[user_search])
        continue
    elif user_search=='quit':
        break
    else:
        print("Key you gave is not defined in dictionary.Enter a correct key")
        continue

