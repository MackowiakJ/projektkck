from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats

import csv
import pandas as pd


def home(request):
    print('Home')
    return render(request, 'home.html')

def instrukcje(request):
    print('Instrukcje')
    return render(request, 'instrukcje.html')

def klasy(request):
    print('Klasy')
    return render(request, 'klasy.html')


def petle(request):
    print('Pętle')
    return render(request, 'petle.html')


def funkcje(request):
    print('Funkcje')
    return render(request, 'funkcje.html')

def listy(request):
    print('Listy')
    return render(request, 'listy.html')

def liczby(request):
    print('Liczby pseudolosowe')
    return render(request, 'liczby.html')

def r_xor_p(x, y, r_xor_p='r'):
    ''' Pearson's r or its p
    Depending of what you would like to get.
    '''
    r, p = stats.pearsonr(x, y)

    if r_xor_p == 'r':
        return r
    else:
        return p
