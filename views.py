from django.shortcuts import render
from .models import PhnomPenh
from .models import Battambang
from .models import Kandal
from .models import Pursat
from .models import Kampongthom
from .models import Preasihanouk
from .models import SteungTreng
from .models import Bantaeymeanchey
from .models import Kampongcham
from .models import Siemreap
from .models import Preyveng
from .models import Svayreang
from .models import Takeo  
from .models import Tbongkhmum
from .models import Kampot 
from .models import Kampongspeu
from .models import KampongChnang
from .models import Kohkong
from .models import kratie
from .models import PreasVihea
from .models import Mondolkiri
from .models import Ratanakiri
from .models import Oudormeanchey
from .models import Kep
from .models import Pailin











def home (request):
    return render (request, "event/home.html",{})
def search_venues(request):
    searched = request.POST.get('searched')
    venues = PhnomPenh.objects.filter(khan_one__contains = searched)
    kandal = Kandal.objects.filter(First_dis__contains=searched)
    btb = Battambang.objects.filter(btb__contains=searched)
    pursat = Pursat.objects.filter(ps__contains=searched)
    k_t = Kampongthom.objects.filter(kpt__contains=searched)
    k_p_s = Preasihanouk.objects.filter(kps__contains=searched)
    s_t = SteungTreng.objects.filter(st__contains=searched)
    b_m_c = Bantaeymeanchey.objects.filter(bmc__contains=searched)
    k_p_c = Kampongcham.objects.filter(kpc1__contains=searched)
    s_r = Siemreap.objects.filter(sr__contains=searched)
    p_v = Preyveng.objects.filter(pv__contains=searched)
    s_v_r = Svayreang.objects.filter(svr__contains=searched)
    t_k = Takeo.objects.filter(tk__contains=searched)
    t_b = Tbongkhmum.objects.filter(tb__contains=searched)
    k_p = Kampot.objects.filter(kp__contains=searched)
    s_p = Kampongspeu.objects.filter(speu__contains=searched)
    k_r = KampongChnang.objects.filter(kongrey__contains=searched)
    k_k = Kohkong.objects.filter(Gpath__contains=searched)
    d_p = kratie.objects.filter(dolphin__contains=searched)
    f_t = PreasVihea.objects.filter(fkthailand__contains=searched)
    i_d_g = Mondolkiri.objects.filter(indigenous__contains=searched)
    y_l = Ratanakiri.objects.filter(yeaklorm__contains=searched)
    t_m = Oudormeanchey.objects.filter(khaet_bos_tamok__contains=searched)
    KeP = Kep.objects.filter(smallest__contains=searched)
    jav_jit = Pailin.objects.filter(diamond__contains=searched)
    if request.method == "POST":
        
       return render (request, "event/search_venues.html",{
           'searched':searched, 
           'venues':venues, 
           'kandal':kandal,
           'btb':btb,
           'pursat':pursat,
           'k_t':k_t,
           'k_p_s':k_p_s,
           's_t':s_t,
           'b_m_c':b_m_c,
           'k_p_c': k_p_c,
           's_r':s_r,
           'p_v':p_v,
           's_v_r':s_v_r,
           't_k':t_k,
           't_b':t_b,
           'k_p':k_p,  
           's_p':s_p,
           'k_r':k_r,
           'k_k':k_k,
           'd_p':d_p,  
           'f_t':f_t,  
           'i_d_g':i_d_g,  
           'y_l':y_l,   
           't_m':t_m,
           'KeP':KeP,
           'jav_jit': jav_jit
           })
    else:
        return render (request, "event/search_venues.html",{})

# Create your views here.
