from app import app
def is_active(arg):
	
	if app.config['CU_PAGE'] == arg:
		return "active"