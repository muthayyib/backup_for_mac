#file name or file object is f

# f = open('data.txt','r')
# # for i in f:
# #     print(i)
# # print(f.write("helldoooo"))
#
#
# f1 = open('selfintro.txt', 'w')
# for data in f:
#     f1.write(data)


#read am image in rb mode means read binarty
#copy taht image into antoer file
img = open('shot.png','rb')
cpimg = open('copyshot.png','wb')
for i in img:
    cpimg.write(i)

f5 = open('/home/thayyib/Desktop/vision.pdf','rb')
f8 = open('visioncp.pdf','wb')

for n in f5:
    print(n)
    f8.write(n)
