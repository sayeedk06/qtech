from django.shortcuts import render
from django.views import View
from Search_history.models import SearchModel,Alluser, SearchTimeModel
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.
class SearchView(View):
    template_name = 'Search_history/search.html'
    def get(self, request):
        user_context = Alluser.objects.all()
        search_context = SearchModel.objects.all()
        time_context = SearchTimeModel.objects.all()
        return render(request, self.template_name, {'user_list': user_context,
                                                    'object_list': search_context,
                                                    'time_list': time_context})



def ajax_filter(request):
    filter_keyword = request.GET.getlist('keyword[]')
    filter_user = request.GET.getlist('user[]')
    print(filter_keyword)
    allSearch = SearchModel.objects.all()
    if len(filter_keyword) > 0:
        allSearch = SearchModel.objects.filter(keywords__in=filter_keyword)
        print(allSearch)
    elif len(filter_user) > 0:
        allSearch = allSearch.filter(user__username__in=filter_user)
        print(allSearch)
    template = render_to_string('Search_history/ajaxFilter.html', {'object_list': allSearch})
    return JsonResponse({'data': template})