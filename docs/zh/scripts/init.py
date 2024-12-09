import os

a = []
r = os.listdir('D:\wjn\ddstudy\docs\zh\work\soft')
for i in r:
    tmp = f"""
- [{i}]({i})
    """
    a.append(tmp)

print("\n".join(a))


