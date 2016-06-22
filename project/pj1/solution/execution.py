iFile = open('input.txt', 'r')
oFile = open('output.txt', 'w')

caseCount = int(iFile.readline())

for c in range(caseCount):

    # number of murlocs in this test case
    murC = 0    # Coldlight Oracle
    murM = 0    # Murloc Warleader
    murO = 0    # Bluegill Warrior
    murB = 0    # Old Murk-Eye

    meta = iFile.readline().split(' ')
    murlocCount = int(meta[0])
    enemyHP = int(meta[1])

    print 'murlocCount = %d' % murlocCount
    print 'enemyHP = %d' % enemyHP

    for m in range(murlocCount):
        murloc = iFile.readline().replace('\n', '')
        print murloc
        if murloc == 'Coldlight Oracle':
            murC += 1
        elif murloc == 'Murloc Warleader':
            murM += 1
        elif murloc == 'Old Murk-Eye':
            murO += 1
        elif murloc == 'Bluegill Warrior':
            murB += 1
        else:
            print 'WTF is "%s"?' % murloc

    print '|C, M, B, O|'
    print '(%d, %d, %d, %d)' % (murC, murM, murB, murO)

    damage = \
    murO * 2 \
    + murO * (murlocCount - 1) \
    + murB * 2 \
    + (murO + murB) * murM * 2

    print 'damage = %d' % damage

    if damage >= enemyHP:
        oFile.write('Mrghllghghllghg')
    else:
        oFile.write('Tell you a joke, the execution of Paladin.')
    oFile.write('\n')

    print '----------'


oFile.close()
iFile.close()
