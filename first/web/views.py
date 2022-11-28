from django.shortcuts import render

# Create your views here.
def main(req):
   kek = {'data': "Hello world! I'm alive!"}
   return render(request=req, template_name='main/index.html', context=kek)