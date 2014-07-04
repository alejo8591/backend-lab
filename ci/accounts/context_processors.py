sentences = ['colombia vs brasil', 'help press', 'aprress']

def test_context_processor(request):
	return {'sentences': sentences }