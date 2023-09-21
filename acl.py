print("-Identificar ACl-")
(""),
acl=int(input("ACL en fomrato IPV4:"))
if acl>=1 and acl >=99:
    print("Estandar")
elif acl>=100 and acl <=199:
    print("extendida")
else:("Este no es conciderado como acl, ingrese de nuevo D:<")
