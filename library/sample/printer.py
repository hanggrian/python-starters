from library_extension.mypattern import pattern

for text in (
    'John Doe',
    'hello world',
):
    print(f'{text}:', bool(pattern.search(text)))
