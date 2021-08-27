import random
def main():
  sum=0
  cnt=int(input('how many time would you like to roll?'))
  mx=int(input('how many side are the dice?'))
  for i in range(0,cnt):
    roll=random.randint(1,mx)
    if roll==1:
      print(f'You rolled a {roll}!fail')
    elif roll ==mx:
      print(f'You rolled a {roll}!success')
    else:
      print(f'You rolled a {roll}')
    sum+=roll
  print(f'You rolled a total of {sum}')

if __name__== "__main__":
  main()