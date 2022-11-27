import requests

oper = input("Insert the operation :").split()

r = requests.get(f'http://127.0.0.1:8080/{oper[0]}?op1={oper[1]}&op2={oper[2]}')
print(r.text)
