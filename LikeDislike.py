_ = input()
array = input().split()
like = set(input().split())
dislike = set(input().split())
print(sum((i in like) - (i in dislike) for i in array))


name =["Ram", "Shyam"]
name1 = set(name)
print(name1)