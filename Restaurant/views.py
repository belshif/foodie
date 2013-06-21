from django.db.models import Q
from django.shortcuts import render_to_response
from Restaurant.models import *
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context


def index(request):
	template = get_template('index.html')
	menu_item = Menu_Item.objects.filter().distinct()
	p_item=menu_item.filter(i_name = "Yebeg T'bbs")
	s_item=menu_item.filter(i_name = "Chicken Pasanda")
	variables = Context({
	"popular": p_item,
	"s_pick": s_item
})
	output=template.render(variables)
	return HttpResponse(output)

def search_result(request):
	query_browse = request.GET.get('b')
	query_input = request.GET.get('q')
	query_cuisine=request.GET.get('c')
	query_location=request.GET.get('l')
	query_delivery = request.GET.get('d')
	query_pickup = request.GET.get('p')
	
	restaurant = Restaurant.objects.filter().distinct()
	location = Location.objects.filter().distinct()
	cuisine = Cuisine.objects.filter().distinct()
	menu_item = Menu_Item.objects.filter().distinct()
	d_item=menu_item.filter(i_name = "Yebeg T'bbs")
	results=Menu_Item.objects.filter().distinct()
	
	if query_input:
		qset=(Q(i_name__icontains=query_input))
		results=results.filter(qset).distinct()
	else:
		query_input=""
	if query_cuisine:
		qset=(Q(i_cuisine__c_name__icontains=query_cuisine))
		results= results.filter(qset).distinct()
	if query_location:
		qset=(Q(i_restaurant__r_location__l_name__icontains=query_location))
		results= results.filter(qset).distinct()
	if query_delivery:
		qset=(Q(i_restaurant__r_delivery=query_delivery))
		results= results.filter(qset).distinct()
	if query_pickup:
		qset=(Q(i_restaurant__r_pickup=query_pickup))
		results= results.filter(qset).distinct()
	if not (query_input or query_cuisine or query_location or query_delivery or query_pickup):
		results=[]
	

	return render_to_response("search_result.html",{"results": results,
	 "query": query_input,
	"query_browse":query_browse ,
	"d_item":d_item,
	 "query_cuisine":query_cuisine,
	'restaurant': restaurant,
	'cuisine': cuisine,
	 'location': location})

def item_select(request,path):
	try:
		results=Restaurant.objects.filter(r_name=path)
		return render_to_response("item_select.html",{"results": results})

	
	except Page.DoesNotExist:
		raise Http404("Page does not exist")


	'''
def static_page(request, page_alias):    # page_alias holds the part of the url
    try:
        active = Page.objects.get(page_alias=page_alias)
    except Page.DoesNotExist:
        raise Http404("Page does not exist")'''