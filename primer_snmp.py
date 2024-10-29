from pysnmp.hlapi import getCmd, SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity

iterator = getCmd(
    SnmpEngine(),
    CommunityData('public', mpModel=0), #NOMBRE DE LA COMUNIDAD NO DEFINIDA
    UdpTransportTarget(('10.10.10.10', 161)), #DIRECCIÓN IP O DNS Y EL PUERTO
    ContextData(),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')) #PONER EL OID DEL ROUTER
)

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

if errorIndication:
    print(errorIndication)

elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))