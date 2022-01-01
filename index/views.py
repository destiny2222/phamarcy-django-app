from django.shortcuts import render,get_object_or_404,redirect
from index.models import *
from Study.models import Study, SemesterCategory, StudyCourse,Textbook
from PANS.models import payofpansdue,pancategory,section
from django.views.generic import TemplateView, ListView,DetailView
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from pharmacy import settings
# Create your views here.
def  HomeView(request):
    inform = Information.objects.all()
    exam = ExamCountdown.objects.all()
    blog = POST.objects.all()
    cours = Course.objects.all()[:8]
    excos = Exco.objects.all()[:3]
    
    context = {
            'exam': exam,
            'blog': blog,
            'inform': inform,
            'cours':cours,
            'excos':excos,
         }
    return render(request, 'index.html', context)



def AboutView(request):
    exam = ExamCountdown.objects.all()
    
    context = {
        'exam': exam,
    }
    return render(request, 'about.html', context)    



class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = {}
        return  context




class ShopView(TemplateView):
    model = ShopIteam
    template_name = 'shop.html'

    def get_context_data(self, **kwargs):
        sales = ShopIteam.objects.filter(Active=True)
        context = {
          'sale':sales,
        }
        return context


class categoryshop_details(DetailView):
    model = Categoryshop
    template_name = 'category_shop.html'
    
    def get_context_data(self, **kwargs):
        categories = get_object_or_404(Categoryshop, pk=self.kwargs['pk'])
        shops = categories.shops.all()
        context = {
           'categories':categories,
            'shops':shops,
        }
        return context



class BlogView(ListView):
    model = POST
    template_name = 'blog.html'


    def get_context_data(self, **kwargs):
        blog = POST.objects.all()
        recentpost = POST.objects.all().order_by('-id')[:4]
        paginator = Paginator(blog, 2)
        page = self.kwargs.get('page')

        try:
            blog = paginator.page(page)
        except PageNotAnInteger:
                # If page is not an integer deliver the first page
            blog = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            blog = paginator.page(paginator.num_pages)
        context = {
            'blog': blog,
            'recentpost': recentpost,
            'page':page,
         }
        return context


class BlogDetailsView(DetailView):
    model = POST
    template_name = 'blog-single.html'


    def get_context_data(self, **kwargs):
        recentpost = POST.objects.all().order_by('-id')[:4]
        details = POST.objects.all().get(pk=self.kwargs['pk'])
        context = {
            'recentpost': recentpost,
            'details': details,
        }
        return  context





class ContactView(TemplateView):
    template_name = 'contact.html'        



class courseView(ListView):
    Model = Course
    queryset = Course.objects.all()
    template_name = 'course/course.html'
    paginate_by = 3

    # def get_queryset(self):
    #      return Course.objects.all()

    # def get_context_data(self, **kwargs):
    #     coures = Course.objects.all()
    #     context = {
    #         'coures':coures,
    #     }
    #     return context


class UploadFileView(ListView):
    model = UploadFiles
    template_name = 'course-list.html'
    def get_context_data(self, **kwargs):
        files = UploadFiles.objects.filter(course__pk=self.kwargs['pk'])
        course = Course.objects.get(pk=self.kwargs['pk'])

        context = {
            'course':course,
            'files':files,
        }
        return context

    # return render(request, 'course-list.html', context)
    


class InformationView(TemplateView):
    model =Information

    template_name = 'information.html' 

    def get_context_data(self, **kwargs):
        inform = Information.objects.all()
        context = {
            'inform': inform, 
        }
        return context





def search(request):
    if request.method == 'POST':
        post = []
        searched = request.POST['searched']
        if searched:
            post = Course.objects.all().filter(name=searched)
        content ={
        'post':post,
        'searched':searched,
        }
        return render(request, 'search.html', content)

    
 
class ExcosView(ListView):
    Model = Exco
    template_name  = 'excos.html'
    queryset = Exco.objects.all()
    def get_context_data(self, **kwargs):
        ecoxs = Exco.objects.all()
        context = {
           'ecoxs':ecoxs,
        }
        return context


class accommodationview(ListView):
    model = Accommodation
    template_name = 'accommodation.html'
    def get_context_data(self, **kwargs):
        accom = Accommodation.objects.all()
        context = {
          'accom':accom,
        }
        return context


class PensView(ListView):
    model = payofpansdue
    template_name ='pans.html'


    def get_context_data(self, **kwargs): # new         
          context =super().get_context_data(**kwargs)        
          context['key'] = settings.PUBLISHABLE_KEY
          context['account'] = payofpansdue.objects.all() 
          context['sect ']= section.objects.filter(active=True)      
          return context    
     
    # def get_context_data(self, **kwargs):
    #     context = ['key'] = settings.PUBLISHABLE_KEY
    #     account = payofpansdue.objects.all()
    #     sect = section.objects.filter(active=True)
        
    #     context = {
    #        'sect':sect,
    #        'account':account,
    #     }
    #     return context 

class pans(DetailView):
    model = pancategory
    template_name = 'pan_category.html'
    
    def get_context_data(self, **kwargs):
        categories = get_object_or_404(pancategory, pk=self.kwargs['pk'])
        sected = categories.sected.all()
        context = {
           'categories':categories,
            'sected':sected,
        }
        return context


class textbook(TemplateView):
    model = Textbook
    template_name = 'textbook.html'
    def get_context_data(self, **kwargs):
        text = Textbook.objects.all()
        context = {'text':text}
        return context       


class studyView(ListView):
    model = Study
    template_name = 'study.html'   
    def get_context_data(self, **kwargs):
        course = StudyCourse.objects.filter(level__pk=self.kwargs['id'])
        sem = Study.objects.all()
        context = {
            'course':course,
            # 'levels':levels,
        }
        return context


class studycategoryView(DetailView):
    model = SemesterCategory
    template_name = 'semester.html'
    
    def get_context_data(self, **kwargs):
        categories = get_object_or_404(SemesterCategory, pk=self.kwargs['pk'])
        semest = categories.semest.all()
        context = {
            'categories':categories,
            'semest':semest,
        }
        return context


class sucess(TemplateView):
    template_name = 'suc.html'