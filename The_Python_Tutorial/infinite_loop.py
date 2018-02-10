words = ['cat', 'window', 'defenestrate']
for w in words:
    print('outer:', words)
    if len(w) > 6:
        words.insert(0, w)
        print('inner:', words)
