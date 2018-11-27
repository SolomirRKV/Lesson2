def user_allocator(age = 15):
    if age < 3 and age > 0:
        msg_for_user = 'You must lay in cradle'
    elif age < 7:
        msg_for_user = 'Go to kindergarten'
    elif age < 18:
        msg_for_user = 'Go to shcool'
    elif age < 23:
        msg_for_user = 'Go to the university'
    elif age < 65:
        msg_for_user = 'Go to work'
    elif age < 100:
        msg_for_user = 'Go to home'
    else:
        msg_for_user = 'Don\'t go anywhare'
    print (msg_for_user)




user_allocator(int(input('Please, input you age:' )))
