import funkcije
import ac 


if __name__ == "__main__":
	
	provera = int(input('Za main 1, a alt 0: '))
	if provera == 1:
		username = 'boskovski650@gmail.com'
		password = 'ivanbrate2'
	else:
		username = ''
		password = ''

	

	funkcije.login(username, password)
	ac.hit_ac()
	# ac.ac_nagrade()
	# funkcije.daily(provera)

