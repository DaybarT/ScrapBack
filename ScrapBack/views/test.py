from django.http import JsonResponse,HttpResponse

class TestView():
    def get(self):
        return JsonResponse({"texto":"OK"})