def deletaMenorValor(lst, vezes = 1):
    if (vezes < 1):
        raise ValueError('Parâmetro recursao não é um valor válido')
    
    i = float("inf")
    idx_menor = -1
    idx = -1
    
    for nr in lst:
        idx += 1
        if nr < i:
            i = nr
            idx_menor = idx
    
    if (idx_menor != -1):
        lst.pop(idx_menor)   
        
    if (vezes == 1):
        return lst
    else:
        return deletaMenorValor(lst, vezes-1)

def aluno_aprovado(freq, acs, prova = 0, sub = 0, pai = None, extra = 0):
    try:
        # testando freq
        freq = float(freq)
        if (freq < 0) and (freq > 1):
            raise ValueError('freq')
        
        #testando acs
        try:
            len(acs)
        except:
            raise ValueError('acs. Não é uma lista válida')
        
        if (len(acs) != 10):
            raise ValueError('acs. Não é uma lista de 10 elementos')
            
        i = 0;    
        while (i <= len(acs)-1):
            ac = acs[i]
            
            #Se não realizou a prova então é zero
            if (ac == None):
                ac = 0
                acs[i] = ac
                
            if (ac < 0) and (ac > 10):
                raise ValueError('AC['+ str(i+1) +']')
            i += 1
        
        #testando prova
        if (prova < 0) and (prova > 10):
            raise ValueError('prova')
            
        #testando sub
        if (sub < 0) and (sub > 10):
            raise ValueError('sub')
        
        #testando PAI
        if (pai != None):
            if (pai < 0) and (pai > 10):
                raise ValueError('P.A.I')
        
        #testando extra        
        if (extra < 0) and (extra > 10):
            raise ValueError('extra')
        
        #Se aluno não fez a prova, então a nota será a da sub
        if (prova == 0):
            prova = sub
            
        sete_melhores = deletaMenorValor(acs, 3)
        media_acs = round(sum(sete_melhores) / len(sete_melhores),2)
       
        #Nao participantes do PAI
        if (pai == None):
            nota_final = (media_acs * 0.6) + (prova * 0.4) + extra
            if (nota_final > 10):
                nota_final = 10
            print('Média ACS: {} / Prova: {} / Extra: {}'.format(media_acs, prova, extra))
        #Participantes do PAI
        else:
            nota_final = (media_acs * 0.5) + (prova * 0.3) + (pai * 0.2) + extra
            if (nota_final > 10):
                nota_final = 10
            print('Média ACS: {} / Prova: {} / Extra: {} / PAI: {}'.format(media_acs, prova, extra, pai))
        
        nota_final = round(nota_final,2)
        print('Nota Final: ', nota_final)
        
        motivo = []
        if (freq < 0.75):
            motivo.append('falta')
            
        if (nota_final < 6):
            motivo.append('nota')
            
        result = {"aprovado": (len(motivo) == 0), "motivo":motivo}
        return result               
    except ValueError as err:
        raise ValueError('Valor inválido para parâmetro '+ str(err) )
        
        
#Aprovado (Sem PAI)
print(aluno_aprovado(0.8, [None,5,5,6,6,7,7,8,2,1], 7.5, 1, None, 1))
print('')

#Aprovado (Com PAI)
print(aluno_aprovado(0.8, [None,5,5,6,6,7,7,8,2,1], 7.5, 1, 7, 1))
print('')

#Reprovado por falta e nota
print(aluno_aprovado(0.65, [None,2,5,6,2,7,2,5,2,1], 4.5, 1, None, 1))
print('')