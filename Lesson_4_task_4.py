def la_la_song(la_line=3, la=3, excl=0):
    for key in range(la_line - 1):
        print('la-' * la, '\b\b')
    if key == la_line - 2:
        if excl == 1:
            print('la-' * (la), '\b\b!')
        else:
            print('la-' * (la), '\b\b.')

la_la_song(3,3,1)






