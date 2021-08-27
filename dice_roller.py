import random
def main():
  sum=0
  cnt=2
  for i in range(0,cnt):
    roll=random.randint(1,6)
    print(f'You rolled a {roll}')
    sum+=roll
  print(f'You rolled a total of {sum}')

if __name__== "__main__":
  main()