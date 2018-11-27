def ask_user():
    answer = ''
    answers = {
    'How are you?': 'Good!',
    'What are you doing?': 'I write code now!',
    'Where you going': 'I go do code!',
    '11':'22',
    'aaa':'fff'
    }
    while True:
        answer = input('How are you?...')
        if answer in answers:
            print(answers[answer])

ask_user()