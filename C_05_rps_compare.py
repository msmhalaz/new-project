# Check that users have entered a valid
# option based on a list
def rps_compare(user_response, valid_ans):
    while True:

        # Get user response and make sure its lowercase
        user_response = user_response.lower()

        for item in valid_ans:
         # check if the user response is a word in the list
            if item == user_response:
                return item

           # check if the user response is the same as
           # the first letter of an item in the list
            elif user_response == item[0]:
                 return item

        return "invalid"


# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ('rock', 'rock', 'tie'),
    ('rock', 'paper', 'lose'),
    ('rock', 'scissors', 'win'),
    ('paper', 'rock', 'win'),
    ('paper', 'paper', 'tie'),
    ('paper', 'scissors', 'lose'),
    ('scissors', 'rock'),
    ('scissors', 'paper', 'win'),
    ('scissors', 'scissors', 'tie'),
]

# run tests!
for item in to_test:
    # retrieve test case and expected value
    user = item[0]
    comp = item[1]
    expected = item[2]

    # get actual value (ie: test ticket function)
    actual = rps_compare(user, comp)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {user} vs {comp}expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {user} vs {comp}expected: {expected}, received: {actual} ❌❌❌")
