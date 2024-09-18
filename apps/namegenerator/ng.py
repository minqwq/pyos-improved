from faker import Faker as f
zh = f(['zh_CN'])
ja = f(['ja_JP'])
en = f(['en_US'])
print("zh_CN:")
for china in range(4):
    print(zh.name())
print("马冬梅")
print("ja_JP:")
for japan in range(4):
    print(ja.name())
print("古明地 恋")
print("en_US:")
for america in range(4):
    print(en.name())
print("Donald J. Trump")
