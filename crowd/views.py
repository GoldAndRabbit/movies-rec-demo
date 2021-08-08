from django.http import HttpResponse
from django.shortcuts import render

def get_suggest_from_crowd_type(crowd):
    metrics = ['渗透率', '近度', '金额', '消耗']
    if crowd is '低低低低':
        suggests = '针对[' + crowd + ']人群的运营建议, 此处略去1w字...'
    elif crowd is '低高高高':
        suggests = '针对[' + crowd + ']人群的运营建议, 此处略去1w字...'
    else:
        suggests = '针对[' + crowd + ']人群的运营建议, 此处略去1w字...'
    return suggests

def crowd_view(request):
    names        = ['内容1', '内容2', '内容3', '内容4', '内容5', '内容6']
    data         = [1, 2, 3, 4, 5, 6]
    cxt          = {}
    cxt['names'] = names
    cxt['data']  = data
    cxt['penetration'], cxt['recent'], cxt['amount'], cxt['cost'] = '低', '低', '低', '低'
    if request.GET:
        cxt['penetration']  = request.GET['penetration']
        cxt['recent']       = request.GET['recent']
        cxt['amount']       = request.GET['amount']
        cxt['cost']         = request.GET['cost']
    crowd = cxt['penetration'] + cxt['recent'] + cxt['amount'] + cxt['cost']
    suggest = get_suggest_from_crowd_type(crowd)
    cxt['suggest'] = suggest
    return render(request, 'crowd.html', cxt)
