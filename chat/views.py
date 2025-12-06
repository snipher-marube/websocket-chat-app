from django.shortcuts import render

def room(request, room_name='general'):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })