#函数input() 让程序暂停运行，等待用户输入一些文本。
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
  
active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
