global Orsa
Orsa = 0
import random

lista_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

def gcd(a, b):
	global Orsa
	while b != 0:
		a, b = b, a % b
		Orsa+= 4
	return a

def multiplicative_inverse(e, phi):
	global Orsa
	d = 0
	x1 = 0
	x2 = 1
	y1 = 1
	temp_phi = phi
	Orsa+=5
	while e > 0:
		temp1 = temp_phi/e
		temp2 = temp_phi - temp1 * e
		temp_phi = e
		e = temp2
		
		x = x2- temp1* x1
		y = d - temp1 * y1
		
		x2 = x1
		x1 = x
		d = y1
		y1 = y
		Orsa += 18
	if temp_phi == 1:
		return d + phi
	Orsa+=1
	
def generate_keypair(p, q):
	global Orsa
	Orsa = 0
	n = p * q
	phi = (p-1) * (q-1)
	e = random.randrange(1, phi)
	g = gcd(e, phi)
	
	while g != 1:
		e = random.randrange(1, phi)
		g = gcd(e, phi)
		Orsa += 4
	
	d = multiplicative_inverse(e, phi)
	Orsa += 12
	
	return ((n, e), (n, d))

def encrypt(pk, plaintext):
	global Orsa
	n, key = pk
	cipher = [(ord(char) ** key) % n for char in plaintext]
	Orsa+=5+len(plaintext)*key
	return cipher

def decrypt(pk, ciphertext):
	global Orsa
	n, key = pk
	plain = [chr((char ** key) % n) for char in ciphertext]
	Orsa+=5+len(ciphertext)*key
	return ''.join(plain)
	
if __name__ == '__main__':
	p = random.choice(lista_prime)
	q = random.choice([x for x in lista_prime if x != p])
	print "Generating your public/private keypairs now . . ."
	public, private = generate_keypair(p, q)
	print "Your public key is ", public ," and your private key is ", private
	message = raw_input("Enter a message to encrypt with your public key: ")
	encrypted_msg = encrypt(public, message)
	print "Your encrypted message is: "
	print ''.join(map(lambda x: str(x), encrypted_msg))
	print "Decrypting message with private key ", private," . . ."
	print "Your message is:"
	print decrypt(private, encrypted_msg)