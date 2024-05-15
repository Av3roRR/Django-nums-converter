from django.shortcuts import render

binary = [chr(i) for i in range(48, 50)]
octal = [chr(i) for i in range(48, 56)]
decimal = [chr(i) for i in range(48, 58)]
hexa = decimal + [chr(i) for i in range(ord('A'), ord('F') + 1)]
systems = [binary, octal, decimal, hexa]

# Create your views here.
def converter(request):
    context = {"message": ' '}
    if request.method == "POST":
        number = request.POST.get("number").strip()
        from_system = request.POST.get('from')
        to_system = request.POST.get('to')
        if number == '':
            context = {"message": "Вы не ввели число"}
        else:
            converted_num = converting_number(number=number, from_system=from_system, to_system=to_system)
            context = {'message': converted_num}
    return render(request, 'converter/index.html', context=context)


def converting_number(number, from_system, to_system):
    l = ['2', '8', '10', '16']
    funcs = [bin, oct, int, hex]
    curr_system = systems[l.index(from_system)]
    check_symbols = all(el in curr_system for el in number)
    if not check_symbols:
        return "Вы ввели неправильное число"
    else:
        tenth_form = int(number, int(from_system))
        if to_system == '10':
            return tenth_form
        else:
            return funcs[l.index(to_system)](tenth_form)[2:]