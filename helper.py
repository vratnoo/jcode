from app import app
import os  
def is_active(arg):
	
	if app.config['CU_PAGE'] == arg:
		return "active"

def pagination(pg,total,next_num,prev_num):
	s = 1
	e = 3
	pgnate = {}
	pgnate['s'] = s
	pgnate['e'] = e
	

	elem = range(1,total+1)
	for i in elem:
		if(e>=len(elem)):
			e = len(elem)
		if i in range(s,e+1):
			if(pg==i):
				pgnate['s'] = s
				pgnate['e'] = e

				print(f"{e}  s->{s} e->{e}")
		else:
			e+=3
			s+=3
			if(e>=len(elem)):
				e = len(elem)

			if i in range(s,e+1):
				if(i==pg):
					pgnate['s'] = s
					pgnate['e'] = e
					print(f"{e}  s->{s} e->{e}")
		if(pgnate['e']<len(elem)):
			pgnate['next_url'] = f"?pg={pgnate['e']+1}"
			
			pgnate['is_next'] = ""
		else:
			pgnate['next_url'] = "#"
			pgnate['is_next'] = "disabled"

		if(pgnate['s']>3):
			pgnate['prev_url'] = f"?pg={pgnate['s']-1}"
			pgnate['is_prev'] = ""
		else:
			pgnate['prev_url'] = "#"
			pgnate['is_prev'] = "disabled"
	return pgnate


