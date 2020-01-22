shaq = "Shaquille O'Neal"
print('z' in shaq)
print(shaq.find('z'))
try ValueError:
  print(shaq.index('z')) # ValueError
except:
  print("找不到")