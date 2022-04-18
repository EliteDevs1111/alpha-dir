import sys

version_info = sys.version_info
x_format = """
Python 🐍
version = {ver}
release = {rel}
""".format(ver=str(version_info.major) + "." + str(version_info.minor)+'.'+str(version_info.micro), rel=version_info.releaselevel)

print(x_format)
