#reverse integer
def reverse_no(x):
    if x < 0:
        x = str(abs(x))
        rev_x=x[::-1]
        print("-"+rev_x)

    else:
        x=str(x)
        rev_x=x[::-1]
        print(rev_x)



reverse_no(79653)
reverse_no(-785)
reverse_no(0)
def main():
   if __name__ == '__main__':
       main()
