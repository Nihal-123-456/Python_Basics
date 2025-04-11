def check_guess(num, guess):
    if guess>100 or guess<1:
        return('invalid')

    if guess == num:
        return ('correct')
        
    elif guess < num:
        if guess < num-30:
            return('too low')
        else:
            return('lower')
    else:
        if guess > num+30:
            return('too high')
        else:
            return('higher')