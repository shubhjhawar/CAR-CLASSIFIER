
import pickle
model = pickle.load(open('car_classifier.pkl', 'rb'))

def predict(buying, maint, doors, persons, lug_boot, safety):
    if buying=='vhigh':
        b=0
    elif( buying=='high'):
        b=1
    elif(buying == 'med'):
        b=2
    elif(buying=='low'):
        b=3

    if maint=='vhigh':
        m=0
    elif( maint=='high'):
        m=1
    elif(maint == 'med'):
        m=2
    elif(maint=='low'):
        m=3

    if doors=='2':
        d=0
    elif(doors=='3'):
        d=1
    elif(doors=='4'):
        d=2
    else:
        d=3

    if lug_boot=='small':
        l=0
    elif lug_boot=='med':
        l=1
    elif lug_boot=='big':
        l=2


    if safety=='low':
        s=0
    elif safety=='med':
        s=1
    elif safety=='high':
        s=2

    prediction=model.predict([[b,m,d,persons,l,s]])
    if prediction==0:
        p='unacc'
    elif prediction==1:
        p='acc'
    elif prediction==2:
        p='vgood'
    elif prediction==3:
        p='good'

    message ='Your class is classified as {}'.format(p)
    return message
