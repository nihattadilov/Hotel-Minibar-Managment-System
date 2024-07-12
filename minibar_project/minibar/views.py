from django.shortcuts import render, get_object_or_404
from .models import Room, Sale
from django.db.models import Sum
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook
from django.http import HttpResponse
from datetime import datetime

def index(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'index.html', context)

def room_sales(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    sales = Sale.objects.filter(room=room)

    total_payment = sum(sale.quantity * sale.product.price for sale in sales)

    for sale in sales:
        sale.total = sale.quantity * sale.product.price  

    context = {
        'room': room,
        'sales': sales,
        'total_payment': total_payment,
    }
    return render(request, 'room_sales.html', context)

def download_sales_report(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if not start_date or not end_date:
        return HttpResponse('Error: Missing start_date or end_date parameters.', status=400)

    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    except ValueError:
        return HttpResponse('Error: Invalid date format. Use YYYY-MM-DD.', status=400)

    sales = Sale.objects.filter(date__range=[start_date, end_date]).select_related('room', 'product')

    wb = Workbook()
    ws = wb.active
    ws.title = "Minibar Sales Report"

    ws.append(['Date', 'Room Number', 'Products', 'Quantities', 'Price per Unit', 'Total'])

    total_payment = 0 

    for sale in sales:
        total = sale.quantity * sale.product.price
        total_payment += total
        ws.append([
            sale.date,
            sale.room.number,
            sale.product.name,
            sale.quantity,
            sale.product.price,
            total
        ])

    ws.append([])
    ws.append(['Total Payment', '', '', '', '', total_payment])

    filename = f"minibar_sales_report_{start_date}_to_{end_date}.xlsx"
    
    response = HttpResponse(content=save_virtual_workbook(wb), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={filename}'

    return response
