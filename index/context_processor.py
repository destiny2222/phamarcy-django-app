from index.models import Level , Categoryshop
from PANS.models import  pancategory
from Study.models import SemesterCategory

def sch_level(request):
    return {
        'sch_level': Level.objects.all()
    }


def menu_shop(request):
    return {
        'menu_shop': Categoryshop.objects.all()
    }


def pans(request):
    return {
        'pens': pancategory.objects.all()
    }        


def semest(request):
    return {
        'semest': SemesterCategory.objects.all()
    }    