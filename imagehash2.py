from PIL import Image
import imagehash

image = "./data3/frame212.jpg"
image2 = "./data2/frame6.jpg"
hash_res1 = imagehash.average_hash(Image.open(image))
hash_res3 = imagehash.average_hash(Image.open(image2))

i = 0
# while i < 135:
# 	hash_res2 = imagehash.average_hash(Image.open('./data2/frame'+str(i)+'.jpg'))
# 	i +=1

# 	print hash_res1-hash_res2
# print "N"
# print hash_res1 - hash_res3
j = 0

while i < 257:
	hash1 = imagehash.average_hash(Image.open('./data2/frame'+str(i)+'.jpg'))

	#hash2 = imagehash.average_hash(Image.open('./data3/frame'+str(i)+'.jpg'))
	i +=1
	print "I::",str(i) 
	if hash_res1-hash1 <=15:
		j +=1
		print "Match"
print j