import platform


sys = platform.system()
print(sys)
if sys == 'Darwin' or 'Linux':
    connection = '/'
else:
    connection = '\\'