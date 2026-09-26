# عملگر های منطقی
"""
OR{
    true or true => true
    true or false => true
    false or true => true
    false or false => false
}
AND{
    true and true => true
    true and false => false
    false and true => false
    false and false => false
}
NOT{
    true => false
    false => true

}

"""

if(2==2 and 2>1):
    pass

if(2==2 or 2<1):
    pass

if(not 2==2):
    pass