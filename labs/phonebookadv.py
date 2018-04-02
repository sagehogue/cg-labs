# phonebookcrud # I AM HAVING TROUBLE WITH THIS SHIT


# Support searching by:
#
# Partial Name
# Phone Number
# Partial Phrase
# If there are multiple results, display each of them. # this one remains - other above features untested but implemented

def wouldyou():
    return input('Would you like to search for a contact, add a new one, or delete one? (search/add/del): ').lower()


def searchtype():
    searchtype = input('Define your search term type. (name/phonenumber/phrase)')


def wouldyou_2():
    return input('Would you like to update this entry? (y/n): ')


def get_name():
    return input('What is the search name?: ')


def get_number():
    return input('What is the search phone number?: ')


def get_phrase():
    return input('What is the search phrase?: ')


def wouldyoudel():
    return input('Would you like to delete a contact or exit the program? (y/n/q): ')


def search_bynum(value):
    for phonebook_index in phonebook:
        for user in phonebook[phonebook_index]:
            if value == user:
                print(user)


def checkphonebook(name):
    lowerbook = phonebook.keys()
    if name in lowerbook:
        return 'yes'
    else:
        return 'no'


def chkpb_phrase(phrase):
    for phonebook_index in phonebook:
        pbk_phr = phonebook[phonebook_index][1].lower()
        user_phr = phrase.lower()
        for user in phonebook[phonebook_index][1]:
            if user_phr in pbk_phr:
                print(phonebook_index)


def newcontactdata():
    name = input('Please input your contact name: ')
    num = input("Please enter your contact's phone number: ")
    phrase = input('Please enter your contact phrase: ')
    return name, num, phrase


def updatedata():
    num = input("Please input your contact's phone number: ")
    phrase = input("Please enter your contact phrase: ")
    return num, phrase

    # Retrieve Contact


def newcontact(name, num, phrase):
    newcontact = {name: [num, phrase]}
    phonebook.update(newcontact)
    print('{} has been added to the phonebook.'.format(newcontact))


def display_searchres:


phonebook = {'Kieran': [8456331959,
                        'Good code is not written, it\'s re-written.', ], 'Lambda': [8454185633,
                                                                                     'I am a robot.']}

while True:
    # Create New Contact
    decision = wouldyou()
    if decision in 'add':
        name, num, phrase = newcontactdata()
        if name not in phonebook:
            newcontact = {name: [num, phrase]}
            phonebook.update(newcontact)
            print('{} has been added to the phonebook.'.format(newcontact))
            continue
    elif decision in 'search':
        search_type = searchtype().lower()
        if searchtype == 'name':
            search_name = get_name()
            if checkphonebook(search_name) in 'yes':
                print(phonebook[search_name])
                updatepermiss = wouldyou_2().lower()
                if updatepermiss == 'yes' or updatepermiss == 'y':
                    update_num, update_phrase = updatedata()
                    update_dict = {search_name: [update_num, update_phrase]}
                    phonebook.update(update_dict)
                    print('Contact updated.\n' + str(phonebook[search_name]))
                    continue
                elif updatepermiss == 'no' or updatepermiss == 'n':
                    print('Contact not updated.')
                    continue
                elif checkphonebook(search_name) in 'no':
                    print("I'm afraid that " + search_name + " is not in the phonebook.")
                    make_contact = input('Would you like to add ' + search_name + ' to the phonebook? (y/n): ')
                    if make_contact in 'yes' or make_contact in 'y':
                        name, num, phrase = newcontactdata()
                        newcontact(name, num, phrase)
                        print('{} has been added to the phonebook.'.format(newcontact))
                    elif make_contact in 'no' or make_contact 'n':
                        pass
        elif searchtype == 'phonenumber':
            value = get_number()
            search_bynum(value)
            continue
        elif searchtype == 'phrase':
            the_phrase = get_phrase()
            chkpb_phrase(the_phrase)
            continue
    elif decision in 'del':
        del_input = wouldyoudel()

        while True:
            if del_input in "y" or del_input in "yes":
                del_target = get_name()
                display_target = phonebook.get(del_target)
                print('Deleting {}'.format(display_target))
                del phonebook[del_target]
            elif del_input in 'q' or del_input in 'quit':
                exit()
            elif del_input in 'no' or del_input 'n':
                pass
    elif decision in 'q' or decision in 'quit':
        exit()
