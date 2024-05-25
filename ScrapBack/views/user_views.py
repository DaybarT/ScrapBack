from django.http import JsonResponse

class Auth():
    def login(self,req):

        if req.method == 'POST':
            usuario = req.POST.get('usuario')
            passw = req.POST.get('passw')
            
            if self.authenticate(usuario, passw): #si authenticate obtiene un objeto o un true, entiende que es exitoso y entra
                return JsonResponse({'status': 'success', 'message': 'Login successful'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid credentials'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)
    
    def forgotPassw(self,req):
        
        return
    
    def changePassw(self,req):
        
        return
    
    def register(self,req):
        
        return
    
    def authToken(self,req):
        
        return
    
    def authenticate(self, usuario, passw):
        
        #consulta a la bbdd, autentica etc.
         
        return usuario == "admin" and passw == "admin123"
    
    