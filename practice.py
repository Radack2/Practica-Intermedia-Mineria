#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:23:39 2020

@author: Eber Sanchez Rodriguez

Practica Intermedia
"""

def percentil(lista, perc):
    pm = (len(lista)-1)*perc
    pl = mt.floor(pm)
    pu = mt.ceil(pm)
    
    return lista[pl]+(lista[pu]-lista[pl])*perc

def summary(lista,name):
    lista.sort()

    Minimo = lista[0]
    Maximo = lista[-1]
    
    mediana = percentil(lista, 0.5)
    fc = percentil(lista, 0.25)
    tc = percentil(lista, 0.75)
    
    media = sum(lista)/len(lista)
    
    varianza=sum([(i-media)**2 for i in lista]) / (len(lista)-1)
    deviation = mt.sqrt(varianza)
    
    print('*********** Summary for ' + name + ' ***********')
    
    print('Minimo',Minimo)
    print('Maximo',Maximo)
    print('Mediana',mediana)
    print('Primer cuatil',fc)
    print('Tercer cuartil',tc)
    print('Varianza',varianza)
    print('Desviacion estandar',deviation)
    print('Media',media)
    print('\n')
    
def Problema1(data):
    datos=data[['Gender','ConvertedComp']]
    datos=datos.dropna()
    
    #Men
    man=datos[datos['Gender']=='Man']
    man2= datos[datos['Gender'].str.contains('Man;')]
    man = pd.concat([man,man2])
    salario_m = man['ConvertedComp'].tolist()
    salario_m = [s for s in salario_m if s > 0]
    
    #Woman
    woman = datos[datos['Gender']=='Woman']
    woman2 = datos[datos['Gender'].str.contains('Woman;')]
    woman = pd.concat([woman,woman2]) 
    salario_w = woman['ConvertedComp'].tolist()
    salario_w = [s for s in salario_w if s > 0]
    
    #No-binary
    nbinary = datos[datos['Gender'].str.contains('genderqueer')]
    salario_nb = nbinary['ConvertedComp'].tolist()
    salario_nb = [s for s in salario_nb if s > 0]
    
   
    
    summary(salario_m, 'Man')
    plt.figure(1)
    plt.boxplot(salario_m)
    plt.title('Man')
    plt.show()
    
    summary(salario_w, 'Woman')
    plt.figure(2)
    plt.boxplot(salario_w)
    plt.title('Woman')
    plt.show()
    
    summary(salario_nb, 'Non-binary, genderqueer, or gender non-conforming')
    plt.figure(3)
    plt.boxplot(salario_nb)
    plt.title('Genderqueer')
    plt.show()
  

def problema2(data):
    datos=data[['Ethnicity','ConvertedComp']]
    datos=datos.dropna()
    etnia = datos['Ethnicity']
    sin = [s for s in etnia if not ';' in s ]

    lista_etnias = []
    for i in sin:
        if not i in lista_etnias:
            lista_etnias.append(i)
    
    i=1
    for e in lista_etnias:
        salario_e = datos[datos['Ethnicity'].str.contains(e)]
        salario = salario_e['ConvertedComp'].tolist()
        salario = [s for s in salario if s > 0]
        summary(salario,e)
        plt.figure(i)
        plt.boxplot(salario)
        plt.title(e)
        i+=1
        
def problema3(data):
    datos=data[['DevType','ConvertedComp']]
    datos=datos.dropna()
    dev = datos['DevType']
    sin = [s for s in dev if not ';' in s ]

    lista_dev = []
    for i in sin:
        if not i in lista_dev:
            lista_dev.append(i)
    
    i=1
    for e in lista_dev:
        salario_dev = datos[datos['DevType'].str.contains(e)]
        salario = salario_dev['ConvertedComp'].tolist()
        salario = [s for s in salario if s > 0]
        summary(salario,e)
        plt.figure(i)
        plt.boxplot(salario)
        plt.title(e)
        i+=1
        
    
def problema4(data):
    datos=data[['Country','ConvertedComp']]
    datos=datos.dropna()
    country = datos['Country']
    
    
    lista_country = []
    for i in country:
        if not i in lista_country:
            lista_country.append(i)
        
    
    for e in lista_country:
        salario_dev = datos[datos['Country'].str.contains(e)]
        salario = salario_dev['ConvertedComp'].tolist()
        salario = [s for s in salario if s > 0]
        if len(salario) and len(salario)>1:
            median = percentil(salario, 0.5)
            mean = sum(salario)/len(salario)
            varianza=sum([(i-median)**2 for i in salario]) / (len(salario)-1)
            deviation = mt.sqrt(varianza)
            print('***********' + e + ' ***********')
            print('Median:',median)
            print('Mean:',mean)
            print('Standard deviation:',deviation)
            print('\n')
            
        elif len(salario) == 1:
            print('***********' + e + ' ***********')
            median = salario[0]
            mean = salario[0]
            print('Median: ',median)
            print('Mean: ',mean)
            print('Standard deviation:','No se puede calcular, solo se tiene un dato')
            print('\n')
            
        else:
            print('***********' + e + ' ***********')
            print('No se tiene ningun dato')
            print('\n')
            
def problema5(data):
    datos=data['DevType']
    datos=datos.dropna()
    sin = [s for s in datos if not ';' in s ]
    
    lista_dev = []
    for i in sin:
        if not i in lista_dev:
            lista_dev.append(i)
    
    datos = pd.DataFrame(datos)       
    frecuencia = []  
    for e in lista_dev:
        salario_e = datos[datos['DevType'].str.contains(e)]
        salario_e['DevType'].tolist()
        frecuencia.append([e,len(salario_e)])
       
    x = []
    y = []
    for i,j in frecuencia:
        x.append(i)
        y.append(j)

    fig,ax = plt.subplots()
    ax.bar(x,y)
    plt.xticks(rotation=90)
    plt.title('Developer type')
    plt.show()
    
    
def problema6(data):
    import pandas as pd
    datos=data[['Gender','YearsCode']]
    datos=datos.dropna()
    
    
    datos=datos.replace('Less than 1 year','0.5')
    datos=datos.replace('More than 50 years','55')
    
    datos['YearsCode'] = pd.to_numeric(datos['YearsCode'])
    
    genero = datos['Gender']
    sin = [s for s in genero if not ';' in s ]
    
    lista_generos = []
    for i in sin:
        if not i in lista_generos:
            lista_generos.append(i)
    
    i=1
    for e in lista_generos:
        pd = datos[datos['Gender'].str.contains(e)]
        plt.figure(i) 
        plt.title('Years Code ' + e)
        plt.hist(pd['YearsCode'], bins=10)
        i+=1
        
def problema7(data):
    datos=data[['DevType','WorkWeekHrs']]
    datos=datos.dropna()
    
    dev = datos['DevType']
    sin = [s for s in dev if not ';' in s ]
    
    lista_dev = []
    for i in sin:
        if not i in lista_dev:
            lista_dev.append(i)
    
    i=1
    for e in lista_dev:
        salario_dev = datos[datos['DevType'].str.contains(e)]
        sal = salario_dev['WorkWeekHrs'].tolist()
        plt.figure(i) 
        plt.title('WorkWeekHrs ' + e)
        plt.hist(sal, bins=10,range=(0,200))
        i+=1
        
def problema8(data):
    datos=data[['Gender','Age']]
    datos=datos.dropna()
    
    
    genero = datos['Gender']
    sin = [s for s in genero if not ';' in s ]
    
    lista_generos = []
    for i in sin:
        if not i in lista_generos:
            lista_generos.append(i)
    
    i=1
    for e in lista_generos:
        pd = datos[datos['Gender'].str.contains(e)]
        plt.figure(i) 
        plt.title('Age ' + e)
        plt.hist(pd['Age'], bins=10,color='y')
        i+=1
        
def problema9 (data):
    datos=data[['Age','LanguageWorkedWith']]
    datos=datos.dropna()
    lenguajes = datos['LanguageWorkedWith']
    
    sin = [s for s in lenguajes if not ';' in s ]
    
    lista_lenguajes = []
    
    for i in sin:
        if not i in lista_lenguajes:
            lista_lenguajes.append(i)
    
    
    for e in lista_lenguajes:
        if e == 'Python':
            age_l = datos[datos['LanguageWorkedWith'].str.contains('Pytho')]
        elif e == 'C++':
            age_l = datos[datos['LanguageWorkedWith'].str.contains('C+')]
        else:
            age_l = datos[datos['LanguageWorkedWith'].str.contains(e)]
           
        edad = age_l['Age'].tolist()
        if len(edad) > 0:
            median = percentil(edad, 0.5)
            mean = sum(edad)/len(edad)
            varianza=sum([(i-median)**2 for i in edad]) / (len(edad)-1)
            deviation = mt.sqrt(varianza)
            print('***********' + e + ' ***********')
            print('Median:',median)
            print('Mean:',mean)
            print('Standard deviation:',deviation)
            print('\n')
            
        else:
            print('***********' + e + ' ***********')
            print('No se puede calcular, datos insuficientes')
            print('\n')

def problema10(data):
    datos=data[['YearsCode','ConvertedComp']]
    datos=datos.dropna()
    
    datos=datos.drop(datos[datos['YearsCode']== 'Less than 1 year'].index)
    datos=datos.drop(datos[datos['YearsCode']== 'More than 50 years'].index)
    
    datos['YearsCode'] = pd.to_numeric(datos['YearsCode'])
    
    correlacion=datos.corr()
    
    print('Correlacion entre experiencia y salario')
    print('Correlacion = ', correlacion['YearsCode']['ConvertedComp'])
    
def problema11(data):
    datos=data[['Age','ConvertedComp']]
    datos=datos.dropna()
    
    datos=datos.drop(datos[datos['Age'] < 5 ].index)
    
    correlacion=datos.corr()
    
    print('Correlacion entre edad y salario')
    
    print('Correlacion = ', correlacion['Age']['ConvertedComp'])
    
def problema12(data):
    datos=data[['EdLevel','ConvertedComp']]
    datos=datos.dropna()
    datos=datos.replace('Bachelor’s degree (BA, BS, B.Eng., etc.)','6')
    datos=datos.replace('Some college/university study without earning a degree','4')
    datos=datos.replace('Master’s degree (MA, MS, M.Eng., MBA, etc.)','7')
    datos=datos.replace('Other doctoral degree (Ph.D, Ed.D., etc.)','8')
    datos=datos.replace('Primary/elementary school','2')
    datos=datos.replace('Associate degree','5')
    datos=datos.replace('Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)','3')
    datos=datos.replace('Professional degree (JD, MD, etc.)','6')
    datos=datos.replace('I never completed any formal education','1')
    datos['EdLevel'] = pd.to_numeric(datos['EdLevel'])
    correlacion=datos.corr()
    print('Correlacion entre nivel educacion y salario')
    print('Correlacion = ', correlacion['EdLevel']['ConvertedComp'])

def problema13(data):
    datos=data['LanguageWorkedWith']
    datos=datos.dropna()
    
    sin = [s for s in datos if not ';' in s ]
    
    lista_lenguajes = []
    for i in sin:
        if not i in lista_lenguajes:
            lista_lenguajes.append(i)
    
    datos = pd.DataFrame(datos)       
    frecuencia = []  
    
    for e in lista_lenguajes:
        if e == 'Python':
            salario_e = datos[datos['LanguageWorkedWith'].str.contains('Pytho')]
            salario_e['LanguageWorkedWith'].tolist()
            frecuencia.append([e,len(salario_e)])
        elif e == 'C++':
            salario_e = datos[datos['LanguageWorkedWith'].str.contains('C+')]
            salario_e['LanguageWorkedWith'].tolist()
            frecuencia.append([e,len(salario_e)])
        else:
            salario_e = datos[datos['LanguageWorkedWith'].str.contains(e)]
            salario_e['LanguageWorkedWith'].tolist()
            frecuencia.append([e,len(salario_e)])
        
    x = []
    y = []
    for i,j in frecuencia:
        x.append(i)
        y.append(j)
    
    fig,ax = plt.subplots()
    ax.bar(x,y,color='g')
    plt.xticks(rotation=90)
    plt.title('Programming languages')
    plt.show()


import pandas as pd
import math as mt
import matplotlib.pyplot as plt

plt.rcParams.update({'figure.max_open_warning': 0})

w_d = 'C:/Users/MI PC/Documents/Eber/Mineria/'
i_f = w_d +'survey_results_public.csv'

data = pd.read_csv(i_f)

Problema1(data)
problema2(data)
problema3(data)
problema4(data)
problema5(data)
problema6(data)
problema7(data)
problema8(data)
problema9(data)
problema10(data)
problema11(data)
problema12(data)
problema13(data)







    
