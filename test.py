from termcolor import colored

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])

print(text)