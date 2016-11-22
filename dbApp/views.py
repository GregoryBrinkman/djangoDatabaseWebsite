from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *


def splashTest(request):
    template_name = 'new.html'
    print(Musicians.objects[0])
    musicians_list = Musicians.objects
    contextual = {'musicians':musicians_list}

    return render(request, template_name, contextual)

def index(request):
    template_name = 'index.html'
    contextual = ({'test': "hello!",})

    return render(request, template_name, contextual)

def MusicianList(ListView):
    model = Musicians
    contextual = 'musicians'

    def get_queryset(self):
        print("querySet")

        SSN = self.request.GET.get("ssn")
        NAME = self.request.GET.get("name")
        PHONE = self.request.GET.get("phone")
        ADDRESS = self.request.GET.get("address")
        print(SSN, NAME, PHONE, ADDRESS)




# class MusiciansCreate(CreateView):
# 	model = Musicians
# 	success_url = reverse_lazy('musicians_list')
# 	#context_object_name = 'musicians'
# 	fields = '__all__'

# class MusiciansUpdate(UpdateView):
# 	model = Musicians
# 	success_url = reverse_lazy('musicians_list')
# 	#context_object_name = 'musicians'
# 	fields = '__all__'

# 	def form_valid(self,form):
# 		#print form
# 		#print form.cleaned_data
# 		#print form.cleaned_data['ssn']
# 		#print type(form.cleaned_data['ssn'])
# 		#print ((re.search('[a-zA-Z]', form.cleaned_data['ssn'])) == None)

# 		if(((re.search('[a-zA-Z]', form.cleaned_data['ssn'])) != None)):
# 			print "Enter numbers"
# 			return HttpResponseRedirect(reverse_lazy('musicians_list'))
# 		return super(MusiciansUpdate, self).form_valid(form)

# class MusiciansDelete(DeleteView):
# 	model = Musicians
# 	success_url = reverse_lazy('musicians_list')
# 	#context_object_name = 'musicians'
# 	fields = '__all__'

# 	def post(self, request, *args, **kwargs):
# 		print request.POST
# 		print request.POST["password"]
# 		if request.POST["password"] != "cs430":
# 			return HttpResponseRedirect(reverse_lazy('musicians_list'))

#         return super(MusiciansDelete, self).post(request, *args, **kwargs)
