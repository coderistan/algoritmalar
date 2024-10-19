# coding: utf-8
# Başlangıç ve bitiş saatleri verilen bir iş listesindeki işlerin
# hangi sıra ile yapılacağını greedy algoritması ile bulma
# Activity selection problem

def find_activities(s,f):
    i = 0
    while i < len(s)+1:
        print("index:",i,"start:",s[i],"finish:",f[i])

        for k in range(len(s[i+1:])):
            if s[k+i+1] >= f[i]:
                i = k+i+1
                break
        else:
            break

def main():
    start_times = [3,7,5,10,12,14,18,20]
    finish_times = [5,8,7,13,13,16,20,24]

    find_activities(start_times,finish_times)


if __name__ == "__main__":
    main()