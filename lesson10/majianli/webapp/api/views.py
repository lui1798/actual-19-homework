import subprocess

from django.http import HttpResponse




def CommandView(request):
	cmd = request.GET.get('cmd', None)
	if cmd:
		p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		stdout, stderr = p.communicate()
                # print("haha")
		return HttpResponse(stdout, content_type="text/plain")
	else:
		return HttpResponse("cmd args is required.")


def LoginView(request):
	username = request.GET.get('username', None)
	password = request.GET.get('password', None)
	if not username or not password:
		return HttpResponse("username or password args is required.")
	
	if username == 'admin' and password == '123456':
		return HttpResponse('Login ok')
	else:
		return HttpResponse('Valid failed.')
	
	
def LoginPageView(request):
	htmlStr = '''
	<html>
		<head>
			<title>51reboot login</title>
		</head>
		<body>
			<form>
				用户名： <input type="text"></br>
				密码： <input type="password">
			</form>
		</body>
	</html>
	'''
	return HttpResponse(htmlStr)
